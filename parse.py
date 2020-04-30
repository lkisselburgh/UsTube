import os
import re
from db import *

def parser(database):
	filename = os.getcwd()
	prev_row = []
	temp = 0; skip_header = 0

	with open(os.path.join(filename,"CSVFile/USvideos.csv"), "r", errors='ignore') as data:
		for row in data:
			if (skip_header == 0):
				skip_header = 1
				headers = row.split(', ')

				if (len(headers) != 16) :
					print("Error, CSV file is not formatted correctly.")
					#EXIT			
				else :
					if(headers[0] != "video_id") :
						print("Error, Column 1 is not video_id")
					if (headers[1] != "trending_date") :
						print("Error, Column 2 is not trending_date")
					if (headers[2] != "title") :
						print("Error, Column 3 is not title")
					if (headers[3] != "channel_title") :
						print("Error, Column 4 is not channel_title")
					if (headers[4] != "category_id") :
						print("Error, Column 5 is not category_id")
					if (headers[5] != "publish_time") :
						print("Error, Column 6 is not publish_time")
					if (headers[6] != "tags") :
						print("Error, Column 7 is not tags")
					if (headers[7] != "views") :
						print("Error, Column 8 is not views")				
					if (headers[8] != "likes") :
						print("Error, Column 9 is not likes")				
					if (headers[9] != "dislikes") :
						print("Error, Column 10 is not dislikes")				
					if (headers[10] != "comment_count") :
						print("Error, Column 11 is not comment_count")				
					if (headers[11] != "thumbnail_link") :
						print("Error, Column 12 is not thumbnail_link")				
					if (headers[12] != "comments_disabled") :
						print("Error, Column 13 is not comments_disabled")				
					if (headers[13] != "ratings_disabled") :
						print("Error, Column 14 is not ratings_disabled")				
					if (headers[14] != "video_error_or_removed") :
						print("Error, Column 15 is not video_error_or_removed")				
					if (headers[15] != "description") :
						print("Error, Column 16 is not description")
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