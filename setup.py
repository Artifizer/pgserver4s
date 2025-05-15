from setuptools import setup

setup(
    setup_requires=["cffi"],
    # dummy but needed for the binaries to work
    cffi_modules=["src/pgserver4s/_build.py:ffibuilder"],
)
