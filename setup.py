# =====================================
# generator=datazen
# version=3.1.4
# hash=c338ebcda9d3270d257a252df9fbd30e
# =====================================

"""
homestead - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from homestead_bootstrap.setup import setup  # type: ignore

# internal
from homestead import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughn@libre-embedded.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.12",
    ],
}
setup(
    pkg_info,
    author_info,
)
