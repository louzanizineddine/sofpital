from flask import request, Response, json, Blueprint

# meeting controller blueprint to be registered with api blueprint

meeting = Blueprint("meeting", __name__)

@meeting.route('/<meeting_id>' , methods = ["GET"])
def get_meeting_by_id(meeting_id):
    """get all information about a meeting"""
    pass

@meeting.route('/<learner_id>', methods = ["GET"])
def get_meetings_for_learner(learner_id):
    """get all meetings for a learner"""
    pass


@meeting.route('/<tutor_id>', methods = ["GET"])
def get_meetings_for_tutor(tutor_id):
    """get all meetings for a tutor"""
    pass

@meeting.route('/', methods = ["POST"])
def create_new_meeting():
    """create a new meeting"""
    pass
