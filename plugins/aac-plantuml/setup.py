"""Setup.py module for the aac-plantuml plugin."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from setuptools import setup
from aac_plantuml_impl import plugin_version

setup(
    version=plugin_version,
    name="aac-plantuml",
    install_requires=["aac"],
    entry_points={
        "aac": ["aac-plantuml=aac_plantuml"],
    }
)
