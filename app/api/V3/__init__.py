from flask import Blueprint
from flask_restful import Api

from .views import Bookings, SingleBooking

version3 = Blueprint('api_v3', __name__, url_prefix='/api/v3')
api = Api(version3)


api.add_resource(Bookings, '/book')
api.add_resource(SingleBooking, '/book/<int:id>')