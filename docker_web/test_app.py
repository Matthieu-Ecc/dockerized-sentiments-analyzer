from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

class sentimentsForm(FlaskForm):
    sentence = StringField('Which sentiments is dominants in this sentence ?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    sentence = ""
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = sentimentsForm()
    message = ""
    # names= ""
    # if form.validate_on_submit():
    #     sentence = form.sentence.data
    #     if sentence.lower() in names:
    #         # empty the form field
    #         form.name.data = ""
    #         id = get_id(ACTORS, name)
    #         # redirect the browser to another route and template
    #         return redirect( url_for('actor', id=id) )
    #     else:
    #         message = "That actor is not in our database."
    # return render_template('index.html', names=names, form=form, message=message)