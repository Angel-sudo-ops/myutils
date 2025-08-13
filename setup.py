from setuptools import setup, find_packages

setup(
    name="myutils",
    version="1.0.0",
    description="Shared utilities (autoupdater, IO, UI helpers)",
    author="Angel Contreras",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0.0",
        "packaging>=23.0",
    ],
)