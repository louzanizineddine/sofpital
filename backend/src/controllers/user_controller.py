from flask import request, Response, json, Blueprint, jsonify
from src.models.user_model import User

# user controller blueprint to be registered with api blueprint
user = Blueprint("user", __name__)


# route for Get the user's profile information.
@user.route('<user_id>/profile')
def get_user_profile(user_id):
    keys = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'birthdate', 'password', 'university', 'gender', 'profile_picture_blob', 'online', 'active', 'last_time_online', 'role'] 
    user = User.query.get(user_id)
    dict = {}
    for key in keys:
        dict[key] = getattr(user, key)
    return jsonify(dict)
    # if user:
    #     return jsonify({key: user[key] for key in keys})
    # else:
    #     return jsonify({'message': 'User not found'}), 404

# route for Update the user's profile information.
@user.route('/profile', methods = ["PUT"])
def update_user_profile():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )