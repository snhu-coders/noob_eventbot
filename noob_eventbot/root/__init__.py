from flask import Blueprint
from flask_restful import Api

root = Blueprint('root', __name__)

api = Api(root)


# Index
from .index import Index
api.add_resource(Index, "/")

# HealthCheck
from .healthcheck import HealthCheck
api.add_resource(HealthCheck, "/healthcheck")
