from flask import request, Response, json, Blueprint, abort, jsonify
from src.models.user_model import User
from src.utils import all, add, hash_password, check_password, check_unique_email, check_unique_username
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
    data['password'] = hash_password(data['password'])
    user = User(**data)
    add(user)
    return jsonify({'status': 'success', 'message': 'User created successfully'}), 200


# route for Login.
@auth.route('/login', methods=["POST"])
def login():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Both email and password are required"}), 400

    # search for the user with the email with sqlalchemy
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401
    else:
        if check_password(password, user.password):
            return jsonify(
                {"status": "success",
                 "message": "Login successfully",
                 "user": {
                     "id": user.id,
                     "username": user.username,
                     "email": user.email,
                     "role": user.role
                 }}), 200
        return jsonify({"error": "Invalid username or password"}), 401
