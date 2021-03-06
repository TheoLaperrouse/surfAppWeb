from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import surfAPI
import json
app = Flask(__name__)
api = Api(app)

CORS(app)


@app.route("/")
def spots():
    fichierSpots = open('serveur/spots.json', 'r')
    data = json.load(fichierSpots)
    return data


@app.route("/bestsRide")
def bestsRide():
    pointGeo = request.args.get('pointGeo', None)
    nomSpot = request.args.get('nomSpot', None)
    orientationPlage = request.args.get('orientationPlage', None)
    return surfAPI.serverResponse(pointGeo, nomSpot, orientationPlage)


@app.route("/addSpot", methods=['POST'])
def addSpot():
    if request.method == "POST":
        spotToAdd = request.json
        surfAPI.addSpot(spotToAdd)
        return '200'
    return '404'


if __name__ == '__main__':
    app.run(port=5002)
