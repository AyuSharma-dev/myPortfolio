from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from wtforms.validators import InputRequired
from Utility.databaseUtil import queryData, insertData

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


class AForm(FlaskForm):
    rName = StringField(validators=[InputRequired()])
    rTitle = StringField(validators=[InputRequired()])
    rEmail = StringField(validators=[InputRequired()])
    rFile = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'])])
    rReview = TextAreaField('Text', validators=[InputRequired()], render_kw={"rows": 4, "cols": 50})


@app.route('/', methods=['POST', 'GET'])
def home():
    form = AForm()
    rows = queryData()
    print(rows)
    return render_template("index.html", form=form, rows=rows)

@app.route('/templates/index.html', methods=['POST', 'GET'])
def renderIndex():
    form = AForm()
    return render_template("index.html", form=form)

@app.route("/saveReview/", methods=['POST'])
def saveReview():
    form = AForm()
    filename = secure_filename(form.rFile.data.filename)
    form.rFile.data.save('static/images/' + filename)
    insertData(( str(form.rName.data), str(form.rEmail.data), 
                    str(form.rTitle.data), str(form.rReview.data), 
                    'images/' + filename ))
    rows = queryData()    
    return render_template("index.html", form=form, rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
