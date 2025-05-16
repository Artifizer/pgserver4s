from setuptools import setup

# This setup.py is configured to read metadata from pyproject.toml
setup(
    name="pgserver4s",
    version="0.1.0",
    description="Self-contained postgres server for your python applications",
    setup_requires=["cffi"],
    # dummy but needed for the binaries to work
    cffi_modules=["src/pgserver4s/_build.py:ffibuilder"],
)
