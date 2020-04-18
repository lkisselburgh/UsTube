import os
import re
import csv

CSVFile = os.getcwd()
quotation = 0
uID = ""

with open(os.path.join(CSVFile,"CSVFile/USvideos.csv"), "r") as csvFile:
	prev_row = []
	rowCount = 0
	for row in csvFile:

		fields = re.split((',(?=(?:[^\"]*\"[^\"]*\")*[^\"]$)'), row)
		count = 1
		if len(fields) < 16:
			rowCount +=1
			for members in fields:
				print(rowCount)
				print (count, members)
				count += 1

	# 	count = 0
	# 	dbList = []
	# 	for member in row.split(','):
	# 		if '"' in member and member.count('"') % 2 != 0:
	# 			index = count 
	# 			quotation += 1
	# 			var = member
	# 		elif (quotation % 2) != 0:
				
	# 		else:
	# 			var = member

	# 		count += 1
	# 	dbList.append(var)	


