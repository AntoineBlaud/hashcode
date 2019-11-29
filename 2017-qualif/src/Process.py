from Objects import *
from IO import IO
import pickle
from copy import deepcopy
import itertools
import numpy as np
import random
import sys
import multiprocessing
from numba.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter("ignore", category=NumbaDeprecationWarning)
warnings.simplefilter("ignore", category=NumbaPendingDeprecationWarning)

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
        self.unattachedServer = []

    def backup(self, filename):
        backup = {"cacheServers": self.cacheServers}
        f = open(BACKUP_PATH + "/" + filename, "wb")
        f.write(pickle.dumps(backup))

    def restore(self, filename):
        f = open(BACKUP_PATH + "/" + filename, "rb")
        backup = pickle.load(f)
        self.cacheServers = backup["cacheServers"]


class Process:
    def __init__(self, data: Data):
        self.data = data
        self.combination = []

    def evalueServerScore(self, server: CacheServer, modify=False) -> int:
        # If remove  = True, supprime aussi la vidéo de l'ancien serveur si le nouveau score
        # est meilleur
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
                        self.data.dataCenter.latency[Id] - server.latency[Id]
                    )
                    endPoint = self.data.endPoints[Id]
                    # Si un autre serveur founit deja l'accès à la video
                    favoriteServerLatency = endPoint.getfavoriteServerLatency(
                        endPoint, video
                    )
   
                    # On enregistre que si le temps de latence du serveur courant est
                    # inférieur au temps de latence de serveur le plus rapide qui fournissait
                    # la vidéo
                    if latency <= favoriteServerLatency:
                        score += tmp_score
                        if modify:
                            endPoint.removeVideo(video)
                           


        return score

    @njit
    def test(self):
        print("Test")

    def evalueTotalScore(self) -> int:
        score = 0
        for server in self.data.cacheServers:
            score += self.evalueServerScore(server)
        return self.computeResult(score)

    def computeResult(self,score):
        total = 0
        for video in self.data.videos:
            for r in video.requests.values():
                total+=r
        return int (score/total)*1000


    def check_if_common_endpoint(self, s1: CacheServer, s2: CacheServer):
        for v1 in s1.latency.keys():
            if v1 in s2.latency.keys():
                return True
        return False

    def find_unattached_servers(self):
        """
        Il ne semble pas avoir de serveur de caches indépendants 
        """
        # Pour chaque serveur
        for server in self.data.cacheServers:
            checkCommon = False
            # Pour chaque listes de serveur indépendant
            for unattachedList in self.data.unattachedServer:
                # Pour chaque serveur dans la liste indépendante
                for tobeComparedServer in unattachedList:
                    # Si il y a un endpoint en commun ce n'est pas bon, on peut arrêter
                    if self.check_if_common_endpoint(server, tobeComparedServer):
                        checkCommon = True
                        unattachedList.append(server)
                        break
                # Si il y pas de vidéo en commun, on peut arrêter car
                # la vidéo à été ajouté
                if checkCommon:
                    break
            # Si la vidéo est indépendantes de tout les autres
            # on créer un nouvelle liste
            if not checkCommon:
                self.data.unattachedServer.append([server])



    def dynamic_resolve(self, servers, step=0):
        # Etapes 1: Evalue la gain de chaque vidéos
        videosStats = {}
        compt = 0
        for server in servers:
            compt += 1
            # On vide le serveur
            server.removeAllVideos()
            # On évalue chaque vidéo
            for video in random.sample(self.data.videos, int(self.data.NVideos/10)):
                server.addVideo(video)
                score = self.evalueServerScore(server, modify=True)
                videosStats[video] = score
                server.removeAllVideos()

            # On s'interesse que au 50 meilleurs
            videosStats = dict(
                sorted(videosStats.items(), key=lambda t: t[1], reverse=True)
            )
            if self.data.NVideos > 150:
                videos = list(videosStats.keys())[:]
                val = list(videosStats.values())[:150]
            else:
                videos = list(videosStats.keys())
                val = list(videosStats.values())

            # On récupere le poid de chaque vidéos:
            W = self.data.sizeCacheServers
            n = len(val)
            wt = []
            for v in videos:
                wt.append(v.size)
            wt = np.asarray(wt)
            val = np.asarray(val)
            best_choice = Process.knapSack(W, wt, val, n)
            for r in best_choice[1:]:
                if r != 0:
                    server.addVideo(videos[r - 1],setLatency=True,endpoints=self.data.endPoints)
            sys.stdout.write(
                "Serveur:"
                + str(compt)
                + "/"
                + str(int(len(servers)))
                + " pass:"
                + str(step)
                + "\r"
            )
            sys.stdout.flush()
            if(compt%10==0):
                pass
                #print("\n" + str(self.evalueTotalScore()))
    

    def dynamic_start(self):

        self.test()
        # Essayer de faire un truc parallel avec numba
        # Essayer de Faire approche hybride

        # Faire des groupes de serveurs cache indépendant
        # self.find_unattached_servers()

        #Résout de mauvaise maniere 10 fois
        # for i in range(0, 2):
        #     p1 = multiprocessing.Process(target=self.dynamic_resolve,args =(self.data.cacheServers[:10],i,))
        #     p2 = multiprocessing.Process(target=self.dynamic_resolve,args =(self.data.cacheServers[10:20],i,))
        #     p3 = multiprocessing.Process(target=self.dynamic_resolve,args =(self.data.cacheServers[20:30],i,))
        #     p4 = multiprocessing.Process(target=self.dynamic_resolve,args =(self.data.cacheServers[40:50],i,))
        #     p1.start()
        #     p2.start()
        #     p3.start()
        #     p4.start()
        #     p1.join()
        #     p2.join()
        #     p3.join()
        #     p4.join()
        #     print("\n" + str(self.evalueTotalScore()))

        #Résout 1 fois bien
        # for i in range(0, 2):
        #     self.dynamic_resolve(self.data.cacheServers, step=i)
        #     print("\n" + str(self.evalueTotalScore()))

    def generateVideoCombination(self, n):
        """
        Return all video combination possible. Use the cache server size  
        """
        c = [i for i in range(1, n + 1)]
        for long in c:
            for p in itertools.combinations(c, long):
                self.combination.append(p)
        return self.combination


    def glouton_start(self):
        pass

    def mip_start(self):
        pass



    @staticmethod
    # @njit
    def knapSack(W, wt, val, n):

        K = np.zeros((n + 1, W + 1), dtype=np.int32)
        N = np.zeros((2, W + 1, n + 1), dtype=np.int32)

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    if val[i - 1] + K[i - 1][w - wt[i - 1]] > K[i - 1][w]:
                        K[i][w] = val[i - 1] + K[i - 1][w - wt[i - 1]]
                        N[i % 2][w] = np.copy(N[(i - 1) % 2][w - wt[i - 1]])
                        N[i % 2][w][i] = i
                    else:
                        K[i][w] = K[i - 1][w]
                        N[i % 2][w] = np.copy(N[(i - 1) % 2][w])
                else:
                    K[i][w] = K[i - 1][w]
                    N[i % 2][w] = np.copy(N[(i - 1) % 2][w])

        N[(n) % 2][W][0] = K[n][W]
        return N[(n) % 2][W]

    @staticmethod
    @jit(forceobj=True)
    def knapSackR(W, wt, val, n) -> int:
        """
        Warning : Must create a r array
        """
        # Base Case
        if n == 0 or W == 0:
            return 0

        # If weight of the nth item is more than Knapsack of capacity
        # W, then this item cannot be included in the optimal solution
        if wt[n - 1] > W:
            if r[W][n - 1] != -1:
                return r[W][n - 1]
            else:
                r[W][n - 1] = Process.knapSackR(W, wt, val, n - 1)
                return r[W][n]

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        else:
            if r[W - wt[n - 1]][n - 1] != -1:
                v1 = r[W - wt[n - 1]][n - 1] + val[n - 1]
            else:
                v1 = Process.knapSackR(W - wt[n - 1], wt, val, n - 1) + val[n - 1]

            if r[W][n - 1] != -1:
                v2 = r[W][n - 1]
            else:
                v2 = Process.knapSackR(W, wt, val, n - 1)

            r[W][n] = max(v1, v2)
            return max(v1, v2)

