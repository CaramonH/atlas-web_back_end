#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request, abort, redirect
import uuid

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """ Basic Flask app, return a JSON """
    return jsonify({"message": "Bienvenue"})


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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Log out """
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ User profile """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ generate a token and respond with a 200 HTTP status """
    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ Update password end-point """
    email = request.form.get('email')
    token = request.form.get('reset_token')
    password = request.form.get('new_password')
    try:
        AUTH.update_password(token, password)
    except Exception:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
