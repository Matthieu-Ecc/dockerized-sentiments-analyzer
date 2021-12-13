import pytest
import time
from flask import Flask
from routes import configure_routes
import requests

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
    url = 'http://vader:5000/?data=This%20was%20the%20worst%20movie%20ever'
    response = client.get(url)
    json_response = response.json()
    assert response.get_data() == json_response