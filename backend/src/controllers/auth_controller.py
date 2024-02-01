from flask import request, Response, json, Blueprint, abort, jsonify
from src.models.user_model import User
from src.utils import all, add
# auth controller blueprint to be registered with api blueprint
auth = Blueprint("auth", __name__)


# @auth.route('/', methods = ["GET"])
# def index():
#     return jsonify({"message": "Welcome to the auth controller"}), 200
# route for signup.
# add hashing
# handle errors
@auth.route('/signup', methods=["POST"])
def signup():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    print(data)
    # if not check_unique_email(data['email']):
    #     return jsonify({'error': 'Email already exists'}), 400
    # if not check_unique_username(data['username']):
    #     return jsonify({'error': 'Username already exists'}), 400
    # data['password'] = hash_password(data['password'])
    user = User(**data)
    user.info();
    add(user)
    return jsonify({'status': 'success', 'message': 'User created successfully'}), 200


# route for Login.
@auth.route('/login', methods=["POST"])
def login():
    if not request.get_json():
        return jsonify({"error": "Not JSON"}), 400
    data = request.get_json()
    user = User.authenticate(**data)
    if not user:
        return jsonify({"error": "Authentication err"}), 400

    return jsonify({"token": user.generate_token(), "status": "success"}), 200