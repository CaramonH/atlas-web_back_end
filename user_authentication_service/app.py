#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request, abort, redirect
from flask import url_for
import uuid

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def users():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = AUTH.register_user(email, password)

        return jsonify({"email": user.email, "message": "user created"}), 200

    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ Log in """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(400, "Email and password are required")

    try:
        if AUTH.valid_login(email, password):
            session_id = str(uuid.uuid4())

            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)

            return response
        else:
            abort(401, "Incorrect login information")
    except ValueError:
        abort(401, "Incorrect login information")


@app.route('/sessions', methods=['DELETE'])
def logout():
    """logout"""
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
