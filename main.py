from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, make_response, send_file
from CSVparser import *
from imp_exp import *
from werkzeug.utils import secure_filename
import os
from io import StringIO
from analyticsClass import *
import plotly.graph_objects as go
#from flask_uploads import UploadSet, configure_uploads, IMAGES

#from flask_uploads import UploadSet, configure_uploads

#create database object
database = ytDB()
#input data into database
parser(database)

testList = ""

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#app = Flask(__name__, static_folder='static')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#csv_file = UploadSet('files', ('csv'))
#configure_uploads(app, csv_file)

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
            return redirect(url_for('import_file')) #change

        elif request.form['submit_button'] == "Export": #new
            print("Exporting file...")
            #export()
            return redirect(url_for('export'))
        
    return render_template('SearchBar.html', testList=testList)

# @app.route('/return-file/')
# def send_file(filename):
#     return send_from_directory(app.static_folder, filename)

@app.route("/Results", methods = ['GET', 'POST']) # new
def results():
    global testList
    if request.method == 'POST':
            return redirect(url_for('search'))
    return render_template('Results.html', testList=testList)

@app.route("/Analytics", methods = ['GET','POST'])
def analytics():
    analyticsobj = analyticsDisplay()
    plotList = database.Analytics.trendsTitleList
    displayObj = analyticsobj.displayLongerTitles(plotList)
    analyticNum = '1'
    if request.method == 'POST':
        analyticNum = request.form['select']
        if analyticNum == '1':
            analyticsobj = analyticsDisplay()
            plotList = database.Analytics.trendsTitleList
            displayObj = analyticsobj.displayLongerTitles(plotList)
        elif analyticNum == '2':
            analyticsobj = analyticsDisplay()
            plotList = database.Analytics.categoryContest
            displayObj = analyticsobj.displayCategory(plotList)
    return render_template('Analytics.html', plot=displayObj, analyticNum=analyticNum)

# @app.route('/Download') #new
# def post(self):
#     si = StringIO.StringIO()
#     cw = csv.writer(si)
#     cw.writerows(csvList)
#     output = make_response(si.getvalue())
#     output.headers["Content-Disposition"] = "attachment; filename=export.csv"
#     output.headers["Content-type"] = "text/csv"
#     return output

@app.route("/Import", methods = ['GET','POST'])
def import_file():
    if request.method == 'POST':
        #global database
        file = request.files['file']

        # if 'file' not in request.files:
        #     print("No file part.")
        #     return redirect(request.url)

        if request.form['submit_button'] == 'Return': #new
            return redirect(url_for('search'))

        if file.filename == '':
            print("No selected file.")
            return redirect(request.url)

        if file:
            file.save(secure_filename(file.filename))
            #return print(file.filename)
            #return file.filename
            parseNew(file.filename)
            #database.ytDBStart(database, file.filename)
            #print("database: " + database.db[1].Title)
        
        elif request.form['submit_button'] == 'Submit':
            print("Submit button was pressed.")
            #parseNew(file.filename)

    return render_template('Import.html')

@app.route("/Export", methods = ['GET','POST'])
def export():
    global database
    expF = open("UsTube.csv", "w")
    expF.write("video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description\n")
    
    for k in range(1,database.counter):
        #print(database.db[k].videoID)
        expF.write(database.db[k].videoID)
        expF.write(',')
        expF.write(database.db[k].trendingDate)
        expF.write(',')
        expF.write(database.db[k].channelTitle)
        expF.write(',')
        expF.write(database.db[k].categoryID)
        expF.write(',')
        expF.write(database.db[k].publishTime)
        expF.write(',')
        expF.write(database.db[k].tags)
        expF.write(',')
        expF.write(database.db[k].views)
        expF.write(',')
        expF.write(database.db[k].likes)
        expF.write(',')
        expF.write(database.db[k].dislikes)
        expF.write(',')
        expF.write(database.db[k].commentCount)
        expF.write(',')
        expF.write(database.db[k].thumbLink)
        expF.write(',')
        expF.write(database.db[k].comDisabled)
        expF.write(',')
        expF.write(database.db[k].ratingsDisabled)
        expF.write(',')
        expF.write(database.db[k].videoEOR)
        expF.write(',')
        expF.write(database.db[k].description)
        #expF.write('\n')
    expF.close()
    
    print("In progress...")

    fname = "UsTube.csv"
    return send_file(fname, as_attachment=True)

def parseNew(newfilename):
    global database
    prev_row = []
    temp = 0; skip_header = 0
    correct = True

    if (newfilename[-4:] == ".csv" or newfilename[-4:] == ".CSV"):
        with open(newfilename, errors='ignore') as data:
            for row in data:
                if (skip_header == 0):
                    skip_header = 1
                    headers = row.split(',')

                    #checks to make sure headers match
                    if (len(headers) != 16) :
                        print("Error, CSV file is not formatted correctly.")
                        correct = False			
                    else :
                        if(headers[0] != "video_id") :
                            print("Error, Column 1 is not video_id")
                            correct = False			
                        if (headers[1] != "trending_date") :
                            print("Error, Column 2 is not trending_date")
                            correct = False			
                        if (headers[2] != "title") :
                            print("Error, Column 3 is not title")
                            correct = False			
                        if (headers[3] != "channel_title") :
                            print("Error, Column 4 is not channel_title")
                            correct = False			
                        if (headers[4] != "category_id") :
                            print("Error, Column 5 is not category_id")
                            correct = False			
                        if (headers[5] != "publish_time") :
                            print("Error, Column 6 is not publish_time")
                            correct = False			
                        if (headers[6] != "tags") :
                            print("Error, Column 7 is not tags")
                            correct = False			
                        if (headers[7] != "views") :
                            print("Error, Column 8 is not views")
                            correct = False							
                        if (headers[8] != "likes") :
                            print("Error, Column 9 is not likes")
                            correct = False							
                        if (headers[9] != "dislikes") :
                            print("Error, Column 10 is not dislikes")
                            correct = False							
                        if (headers[10] != "comment_count") :
                            print("Error, Column 11 is not comment_count")
                            correct = False							
                        if (headers[11] != "thumbnail_link") :
                            print("Error, Column 12 is not thumbnail_link")	
                            correct = False						
                        if (headers[12] != "comments_disabled") :
                            print("Error, Column 13 is not comments_disabled")
                            correct = False							
                        if (headers[13] != "ratings_disabled") :
                            print("Error, Column 14 is not ratings_disabled")
                            correct = False							
                        if (headers[14] != "video_error_or_removed") :
                            print("Error, Column 15 is not video_error_or_removed")
                            correct = False							
                        if (headers[15] != "description\n") :
                            print("Error, Column 16 is not description\n")
                            correct = False
                        if (correct == False):
                            return database
                        else:
                            del database
                            database = ytDB()		

                else :
                    count = 0
                    count = row.count('"')
                    
                    if (count % 2 == 0 and count != 0):
                        fields = re.split((",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"), row)
                        database.ytDBStart(fields)
                    
                    else:  
                        if (temp == 0):
                            temp = 1
                            prev_row = row
                        
                        else:
                            prev_row = prev_row + row
                            if (count == 1):
                                temp = 0
                                prev_row = prev_row.replace("\r"," ")
                                prev_row = prev_row.replace("\n"," ")
                                fields = re.split((",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"), prev_row)
                                database.ytDBStart(fields)
            
            return database
    else:
        print("File must be .csv")
        return database

#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'],
                               #filename)
    
app.run(debug = True, use_reloader = False)