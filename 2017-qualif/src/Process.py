from Objects import *
from IO import IO
import pickle

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

    def glouton_start(self):
        pass

    def genetic_start(self):
        pass

    @staticmethod
    def generateVideoCombination():
        """
        Return all video combination possible. Use the cache server size  
        """
        pass
    

