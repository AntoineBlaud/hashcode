from Item import Item
import json
import pickle
import collections
import random
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
        self.backupFile = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/data/backup.json"
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
        '''
        Starting point function
        '''
        self.referenceServeur = self.getFasterServerIndex()
        self.backup()
        self.divisionProcess(target)
    
    def divisionProcess(self,target):
        '''
        Subdivide, Subdivide graph until a leaf, place the leaf and goes back. Each step we use
        placeNodeInBestPosition to place the node
        '''
        # Available Time
        cT = {}
        for node in target.childrens.values():
            cT[node] = self.evalGraph(node)
        cT = dict(sorted(cT.items(), key=lambda t: t[1],reverse=True))


        for node in cT.keys():
            self.divisionProcess(node)
        
        self.placeNodeInBestPosition(target)

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
        fastest_server_time = self.getServeurWaitingTime(self.getFasterServerIndex())
        current_server_time = self.getServeurWaitingTime(self.referenceServeur)
        rT = node.packs["rT"]
        cT = node.packs["cT"]
        

        if(node.name not in self.aT.keys()):
    
            # If node is a leaf we place it where the waiting time is the min
            if(fastest_server_time+ rT < current_server_time):
                pos = self.getFasterServerIndex()
            else:
                pos = self.referenceServeur

            for children in node.childrens.values():
                if((self.aT[children.name])> current_server_time):
                    pos = self.getNodeServerPosition(children)
                    aT = self.aT[children.name]
            #Placer le noeud
            self.aT[node.name] = cT +  rT + self.getServeurWaitingTime(pos)
            self.pos[node.name] = pos
            self.place(node,pos)

        elif (self.aT[node.name] > random.randint(1,3)*current_server_time + cT):
            pos = self.referenceServeur
             #Placer le noeud
            self.place(node,pos)
        

        

    
    def evalGraph(self,node, visited={}):
        '''
        Return the time to compile all a graph on 1 Server
        '''
        T = 0
        for n in node.childrens.values():
            T+=self.evalGraph(n)
        return T+node.packs["rT"] 

    def getNodeServerPosition(self,node):
        '''
        Get the curr pos of a node (can be multiple), return the fastest
        '''
        return self.pos[node.name]
 
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
        with open(self.backupFile, 'wb') as f:
            backup={"servers":self.servers,"aT":self.aT,"times":self.times,
            "pos":self.pos}
            pickle.dump(backup,f)

    def restore(self):
        with open(self.backupFile, 'wb') as f:
            backup = pickle.load(f)
        #restore 
        self.servers = backup["servers"]
        self.aT = backup["aT"]
        self.times = backup ["times"]
        self.pos = backup["pos"]



    def getFasterServerIndex(self):
        #Defaults
        Min = self.times[0]
        bestServer = 0
        i = 0
        for waitingTime in self.times:
            if(waitingTime<Min):
                Min = waitingTime
                bestServer  = i
            i+=1
        return bestServer

    
    def getServeurWaitingTime(self,pos):
        return self.times[pos]
    
    def addServeurWaitingTime(self,pos,value):
        self.times[pos] += value

    def place(self,node,pos):
        '''
        Place the file on the server pos and 
        '''
        Max = 0
        Pos = 0
        timelapse = 0
        for child in node.childrens.values():
            if(self.aT[child.name]>Max):
                Max = self.aT[child.name]
            if(pos == self.pos[child.name]):
                Max-=child.packs["rT"]

        wait = self.getServeurWaitingTime(pos)
        if(Max-wait > 0):
            timelapse = Max - wait
        self.servers[pos].append(Item(node,max(Max,wait)))
        # Update Waiting time
        self.addServeurWaitingTime(pos,timelapse + node.packs["cT"])




    