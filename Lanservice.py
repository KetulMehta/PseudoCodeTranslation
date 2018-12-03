#here Importing the parseXML class and use it here:

class Lanservice:

	def __init__(self,p):
		self.__p = p
		self.__d = {}
		self.sen = []

	def getVarType(self,x):
		return self.__d[x];

	def addVarType(self,a,b):
		self.__d[a]=b;

	def getRoot(self):
		return self.__p.getRoot()

	def getSentences(self):
		return self.sen

	def addSen(self,a,b):
		#print("ADDING:"+a)
		self.sen.append((a,b));

	#other Service function useful to externalparseXML
