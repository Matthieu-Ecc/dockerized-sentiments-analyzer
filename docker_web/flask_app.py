from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


appFlask = Flask(__name__)

@appFlask.route("/askSentiments", methods = ['POST','GET'])
def askSentiments():
    if request.method == 'POST':
        studentName = request.form['studentName'] website = request.form.get('website')
        return 'Submitted!'
        return '''<form method = "post">
        <p>Enter Name:</p>
        <p><input type = "text" name = "studentName" /></p>
        <p>Enter Website:</p>
        <p><input type = "text" name = "website" /></p>
        <p><input type = "submit" value = "submit" /></p>
        </form>'''


if __name__ == "__main__":
    appFlask.run(debug=True)