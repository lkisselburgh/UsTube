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
                #print("Msg Saved")
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

        elif request.form['submit_button'] == "Save": # new
            #if request.method == 'POST':
            
            id = request.form['SavedVideo']
            idval = int(id)
            for members in testList:
                if members[0] == idval:
                    print("Members: ", members[1].Title)
                    members[1].Title = "funfetti is for psychopaths"
                    #testList.remove(members)
            #database.delete(idval)
            #new_members = ['MltuW2kcREI', '17.15.11', "funfetti is for psychopaths",	'emma chamberlain',	'24',	'2017-11-14T20:28:53.000Z',	'emma chamberlain|"emma chambie"|"cooking with emma"|"funfetti"|"recipe"|"how to"|"baking"|"how to make cake"|"funfetti cake recipe"|"healthy"|"vegan"|"paleo"|"comedy"|"funny"',	'126438',	'12229',	'86',	'1865',	'https://i.ytimg.com/vi/MltuW2kcREI/default.jpg',	'FALSE',	'FALSE',	'FALSE',	"the mini whisk IS BACK\n\nIf you liked this video and want to see more from me, I post tuesdays, thursdays, and sundays, SO SUBSCRIBE FOR A GOOD TIME YO :)\n\nâœ© LINK TO THE SHIRT Iâ€™M WEARING (before I change haha) âœ©\n\nâœ­ https://goo.gl/LVhfNg\n\nâœ© MERCH: âœ©\n\nâœ­ KEEP IN MIND THAT YOU CAN CHANGE THE COLOR AND STYLE OF EACH DESIGN (like you can do a t-shirt, hoodie, travel mug, sticker, etc.) I LOVE YOU ALL AND HOPE U ENJOY THIS STUFF :)\nâœ­  https://www.redbubble.com/people/emmachambie/shop \n\nâœ© SOCIAL MEDIA âœ©\n\nâœ­ instagram: @_emmachamberlain\nâœ­ snapchat: @emmachambie\nâœ­ twitter: @emmachambie\nâœ­ pinterest: @emmachambie\nâœ­ VSCO: @emmachambie\nâœ­ depop: @emmachambie\nâœ­ email: emmafcham.business@gmail.com \nâœ­ spotify: https://open.spotify.com/user/emmachambie (or try typing in â€œEmma Frances Chamberlain) \n\nâœ© P.O. Box âœ©\n\nEmma Chamberlain\nP.O. Box #4058\nFoster City, California, 94404  USA\n\nâœ© MUSIC âœ©\n\nâœ­ Music from my outro\nJoakim Karud - Love Mode\nCheck out his channel!! - https://www.youtube.com/user/JoakimKarud/"]
            #database.ytDBStart(new_members)
                
            
            #idval = int(items)
            #database.delete(idval)
            
            #for members in testList:
                #if members[0] == idval:
                    #testList.remove(members)
                    #database.ytDBStart(id)
            #====== END Lacey
            
            #database.delete(idval)

            #updateList = list()
            #update = request.form

            #for member in update:
                #updateList.append(update[member])

            #print(updateList)
            #database.ytDBStart(updateList)
            #====== END Kiana

            return redirect(url_for('search'))

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
            addList = list()
            addForm = request.form
            #print(addForm)
            for member in addForm:
                if member == 'submit_button':
                    continue
                else:
                    addList.append(addForm[member])
            print(addList, len(addList))
            database.ytDBStart(addList)

        elif request.form['submit_button'] == "Import": #new
            request.form['ImportFile']
            print("enter")
            return redirect(url_for('import_file')) #change
        
    return render_template('SearchBar.html', testList=testList)

@app.route("/Results", methods = ['GET', 'POST']) # new
def results():
    global testList
    if request.method == 'POST':
            return redirect(url_for('search'))
    return render_template('Results.html', testList=testList)

@app.route("/Import", methods = ['GET','POST'])
def import_file():
    return render_template('Import.html')
    
app.run(debug = True, use_reloader = False)