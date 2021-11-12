"""Setup.py module for the aac-gen-gherkin-behaviors plugin."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from setuptools import setup
from aac_gen_gherkin_behaviors.aac_gen_gherkin_behaviors_impl import plugin_version

setup(
    version=plugin_version,
    name="aac-gen-gherkin-behaviors",
    install_requires=["aac"],
    entry_points={
        "aac": ["aac-gen-gherkin-behaviors=aac_gen_gherkin_behaviors.aac_gen_gherkin_behaviors"],
    }
)
