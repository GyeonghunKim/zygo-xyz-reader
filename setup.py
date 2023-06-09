import io
from setuptools import find_packages, setup

# Read in the README for the long description on PyPI
def long_description():
    with io.open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    return readme


setup(
    name="zygo_xyz_reader",
    version="0.1",
    description="Zygo *.xyz file reader",
    long_description=long_description(),
    url="https://github.com/GyeonghunKim/zygo-xyz-reader",
    author="Gyeonghun Kim",
    author_email="gyeonghun.kim@duke.edu",
    license="",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    zip_safe=False,
)