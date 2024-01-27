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
        return jsonify({"error": "Tutor not found"}), 404
    return jsonify(to_dict(tutor))


@tutor.route('/<tutor_id>/offers', methods = ["GET"])
def get_offers_for_tutor(tutor_id):
    """Get all offers offered by the tutor."""
    offer_list = []
    tutor = Tutor.query.get(tutor_id)
    if not tutor:
        return jsonify({"error": "Tutor not found"}), 404
    for offer in tutor.offers:
        offer_list.append(to_dict(offer))
    return jsonify(offer_list)


@tutor.route('/<tutor_id>/offers/post/<post_id>', methods = ["POST"])
def creat_new_offer(tutor_id, post_id):
    """
        Make an offer.
        we make sure that the tutor exists and the post exists.
        we make sure that tutor can make only one offer for a post.
    """
    tutor = Tutor.query.get(tutor_id)
    if not tutor:
        return jsonify({"error": "Tutor not found"}), 404
    if not request.get_json():
        abort(400, description="Not a JSON")
    
    # check if the tutor already made an offer for this post
    for offer in tutor.offers:
        if offer.post_id == post_id:
            return jsonify({"error": "You already made an offer for this post"}), 400
    data = request.get_json()
    offer = Offer(**data)
    offer.tutor_id = tutor_id
    offer.post_id = post_id
    add(offer)
    return jsonify(to_dict(offer)), 200


@tutor.route('/<tutor_id>/offers/<offer_id>', methods = ["GET"])
def get_one_offer_by_id(tutor_id, offer_id):
    offer = Offer.query.filter_by(id=offer_id, tutor_id=tutor_id).first()
    if offer is None:
        return jsonify({'error': 'Offer not found or offer does not belong to tutor'}), 404
    
    return jsonify(to_dict(offer)), 200
