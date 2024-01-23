# Flask Authentication Project

This project is designed for learning purposes to understand the implementation of authentication mechanisms in a Flask app.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Module](https://docs.python-requests.org/en/master/)
- [HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without relying on external resources:

- Declaring API routes in a Flask app
- Getting and setting cookies in Flask
- Retrieving request form data
- Returning various HTTP status codes

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- README.md file at the root of the project folder is mandatory
- Code should use the pycodestyle style (version 2.5)
- SQLAlchemy version 1.3.x should be used
- All files must be executable
- File lengths will be tested using `wc`
- Modules, classes, and functions should have documentation
- Functions should be type-annotated
- Flask app should only interact with Auth and never with DB directly
- Only public methods of Auth and DB should be used outside these classes

## Setup

Install `bcrypt` using the following command:

```bash
pip3 install bcrypt
