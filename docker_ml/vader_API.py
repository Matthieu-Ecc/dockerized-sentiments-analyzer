from flask import Flask, request
from flask_restful import Resource, Api

from analyzer import sentiment_scores

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        sentence = request.args.get("data")
        sentiment = sentiment_scores(sentence)
        return {'sentence': sentence, 'sentiment': sentiment[0], 'neg': sentiment[1], 'neut': sentiment[2],
                'pos': sentiment[3]}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
