from flask import Flask,request,render_template,redirect
import pickle
from diabetes import *
import json
app = Flask(__name__)
from diabetes import *
import logging
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app = Flask(__name__)
database = {'manasa': '123', 'jayesh': 'abcd', 'karthik': 'assman'}
@app.route('/')
def hello_world():
    return render_template("login.html")
@app.route('/form_login', methods=['POST', 'GET'])  #taking the input from the webpage to the backend flask py file
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 in database and database[name1] == pwd:  # Check if the credentials are correct
        return redirect('/diet')  # Redirect to the index page
    else:
        return render_template('login.html', info='Invalid username or password')
@app.route("/diet",methods=['GET','POST'])  #  giving the credential to the diabeties function from the diet site 
def index():
	exercise = {}
	diet = {}
	if(request.method == "POST"):
		height = int(request.values["height"])
		height_unit = request.values["height_unit"]
		height = height / 100 if height_unit == "cm" else height
		weight = int(request.values["weight"])
		weight_unit = request.values["weight_unit"]
		weight = weight * 0.45 if weight_unit == "lbs" else weight
		diet = request.values["diet"]
		result = get_recommendation(weight,height,diet)		
		exercise = result["exercise"]
		diet = result["diet"]
	return render_template("index.html",exercise=exercise,diet=diet)
@app.route("/diabetes")
def diabetes():
	return render_template("diabetes.html")
@app.route("/export")
def export():
	return "export"
if __name__ == '__main__':
    app.run(debug=True,port=8080)
