from flask import request, Response, json, Blueprint

# meeting controller blueprint to be registered with api blueprint

meeting = Blueprint("meeting", __name__)

@meeting.route('/<meeting_id>')
def get_meeting_by_id(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@meeting.route('/<meeting_id>/cancel', methods = ["DELETE"])
def delete_meeting_by_id(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

@meeting.route('/<meeting_id>/reschedule', methods = ["POST"])
def post_meeting_reschedule(meeting_id):
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )