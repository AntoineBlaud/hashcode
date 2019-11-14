

class Item():
    def __init__(self, node,Max=0):
        self.name = node.name
        self.cT = node.packs["cT"]
        self.rT = node.packs["rT"]
        self.aTin = self.cT + Max
        self.aTOut = self.cT + self.rT + Max
     