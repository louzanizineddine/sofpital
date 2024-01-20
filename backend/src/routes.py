from flask import Blueprint
from src.controllers.user_controller import user  
from src.controllers.auth_controller import auth 
from src.controllers.learner_controller import learner
from src.controllers.tutor_controller import tutor
from src.controllers.meeting_controller import meeting

# main blueprint to be registered with application
api = Blueprint('api', __name__)

    # register user with api blueprint
api.register_blueprint(user, url_prefix="/user")
api.register_blueprint(auth, url_prefix="/auth")
api.register_blueprint(learner, url_prefix="/learner")
api.register_blueprint(tutor, url_prefix="/tutor")
api.register_blueprint(meeting, url_prefix="/meeting")