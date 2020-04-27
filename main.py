from flask import Flask, render_template, request, redirect, url_for, session
from db import *
from parse import *

#create database object
database = ytDB()
#input data into database
parser(database)

testList = ""

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
    global testList
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
            if 'Title' in request.form:
                query = request.form
                titleQ = query['Title']
                catQ = query['categoryID']
                #searchType = query['SearchType']
                #sliderQ = query['SearchContent']
                testList = database.searchDB(titleQ,catQ)
                return redirect(url_for('search'))
                #redirect(url_for('results'))

        elif request.form['submit_button'] == "Return to Home":
            return redirect(url_for('begin'))

        elif request.form['submit_button'] == "Delete":
            id = request.form['Video']
            idval = int(id)
            for members in testList:
                if members[0] == idval:
                    testList.remove(members)
            database.delete(idval)
            return redirect(url_for('search'))

        elif request.form['submit_button'] == "Add":
           print(request.form)

    return render_template('SearchBar.html', testList=testList)

@app.route("/Results", methods = ['GET', 'POST']) # new
def results():
    global testList
    if request.method == 'POST':
            return redirect(url_for('search'))
    return render_template('Results.html', testList=testList)
    
app.run(debug = True, use_reloader = False)