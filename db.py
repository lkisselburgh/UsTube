class ytDB:
	def __init__(self):
		self.db = dict()
		self.videoData = self.videoData()
		self.counter = 1 #video ids are not unique so counter will be keys to dictionary

	def ytDBStart(self, columns):
		if len(columns) == 16:
			self.videoData.setVars(columns[0], columns[1], columns[2], columns[3], columns[4],
							columns[5], columns[6], columns[7], columns[8], columns[9],
							columns[10],columns[11], columns[12], columns[13], columns[14],
							columns[15])
			self.db[self.counter] = self.videoData
			self.counter += 1
		else: 
			return

	# def searchDB(self, uID):
	# 	if self.db is None or self.db[]:
	# 		return None
	# 	else:
	# 		for unique in self.db:
	# 			if unique is uID:
	# 				print(self.db[uID])


	# def add():

	# def delete();

	# def update():

	#added inner class to make content retrieval and search easier
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