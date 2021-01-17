from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from wtforms.validators import InputRequired
from Utility.databaseUtil import queryData, insertData, reviewObj, authObj, getUserPass, deleteReviewRecord
from json import dumps, loads
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


class AForm(FlaskForm):
    rName = StringField(validators=[InputRequired()])
    rTitle = StringField(validators=[InputRequired()])
    rEmail = StringField(validators=[InputRequired()])
    rComp = StringField(validators=[InputRequired()])
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

@app.route('/sendForApproval', methods=['POST', 'GET'])
def sendForApproval():
    form = AForm()
    print( str(form.rName.data) )
    print( str(form.rFile.data) )
    filename = secure_filename(form.rFile.data.filename)
    form.rFile.data.save('static/images/' + filename)
    reviewData = { "Name":str(form.rName.data),
                   "Email__c":str(form.rEmail.data),
                   "Title__c":str(form.rTitle.data),
                   "Company__c":str(form.rComp.data),
                   "Comment__c":str(form.rReview.data),
                   "Image__c":'images/' + filename }
    response = requests.post('https://ayu-dev-sharma-developer-edition.ap5.force.com/portfolio/services/apexrest/createReview',
                data= dumps( reviewData, indent = 4 ),
                headers={'content-type':'application/json'}
                 )
                 
    print( response.status_code )
    print( response.content )
    
    return redirect("/")
    

@app.route("/saveReview", methods=['POST'])
def saveReview():
    form = AForm()
    authObj = getUserPass()
    print(request.args.get('username'))
    print(request.args.get('password'))
    if( authObj.username == request.args.get('username') and authObj.password == request.args.get('password') ):
        reviewObj = request.json
        print( reviewObj )
        insertData(( reviewObj['Name'], reviewObj['Email__c'], reviewObj['Title__c'], 
                     reviewObj['Company__c'], reviewObj['Comment__c'], reviewObj['Image__c']))

        response = {'message':'Review added on the page.'}
        return response, 200
    return {'message':'Username or Password did not match'}, 401


@app.route("/deleteReview", methods=['POST'])
def deleteReview():
    form = AForm()
    authObj = getUserPass()
    print(request.args.get('username'))
    print(request.args.get('password'))
    if( authObj.username == request.args.get('username') and authObj.password == request.args.get('password') ):
        reviewObj = request.json
        print( reviewObj )
        deleteReviewRecord( reviewObj['Email__c'] )

        response = {'message':'Review delete/Rejected successfully'}
        return response, 200
    return {'message':'Username or Password did not match'}, 401

if __name__ == '__main__':
    app.run(debug=True)
