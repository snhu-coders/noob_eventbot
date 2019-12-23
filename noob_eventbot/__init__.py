from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for

app = Flask(__name__)


# Register Blueprints
from .root import root
app.register_blueprint(root)

from .events import events
app.register_blueprint(events)