from flask import request, Blueprint, jsonify, abort
from src.models.learner_model import Learner
from src.utils import all, get_by_id, to_dict, add, update
from src.models.user_model import User
from src.models.post_model import Post
from src.models.offer_model import Offer

# learner controller blueprint to be registered with api blueprint
learner = Blueprint("learner", __name__)


@learner.route('/<learner_id>', methods = ["GET"])
def get_learner(learner_id):
    """Get the learner's profile information."""
    """we can just call /api/user/<user_id>"""
    learner = Learner.query.get(learner_id)
    if not learner:
        abort(404)
    dict = to_dict(learner)
    user_id = dict.get("user_id")
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return jsonify(user)


@learner.route('/<learner_id>/posts', methods = ["GET"])
def get_posts_for_learner(learner_id):
    """Get all questions asked by the learner."""
    """select * from post where learner_id = learner_id"""
    list_posts = []
    learner = Learner.query.get(learner_id)
    if not learner:
        abort(404)
    for post in learner.posts:
        list_posts.append(to_dict(post))
    return jsonify(list_posts)

@learner.route('/<learner_id>/posts', methods = ["POST"])
def creaet_new_post(learner_id):
    """Ask a question."""
    """insert into post (learner_id, title, description, poste_date, status) values (learner_id, title, description, poste_date, status)"""
    learner = Learner.query.get(learner_id)
    if not learner:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    post = Post(**data)
    post.learner_id = learner_id
    add(post)
    return jsonify(to_dict(post)), 200



@learner.route('/<learner_id>/posts/<post_id>', methods = ["GET"])
def get_one_post_by_id(learner_id, post_id):
    """Get a question by its id."""
    """select * from post where id = post_id"""
    post = Post.query.get(post_id)
    if not post:
        abort(404)
    return jsonify(to_dict(post))

@learner.route('/<learner_id>/posts/<post_id>/accept_offer/<offer_id>', methods = ["PUT"])
def accept_offer(learner_id, post_id, offer_id):
    """Accept an offer for a post."""
    """make sure to update the offer status to accepted as well"""
    """make sure to update the post status to accepted as well"""
    """make sure to make all other offers for this post rejected"""
    post = Post.query.get(post_id)
    if not post:
        abort(404)
    post.status = "accepted"
    offer = Offer.query.get(offer_id)
    if not offer:
        abort(404)
    offer.status = "accepted"
    for offer in post.offers:
        if offer.id != offer_id:
            offer.status = "rejected"
    update(post)
    update(offer)
    return jsonify(to_dict(post)), 200


@learner.route('/<learner_id>/posts/<post_id>/reject_offer/<offer_id>', methods = ["PUT"])
def reject_offer(learner_id, post_id, offer_id):
    """Reject an offer for a post."""
    """make sure to update the offer status to be rejeced"""
    offer = Offer.query.get(offer_id)
    if not offer:
        abort(404)
    offer.status = "rejected"
    update(offer)
    return jsonify(to_dict(offer)), 200



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