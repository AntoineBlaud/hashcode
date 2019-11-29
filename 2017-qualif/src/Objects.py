from copy import deepcopy
import math
from numba import *
import numpy as np


import line_profiler
import atexit

profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)


INF  = 400000000

class DataCenter:
    def __init__(self):
        # endPoint -> temps de latence
        self.latency = {}

    def addEndPoint(self, id: int, latency: int):
        '''
        Parameters:
        id (int), latency (int)
        '''
        self.latency[id] = latency


class Video:
    def __init__(self, id: int, size: int):
        self.id = id
        self.size = size
        # endpoint -> Nombre de requete
        self.requests = {}
        self.indexRequest = 0

    def __str__(self):
        return "V:" + str(self.id)

    def __repr__(self):
        return "V:" + str(self.id)

    def addRequest(self, id, value:int):
        '''
        Ajoute un endpoint avec un nombre de requete pour cette video spécifique
        Parameters:
        id (int), latency (int)
        '''
        self.requests[id] = value



class CacheServer:
    def __init__(self, id: int, size: int):
        self.id = id
        self.size = size
        self.size_free = size
        # Represente les vidéos stockés dans le cacher server
        self.stocked_videos = np.ones((1, 100),dtype=object)
        self.indexVideo = 0
        # Pour chaque endPoint index est associé une latence
        self.latency = {}

    def __str__(self):
        return "S:"+str(self.id)

    def __repr__(self):
        return "S:"+str(self.id)

    
    def addVideo(self, video: Video,setLatency=False,endpoints= []):
        '''
        Ajoute une video au server
        Parameters:
        video (Video)
        '''
        self.stocked_videos[0][self.indexVideo] = video
        self.indexVideo+=1
        if(setLatency):
            for i in self.latency.keys():
                if(i in video.requests.keys()):
                    endP = endpoints[i]
                    endP.setfavoriteServerLatency(video,self.latency[i])


    @jit(forceobj=True)
    def removeVideo(self, video):
        index = self.getVideoIndex(video)
        for i in range(index, self.indexVideo):
            self.stocked_videos[0][index] = self.stocked_videos[0][index + 1]
        self.indexVideo -= 1

    def removeAllVideos(self):
        self.stocked_videos = np.empty((1, 100),dtype=object)
        self.indexVideo = 0

    def getVideoIndex(self,video):
        for i in range(0,self.indexVideo+1):
            if(video ==self.stocked_videos[0][i]):
                return i

    def addEndPoint(self, id: int, size: int):
        self.latency[id] = size

    def getStockedVideo(self):
        return self.stocked_videos[0][0:self.indexVideo]

class EndPoint:
    def __init__(self, id):
        self.id = id
        # Liste des serveurs caches rattaché à ce endPoint
        self.connectedServer = []

    def addServer(self, server: CacheServer):
        '''
        Ajoute un serveur (connecte au endpoint)
        Parameters:
        server (CacheServer)
        '''
        self.connectedServer.append(server)
        self.videoLatency = {}

    def __str__(self):
        return "E:"+str(self.id)

    def __repr__(self):
        return "E:"+str(self.id)
    
    #Trop lent
    # def favoriteServerLatency(self,endPoint,video):
    #     '''
    #     Pour une video spécifier et un endPoint spécifier, regarde dans les serveurs connecté au endpoint
    #     si la video est dedans. Retourne le plus petit temps de latence
    #     Parameters:
    #     server (CacheServer)
    #     '''
    #     latency = INF
    #     for server in self.connectedServer:
    #         for v in server.getStockedVideo():
    #             if(v==video and server.latency[endPoint.id]<latency):
    #                 latency = server.latency[endPoint.id]
    #     return latency

    def getfavoriteServerLatency(self,endPoint,video):
        '''
        Pour une video spécifier et un endPoint spécifier, regarde dans les serveurs connecté au endpoint
        si la video est dedans. Retourne le plus petit temps de latence
        Parameters:
        server (CacheServer)
        '''
        for v in self.videoLatency.keys():
            if(v == video):
                return self.videoLatency[video]
        #Si elle n'y est pas retourne la latence INFINIE
        return INF
        
    def setfavoriteServerLatency(self,video,latency):
        self.videoLatency[video] = latency

    def removeVideo(self,video):
        leave = False
        for server in self.connectedServer:
            for v in server.getStockedVideo():
                if(v==video):
                    server.removeVideo(video)
                    leave= True
                    break
            if(leave):
                break
        



