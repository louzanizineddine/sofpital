from flask import request, Response, json, Blueprint, jsonify, abort
from src.models.tutor_model import Tutor
from src.models.offer_model import Offer
from src.utils import all, get_by_id, to_dict, add 

# tutor controller blueprint to be registered with api blueprint
tutor = Blueprint("tutor", __name__)

@tutor.route('/<tutor_id>', methods = ["GET"])
def get_tutor(tutor_id):
    """Get the tutor's profile information."""
    """we can just call /api/user/<user_id>"""
    tutor = Tutor.query.get(tutor_id)
    if not tutor:
        abort(404)
    return jsonify(to_dict(tutor))


@tutor.route('/<tutor_id>/offers', methods = ["GET"])
def get_offers_for_tutor(tutor_id):
    """Get all offers offered by the tutor."""
    offer_list = []
    tutor = Tutor.query.get(tutor_id)
    if not tutor:
        abort(404)
    for offer in tutor.offers:
        offer_list.append(to_dict(offer))
    return jsonify(offer_list)

@tutor.route('/<tutor_id>/offers/post/<post_id>', methods = ["POST"])
def creaet_new_offer(tutor_id, post_id):
    """Make an offer."""
    tutor = Tutor.query.get(tutor_id)
    if not tutor:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    offer = Offer(**data)
    offer.tutor_id = tutor_id
    offer.post_id = post_id
    add(offer)
    return jsonify(to_dict(offer)), 200


@tutor.route('/<tutor_id>/offers/<offer_id>', methods = ["GET"])
def get_one_offer_by_id(offer_id):
    """Get an offer by its id."""
    offer = Offer.query.get(offer_id)
    if not offer:
        abort(404)
    return jsonify(to_dict(offer))

