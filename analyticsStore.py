from Jparser import *

class AnalyticStorage:
	def __init__(self):
		self.enVdis = [0, 0]
		self.descripVviews = list()
		self.channels = dict()
		self.ratings = dict()
		self.monthlyGenres = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}}
		self.trendsList = list()
		self.trendsTitle = dict()
		self.categoryTrends = dict()
		

	def add_trendsTitleCat(self, fields):
		#Analytic 1
		vID = fields.videoID
		title = fields.Title 
		key = len(title)
		if key not in self.trendsTitle:
			self.trendsTitle[key] = 1
		else:
			self.trendsTitle[key] += 1

		#Analytic 2
		catEntry = fields.categoryID
		if catEntry not in self.categoryTrends:
			self.categoryTrends[catEntry] = 1
		else:
			self.categoryTrends[catEntry] += 1


	def add(self, fields):

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




	

