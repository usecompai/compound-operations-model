"""status tool — proxies to the compai_init status module."""
from __future__ import annotations
import sys
from pathlib import Path
from typing import Any

from config import COMPAI_HOME, BRAND_SLUG


async def run(*, principal) -> Any:
    # compai_init lives at /opt/compai/services/init/cli/compai_init
    cli_path = COMPAI_HOME / "services" / "init" / "cli"
    if str(cli_path) not in sys.path:
        sys.path.insert(0, str(cli_path))
    try:
        from compai_init import status as status_mod  # type: ignore
        return status_mod.build_report(COMPAI_HOME, BRAND_SLUG)
    except Exception as e:  # noqa: BLE001
        return {"error": f"status unavailable: {e}", "brand": BRAND_SLUG}
