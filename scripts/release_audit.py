#!/usr/bin/env python3
"""Fail a Compai release when public claims and shipped artifacts drift."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tarfile
import zipfile
from pathlib import Path


TEXT_SUFFIXES = {
    ".css", ".html", ".js", ".json", ".md", ".py", ".sh", ".toml",
    ".txt", ".yaml", ".yml",
}
PRIVATE_MARKERS = (
    "/Users/" + "diego" + "arroyo",
    "diego@" + "laa" + "gam",
    "@" + "laa" + "gam.com",
    "knowledge/" + "laa" + "gam/",
)
STALE_CLAIMS = {
    "352 skills": re.compile(r"\b352\s+skills\b", re.IGNORECASE),
    "95 tools": re.compile(r"\b95\s+(?:MCP\s+)?tools\b", re.IGNORECASE),
    "18:1": re.compile(r"\b18:1\b", re.IGNORECASE),
    "53 chapters": re.compile(r"\b53\s+chapters\b", re.IGNORECASE),
    "62-chapter": re.compile(r"\b62-chapter\b", re.IGNORECASE),
}
REQUIRED_CHAPTERS = {
    "10aa-truth-and-evidence.md",
    "10ab-architecture-contract.md",
    "10ac-skill-governance.md",
    "10ad-closure-first-execution.md",
    "10t-the-intelligence-layer.md",
}
SECRET_PATTERNS = {
    "Shopify token": re.compile(r"shpat_[A-Za-z0-9]{24,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--site-root", type=Path)
    parser.add_argument("--playbook-source", type=Path)
    parser.add_argument("--zip", dest="zip_path", type=Path)
    return parser.parse_args()


def text_files(root: Path):
    ignored = {".git", "__pycache__", "node_modules"}
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            if not ignored.intersection(path.parts):
                yield path


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def count_files(root: Path, pattern: str) -> int:
    return sum(1 for path in root.glob(pattern) if path.is_file())


def audit_text(root: Path, failures: list[str], allow_legacy_operai: set[str]) -> None:
    for path in text_files(root):
        rel = relative(path, root)
        if rel == "scripts/release_audit.py":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lower = content.lower()
        for marker in PRIVATE_MARKERS:
            if marker.lower() in lower:
                failures.append(f"private marker {marker!r} in {rel}")
        for claim, pattern in STALE_CLAIMS.items():
            if pattern.search(content):
                failures.append(f"stale claim {claim!r} in {rel}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                failures.append(f"possible {label} in {rel}")
        if "operai" in lower and rel not in allow_legacy_operai:
            failures.append(f"legacy OperAI reference in {rel}")


def audit_repo(repo: Path, failures: list[str]) -> dict:
    manifest_path = repo / "release-manifest.json"
    if not manifest_path.is_file():
        failures.append("release-manifest.json is missing")
        return {}

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected = manifest["public_package"]
    actual = {
        "chapters": count_files(repo / "chapters", "*.md"),
        "skills": count_files(repo / "skills", "*/SKILL.md"),
        "kit_files": sum(1 for path in (repo / "kit").rglob("*") if path.is_file()),
        "patterns": sum(
            1
            for path in (repo / "pattern-library").rglob("*")
            if path.is_file() and path.suffix in {".yml", ".yaml"}
        ),
    }
    for key, value in actual.items():
        if value != expected[key]:
            failures.append(f"{key}: manifest={expected[key]} actual={value}")

    chapters = {path.name for path in (repo / "chapters").glob("*.md")}
    missing = sorted(REQUIRED_CHAPTERS - chapters)
    if missing:
        failures.append(f"required chapters missing: {', '.join(missing)}")

    index_path = repo / "chapters" / "00-index.md"
    index = index_path.read_text(encoding="utf-8")
    if ".html)" in index:
        failures.append("source chapter index contains .html links")
    links = set(re.findall(r"\]\(([^)#]+\.md)\)", index))
    expected_links = chapters - {"00-index.md"}
    if links != expected_links:
        absent = sorted(expected_links - links)
        extra = sorted(links - expected_links)
        failures.append(f"chapter index mismatch; absent={absent} extra={extra}")

    for path in repo.rglob("*"):
        if path.is_file() and "operai" in path.name.lower():
            failures.append(f"legacy OperAI filename: {relative(path, repo)}")

    audit_text(repo, failures, {"README.md"})
    return manifest


def audit_playbook(repo: Path, source: Path, failures: list[str]) -> None:
    repo_chapters = repo / "chapters"
    for chapter in repo_chapters.glob("*.md"):
        source_path = source / chapter.name
        if not source_path.is_file():
            failures.append(f"playbook source missing {chapter.name}")
        elif chapter.read_bytes() != source_path.read_bytes():
            failures.append(f"playbook/repo drift: {chapter.name}")


def audit_site(site: Path, manifest: dict, failures: list[str]) -> None:
    site_manifest = site / "public-manifest.json"
    if not site_manifest.is_file():
        failures.append("site/public-manifest.json is missing")
    elif json.loads(site_manifest.read_text(encoding="utf-8")) != manifest:
        failures.append("site public manifest differs from repository manifest")
    for path in site.rglob("*"):
        if path.is_file() and "operai" in path.name.lower():
            failures.append(f"legacy OperAI filename in site: {relative(path, site)}")
    runtime_archive = site / "init" / "compai-runtime-v0.5.0.tar.gz"
    if not runtime_archive.is_file():
        failures.append("current Compai runtime archive is missing")
    else:
        with tarfile.open(runtime_archive, "r:gz") as archive:
            bad_names = [
                name for name in archive.getnames()
                if "operai" in name.lower() or name.endswith((".pyc", "/__pycache__"))
            ]
        if bad_names:
            failures.append(f"legacy or generated files in runtime archive: {bad_names[:5]}")
    audit_text(site, failures, {"vercel.json"})


def audit_zip(zip_path: Path, manifest: dict, failures: list[str]) -> None:
    if not zip_path.is_file():
        failures.append(f"release ZIP missing: {zip_path}")
        return
    with zipfile.ZipFile(zip_path) as archive:
        files = [name for name in archive.namelist() if not name.endswith("/")]
        bad = [name for name in files if "operai" in name.lower()]
        if bad:
            failures.append(f"legacy OperAI filenames in ZIP: {bad[:5]}")
        if len(files) != manifest["public_package"]["kit_files"]:
            failures.append(
                "ZIP file count: "
                f"manifest={manifest['public_package']['kit_files']} actual={len(files)}"
            )


def main() -> int:
    args = parse_args()
    repo = args.repo_root.resolve()
    failures: list[str] = []
    manifest = audit_repo(repo, failures)
    if args.playbook_source:
        audit_playbook(repo, args.playbook_source.resolve(), failures)
    if args.site_root and manifest:
        audit_site(args.site_root.resolve(), manifest, failures)
    if args.zip_path and manifest:
        audit_zip(args.zip_path.resolve(), manifest, failures)

    if failures:
        print("RELEASE AUDIT FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RELEASE AUDIT PASSED")
    print(f"- version: {manifest['version']}")
    for key, value in manifest["public_package"].items():
        print(f"- {key}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
