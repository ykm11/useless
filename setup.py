#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="useless",
    version="0.2.0",
    description="Useless Library",
    long_description=long_description,
    author="ykm_kn",
    author_email="ushiromiya3@gmail.com",
    url="https://github.com/ykm11/useless",
    include_package_data=True,
    install_requires=["pycrypto"],
    tests_require=["nose"],
    license="MIT",
    keywords="",
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: MIT License",
    ],
)
