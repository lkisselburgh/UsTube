from Jparser import *

categoryList = jParser()

class ytDB:
	def __init__(self):
		self.db = dict()
		self.counter = 1 			#video ids are not unique so counter will be keys to dictionary
		self.lastdeletedKey = None
		self.trendCount = dict()	#need this for subclass	
		self.dbnoRepeats = dict()	#this database helps for not having repeats of videos
		self.vidTagLength = dict()	#to keep track of length of tags

	def ytDBStart(self, columns):
		if len(columns) == 16:
			videoD = videoData()

			#tried to make a helper function but caused problems and looked ugly
			for member in categoryList:
				if columns[4] in member:
					catinWords = member[1]


			videoD.setVars(columns[0], columns[1], columns[2], columns[3], catinWords,
							columns[5], columns[6], columns[7], columns[8], columns[9],
							columns[10],columns[11], columns[12], columns[13], columns[14],
							columns[15])
			
			if columns[0] not in self.trendCount:
				self.trendCount[columns[0]] = 1
				tagLength = len(columns[6].split('|'))
				if columns[6] == '[none]':
					self.vidTagLength[columns[0]] = 0
				else:	
					self.vidTagLength[columns[0]] = tagLength
			if columns[0] in self.trendCount:
				self.trendCount[columns[0]] += 1

			
			if(self.db.get(self.lastdeletedKey) == None):
				self.db[self.lastdeletedKey] = videoD

			#
			if columns[0] not in self.dbnoRepeats:
				self.dbnoRepeats[columns[0]] = videoD			

			self.db[self.counter] = videoD
			self.counter += 1
		else: 
			return

	def searchDB(self, titleQuery, cidQuery):
		resultList = []	
		if self.db is None:
			return None

		if titleQuery != "":
			parser = self.db
			displayList = []
			for keys in parser:
				if parser[keys].Title.find(titleQuery) != -1:
					displayList.append([keys,parser[keys]])
			return displayList
		
		if cidQuery != "":
			parser = self.db
			cidList = []
			cidQuery = cidQuery.lower()
			for keys in parser:
				genreID = parser[keys].categoryID
				for members in categoryList:
					if genreID in members:
						nameofCat = members[1].lower()
						if cidQuery in nameofCat or cidQuery == nameofCat:
							cidList.append([keys, parser[keys]])
			return cidList

#		if sliderQuery != "":
#			parser = self.db
#			sliderList = []
#
#			if searchType == "publishTime":
#				for keys in parser:
#					if sliderQuery.lower() == parser[keys].publishTime:
#						sliderList.append[parser[keys]]
#
#			if searchType == "views":
#				for keys in parser:
#					if sliderQuery.lower() == parser[keys].views:
#						sliderList.append[parser[keys]]
#
#			if searchType == "tags":
#				for keys in parser:
#					splitQuery = sliderQuery
#					if ',' in sliderQuery:
#						splitQuery = sliderQuery.split(',')
#					
#					tagSplit = parser[keys].tags.split('|')
#
#					compList = list(set(splitQuery) & set(tagSplit))
#
#					if compList == splitQuery:
#						sliderList.append(parser[keys])
#
#				return sliderList		

		return resultList

	def delete(self,key):
		self.lastdeletedKey = key
		self.db.pop(key, None)

	# def update(key, newData):
	# 	self.db[key]
	
	@property
	def Analytics(self):
		return _Analytics(self)


