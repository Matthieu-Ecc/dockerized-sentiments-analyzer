from flask import Flask, render_template, request
import numpy
from analyzer import sentiment_scores

app = Flask(__name__)


@app.route("/", methods=["GET"])
def vader():
    sentence = request.args.get("sentence")
    return sentiment_scores(sentence)