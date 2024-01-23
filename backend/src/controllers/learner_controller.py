from flask import request, Response, json, Blueprint, jsonify
from src.models.learner_model import Learner
from src.utils import all, get_by_id
from src.models.user_model import User

# learner controller blueprint to be registered with api blueprint
learner = Blueprint("learner", __name__)


@learner.route('/<learner_id>', methods = ["GET"])
def get_learner(learner_id):
    """Get the learner's profile information."""
    """we can just call /api/user/<user_id>"""
    pass


@learner.route('/<learner_id>/posts', methods = ["GET"])
def get_posts_for_learner(learner_id):
    """Get all questions asked by the learner."""
    """select * from post where learner_id = learner_id"""
    pass

@learner.route('/<learner_id>/posts', methods = ["POST"])
def creaet_new_post(learner_id):
    """Ask a question."""
    """insert into post (learner_id, title, description, poste_date, status) values (learner_id, title, description, poste_date, status)"""
    pass


@learner.route('/<learner_id>/posts/<post_id>', methods = ["GET"])
def get_one_post_by_id(learner_id, post_id):
    """Get a question by its id."""
    """select * from post where id = post_id"""
    pass

@learner.route('/<learner_id>/posts/<post_id>/accept_offer/<offer_id>', methods = ["PUT"])
def accept_offer(learner_id, post_id, offer_id):
    """Accept an offer for a post."""
    """make sure to update the offer status to accepted as well"""
    """make sure to update the post status to accepted as well"""
    """make sure to make all other offers for this post rejected"""
    pass


@learner.route('/<learner_id>/posts/<post_id>/reject_offer/<offer_id>', methods = ["PUT"])
def reject_offer(learner_id, post_id, offer_id):
    """Reject an offer for a post."""
    """make sure to update the offer status to be rejeced"""
    pass



# @learner.route('/meetings')
# def get_learner_meetings():
#     return Response(
#         response=json.dumps({'status': "success"}),
#         status=200,
#         mimetype='application/json'
#     )

# @learner.route('/meetings/<meeting_id>/rate', methods = ["POST"])
# def post_meeting_rating(meeting_id):
#     return Response(
#         response=json.dumps({'status': "success"}),
#         status=200,
#         mimetype='application/json'
#     )

# @learner.route('/meetings/<meeting_id>/feedback', methods = ["POST"])
# def post_meeting_feedback(meeting_id):
#     return Response(
#         response=json.dumps({'status': "success"}),
#         status=200,
#         mimetype='application/json'
#     )

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