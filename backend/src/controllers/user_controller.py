from flask import request, Response, json, Blueprint, jsonify
from src.models.user_model import User
import base64
from src import db
from src.utils import get_by_id, all, update, add, delete

# user controller blueprint to be registered with api blueprint
user = Blueprint("user", __name__)


# route for Get the user's profile information.
@user.route('/<user_id>')
def get_user(user_id):
    dict = get_by_id(User, user_id)
    return jsonify(dict)


@user.route('/<user_id>/', methods = ["POST"])
def create_user(user_id):
    data = request.get_json()
    user = User(**data)
    add(user)
    return jsonify({'message': 'User created successfully'}), 200


@user.route('/<user_id>', methods = ["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    delete(user)
    return jsonify({'message': 'User deleted successfully'}), 200



# route for Update the user's profile information.
@user.route('/<user_id>', methods = ["PUT"])
def update_user_profile(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    for key, val in data.items():
        if key == 'profile_picture_blob' and val is not None:
            # Convert base64-encoded string to bytes
            val = base64.b64decode(val)
        setattr(user, key, val)
    update(user)
    return jsonify({'message': 'User updated successfully'}), 200

# @user.route('/')
# def get_all_users():
#     users = all(User)
#     list = [users[key] for key in users]
#     return jsonify(list)