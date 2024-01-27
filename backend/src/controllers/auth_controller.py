from flask import request, Response, json, Blueprint, abort, jsonify
from src.models.user_model import User
from src.utils import all, add

# auth controller blueprint to be registered with api blueprint
auth = Blueprint("auth", __name__)

# route for signup.
@auth.route('/signup', methods = ["POST"])
def signup():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    user = User(**data)
    add(user)
    return jsonify({'message': 'User created successfully'}), 200


# route for Login.
@auth.route('/login', methods = ["POST"])
def login():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"error": "Both email and password are required"}), 400
    users = all(User)
    for user in users:
        if user['email'] == email and user['password'] == password:
            return jsonify({"message": "Login successfully"}), 200
    return jsonify({"error": "Invalid username or password"}), 401
