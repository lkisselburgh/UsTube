import os
import re
from db import *


#class ImpExp:

# def export():
#     global database
#     expF = open("UsTube.csv", "w")
#     for entry in database.db:
#         print(entry[1].videoID)



# def parseNew(newfilename):
#     global database
#     prev_row = []
#     temp = 0; skip_header = 0
#     correct = True

#     if (newfilename[-4:] == ".csv" or newfilename[-4:] == ".CSV"):
#         with open(newfilename, errors='ignore') as data:
#             for row in data:
#                 if (skip_header == 0):
#                     skip_header = 1
#                     headers = row.split(',')

#                     #checks to make sure headers match
#                     if (len(headers) != 16) :
#                         print("Error, CSV file is not formatted correctly.")
#                         correct = False			
#                     else :
#                         if(headers[0] != "video_id") :
#                             print("Error, Column 1 is not video_id")
#                             correct = False			
#                         if (headers[1] != "trending_date") :
#                             print("Error, Column 2 is not trending_date")
#                             correct = False			
#                         if (headers[2] != "title") :
#                             print("Error, Column 3 is not title")
#                             correct = False			
#                         if (headers[3] != "channel_title") :
#                             print("Error, Column 4 is not channel_title")
#                             correct = False			
#                         if (headers[4] != "category_id") :
#                             print("Error, Column 5 is not category_id")
#                             correct = False			
#                         if (headers[5] != "publish_time") :
#                             print("Error, Column 6 is not publish_time")
#                             correct = False			
#                         if (headers[6] != "tags") :
#                             print("Error, Column 7 is not tags")
#                             correct = False			
#                         if (headers[7] != "views") :
#                             print("Error, Column 8 is not views")
#                             correct = False							
#                         if (headers[8] != "likes") :
#                             print("Error, Column 9 is not likes")
#                             correct = False							
#                         if (headers[9] != "dislikes") :
#                             print("Error, Column 10 is not dislikes")
#                             correct = False							
#                         if (headers[10] != "comment_count") :
#                             print("Error, Column 11 is not comment_count")
#                             correct = False							
#                         if (headers[11] != "thumbnail_link") :
#                             print("Error, Column 12 is not thumbnail_link")	
#                             correct = False						
#                         if (headers[12] != "comments_disabled") :
#                             print("Error, Column 13 is not comments_disabled")
#                             correct = False							
#                         if (headers[13] != "ratings_disabled") :
#                             print("Error, Column 14 is not ratings_disabled")
#                             correct = False							
#                         if (headers[14] != "video_error_or_removed") :
#                             print("Error, Column 15 is not video_error_or_removed")
#                             correct = False							
#                         if (headers[15] != "description\n") :
#                             print("Error, Column 16 is not description\n")
#                             correct = False
#                         if (correct == False):
#                             return database
#                         else:
#                             del database
#                             database = ytDB()		

#                 else :
#                     count = 0
#                     count = row.count('"')
                    
#                     if (count % 2 == 0 and count != 0):
#                         fields = re.split((",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"), row)
#                         database.ytDBStart(fields)
                    
#                     else:  
#                         if (temp == 0):
#                             temp = 1
#                             prev_row = row
                        
#                         else:
#                             prev_row = prev_row + row
#                             if (count == 1):
#                                 temp = 0
#                                 prev_row = prev_row.replace("\r"," ")
#                                 prev_row = prev_row.replace("\n"," ")
#                                 fields = re.split((",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"), prev_row)
#                                 database.ytDBStart(fields)
#             print("In Function: database: " + database.db[1].Title)
#             return database
#     else:
#         print("File must be .csv")
#         return database