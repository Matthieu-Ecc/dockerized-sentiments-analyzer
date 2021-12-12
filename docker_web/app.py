from flask import Flask, request, render_template
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def analyse():
    text_to_analyse = request.form['text']
    #final = Appeler l'autre docker pour inferer
    api_url = "http://vader:5000/?data="+text_to_analyse
    response = requests.get(api_url)
    return response.text

if __name__ == "__main__":
    app.run(debug=True)