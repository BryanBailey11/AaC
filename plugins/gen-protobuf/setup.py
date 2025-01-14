"""Setup.py module for the aac-gen-protobuf plugin."""
# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.
from aac_gen_protobuf.aac_gen_protobuf_impl import plugin_version
from setuptools import setup

with open("README.md", "r") as fh:
    readme_description = fh.read()

runtime_dependencies = [
    "Jinja2 >= 3.0",
]

development_dependencies = []

test_dependencies = [
    "nose2 >= 0.10.0",
]

setup(
    version=plugin_version,
    name="aac-gen-protobuf",
    install_requires=["aac >= 0.0.4"],
    entry_points={
        "aac": ["aac_gen_protobuf=aac_gen_protobuf.aac_gen_protobuf"],
    },
    extras_require={
        "test": test_dependencies,
        "dev": development_dependencies,
        "all": test_dependencies + development_dependencies,
    },
)
