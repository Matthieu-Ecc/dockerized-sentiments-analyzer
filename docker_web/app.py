from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def analyse():
    text_to_analyse = request.form['text']
    #final = Appeler l'autre docker pour inferer
    api_url = "vader-server?sentence="
    response = requests.get(api_url+text_to_analyse)
    return format(response)


if __name__ == "__main__":
    app.run(debug=True)