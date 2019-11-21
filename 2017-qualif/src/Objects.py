import numpy as np
from copy import deepcopy

class DataCenter():
    def __init__(self):
        self.endPoints = {}

    def addEndPoint(self,id:int,latency:int):
        self.endPoints[id] = latency

    
class Video():
    def __init__(self,id:int,size:int):
        self.id = id
        self.size = size
        self.requests = np.ones((2,1),dtype='i')
        self.indexRequest = 0
    

class Request():
    def __init__(self,video:Video,idEndPoint:int,nRequest:int):
        self.video = video
        self.idEndPoint = idEndPoint
        self.nRequest = nRequest


    def __str__(self):
        return "V"+self.id+":"+self.size

    def __repr__(self):
        return "V"+self.id+":"+self.size

    def addRequest(self, id, value):
        n = np.asarray([[id],[value]])
        self.requests = np.append(self.requests,n,axis=1)


class CacheServer():
    def __init__(self,id:int,size:int):
        self.id = id
        self.size = size
        self.size_free = size
        self.stocked_videos = np.ones((1,100))
        self.indexVideo = 0
        self.endPoints = np.ones((2,0),dtype='i')
        self.indexEndPoints = 0

    def __str__(self):
        return "C"+self.id

    def __repr__(self):
        return "C"+self.id
    
    def addVideo(self,video : Video):
        self.stocked_videos[self.indexVideo] = video

    def removeVideo(self,index):
        for i in range(index,self.indexVideo):
            self.stocked_videos[index]= deepcopy(self.stocked_videos[index+1])
        self.indexVideo -= 1

    def removeAllVideos(self):
        self.stocked_videos = np.empty((1,100))

    def addEndPoint(self,id:int,size:int):
        n = np.asarray([[id],[size]])
        self.endPoints = np.append(self.endPoints,n,axis=1)

