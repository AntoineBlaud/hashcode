from Node import Node

class  Root(Node):

    def __init__(self,name):
        Node.__init__(self,None,name)
        self.deepth  = 0

    
    def setBranchValue(self,value):
        pass
