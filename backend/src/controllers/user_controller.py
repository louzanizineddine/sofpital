from flask import request, Response, json, Blueprint, jsonify, abort
from src.models.user_model import User
import base64
from src import db
from src.utils import get_by_id, all, update, add, delete, to_dict, token_required

# user controller blueprint to be registered with api blueprint
user = Blueprint("user", __name__)


# route for Get the user's profile information.
@user.route('/<user_id>')
@token_required
def get_user(current_user, user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return jsonify(to_dict(user))


@user.route('/', methods = ["POST"])
def create_user():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    user = User(**data)
    add(user)
    return jsonify({'message': 'User created successfully'}), 200

# when delete a user, we need to delete all the posts and offers that the user created
@user.route('/<user_id>', methods = ["DELETE"])
@token_required
def delete_user(current_user, user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    delete(user)
    return jsonify({'message': 'User deleted successfully'}), 200



# route for Update the user's profile information.
@user.route('/<user_id>', methods = ["PUT"])
def update_user_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, val in data.items():
        if key == 'profile_picture_blob' and val is not None:
            # Convert base64-encoded string to bytes
            val = base64.b64decode(val)
        setattr(user, key, val)
    update(user)
    return jsonify({'message': 'User updated successfully'}), 200
