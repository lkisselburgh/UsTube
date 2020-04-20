from flask import Flask, render_template, request, redirect, url_for
from db import *
from parser import *

#create database object
database = ytDB()
#input data into database
parser(database)


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def begin():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Send': #new
            Message = request.form['Message']
            print("{} has been recieved".format(Message))
            return redirect(url_for('home', Message=Message))

        elif request.form['submit_button'] == 'Search bar': #new
            return redirect(url_for('search'))
        
    return render_template('Home.html')

@app.route("/Home", methods = ['GET','POST'])
def home():
    Message = request.args.get('Message',None)
    if request.method == 'POST':
        return redirect(url_for('begin'))
    return render_template('Recieved.html', Message=Message)

@app.route("/Search", methods = ['GET', 'POST']) # new
def search():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            return redirect(url_for('results'))
        
        elif request.form['submit_button'] == "Return to Home":
            return redirect(url_for('begin'))

    return render_template('SearchBar.html')

@app.route("/Results", methods = ['GET', 'POST']) # new
def results():
	query = request.form
	if request.method == 'POST':
		if  'search' in request.form:
			return redirect(url_for('search'))
	return render_template('Results.html', query=query)

        
app.run(debug = True)