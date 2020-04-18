class ytDB:
	def __init__(self):
		self.db = dict()

	def ytDBStart(self, uID, columns):
		if uID not in self.db:
			self.db[uID] = columns

	def searchDB(self, uID):
		if self.db is None or self.db[]:
			return None
		else:
			for unique in self.db:
				if unique is uID:
					print(self.db[uID])


	# def add():

	# def delete();

	# def update():

