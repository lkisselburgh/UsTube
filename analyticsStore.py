from Jparser import *

class AnalyticStorage:
	def __init__(self):
		self.idList = list()
		self.catVDays = dict()
		self.titleLength = dict()
		self.tagDisplay = dict()
		self.tagTrends = dict()
		self.timeoDay = plot = {'12 AM': 0,'1 AM': 0,'2 AM': 0,'3 AM': 0,'4 AM': 0, '5 AM': 0, '6 AM': 0, '7 AM': 0, '8 AM': 0, '9 AM': 0, '10 AM': 0, '11 AM': 0, '12 PM':0 , '1 PM': 0, '2 PM': 0, '3 PM': 0 ,'4 PM': 0, '5 PM': 0 , '6 PM': 0, '7 PM': 0, '8 PM': 0 , '9 PM': 0, '10 PM': 0, '11 PM': 0}	
		self.enVdis = [0, 0]
		self.descripVviews = list()
		self.channels = dict()
		self.ratings = dict()
		self.monthlyGenres = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}}
		

	def add(self, fields):
		if fields.videoID not in self.idList:
	#FIX	#analytic 1: 
			titleLen = len(fields.Title)
			if titleLen not in self.titleLength:
				self.titleLength[titleLen] = 1

	#FIX	#Analytic 2: Category vs Days Trending
			catEntry = fields.categoryID
			if catEntry not in self.catVDays:
				self.catVDays[catEntry] = 1

			#Analytic 3 Tag occurence
			tags = fields.tags
			splitTag = tags.split('|')
			for tag in splitTag:
				if tag not in self.tagDisplay:
					self.tagDisplay[tag] = 1
				else:
					self.tagDisplay[tag] += 1

			#Analytic 4 (TBD)

			#Analytic 5 Best TIme to Trend
			def checkTime(temp):
				self.timeoDay[temp] += 1

			time = fields.publishTime
			time = time.split('T')
			time = time[1].split('.')
			time = time[0].split(':')
			hour = int(time[0])
			if hour > 12:
				hour = hour - 12
				hour = str(hour) + " PM"
				checkTime(hour)
			elif hour == 0:
				hour = "12 AM"
				checkTime(hour)
			elif hour == 12:
				hour = "12 PM"
				checkTime(hour)
			else:
				hour = str(hour) + " AM"
				checkTime(hour)

			#Analytic 6: comments enabled vs disabled
			if fields.comDisabled == 'True':
				self.enVdis[0] += 1
			else:
				self.enVdis[1] += 1

			#Analytic 7: description length vs views
			viewsNew = int(fields.views)
			descripLength = len(fields.description.split(' '))
			if descripLength <= 850 and viewsNew <= 20000000:
				self.descripVviews.append([descripLength, viewsNew])

			#Analytic 8: top channels
			channel = fields.channelTitle
			if channel not in self.channels:
				self.channels[channel] = 1
			else:
				self.channels[channel] += 1

			
			#Analytic 9: average rating
			likes = fields.likes
			dislikes = fields.dislikes
			if (int(likes) == 0 and int(dislikes) == 0):
					rating = 0
			else:
				rating = (int(likes) / (int(dislikes) + int(likes))) * 100
				rating = round(rating)
			if rating not in self.ratings:
				self.ratings[rating] = 1
			else:
				self.ratings[rating] += 1


			#Analytic 10: Genres Throughout Year
			genre = fields.categoryID
			month = fields.publishTime
			month = month.split('T')
			month = month[0].split('-')
			month = int(month[1])
			if genre not in self.monthlyGenres[month]:
				self.monthlyGenres[month][genre] = 1
			else:
				self.monthlyGenres[month][genre] += 1

			self.idList.append(fields.videoID)

		else:
			titleLen = len(fields.Title)
			catEntry = fields.categoryID
			self.titleLength[titleLen] += 1
			self.catVDays[catEntry] += 1


	def read_descripVview(self):
		def sortSecond(val):
			return val[0]
		self.descripVviews.sort(key = sortSecond)
		return self.descripVviews
	
	def read_topMonthlyGenres(self):
		#change keys to months
		plot = {'January': 0,'February': 0,'March': 0,'April': 0,'May': 0, 'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}
		for key1, key2 in zip(self.monthlyGenres, plot):
			plot[key2] = self.monthlyGenres[key1]

		for month in plot:
			temp = {}
			for k in range(3):
				if (plot[month]):
					max_key = max(plot[month], key=plot[month].get)
					temp[max_key] = plot[month][max_key]
					del plot[month][max_key]
					
				k += 1
			
			plot[month] = list(temp.items())

		return plot




	

