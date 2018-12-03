import xml.etree.ElementTree as ET
from xml.dom import minidom


class Translator:


	def __init__(self,stats):
		self.__stats=stats
		self.__start = ET.Element('start')  

	def getMyRealType(self,varType):
		if(varType=="integer"):
			return "int";
		else:
			return "";

	def s1Parse(self,node):
		#print("S1 STSART")
		s1 = node.getChildWithTag("variable")
		s2 = node.getChildWithTag("datatype")
		for myvar in s1:
			var=ET.SubElement(self.__start,'var')
			name=ET.SubElement(var,'name')
			varType = ET.SubElement(var,'type')
			name.text=myvar
			varType.text=self.getMyRealType(s2[0])
		#print(s1[0])
		#print(s2[0])
		#print("S1 END")

	def getXMLOperand(self,varName):
		operand = ET.Element('operand')
		operand.text =varName
		return operand

	def attachOperand(self,parent,varName):
		operand1 = ET.SubElement(parent,'operand')
		operand1.text =varName

	def attachCon(self,parent,varName):
		operand1 = ET.SubElement(parent,'con')
		operand1.text =varName


	def s3Parse(self,node):
		s1 = node.getChildWithTag("constant")
		s2 = node.getChildWithTag("variable")
		
		assign=ET.SubElement(self.__start,'assign')
		
		input1=ET.SubElement(assign,'input1')
		self.attachCon(input1,s1[0])
		
		outout=ET.SubElement(assign,'output')
		self.attachOperand(outout,s2[0])


	def s2Parse(self,node):
		s1 = node.getChildWithTag("variable")
		s2 = node.getChildWithTag("operation")

		
		
		assign=ET.SubElement(self.__start,'assign')
		
		input1=ET.SubElement(assign,'input1')
		self.attachOperand(input1,s1[0])

		input2=ET.SubElement(assign,'input2')
		self.attachOperand(input2,s1[1])

		output=ET.SubElement(assign,'output')
		self.attachOperand(output,s1[2])

		operation =ET.SubElement(assign,'op')
		operation.text = self.getOpCode(s2[0])

	def getOpCode(self,operation):
		#print("Getting opcode for",operation)
		if(operation=="addition"):
			return "1"
		else:
			return "0"


	def s4Parse(self,node):
		s1 = node.getChildWithTag("variable")

		printS = ET.SubElement(self.__start,'vwrite')
		printS.text = s1[0]

	def translate(self):
		for stat in self.__stats:
			methodName = stat.getChildren()[0].getTag()+"Parse"
			if(methodName in dir(self)):
				eval("self."+methodName+"(stat)")

		#mydata = ET.dump(self.__start)
		#print(mydata)
		#myfile = open("items2.xml", "w")  
		#myfile.write(mydata) 

		mydata = minidom.parseString(ET.tostring(self.__start).decode("utf-8")).toprettyxml(indent="   ")
		#xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ") 
		myfile = open("XMLFile.xml", "w")  
		myfile.write(mydata)  