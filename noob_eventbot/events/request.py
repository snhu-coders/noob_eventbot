from flask import request
from flask_restful import Resource

class Request(Resource):
    def get(self):
        return {"msg": "Send a challenge to me!"}

    def post(self):
        data = request.json

        if data["type"] == "url_verification":           

            if "challenge" in data:
                return {"challenge": data["challenge"]}
            else:
                return {"error": "No challenge detected"}, 400

        return {"ok": True}

