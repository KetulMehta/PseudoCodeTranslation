import xml.etree.ElementTree as ET


#here There will list of tuple that store the variable information

class internalParseXML:

	def __init__(self,s):
		self.__s=s


	def varTag(self,node):
		t = ""
		name =""
		init = ""
		for child in node:
			if(child.tag=="name"):
				name = child.text
			elif(child.tag=="type"):
				t = child.text;
				self.__s.addVarType(name,t);

	def startParsing(self):
		node=self.__s.getRoot()
		self.__normalParent(node)

	def callMethodName(self,methodName,node):
		#print("FOR CMN:"+node.tag)
		if(methodName in dir(self)):
			#print("FOR CMN:"+node.tag+" calling "+methodName)
			eval("self."+methodName+"(node)")

	def __normalParent(self,node):
		self.callMethodName("st"+node.tag+"Tag",node)
		for child in node:
			#print("FOR CHILD OF:"+node.tag+" CHILD NAME: "+child.tag)
			self.callMethodName(child.tag+"Tag", child)
		self.callMethodName("en"+node.tag+"Tag",node)
		#print("FOR END:"+node.tag)

	
