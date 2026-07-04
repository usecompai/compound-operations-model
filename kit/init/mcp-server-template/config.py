"""Runtime config — resolves $COMPAI_HOME and brand slug."""
import os
from pathlib import Path

COMPAI_HOME = Path(os.environ.get("COMPAI_HOME", "/opt/compai"))


def _resolve_brand() -> str:
    env = os.environ.get("COMPAI_BRAND")
    if env:
        return env
    kb = COMPAI_HOME / "brain" / "knowledge"
    if kb.exists():
        reserved = {"platform", "personal", "projects"}
        for child in sorted(kb.iterdir()):
            if child.is_dir() and child.name not in reserved:
                return child.name
    return "unknown"


BRAND_SLUG = _resolve_brand()
BRAIN_ROOT = COMPAI_HOME / "brain"
KNOWLEDGE_ROOT = BRAIN_ROOT / "knowledge"
CRED_DIR = COMPAI_HOME / "credentials"
KEYS_FILE = CRED_DIR / "mcp-keys.json"
