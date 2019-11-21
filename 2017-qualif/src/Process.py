from Objects import *
from IO import IO

class Data():
    def __init__(self, io: IO):
        self.videos = io.videos
        self.NVideos = io.NVideos
        self.cacheServers = io.cacheServers
        self.NCacheServers = io.NCacheServers
        self.sizeCacheServers = io.sizeCacheServers
        self.NRequests = io.NRequests
        self.NEndPoints = io.NEndPoints
        self.dataCenter = io.DataCenter


class Process():

    def __init__(self,data:Data):
        self.data = data

    
    def evalueServerScore(self,server:CacheServer):
        pass

    def evalueTotalScore(self) ->int:
        pass

    def glouton_start(self):
        pass

    def genetic_start(self):
        pass

    @staticmethod
    def generateVideoCombination():
        '''
        Return all video combination possible. Use the cache server size  
        '''
        pass


