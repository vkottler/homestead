"""
A module implementing generic runtime-configuration utilities.
"""

# internal
from runtimepy.net.arbiter.config import ConfigObject


def disable_ui_psutil(data: ConfigObject) -> None:
    """Disable UI struct's system metrics (we're bringing our own)."""

    for struct in data.get("structs", []):
        if struct["name"] == "ui":
            struct_cfg = struct.setdefault("config", {})
            struct_cfg["psutil"] = False
