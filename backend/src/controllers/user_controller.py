from flask import request, Response, json, Blueprint, jsonify
from src.models.user_model import User
import base64
from src import db

# user controller blueprint to be registered with api blueprint
user = Blueprint("user", __name__)


# route for Get the user's profile information.
@user.route('/profile/<user_id>')
def get_user_profile(user_id):
    keys = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'birthdate', 'password', 'university', 'gender', 'profile_picture_blob', 'online', 'active', 'last_time_online', 'role'] 
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    dict = {}
    for key in keys:
        if key == 'profile_picture_blob' and getattr(user, key) is not None:
                # Convert bytes to base64-encoded string
                dict[key] = base64.b64encode(getattr(user, key)).decode('utf-8')
        else:
            dict[key] = getattr(user, key)
    return jsonify(dict)

# route for Update the user's profile information.
@user.route('/profile', methods = ["PUT"])
def update_user_profile():
    data = request.get_json()
    user = User.query.get(data['id'])
    for key, val in data.items():
        if key == 'profile_picture_blob' and val is not None:
            # Convert base64-encoded string to bytes
            val = base64.b64decode(val)
        setattr(user, key, val)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200
    