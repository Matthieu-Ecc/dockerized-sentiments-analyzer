import pytest
import time
from flask import Flask, request
from docker_web.routes import configure_routes
import requests
from flask_restful import Resource, Api
from docker_ml.analyzer import sentiment_scores


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200

def test_sentiment():
    app = Flask(__name__)
    api = Api(app)
    class HelloWorld(Resource):
        def get(self):
            sentence = request.args.get("data")
            sentiment = sentiment_scores(sentence)
            return {'sentence': sentence, 'sentiment' : sentiment[0] , 'neg' : sentiment[1], 'neut' : sentiment[2], 'pos' : sentiment[3]}

    api.add_resource(HelloWorld, '/')
    client = app.test_client()

    url = '/?data=This%20was%20the%20worst%20movie%20ever'
    response = client.get(url)
    assert response.get_data()


def test_connection():
    assert requests.get("http://localhost:5000").status_code == 200 , "web site is not up"