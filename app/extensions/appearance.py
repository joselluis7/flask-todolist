from flask_moment import Moment


def init_app(app):
    Moment(app)