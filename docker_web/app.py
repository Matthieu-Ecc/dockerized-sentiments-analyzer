import flask
#import numpy as np
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello to my flask app, to test the mean function copy/paste this in tour webrowser\n " \
           "localhost:5000/mean?list=1&list=2&list=3&list=4 "


@app.route("/askSentiments", methods = ['POST','GET'])
def askSentiments():
    if request.method == 'POST':
        studentName = request.form['studentName']
        website = request.form.get('website')
        return 'Submitted!'
        return '''<form method = "post">
        <p>Enter Name:</p>
        <p><input type = "text" name = "studentName" /></p>
        <p>Enter Website:</p>
        <p><input type = "text" name = "website" /></p>
        <p><input type = "submit" value = "submit" /></p>
        </form>'''


if __name__ == "__main__":
    app.run(debug=True)