from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, make_response, send_file, flash
from CSVparser import *
from werkzeug.utils import secure_filename
import os
from io import StringIO
from analyticsClass import *
import time
#from analyticsStore import *
import plotly.graph_objects as go
#from flask_uploads import UploadSet, configure_uploads, IMAGES

#from flask_uploads import UploadSet, configure_uploads

#create database object
database = ytDB()
anStore = AnalyticStorage()
#input data into database
parser(database, anStore)

testList = ""

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#app = Flask(__name__, static_folder='static')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'lacey copy and pasted this'
firstRender = True
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
    global firstRender
    analyticsobj = analyticsDisplay()
    layout = {}
    if (firstRender):
        tic = time.perf_counter()
        plotList = anStore.trendsTitle
        #plotList = database.Analytics.trendsTitleList
        displayObj = analyticsobj.displayLongerTitles(plotList)
        toc = time.perf_counter()
        print("Finished in " , toc - tic, "seconds")
        flash("Time elapsed: " + str(toc - tic) + " seconds")
        analyticNum = '1'
        firstRender=False
    else:
        if request.method == 'POST':
            analyticNum = request.form['select']
            if analyticNum == '1':
                tic = time.perf_counter()
                plotList = database.Analytics.trendsTitleList
                plotList = anStore.trendsTitle
                displayObj = analyticsobj.displayLongerTitles(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '2':
                tic = time.perf_counter()
                #plotList = database.Analytics.categoryContest
                plotList = anStore.categoryTrends
                displayObj = analyticsobj.displayCategory(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '3':
                tic = time.perf_counter()
                plotList = anStore.tagDisplay
                #plotList = database.Analytics.tagOccurence
                displayObj = analyticsobj.displayTopTags(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '4':
                tic = time.perf_counter()
                plotList = anStore.tagTrends
                #plotList = database.Analytics.tagTrends
                displayObj = analyticsobj.displayTagLength(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '5':
                tic = time.perf_counter()
                plotList = anStore.timeoDay
                #plotList = database.Analytics.timeofDay
                displayObj = analyticsobj.displayTimeODay(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '6':
                tic = time.perf_counter()
                #plotList = database.Analytics.enabledVDisabled
                plotList = anStore.enVdis
                displayObj = analyticsobj.displayComments(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '7':
                tic = time.perf_counter()
                #plotList = database.Analytics.descriptionVViews
                plotList = anStore.descripVviews
                displayObj = analyticsobj.displayDesvViews(plotList)
                #print(displayObj)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '8':
                tic = time.perf_counter()
                #plotList = database.Analytics.channelOccurence
                plotList = anStore.channels
                displayObj = analyticsobj.displayTopChannels(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False
                
            elif analyticNum == '9':
                tic = time.perf_counter()
                #plotList = database.Analytics.avgRating
                plotList = anStore.ratings
                displayObj = analyticsobj.displayAvgRatings(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

            elif analyticNum == '10':
                tic = time.perf_counter()
                #plotList = database.Analytics.timeofYear
                plotList = anStore.read_topMonthlyGenres()
                displayObj = analyticsobj.displayTimeOfYear(plotList)
                toc = time.perf_counter()
                print("Finished in " , toc - tic, "seconds")
                flash("Time elapsed: " + str(toc - tic) + " seconds")
                firstRender = False

    return render_template('Analytics.html', plot=displayObj, analyticNum=analyticNum)


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
            
        
        elif request.form['submit_button'] == 'Submit':
            print("Submit button was pressed.")

    return render_template('Import.html')

@app.route("/Export", methods = ['GET','POST'])
def export():
    global database
    
    expF = open("UsTube.csv", "w")
    expF.write("video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description\n")
    
    for keys in database.db:
        #print(database.db[keys].Title)
        expF.write(database.db[keys].videoID)
        expF.write(',')
        expF.write(database.db[keys].trendingDate)
        expF.write(',')
        expF.write(database.db[keys].Title)
        expF.write(',')
        expF.write(database.db[keys].channelTitle)
        expF.write(',')
        expF.write(database.db[keys].categoryID)
        expF.write(',')
        expF.write(database.db[keys].publishTime)
        expF.write(',')
        expF.write(database.db[keys].tags)
        expF.write(',')
        expF.write(database.db[keys].views)
        expF.write(',')
        expF.write(database.db[keys].likes)
        expF.write(',')
        expF.write(database.db[keys].dislikes)
        expF.write(',')
        expF.write(database.db[keys].commentCount)
        expF.write(',')
        expF.write(database.db[keys].thumbLink)
        expF.write(',')
        expF.write(database.db[keys].comDisabled)
        expF.write(',')
        expF.write(database.db[keys].ratingsDisabled)
        expF.write(',')
        expF.write(database.db[keys].videoEOR)
        expF.write(',')
        expF.write(database.db[keys].description)
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
                        
                        #print(database there)
                        database.ytDBStart(fields)
                        #print(fields)
                    
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
                                #print(fields)
            
            return database
    else:
        print("File must be .csv")
        return database

#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'],
                               #filename)
    
app.run(debug = True, use_reloader = False)