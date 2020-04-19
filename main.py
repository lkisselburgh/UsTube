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
        Message = request.form['Message']
        print("{} has been recieved".format(Message))
        return redirect(url_for('home', Message=Message))
    return render_template('Home.html')

@app.route("/Home", methods = ['GET','POST'])
def home():
    Message = request.args.get('Message',None)
    if request.method == 'POST':
        return redirect(url_for('begin'))
    return render_template('Recieved.html', Message=Message)
        
app.run(debug = True)