

class Server():

    def __init__(self,N = 1):

        #Create server store compilation step
        self.servers = []
        self.servers_backup = []
        self.N = N
        self.aT = {}
        #each server have a compiledTime
        self.times = []
        # each server is represented by a list
        for i in range(0,N):
            self.servers.append([])
    
    def divisionProcess(self,target):

        # Available Time
        aT = {}
        for node in target:
            aT[node] = self.evalueGraph(node)+node.packs["rT"]
        sorted(aT.items(), key=lambda t: t[1])

        for node in aT.values:
            self.divisionProcess(node)
        
        self.placeNodeInBestPosition(node)


    def placeNodeInBestPosition(self,node):
        if(node not in self.aT):
            aT = 0
            place = 0
            for children in node:
                if(self.aT[children] > aT):
                    place = self.getNodeServerPosition(children)
        servers[place].append(children)
        self.aT[children] = children.packs("cT") +  children.packs("rT") + self.times[place]
        self.times[place]+=children.packs("cT")

    
    def evalueGraph(self,node, visited={}):
        T = 0
        for n in node:
            if(node in self.aT):
                visited.append(node)
                T+=self.aT[node]
            elif(node not in visited):
                visited.append(node)
                T+=node.evalueGraph()
        return T+node.packs["cT"]

    def getNodeServerPosition(self,node):
        pass




    