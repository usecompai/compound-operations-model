from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from release_audit import audit_text


class SecretPatternTests(unittest.TestCase):
    def test_risk_based_is_not_an_openai_token(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "page.html").write_text("A risk-based approach", encoding="utf-8")
            failures: list[str] = []
            audit_text(root, failures, set())
            self.assertEqual(failures, [])

    def test_openai_token_shape_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            token = "sk-" + "a" * 40
            (root / "page.html").write_text(f"token: {token}", encoding="utf-8")
            failures: list[str] = []
            audit_text(root, failures, set())
            self.assertEqual(failures, ["possible OpenAI token in page.html"])


if __name__ == "__main__":
    unittest.main()
