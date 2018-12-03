from parsimonious.grammar import Grammar
from Node import Node

from parsimonious.grammar import Grammar
from Translator import Translator





def getListOfNodes(grammar):
	listOfNode = []
	f = open("psuedocode.txt","r")
	for sentence in f.readlines():
		#sentence = sentence[:-1]
		#print(sentence)
		listOfNode.append(grammar.parse(sentence.rstrip('\n')))
	f.close()
	return listOfNode


def recur(node,root):
	#print("Node Start")
	tag=""
	if(node.expr.name!=""):
		tag=node.expr.name
	else:
		tag=node.expr.as_rule()
		tag=tag[1:]
		tag=tag[:-1]
	root.setTag(tag)
	for child in node:
		x = Node()
		root.addChild(x)
		recur(child,x)

def makeTree(t):
	root=Node()
	recur(t,root)
	return root

def recurNode(node):
	#print("START:",node.getTag())
	for child in node.getChildren():
		recurNode(child)
	#print("END:",node.getTag())

def tranMain():
	
	grammar = Grammar("""

        s   = s1 / s2 / s3 / s4
        s1  = start space (variable space)*  prep space datatype
        s2  = start space operation space prep space variable space variable space prep space variable
        s3  = start space constant space prep space variable
        s4  = start space variable
        datatype  = "integer" / "double"
        operation = "addition" / "subtraction" / "multiplication" / "division"
        start = "let" / "assign" / "print" 
        prep  = "of" / "be" / "to"
        variable = 'a' / 'b' / 'c'
        constant = '0' / '1' / '2'
        space = " "

        """)

	listOfMyNode = []	
	listOfNode = getListOfNodes(grammar)
	for line in listOfNode:
		listOfMyNode.append(makeTree(line))

	n = Translator(listOfMyNode)
	recurNode(listOfMyNode[0])
	n.translate()

tranMain()