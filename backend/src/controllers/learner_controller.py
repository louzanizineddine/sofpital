from flask import request, Response, json, Blueprint, jsonify
from src.models.learner_model import Learner
from src.utils import all, get_by_id
from src.models.user_model import User

# learner controller blueprint to be registered with api blueprint
learner = Blueprint("learner", __name__)

@learner.route('/questions')
def get_questions():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@learner.route('/questions', methods = ["POST"])
def post_questions():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@learner.route('/question/<question_id>')
def get_question_by_id(question_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@learner.route('/meetings')
def get_learner_meetings():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@learner.route('/meetings/<meeting_id>/rate', methods = ["POST"])
def post_meeting_rating(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@learner.route('/meetings/<meeting_id>/feedback', methods = ["POST"])
def post_meeting_feedback(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@learner.route('/')
def get_all_learner():
    learners = all(Learner)
    lst = []
    for val in learners.values():
        dict = {}
        user_id = val['user_id']
        dict[val['id']] = get_by_id(User, user_id)
        lst.append(dict)
    return jsonify(lst)