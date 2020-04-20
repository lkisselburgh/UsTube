import json
import os

def jParser():
	categoryList = []
	filename = os.getcwd()
	with open(os.path.join(filename,"CSVFile/US_category_id.json"), "r", errors='ignore') as data:
		jsonObj = json.load(data)

		itemList = jsonObj['items']
		for members in itemList:
			cID = members['id']
			catName = members['snippet']['title']
			categoryList.append([cID, catName])

		return categoryList