import xml.etree.ElementTree as ET
import configparser
from internalParseXML import internalParseXML
from Lanservice import Lanservice


class parseXML:
	#__internObj
	#__externalObj
	#__tree
	#__code
	#__language
	#__configObj
	#__service

	def __init__(self):

		
		self.__tree = ET.parse("XMLFile.xml")
		
		self.__code = "";
		
		self.__configObj = configparser.RawConfigParser()
		self.__configObj.read("mapperConfig.conf");
		self.__language = self.__configObj.get('my-config', 'langauge')
		
		self.setServiceObj()
		self.__extension = self.__configObj.get('my-config', 'extension')
		self.__internalObj = internalParseXML(self.__service)
		self.__externalObj = self.get_class(self.__configObj.get('my-config', 'package')) (self.__service)
		

	def start(self):
		
		self.__internalObj.startParsing()
		self.__externalObj.startParsing()
		l = self.__service.getSentences()
		self.writeListInFile(l);		

	def writeListInFile(self,li):
		f = open("sourceCode."+self.__extension, 'w')
		for x in li:
			for i in range(x[1]):
				f.write("\t")
			f.write(x[0])
			f.write("\n")


	def __callForChildRec(self,node):
		methodName = node.tag + "Tag"
		if(methodName in dir(__internalObj)):
			__code += eval("__internalObj."+node.tag)
		for child in node:
			__callForChildRec(child)

	def setServiceObj(self):
		self.__service = Lanservice(self)

	def __parseFor(self):
		root = self.__tree.getroot()
		__callForChildRec(root)

	def get_class( self,kls ):
	    parts = kls.split('.')
	    module = ".".join(parts[:-1])
	    m = __import__( module )
	    for comp in parts[1:]:
	        m = getattr(m, comp)            
	    return m


	def getRoot(self):
		return self.__tree.getroot()

def mapperMain():
	obj = parseXML()
	obj.start()

mapperMain()
