# Project Title

Brief description of the project.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Files](#files)
- [Testing](#testing)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)

## Overview

Explain the purpose of the project and provide a brief overview of what is covered.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle style (version 2.5).
- All your files must be executable.
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).
- All your functions and coroutines must be type-annotated.

## Files

- [utils.py](utils.py)
- [client.py](client.py)
- [fixtures.py](fixtures.py)

## Testing

- [Testing Patterns](#testing-patterns)
  - Unit testing
  - Integration testing

Execute your tests with:

```bash
$ python -m unittest path/to/test_file.py