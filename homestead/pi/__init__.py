"""
A module implementing interfaces for the Raspberry Pi platform.
"""

# internal
from runtimepy.net.arbiter.config import ConfigObject


def config(data: ConfigObject) -> None:
    """Sample config-builder method."""

    # Disable UI struct's system metrics (we're bringing our own).
    for struct in data.get("structs", []):
        if struct["name"] == "ui":
            struct_cfg = struct.setdefault("config", {})
            struct_cfg["psutil"] = False
