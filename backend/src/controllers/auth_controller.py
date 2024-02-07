from flask import request, Response, json, Blueprint, abort, jsonify
from src.models.user_model import User
from src.models.tutor_model import Tutor, TutorSubject, Subject
from src.models.learner_model import Learner
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
    subjects = data.get("subjects", [])
    subjects = data.pop("subjects", [])

    user = User(**data)
    user.info()
    add(user)

    # if user it tutor add to tutor table
    # if user it learner add to learner table
    # if user it admin add to admin table

    if user.role == "tutor":
        tutor= Tutor(user_id=user.id)
        add(tutor)
        # subjects = data.get("subjects", [])
        for subject_name in subjects:
            subject = Subject.query.filter_by(name=subject_name).first()
            if not subject:
                subject = Subject(name=subject_name)
                add(subject)

                    # Associate the tutor with subjects
            tutor_subject = TutorSubject.query.filter_by(tutor_id=tutor.id, subject_id=subject.id).first()
            if not tutor_subject:
                # Associate the tutor with subjects
                tutor_subject = TutorSubject(tutor_id=tutor.id, subject_id=subject.id)
                add(tutor_subject)
    else:
        learner= Learner(user_id=user.id)
        add(learner)

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

    return jsonify(
        {"token": user.generate_token(), "status": "success", "role": user.role}), 200