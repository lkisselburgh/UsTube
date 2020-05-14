import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import json

class analyticsDisplay:
		def __init__(self):
			self.helper = str()

		def displayLongerTitles(self, listData):
			dictItems = list(listData.items())
			arr = np.array(dictItems)
			df = pd.DataFrame(arr, columns=['Length','TrendAmount']) # creating a sample dataframe

			data = [
				go.Bar(
					x=df['Length'], # assign x as the dataframe column 'x'
					y=df['TrendAmount'],
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	
			return Jobj

		def displayCategory(self, listData):
			dictItems = list(listData.items())
			dtype = [('CategoryName', 'U30'), ('Amount', int)]
			arr = np.array(dictItems, dtype=dtype)
			arr = np.sort(arr, order='Amount')
			df = pd.DataFrame(arr) # creating a sample dataframe

			data = [
				go.Bar(
					x=df['CategoryName'], # assign x as the dataframe column 'x'
					y=df['Amount'],
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	
			return Jobj

		def displayTopTags(self, listData):
			dictItems = list(listData.items())
			dtype = [('Tag', 'U30'), ('Amount', int)]
			arr = np.array(dictItems, dtype=dtype)
			arr = np.sort(arr, order='Amount')
			lastArr = len(arr)
			topFifty = lastArr - 50
			arr = arr[topFifty:lastArr]
			df = pd.DataFrame(arr) # creating a sample dataframe
			data = [
				go.Bar(
					x=df['Tag'], # assign x as the dataframe column 'x'
					y=df['Amount'],
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	

			return Jobj

		def displayTagLength(self,listData):
			dictItems = list(listData.items())
			dtype = [('TagLength', 'U30'), ('TrendingCount', int)]
			arr = np.array(dictItems, dtype=dtype)
			arr = np.sort(arr, order='TagLength')
			df = pd.DataFrame(arr) # creating a sample dataframe

			data = [
				go.Bar(
					x=df['TagLength'], # assign x as the dataframe column 'x'
					y=df['TrendingCount'],
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	

			return Jobj

		def displayTimeODay(self, listData):
			dictItems = list(listData.items())
			dtype = [('Hour', 'U30'), ('TrendingCount', int)]
			arr = np.array(dictItems, dtype=dtype)
			df = pd.DataFrame(arr) # creating a sample dataframe

			data = [
				go.Bar(
					x=df['Hour'], # assign x as the dataframe column 'x'
					y=df['TrendingCount'],
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	

			return Jobj
		def displayComments(self, listData):
			data = [
				go.Pie(
					labels = ['Disabled', 'Enabled'],
					values = listData,
					marker = dict(colors=['Red','Black'])  
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	

			return Jobj

		def displayDesvViews(self, listData):
			df = pd.DataFrame(listData, columns=['Description', 'Views']) # creating a sample dataframe

			data = [
				go.Scatter(
					x=df['Description'], # assign x as the dataframe column 'x'
					y=df['Views'],
					mode = 'markers',
					marker_color = 'black'
				),
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	

			return Jobj

		def displayTopChannels(self, listData):
			dictItems = list(listData.items())
			dtype = [('Channel', 'U30'), ('Amount', int)]
			arr = np.array(dictItems, dtype=dtype)
			arr = np.sort(arr, order='Amount')
			lastArr = len(arr)
			topFifty = lastArr - 50
			arr = arr[topFifty:lastArr]
			df = pd.DataFrame(arr)
			data = [
				go.Bar(
					x=df['Channel'],
					y=df['Amount'],
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

			return Jobj

		def displayAvgRatings(self, listData):
			dictItems = list(listData.items())
			dtype = [('Rating', 'U30'), ('Amount', int)]
			arr = np.array(dictItems, dtype=dtype)
			df = pd.DataFrame(arr)
			data = [
				go.Bar(
					x=df['Rating'],
					y=df['Amount'],
					marker_color = 'black',
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

			return Jobj	

		def displayTimeOfYear(self, listData):
			#listData is a dictionary with each value being another dictionary with the top 3 genres of that month
			# {'January': {'Entertainment': 122, 'Music': 100, 'People': 85}, 'February': {'Entertainment': 122, ...} ...} etc
			
			dictItems = list(listData.items())
			#print(dictItems)

			# print(dictItems)
			months = []
			genres = []
			gdata = []
			for month in dictItems:
				months.append(month[0])
				#genres.append(month[1][0])
				gdata.append(month[1])
			# print("months", months)
			#print("data", gdata)

			dtype = [('Genre', 'U30'), ('TrendingCount', int)]
			arr = np.array(gdata[0], dtype=dtype)
			#print(arr)
			df = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre2', 'U30'), ('TrendingCount2', int)]
			arr = np.array(gdata[1], dtype=dtype)
			#print(arr)
			df2 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre3', 'U30'), ('TrendingCount3', int)]
			arr = np.array(gdata[2], dtype=dtype)
			df3 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre4', 'U30'), ('TrendingCount4', int)]
			arr = np.array(gdata[3], dtype=dtype)
			df4 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre5', 'U30'), ('TrendingCount5', int)]
			arr = np.array(gdata[4], dtype=dtype)
			df5 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre6', 'U30'), ('TrendingCount6', int)]
			arr = np.array(gdata[5], dtype=dtype)
			df6 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre7', 'U30'), ('TrendingCount7', int)]
			arr = np.array(gdata[6], dtype=dtype)
			df7 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre8', 'U30'), ('TrendingCount8', int)]
			arr = np.array(gdata[7], dtype=dtype)
			df8 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre9', 'U30'), ('TrendingCount9', int)]
			arr = np.array(gdata[8], dtype=dtype)
			df9 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre10', 'U30'), ('TrendingCount10', int)]
			arr = np.array(gdata[9], dtype=dtype)
			df10 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre11', 'U30'), ('TrendingCount11', int)]
			arr = np.array(gdata[10], dtype=dtype)
			df11 = pd.DataFrame(arr) # creating a sample dataframe

			dtype = [('Genre12', 'U30'), ('TrendingCount12', int)]
			arr = np.array(gdata[11], dtype=dtype)
			df12 = pd.DataFrame(arr) # creating a sample dataframe

			data = [
				go.Bar(
					x=df['Genre'], # assign x as the dataframe column 'x'
					y=df['TrendingCount'],
					marker_color = 'midnightblue',
					name = "January"
				),
				go.Bar(
					x=df2['Genre2'],
					y=df2['TrendingCount2'],
					marker_color = 'plum',
					name = "February"
				),
				go.Bar(
					x=df3['Genre3'],
					y=df3['TrendingCount3'],
					marker_color = 'hotpink',
					name = "March"
				),
				go.Bar(
					x=df4['Genre4'],
					y=df4['TrendingCount4'],
					marker_color = 'darkviolet',
					name = "April"
				),

				go.Bar(
					x=df5['Genre5'],
					y=df5['TrendingCount5'],
					marker_color = 'cyan',
					name = "May"
				),

				go.Bar(
					x=df6['Genre6'],
					y=df6['TrendingCount6'],
					marker_color = 'maroon',
					name = "June"
				),

				go.Bar(
					x=df7['Genre7'],
					y=df7['TrendingCount7'],
					marker_color = 'orangered',
					name = "July"
				),

				go.Bar(
					x=df8['Genre8'],
					y=df8['TrendingCount8'],
					marker_color = 'magenta',
					name = "August"
				),

				go.Bar(
					x=df9['Genre9'],
					y=df9['TrendingCount9'],
					marker_color = 'darksalmon',
					name = "September"
				),

				go.Bar(
					x=df10['Genre10'],
					y=df10['TrendingCount10'],
					marker_color = 'lime',
					name = "October"
				),

				go.Bar(
					x=df11['Genre11'],
					y=df11['TrendingCount11'],
					marker_color = 'lightseagreen',
					name = "November"
				),

				go.Bar(
					x=df12['Genre12'],
					y=df12['TrendingCount12'],
					marker_color = 'forestgreen',
					name = "December"
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	

			return Jobj