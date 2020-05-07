import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

class analyticsDisplay:
		def __init__(self):
			self.helper = str()

		def displayLongerTitles(self, listData):
			dictItems = list(listData.items())
			arr = np.array(dictItems)
			#N = 14
			#x = np.linspace(0, 1, N)
			#y = np.random.randn(N)
			df = pd.DataFrame(arr, columns=['Length','TrendAmount']) # creating a sample dataframe


			data = [
				go.Bar(
					x=df['Length'], # assign x as the dataframe column 'x'
					y=df['TrendAmount'],
					marker_color='black'
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
					marker_color='black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	
			return Jobj
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
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

			return Jobj	

		def displayTimeOfYear(self, listData):
			#listData is a dictionary with each value being another dictionary with the top 3 genres of that month
			# {'January': {'Entertainment': 122, 'Music': 100, 'People': 85}, 'February': {'Entertainment': 122, ...} ...} etc
			
			dictItems = list(listData.items())
			dtype = [('Month', 'U30'), ('Genre', str), ('Amount', int)]
			arr = np.array(dictItems, dtype=dtype)
			df = pd.DataFrame(arr) # creating a sample dataframe

			data = [
				go.Bar(
					x=df['Month'], # assign x as the dataframe column 'x'
					y=df['TrendingCount'],
					marker_color = 'black'
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	

			return Jobj