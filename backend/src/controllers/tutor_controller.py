from flask import request, Response, json, Blueprint

# tutor controller blueprint to be registered with api blueprint
tutor = Blueprint("tutor", __name__)

@tutor.route('/questions/<learner_id>')
def get_learner_question(learner_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@tutor.route('/questions/<question_id>/respond', methods = ["POST"])
def post_question_response(question_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@tutor.route('/meetings')
def get_tutor_meetings():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@tutor.route('/meetings/<meeting_id>/accept', methods = ["POST"])
def post_meeting_accept(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@tutor.route('/meetings/<meeting_id>/reject', methods = ["POST"])
def post_meeting_reject(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@tutor.route('/meetings/<meeting_id>/feedback', methods = ["POST"])
def post_meeting_feedback(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )