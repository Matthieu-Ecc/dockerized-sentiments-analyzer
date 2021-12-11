from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')


@app.route("/askSentiments", methods = ['POST','GET'])
def askSentiments():
    if request.method == 'POST':
        student_name = request.form['student_name']
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