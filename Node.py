class Node:

    def __init__(self):
        self.child=[]
        self.tag=""
    
    def addChild(self,c):
        self.child.append(c)
    
    def getChildren(self):
        return self.child
    
    def getTag(self):
        return self.tag

    def setTag(self,label):
        self.tag=label


    def getChildWithTag(self,sti):
        #print("Node:",self.tag," ",sti)
        l = []
        for child in self.child:
            if(self.tag==sti):
                #print("YUP this happened")
                l.append(child.tag)
            l += child.getChildWithTag(sti)
        #print("END Node:",self.tag," ",sti)
        return l;