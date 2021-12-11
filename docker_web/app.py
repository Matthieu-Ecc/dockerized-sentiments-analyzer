from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def analyse():
    text_to_analyse = request.form['text']
    #final = Appeler l'autre docker pour inferer
    return text_to_analyse


if __name__ == "__main__":
    app.run(debug=True)