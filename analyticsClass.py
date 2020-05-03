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
					y=df['TrendAmount']
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
					y=df['Amount']
				)
			]

			Jobj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)	
			return Jobj