class _Analytics(object):
	def __init__(self, currentDB):
		self._currentDB = currentDB

	@property
	def trendsTitleList(self):
		model = self._currentDB.db
		tempCount = self._currentDB.trendCount
		tList = list()
		plot = dict()

		if len(model) == 0:
			return None

		for keys in model:
			if model[keys].videoID not in tList:
				vID = model[keys].videoID
				title = model[keys].Title
				key = len(title)
				if key not in plot:
					plot[key] = tempCount[vID]
				else:
					plot[key] += tempCount[vID]
				tList.append(vID)
		return plot

	@property
	def categoryContest(self):
		model = self._currentDB.dbnoRepeats
		tCount = self._currentDB.trendCount
		plot = dict()
		for keys in model:
			catEntry = model[keys].categoryID
			if catEntry not in plot:
				plot[catEntry] = tCount[keys]
			else:
				plot[catEntry] += tCount[keys]
		return plot

	@property
	def tagOccurence(self):
	 	model = self._currentDB.dbnoRepeats
	 	plot = dict()

	 	for key in model:
	 		tags = model[key].tags
	 		splitTag = tags.split('|')
	 		for tag in splitTag:
	 			if tag not in plot:
	 				plot[tag] = 1
 				else:
 					plot[tag] +=1
	 	return plot

	@property
	def tagTrends(self):
		model = self._currentDB.dbnoRepeats
		tagLength = self._currentDB.vidTagLength
		trendNum = self._currentDB.trendCount
		plot = dict()

		for key in model:
			tag = tagLength[key]
			tNum = trendNum[key]
			if tag not in plot:
				plot[tag] = tNum
			else:
				plot[tag] += tNum
		
		return plot
	
	@property
	def timeofDay(self):
		model = self._currentDB.dbnoRepeats
		tempPlot = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12:0 , 13: 0, 14: 0, 15: 0 ,16: 0, 17: 0 , 18: 0, 19: 0, 20: 0 , 21: 0, 22: 0, 23: 0}
		plot = {'12 AM': 0,'1 AM': 0,'2 AM': 0,'3 AM': 0,'4 AM': 0, '5 AM': 0, '6 AM': 0, '7 AM': 0, '8 AM': 0, '9 AM': 0, '10 AM': 0, '11 AM': 0, '12 PM':0 , '1 PM': 0, '2 PM': 0, '3 PM': 0 ,'4 PM': 0, '5 PM': 0 , '6 PM': 0, '7 PM': 0, '8 PM': 0 , '9 PM': 0, '10 PM': 0, '11 PM': 0}
		for key in model:
			time = model[key].publishTime
			time = time.split('T')
			time = time[1].split('.')
			time = time[0].split(':')
			hour = int(time[0])
			tempPlot[hour] += 1

		for key1, key2 in zip(tempPlot, plot):
			plot[key2] = tempPlot[key1]

		return plot

	@property
	def enabledVDisabled(self):
		model = self._currentDB.dbnoRepeats
		plot = [0, 0]

		for key in model:
			enaoDis = model[key].comDisabled
			if enaoDis == 'True':
				plot[0] +=1
			else:
				plot[1] +=1
		return plot
	
	@property
	def descriptionVViews(self):
		def sortSecond(val):
			return val[0]

		model = self._currentDB.dbnoRepeats
		plot = list()
		for key in model:
			viewsNew = int(model[key].views)
			descripLength = len(model[key].description.split(' '))
			if descripLength <= 850 and viewsNew <= 20000000:
				plot.append([descripLength, viewsNew])
		plot.sort(key = sortSecond)
		return plot
	
	
#added class 
class videoData(object):
	def __init__(self):
		self.videoID = str()
		self.trendingDate = str() 
		self.Title = str()
		self.channelTitle = str()
		self.categoryID = str()
		self.publishTime = str()
		self.tags = str()
		self.views = str()
		self.likes = str()
		self.dislikes = str()
		self.commentCount = str()
		self.thumbLink = str()
		self.comDisabled = str()
		self.ratingsDisabled = str()
		self.videoEOR = str()
		self.description = str()
		
	def setVars(self, videoID, trendingDate, Title, channelTitle, categoryID,
				publishTime, tags, views, likes, dislikes, commentCount,
				thumbLink, comDisabled, ratingsDisabled, videoEOR, description):
		self.videoID = videoID
		self.trendingDate = trendingDate 
		self.Title = Title
		self.channelTitle = channelTitle
		self.categoryID = categoryID
		self.publishTime = publishTime
		self.tags = tags
		self.views = views
		self.likes = likes
		self.dislikes = dislikes
		self.commentCount = commentCount
		self.thumbLink = thumbLink
		self.comDisabled = comDisabled
		self.ratingsDisabled = ratingsDisabled
		self.videoEOR = videoEOR
		self.description = description