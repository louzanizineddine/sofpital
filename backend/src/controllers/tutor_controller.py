from flask import request, Response, json, Blueprint

# tutor controller blueprint to be registered with api blueprint
tutor = Blueprint("tutor", __name__)

@tutor.route('/<tutor_id>', methods = ["GET"])
def get_tutor(tutor_id):
    """Get the tutor's profile information."""
    """we can just call /api/user/<user_id>"""
    pass


@tutor.route('/<tutor_id>/offers', methods = ["GET"])
def get_offers_for_tutor(tutor_id):
    """Get all offers offered by the tutor."""
    pass

@tutor.route('/<tutor_id>/offers/post/<post_id>', methods = ["POST"])
def creaet_new_offer(tutor_id, post_id):
    """Make an offer."""
    pass


@tutor.route('/<tutor_id>/offers/<offer_id>', methods = ["GET"])
def get_one_offer_by_id(offer_id):
    """Get an offer by its id."""
    pass

