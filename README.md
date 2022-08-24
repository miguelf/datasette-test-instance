# datasette-test-instance

[![PyPI](https://img.shields.io/pypi/v/datasette-test-instance.svg)](https://pypi.org/project/datasette-test-instance/)
[![Changelog](https://img.shields.io/github/v/release/miguelf/datasette-test-instance?include_prereleases&label=changelog)](https://github.com/miguelf/datasette-test-instance/releases)
[![Tests](https://github.com/miguelf/datasette-test-instance/workflows/Test/badge.svg)](https://github.com/miguelf/datasette-test-instance/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/miguelf/datasette-test-instance/blob/main/LICENSE)

null

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-test-instance

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-test-instance
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
