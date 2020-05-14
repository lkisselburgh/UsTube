import os
import re
from db import *


def parser(database, anStore):
	filename = os.getcwd()
	prev_row = []
	temp = 0; skip_header = 0

	with open(os.path.join(filename,"CSVFile/USvideos.csv"), "r", errors='ignore') as data:
		for row in data:
			if (skip_header == 0):
				skip_header = 1
				
			else :
				count = 0
				count = row.count('"')
				
				if (count % 2 == 0 and count != 0):
					fields = re.split((",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"), row)
					
					database.ytDBStart(fields, anStore)
					#anStore.add(fields)
				
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
							
							database.ytDBStart(fields, anStore)
							#anStore.add(fields)
	