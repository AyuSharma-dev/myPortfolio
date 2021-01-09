from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, StringField
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from json import loads

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


class AForm(FlaskForm):
    rName = StringField('Text')
    rTitle = StringField('Text')
    rEmail = StringField('Text')
    rReview = TextAreaField('Text', render_kw={"rows": 4, "cols": 50})
    quoted = BooleanField()


@app.route('/', methods=['POST', 'GET'])
def home():
    form = AForm()
    # if form.validate_on_submit():
    #     jsonBody = form.jsonCode.data
    #     quoted = form.quoted.data
    #     if str(jsonBody) != '':
    #         if(quoted):
    #             jsonBody = parseQuotedJson(str(jsonBody))
    #         form.apexCode.data = getApexCode(str(jsonBody))
    #     else:
    #         form.apexCode.data = ''
    return render_template("index.html", form=form)

@app.route('/templates/index.html', methods=['POST', 'GET'])
def renderIndex():
    form = AForm()
    return render_template("index.html", form=form)

@app.route("/saveReview/", methods=['POST'])
def saveReview():
    print("saveReview called")


if __name__ == '__main__':
    app.run(debug=True)
