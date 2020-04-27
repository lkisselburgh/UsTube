from Jparser import *

categoryList = jParser()

class ytDB:
	def __init__(self):
		self.db = dict()
		self.counter = 1 #video ids are not unique so counter will be keys to dictionary
		self.lastdeletedKey = None

	def ytDBStart(self, columns):
		if len(columns) == 16:
			videoD = videoData()
			videoD.setVars(columns[0], columns[1], columns[2], columns[3], columns[4],
							columns[5], columns[6], columns[7], columns[8], columns[9],
							columns[10],columns[11], columns[12], columns[13], columns[14],
							columns[15])

			if(self.db.get(lastdeletedKey) == None):
				self.db[lastdeletedKey] = videoD
			self.db[self.counter] = videoD
			self.counter += 1
		else: 
			return

	def searchDB(self, titleQuery, cidQuery, searchType, sliderQuery):
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

		if sliderQuery != "":
			parser = self.db
			sliderList = []

			if searchType == "publishTime":
				for keys in parser:
					if sliderQuery.lower() == parser[keys].publishTime:
						sliderList.append[parser[keys]]

			if searchType == "views":
				for keys in parser:
					if sliderQuery.lower() == parser[keys].views:
						sliderList.append[parser[keys]]

			if searchType == "tags":
				for keys in parser:
					splitQuery = sliderQuery
					if ',' in sliderQuery:
						splitQuery = sliderQuery.split(',')
					
					tagSplit = parser[keys].tags.split('|')

					compList = list(set(splitQuery) & set(tagSplit))

					if compList == splitQuery:
						sliderList.append(parser[keys])

				return sliderList		

		return resultList

	def delete(key):
		self.lastdeletedKey = key
		self.db.pop(key, None)

	def update(key, newData):

		self.db[key]

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