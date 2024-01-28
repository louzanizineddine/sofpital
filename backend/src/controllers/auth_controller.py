from flask import request, Response, json, Blueprint, abort, jsonify
from src.models.user_model import User
from src.utils import all, add, hash_password, check_password, check_unique_email, check_unique_username
from src.utils import is_strong_password, is_valid_email, is_valid_phone_number, is_valid_birthdate, validate_role
from src.utils import validate_gender
# auth controller blueprint to be registered with api blueprint
auth = Blueprint("auth", __name__)

# route for signup.

# add hashing 
# handle errors
@auth.route('/signup', methods = ["POST"])
def signup():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if not check_unique_email(data['email']):
        return jsonify({'error': 'Email already exists'}), 400
    if not check_unique_username(data['username']):
        return jsonify({'error': 'Username already exists'}), 400
    if not is_strong_password(data['password']):
        return jsonify({'error': 'Password is weak. Please follow the password requirements.'}), 400
    if not is_valid_email(data['email']):
        return jsonify({'error': 'Invalid email'}), 400
    if not is_valid_phone_number(data['phone_number']):
        return jsonify({'error': 'Invalid phone number'}), 400
    if not is_valid_birthdate(data['birthdate']):
        return jsonify({'error': 'Invalid birthdate'}), 400
    if not validate_role(data['role']):
        return jsonify({'error': 'Invalid role. Choose either "learner" or "tutor"'}), 400
    if not validate_gender(data["gender"]):
        return jsonify({'error': 'Invalid gender. Choose either "male" or "female"'}), 400
    data['password'] = hash_password(data['password'])
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
    # hash the password and compare it with the one in the database
    if not email or not password:
        return jsonify({"error": "Both email and password are required"}), 400
    users = all(User)
    for user in users:
        if user['email'] == email and check_password(password, user['password']):
            return jsonify({"message": "Login successfully"}), 200
    return jsonify({"error": "Invalid username or password"}), 401
