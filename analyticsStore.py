from Jparser import *

class AnalyticStorage:
	def __init__(self):
		self.enVdis = [0, 0]
		self.channels = dict()
		self.channels_rank = []

	def add(self, fields):
		#Analytic 6: comments enabled vs disabled
		if fields[12] == 'True':
			self.enVdis[0] += 1
		else:
			self.enVdis[1] += 1

		#Analytic 8: top channels
		channel = fields[3]
		if channel not in self.channels:
			self.channels[channel] = 1
			self.channels_rank.append(channel)
		else:
			self.channels[channel] += 1
			#find new rank
			oldindex = self.channels_rank.index(channel)
			if (oldindex > 0):
				newindex = oldindex
				while (self.channels[channel] > self.channels[self.channels_rank[newindex - 1]]):
					newindex -= 1
				if newindex != oldindex:
					self.channels_rank.insert(newindex, self.channels_rank.pop(oldindex))
				
		
	def read_enVdis(self):
		return self.enVdis

	def read_top50Channels(self):
		topChannels = dict()
		for i in range(50):
			key = self.channels_rank[i]
			topChannels[key] = self.channels[key]
		#print(topChannels)
		return topChannels

	

