<h1 align="center">📄 detapack</h1>
<p align="center"><strong>Import/Export data from/to Deta Bases</strong></p>
<p align="center">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/detapack">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/detapack">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/detapack">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/berrysauce/detapack">
    <img alt="GitHub CodeQL" src="https://github.com/berrysauce/detapack/actions/workflows/codeql-analysis.yml/badge.svg">
</p>

## What is detapack?
detapack is a tiny & simple CLI built with [Typer](https://github.com/tiangolo/typer) (in Python) which can import and export data from and to Deta Bases.

## How to install detapack?
detapack can be installed from the Python Package Index.
```
pip install detapack
```
Run `detapack version` to check if detapack was installed successfully. You may need to add detapack to your shell configuration.

## Commands

Detapack is mainly used with two commands:

```bash
detapack export <BASE NAME>
```

```bash
detapack import <BASE NAME> <PATH TO JSON>
```

Both commands will ask you for your Deta project key, which will be used to access your bases. For security reasons, detapack asks for this key every time and doesn't store it anywhere.

You can read more about each command by putting `-- help` at the end.