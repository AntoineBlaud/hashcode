
# 1) Ajouter la transformation de noeud en item sinon tout va buger
# 2) Ajouter multiple fichier dans placeNodeInBestPos
# 3) Modifier evalQuality dans main.py
# 4) Faire les fonctions non faites

class Server():

    def __init__(self,N = 1):

        #Create server store compilation step
        self.servers = []
        self.servers_backup = []
        self.N = N
        # All node are append are in aT, value are rT+cT
        self.aT = {}
        #each server have a compiledTime
        self.times = []
        # each server is represented by a list
        for i in range(0,N):
            self.servers.append([])
            self.times.append(0)
    
    def divisionProcess(self,target):
        '''
        Subdivide, Subdivide graph until a leaf, place the leaf and goes back. Each step we use
        placeNodeInBestPosition to place the node
        '''
        # Available Time
        aT = {}
        for node in target:
            aT[node] = self.evalGraph(node)+node.packs["rT"]
        sorted(aT.items(), key=lambda t: t[1])

        for node in aT.values:
            self.divisionProcess(node)
        
        self.placeNodeInBestPosition(node)

        # call place target


    def placeNodeInBestPosition(self,node):
        '''
        Place a node taking in account only process before childrens comp + rep
        Choose the server where the max(rep + compil) children's time is MAX
        '''

        '''
        WARNING !!!! 
        ajouter un deuxiéme exemplaire si plus rapide
        '''
        if(node not in self.aT):
            aT = 0
            # If node is a leaf we place it where the waiting time is the min
            place = self.getFasterServerIndex()
            for children in node:
                if(self.aT[children] > aT):
                    place = self.getNodeServerPosition(children)
        servers[place].append(children)
        self.aT[children] = children.packs("cT") +  children.packs("rT") + self.times[place]
        self.times[place]+=children.packs("cT")

    
    def evalGraph(self,node, visited={}):
        '''
        Return the time to compile all a graph on 1 Server
        '''
        T = 0
        for n in node:
            if(node in self.aT):
                visited.append(node)
                T+=self.aT[node]
            elif(node not in visited):
                visited.append(node)
                T+=node.evalGraph()
        return T+node.packs["cT"]

    def getNodeServerPosition(self,node):
        '''
        Get the curr pos of a node (can be multiple)
        '''
        pass

    def evalTargetPoint(self,target):
        '''
        Return profit of a target
        '''
        pass

    def evalServerPoint(self):
        '''
        return Point gen by all servers
        '''
        pass

    def placeTarget(self,target):
        '''
        Place the final node in the best position
        '''
        pass

    def backup(self):
        '''
        Save Save and recave to be lot of more efficient in combination tests
        '''
    def getFasterServerIndex(self):
        pass




    