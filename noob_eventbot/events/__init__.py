from flask import Blueprint
from flask_restful import Api

events = Blueprint('events', __name__, url_prefix="/events")

api = Api(events)

from .request import Request
api.add_resource(Request, '/request')
