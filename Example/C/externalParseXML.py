

class externalParseXML:

	def __init__(self, serviceObj):
		self.__serviceObj = serviceObj
		self.code = ""
		self.tab = 0



	def varTag(self,node):
		t = ""
		name =""
		init = ""
		for child in node:
			if(child.tag=="name"):
				name = child.text
			elif(child.tag=="type"):
				t = child.text;
			elif(child.tag=="init"):
				init = " = " + child.text;
		self.__serviceObj.addSen(t + " " + name + init + ";",self.tab)

	def vwriteTag(self,node):
		stri="printf(\""
		varName=node.text
		varType=self.__serviceObj.getVarType(varName)
		if(varType=="int"):
			stri+="%d"
		elif(varType=="Double"):
			stri+="%f"
		stri+="\","+varName+");"
		self.__serviceObj.addSen(stri,self.tab)

	def swriteTag(self,node):
		self.__serviceObj.addSen("printf(\""+node.text+"\");",self.tab)

	

	def assignTag(self,node):
		inut1 = ""
		input2 =""
		output = ""
		operation = ""
		for child in node:
			if(child.tag=="input1"):
				input1 = self.getOprand(child[0])
			elif(child.tag=="input2"):
				input2 = self.getOprand(child[0])
			elif(child.tag=="output"):
				output = self.getOprand(child[0])
			else:
				operation = self.getOpCode(child.text)
		self.__serviceObj.addSen(output + " = " + input1 + " " + operation + " " + input2 + ";",self.tab)

	def getOpCode(self,code):
		#print("Code:",code)
		if(code=="1"):
			return "+"
		if(code=="2"):
			return ">"
		#print("RET:NULL")
		return "";

	def ifTag(self,node):
		return self.__normalParent(node)

	def elseTag(self,node):
		return self.__normalParent(node)

	def execTag(self,node):
		self.__normalParent(node)

	def stelseTag(self,node):
		self.__serviceObj.addSen("else",self.tab)
		self.__serviceObj.addSen("{",self.tab)
		self.tab+=1

	def enelseTag(self,node):
		self.tab-=1
		self.__serviceObj.addSen("}",self.tab)

	def stifTag(self,node):
		self.__serviceObj.addSen("if("+self.myCondTag(node[0]),self.tab)
		
		self.__serviceObj.addSen("{",self.tab)
		self.tab+=1

	def enifTag(self,node):
		self.tab-=1
		self.__serviceObj.addSen("}",self.tab)
		

	def myCondTag(self,node):
		op1 = ""
		op2 = ""
		operation = ""
		for child in node:
			if(child.tag=="op1"):
				op1 = self.getOprand(child[0])
			elif(child.tag=="op2"):
				op2 = self.getOprand(child[0])
			else:
				operation = self.getOpCode(child.text)
		return op1 + " " + operation + " " + op2 + ")"; 


	def getOprand(self,node):
		#print("Here is the node")
		if(node.tag=="operand"):
			#print("RET:",node.text)
			return node.text
		#print("RET:",node.text)
		return node.text

	def startTag(self,node):
		self.__normalParent(node)



	def callMethodName(self,methodName,node):
		#print("FOR CMN:"+node.tag)
		if(methodName in dir(self)):
			#print("FOR CMN:"+node.tag+" calling "+methodName)
			eval("self."+methodName+"(node)")


	def __normalParent(self,node):
		#print("FOR:"+node.tag)
		self.callMethodName("st"+node.tag+"Tag",node)
		for child in node:
			#print("FOR CHILD OF:"+node.tag+" CHILD NAME: "+child.tag)
			self.callMethodName(child.tag+"Tag", child)
		self.callMethodName("en"+node.tag+"Tag",node)
		#print("FOR END:"+node.tag)
		

	def callForNode(self,node):
		#print("FOR CFN:"+node.tag)
		self.callMethodName(node.tag+"Tag",node)

	def startParsing(self):
		self.__serviceObj.addSen("#include<stdio.h>",self.tab)
		self.__serviceObj.addSen("int main()",self.tab)
		self.__serviceObj.addSen("{",self.tab)
		self.tab+=1
		node=self.__serviceObj.getRoot()
		self.__normalParent(node)
		self.__serviceObj.addSen("return 0;",self.tab)
		self.tab-=1
		self.__serviceObj.addSen("}",self.tab)
