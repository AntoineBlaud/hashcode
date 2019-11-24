from Objects import *
from IO import IO
import pickle
from copy import deepcopy
import itertools
import numpy as np
import random

from numba.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)


BACKUP_PATH = "/home/darkloner99/code/Hashcode/Hashcode/2017-qualif/backup"
class Data:
    def __init__(self, io: IO):
        self.videos = io.videos
        self.NVideos = io.NVideos
        self.cacheServers = io.cacheServers
        self.NCacheServers = io.NCacheServers
        self.sizeCacheServers = io.sizeCacheServers
        self.NRequests = io.NRequests
        self.NEndPoints = io.NEndPoints
        self.dataCenter = io.dataCenter
        self.endPoints = io.endPoints

    def backup(self,filename):
        backup = {"cacheServers":self.cacheServers}
        f = open(BACKUP_PATH+"/"+filename,"wb")
        f.write(pickle.dumps(backup))

    def restore(self, filename):
        f = open(BACKUP_PATH+"/"+filename,"rb")
        backup = pickle.load(f)
        self.cacheServers = backup["cacheServers"];


class Process:

    def __init__(self, data: Data):
        self.data = data
        self.combination= []

    def evalueServerScore(self, server: CacheServer) -> int:
        score = 0

        # Pour chaque videos stocker dans le serveur
        for video in server.getStockedVideo():
            s = video.requests
            # Pour chaque endpoint->number request dans video
            for Id, requests in video.requests.items():

                # Si la vidéo est demandé par un endPoint connecté au serveur
                if Id in server.latency:
                    latency = server.latency[Id]
                    tmp_score = requests * (
                        self.data.dataCenter.latency[Id] - server.latency[Id])
                    endPoint = self.data.endPoints[Id]
                    # Si un autre serveur founit deja l'accès à la video
                    favoriteServerLatency = endPoint.favoriteServerLatency(endPoint,video)
                    if(favoriteServerLatency!=INF):
                        # On enregistre que si le temps de latence du serveur courant est
                        # inférieur au temps de latence de serveur le plus rapide qui fournissait
                        # la vidéo
                        if favoriteServerLatency <= latency:
                            score += tmp_score
                    else:
                        score += tmp_score

        return score

    def evalueTotalScore(self) -> int:
        score = 0
        for server in self.data.cacheServers:
            score+=self.evalueServerScore(server)
        return score

    @staticmethod
    @njit
    def knapSack(W, wt, val, n):

        K = np.full((n + 1, W + 1), 0)
        N = np.full((2, W + 1, W + 1), 0)

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    if val[i - 1] + K[i - 1][w - wt[i - 1]] > K[i - 1][w]:
                        K[i][w] = val[i - 1] + K[i - 1][w - wt[i - 1]]
                        N[i%2][w] = np.copy(N[(i - 1)%2][w - wt[i - 1]])
                        N[i%2][w][i] = i
                    else:
                        K[i][w] = K[i - 1][w]
                        N[i%2][w] = N[(i - 1)%2][w]
                else:
                    K[i][w] = K[i - 1][w]
        N[(n)%2][W][0] = K[n][W]
        return N[(n)%2][W]


    @staticmethod
    def knapSackR(W, wt, val, n): 
    
        # Base Case 
        if n == 0 or W == 0 : 
            return 0
    
        # If weight of the nth item is more than Knapsack of capacity 
        # W, then this item cannot be included in the optimal solution 
        if (wt[n-1] > W): 
            return Process.knapSackR(W, wt, val, n-1) 
    
        # return the maximum of two cases: 
        # (1) nth item included 
        # (2) not included 
        else: 
            return max(val[n-1] + Process.knapSackR(W-wt[n-1], wt, val, n-1), 
                    Process.knapSackR(W, wt, val, n-1)) 

    def glouton_start(self):
        pass

    def genetic_start(self):
        pass

    def dynamic_start(self):
        # Essayer de faire un truc parallel
        # Essayer de Faire approche hybride
        pass

    def mip_start(self):
        pass


    def generateVideoCombination(self,n):
        """
        Return all video combination possible. Use the cache server size  
        """
        c = [i for i in range(1,n+1)]
        for long in c:
            for p in itertools.combinations(c,long):
                self.combination.append(p)
        return self.combination
      

        
    

