import numpy as np
import re
from copy import deepcopy

class IO():

    def __init__(self,filename:str):
        self.filename = filename
        self.videos = []
        self.NVideos = 0
        self.cacheServers = []
        self.NCacheServers = 0
        self.sizeCacheServers = 0
        self.NRequests = 0
        self.NEndPoints = 0
        self.dataCenter = DataCenter()
        self.endPoints = []


    def readLine(self,f):
        line = f.readline()
        line = re.sub("\n","",line)
        line = line.split(" ")
        return line

    def getData(self):
        f = open(self.filename,'r')
        line = self.readLine(f)
        self.NVideos = int(line[0])
        self.NEndPoints = int(line[1])
        self.NRequests = int(line[2])
        self.NCacheServers = int(line[3])
        self.sizeCacheServers = int(line[4])

        for i in range(0,self.NCacheServers):
            self.cacheServers.append(CacheServer(i,self.sizeCacheServers))
        
        line = self.readLine(f)

        for i in range(0,self.NVideos):
            self.videos.append(Video(i,int(line[i])))

        for i in range(0,self.NEndPoints):
            line = self.readLine(f)
            eP_ID = i
            eP = EndPoint(eP_ID)
            self.endPoints.append(eP)
            latency = int(line[0])
            self.dataCenter.addEndPoint(eP_ID,latency)
            for j in range(0,int(line[1])):
                line = self.readLine(f)
                server_ID = int(line[0])
                latency = int(line[1])
                server = self.cacheServers[server_ID]
                server.addEndPoint(eP_ID,latency)
                eP.addServer(server)

        requests = [[],[]]
        for i in range(0,self.NRequests):
            line = self.readLine(f)
            video_ID = int(line[0])
            endPoint_ID = int(line[1])
            requests =  int(line[2])
            self.videos[video_ID].addRequest(endPoint_ID,requests)


        

