from flask_moment import Moment

#Flask Extension for Date format
def init_app(app):
    Moment(app)