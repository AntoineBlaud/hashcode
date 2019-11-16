from Node import Node

class Leaf(Node):

    def __init__(self,father,name):
        Node.__init__(self,father,name)
        self.childrens = None


    def createLeaf(self,name):
        raise Exception("Cannot add leaf to leaf")

    def createNode(self,name):
        raise Exception("Cannot add node to leaf")

    def __str__(self):
        pass

    