from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-test-instance",
    description="null",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Miguel A. Figueroa-Villanueva",
    url="https://github.com/miguelf/datasette-test-instance",
    project_urls={
        "Issues": "https://github.com/miguelf/datasette-test-instance/issues",
        "CI": "https://github.com/miguelf/datasette-test-instance/actions",
        "Changelog": "https://github.com/miguelf/datasette-test-instance/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_test_instance"],
    entry_points={"datasette": ["test_instance = datasette_test_instance"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
