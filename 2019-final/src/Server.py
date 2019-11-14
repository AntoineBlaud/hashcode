from Item import Item
import json
# 1) Ajouter la transformation de noeud en item sinon tout va buger
# 2) Ajouter multiple fichier dans placeNodeInBestPos
# 3) Modifier evalQuality dans main.py ( Pour loic)
# 4) Faire les fonctions non faites
# 5) Ecrire a la meme place

##copy node dans io !!!!!
class Server():

    def __init__(self,N = 1):

        #Create server store compilation step
        self.servers = []
        self.jsonBackupFile = "backup.json"
        #Number of servers
        self.N = N
        # All new node append are in aT, value are rT+cT
        self.aT = {}
        #each server have a compiledTime
        self.times = []
        #All new node have a position in a server
        self.pos = {}
        #Each server is represented by a list

        for i in range(0,N):
            self.servers.append([])
            self.times.append(0)

        self.json_data = {"servers":self.servers,"aT":self.aT,"times":self.times,"pos":self.pos}


    def start(self,target):
        self.referenceServeur = getFasterServerIndex()
        self.divisionProcess(target)
    
    def divisionProcess(self,target):
        '''
        Subdivide, Subdivide graph until a leaf, place the leaf and goes back. Each step we use
        placeNodeInBestPosition to place the node
        '''
        # Available Time
        cT = {}
        for node in target:
            cT[node] = self.evalGraph(node)
        sorted(cT.items(), key=lambda t: t[1],reverse=True)

        for node in cT.items():
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
            if(self.getServeurWaitingTime(self.getFasterServerIndex) + node.packs("rT") < self.getServeurWaitingTime(self.referenceServeur)):
                place = self.getFasterServerIndex()
            else:
                place = self.referenceServeur

            for children in node:
                if(self.aT[children] > aT):
                    place = self.getNodeServerPosition(children)
                    aT = self.aT[children]
            #Placer le noeud
            self.aT[node] = node.packs("cT") +  node.packs("rT") + self.getServeurWaitingTime(place)
            self.times[place]+=node.packs("cT")
            self.pos[node] = place

        elif (self.aT[node]>self.getFasterServerIndex() > self.getServeurWaitingTime(self.referenceServeur) + 1.5*node.packs["cT"]):
            place = self.referenceServeur
             #Placer le noeud
            self.times[place]+=node.packs("cT")
        

    
    def evalGraph(self,node, visited={}):
        '''
        Return the time to compile all a graph on 1 Server
        '''
        T = 0
        for n in node:
            T+=n.evalGraph()
        return T+node.packs["cT"]

    def getNodeServerPosition(self,node):
        '''
        Get the curr pos of a node (can be multiple), return the fastest
        '''
        return self.pos[node]
 
    def evalTargetPoint(self,target):
        '''
        Return profit of a target
        '''
        pass

        

    def evalTotalPoint(self):
        '''
        return Point gen by all servers
        '''
        pass


    def backup(self):
        '''
        Save Save and recave to be lot of more efficient in combination tests
        '''
        f = open(self.jsonBackupFile)

    def getFasterServerIndex(self):
        pass
    
    def getServeurWaitingTime(self,index):
        pass

    def placeFile(self,node,pos):
        '''
        Place the file on the server pos and 
        '''
        Max = 0
        Pos = 0
        for child in node.childrens.values():
            if(self.aT[child]>Max):
                Max = self.aT[child]
            if(pos == self.pos[child]):
                Max-=child.packs["rT"]

        size = len(self.servers[pos])
        self.servers[pos].push(Item(node,Max))




    