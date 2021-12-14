import requests
from flask import request, render_template


def configure_routes(app):
    @app.route('/')
    def form():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def analyse():
        text_to_analyse = request.form['text']
        api_url = "http://vader:5000/?data=" + text_to_analyse
        response = requests.get(api_url)
        json_response = response.json()
        return render_template('index.html', final=json_response['sentiment'], text=json_response['sentence'],
                               neg=json_response['neg'], neut=json_response['neut'], pos=json_response['pos'])
