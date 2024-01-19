from src import config, app

from flask import Blueprint
from src.controllers.user_controller import users


if __name__ == "__main__":
    app.run(host= config.HOST,
            port= config.PORT,
            debug= config.DEBUG)

