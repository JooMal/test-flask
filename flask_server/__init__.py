from flask import Flask, jsonify, request
from flask_restx import Resource, Api
from controller import getResults
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, resource={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return {"resultWord" : "Hello world"}

@api.route("/test")
class Test(Resource) :
    def get(self) :
        return jsonify({"resultWord" : "Testing API - GET"})

# pagniation 들어가면 좋은 상황
@api.route("/getResLst")
class getResultList(Resource) :
    def get(self):

        args = {}

        args['category'] = request.args.get('category')
        args['numOfRows'] = request.args.get('numOfRows')
        args['pageNo'] = request.args.get('pageNo')

        res = getResults(args)
        return jsonify(res)