import numpy as np
import re
from Objects import DataCenter,Video,Request,CacheServer

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

    def getData(self):
        f = open(self.filename,'r')
        line = f.readline().split(" ")
        self.NVideos = int(line[0])
        self.NEndPoints = int(line[1])
        self.NRequests = int(line[2])
        self.NCacheServers = int(line[3])
        self.sizeCacheServers = int(line[4])

        for i in range(0,self.NCacheServers):
            self.cacheServers.append(CacheServer(i,self.sizeCacheServers))
        
        line = f.readline()
        line = re.sub("\n","",line)
        line = line.split(" ")

        for i in range(0,self.NVideos):
            self.videos.append(Video(i,int(line[i])))

        for i in range(0,self.NEndPoints):
            line = f.readline()
            line = re.sub("\n","",line)
            line = line.split(" ")
            self.dataCenter.addEndPoint(i,int(line[0]))
            for j in range(0,int(line[1])):
                
                line = f.readline()
                line = re.sub("\n","",line)
                line = line.split(" ")
                self.cacheServers[int(line[0])].addEndPoint(i,int(line[1]))

        requests = [[],[]]
        for i in range(0,self.NRequests):
            line = f.readline()
            line = re.sub("\n","",line)
            line = line.split(" ")
            self.videos[int(line[0])].addRequest(int(line[1]),int(line[2]))


        

