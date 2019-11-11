

class Item():
    def __init__(self, name, compileT, replicateT):
        self.name = name
        self.ct = compileT
        self.rT = replicateT

    def setAvailableT(self,v):
        self.aT = v