from flask import request, Response, json, Blueprint, jsonify, abort
from src.models.meeting_model import Meeting
from src.models.learner_model import Learner
from src.models.tutor_model import Tutor
from src.utils import all, get_by_id, to_dict, add

# meeting controller blueprint to be registered with api blueprint

meeting = Blueprint("meeting", __name__)

@meeting.route('/<meeting_id>' , methods = ["GET"])
def get_meeting_by_id(meeting_id):
    """get all information about a meeting"""
    meeting = Meeting.query.get(meeting_id)
    if not meeting:
        return jsonify({"error": "Meeting not found"}), 404
    return jsonify(to_dict(meeting))

@meeting.route('/<learner_id>', methods = ["GET"])
def get_meetings_for_learner(learner_id):
    """get all meetings for a learner"""
    learner = Learner.query.get(learner_id)
    if not learner:
        return jsonify({"error": "Learner not found"}), 404
    list_meetings = []
    for meeting in learner.meetings:
        list_meetings.append(to_dict(meeting))
    return jsonify(list_meetings)


@meeting.route('/<tutor_id>', methods = ["GET"])
def get_meetings_for_tutor(tutor_id):
    """get all meetings for a tutor"""
    tutor = Tutor.query.get(tutor_id)
    if not tutor:
        return jsonify({"error": "Tutor not found"}), 404
    list_meetings = []
    for meeting in tutor.meetings:
        list_meetings.append(to_dict(meeting))
    return jsonify(list_meetings)
    
@meeting.route('/', methods = ["POST"])
def create_new_meeting():
    """create a new meeting"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    meeting = Meeting(**data)
    add(meeting)
    return jsonify(to_dict(meeting)), 200