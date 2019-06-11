from flask import Blueprint
from flask_restful import Api

from .views import Bookings, SingleBooking

version2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version2)


api.add_resource(Bookings, '/book')
api.add_resource(SingleBooking, '/book/<int:id>')