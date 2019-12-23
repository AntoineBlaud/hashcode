import sys
import os
import time
import argparse
import re
from copy import copy
from math import *
from random import *

'''
@ Loic: ajuster R (rayon) suivant nombre de drone et valeur incluses
        scoring 
'''

######################################################################################
import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)
######################################################################################

DEFAULT_F = "/home/darkloner99/code/Hashcode/Hashcode/2016-qualif/qualification_round_2016.in/exemple.in"
OUTPUT_F =  "/home/darkloner99/code/Hashcode/Hashcode/2016-qualif/out/result.txt"

parser = argparse.ArgumentParser(description='Compute hashcode 2018 ride')
parser.add_argument('-f','--file',help='Input file',default=DEFAULT_F,type=str)
parser.add_argument('-o','--out',help='Ouput file',default=OUTPUT_F,type=str)
parser.add_argument('-v','--verbose',default=-1,help='verbose mode',type=int)
args = parser.parse_args()

##########################################
# items weight
items = {}
# Warhouse objects
warehouses = []
# Orders
orders = []
# Chaine de caractere qu'on de vrai ecrire a la fin
OUTPUT_B = ""
# Commande completés
orderCompleted = []
##########################################

# convert line to integer. 
def lineToMap(f):
    return map(int,f.readline().strip().split(" "))

# convert line to a list of  integer.
def lineToList(f):
    return list(map(int,f.readline().strip().split(" ")))

class Warehouse:
    def __init__(self,x,y,id):
        self.x = x
        self.y = y
        self.id = id

    def setProductList(self,products:list):
        self.products = products
    
    def getProduct(self,i:int,q:int):
        if(self.products[i] - q >=0): self.products[i]-=q;return True
        return False

    def getQ(self,idP):
        return self.products[idP]
    def __str__(self):
        return "W_%d_%d"%(self.x,self.y)

    def __repr__(self):
        return "W_%d_%d"%(self.x,self.y)


class Order:
    def __init__(self,x,y,q,id):
        self.x = x
        self.y = y
        self.q = q
        self.id = id
        self.completed = None

    def setProductsOrder(self,products: list):
        self.products = products
    
    def inOrder(self,i:int):
        return i in self.order
    
    def removeProduct(self,i,q):
        self.products[i]-= q
        self.q-=q

    def __str__(self):
        return "O_%d_%d_%d"%(self.x,self.y,self.q)

    def __repr__(self):
        return "O_%d_%d_%d"%(self.x,self.y,self.q)

    def __len__(self):
        return len([x for x in self.products if x==1])


class Drone:
    def __init__(self,c,id):
        self.c = c
        self.x = 0
        self.y = 0
        self.id = id
        self.items = {}
        self.Tavailable = 0

    def move(self,x,y):
        self.x = x
        self.y = y
    
    def getPos(self):
        return self.x,self.y

    def load(self,idP, q):
        if(object in self.items.keys()):
            self.items[idP]+=q
            c-=c*items[idP]
        else:
            self.items[idP]=q
            c-=c*items[idP]

    def unload(self,idP,q):
        self.items[idP]-=q
        c+=c*items[idP]

    def getQuantity(self,idP):
        if(idP in self.items.keys()): return self.items[object]
        return 0

    def inDrone(self,idP):
        if(idP in self.items.keys()):
            return self.items[idP]
        return 0


# Read input file and create var.
with open(args.file,"r") as f:
    rowsN, columnsN,dronesN,turnN,payload = lineToMap(f)
    itemN, = lineToMap(f)
    i = 0
    for item in lineToMap(f):
        items[i] = item;i+=1
    warehouseN, = lineToMap(f)
    for i in range(warehouseN):
        x,y = lineToMap(f)
        w = Warehouse(x,y,i)
        stock = lineToList(f)
        w.setProductList(stock)
        warehouses.append(w)
    ordersN, = lineToMap(f)
    for i in range(ordersN):
        x,y = lineToMap(f)
        q, = lineToMap(f)
        o = Order(x,y,q,i)
        products = lineToList(f)
        o.setProductsOrder(products)
        orders.append(o)


if(args.verbose == 0):   
    print(warehouses)
    print(items)
    print(orders)


def distance(x1,y1,x2,y2):
    return sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)


def foundOptimumR(warehouses,orders):
    #Permet de trouver le rayon optimal des livraisons autour des entrepôts.
    cover = 0
    rT = 0
    for r in range(1,min(rowsN,columnsN)):
        ordersPerW = []
        for warehouse in warehouses:
            for e in getOrderAtProximity(warehouse,orders,r):
                ordersPerW.append(e)
        ordersPerWuniq = set(ordersPerW)
        if((len(ordersPerWuniq)/len(orders))>0.7 and (len(ordersPerW)/len(orders))<=1.4):
            return r
        elif (len(ordersPerWuniq)/len(orders))>cover and (len(ordersPerW)/len(orders))<=1.4:
            rT = r
            cover = len(ordersPerWuniq)/len(orders)
    return rT




def getOrderAtProximity(w,orders, r):
    # Retourne toutes les commandes dans un rayon r autour d'un entrepot.
    ordersAtProximity = []
    xw = w.x
    yw = w.y
    for order in orders:
        xo = order.x
        yo = order.y
        if(distance(xo,yo,xw,yw)<r): ordersAtProximity.append(order)
    return ordersAtProximity


def getWarehousePerProximity(x1,y1,warehouses):
    # Retourne les entrepot par distance a des coordonnées (qui peuvent être une moyenne entre
    # le drone et la commande ou autre)
    
    distances = {}
    for w in warehouses:
        distances[w.id]= (distance(x1,y1,w.x,w.y))
    
    warehouseSorted = dict(sorted(distances.items(), key=lambda t: t[1]))
    warehouseSorted = list(warehouseSorted.keys())
    if(args.verbose==2):
        print(warehouseSorted)  
    return warehouseSorted
    

def rangeOrdersPerInterest(warehouses:list,orders:list,dronesN:int):
    # 1. Regrouper commande par proximité à un entrepot.
    ordersPerProximityToWarehouse = []
    warehousesPath = []
    for w in warehouses:
        ordersP = getOrderAtProximity(w,orders,R)
        ordersPerProximityToWarehouse.append(ordersP) 
    # 2. Trier groupe de commande par proximité entre elle et par rapport au point de départ.
    b = rowsN+columnsN
    bestW = warehouses[0]
    xt,yt = 0,0
    while(len(warehousesPath)!=len(warehouses)):
        for w in warehouses:
            d = distance(w.x,w.y,xt,yt)
            if(d<b and w not in warehousesPath):
                bestW = w; b = d
        warehousesPath.append(bestW)
        b = rowsN+columnsN
        wt,yt = w.x,w.y
    
    # 3. Réeordonner les commandes suivant warehousePath
    warehousesPath = [w.id for w in warehousesPath]
    ordersPerProximityToWarehouse = [copy(ordersPerProximityToWarehouse[i]) for i in warehousesPath]
    # 4. A l'intérieur des packet on melange de maniere aléatoire
    for listO in ordersPerProximityToWarehouse:
        listO = shuffle(listO)

    return ordersPerProximityToWarehouse



def foundClosestWharehouse(drone,idP, q):
    global warehouses
    # Ici meilleur entrepot mais qui n'a pas tout les élements
    bestQ0D = columnsN + rowsN
    bestQ0Q = 0
    bestQ0 = False
    # Ici meilleur entrepot avec assez de produit en stock 
    bestQ1D = columnsN + rowsN
    bestQ1 = False
    for w in warehouses:
        d = distance(w.x,w.y,drone.x,drone.y) + drone.Tavailable
        # Si dans l'entrepot il y a une quantité suffisante et la distance est meilleur
        if(w.getQ(idP)>=q and bestQ1D>d):
            bestQ1D = d
            bestQ1 = w

        # Sinon on enregistre la meilleur solution
        if(w.getQ(idP)>=bestQ0Q  and bestQ0D>d):
            bestQ0D = d
            bestQ0 = w
            bestQ1Q = w.getQ(idP)

    # Ici pareil que pour drone modifier
    if(bestQ1):
        return bestQ1,q
    return bestQ0, bestQ0Q

        
    

def foundBestInterestingDrone(order,drones,idP,q):
    # Retourne le drone le plus intéressent 
    global diMax,qiMax
    distances =  {}
    xo = order.x
    yo = order.y
    i = 0
    for drone in drones:
        xd = drone.x
        yd = drone.y
        # Quantité du produit dans le drone
        qInDrone = drone.inDrone(idP)
        # Si la quantité de produit dans le drone est suffisante
        if(qInDrone>=q):
            d = distance(xo,yo,xd,yd) + drone.Tavailable
            q2 = q
        else:
            w,q2 = foundClosestWharehouse(drone,idP,q-qInDrone)
            if(q2==q):
                d = distance(xo,yo,w.x,w.y) + distance(w.x,w.y,drone.x,drone.y) + drone.Tavailable

        distances[i] = (d, q2)

    droneSorted = dict(sorted(distances.items()[0], key=lambda t: t[1]))
    best = list(droneSorted.keys())

    # Ici modifier pour peut etre preférer passer par un entrepot suivant le contenu des drones
    # si ils ont tous les produits ou non etc...
    (di, qi) = distance[best[0]]
    if(di<diMax and (q-qi)<qiMax):
        return drones[di]
    return False
    

def deliverProduct(drone:Drone,order:Order,idP):
    # ici on gere aussi load , wait etc...
    # changer completed 
    if(len(order)==0):
            if(order not in orderCompleted):
                pass


def dronesDispo(drones:list):
    # si temps de simulation pour chaque drone > temps max alors return false
    for drone in drones:
        if(drone.Tavailable<turnN):
            return True


def closeOrder(order):
    pass


def processDelivery(orderSorted,drones):
    global orderCompleted
    # Attention, il peut y avoir plusieurs fois la même commande dans la liste orderSorted
    while(len(orderSorted)> 0 and dronesDispo(drones)):
        order = orderSorted.pop()
        # Si la commande a encore des articles
        if(len(order)>0):
            for id,q in zip(order.products,range(itemN)):
                if(q>0):
                    # Recuperer drone le plus interessant pour livrer 
                    drone = foundBestInterestingDrone(drones,id,order)
                    # Si la livraison est interessente
                    if(drone!=False):
                        deliverProduct(drone,Order,id)

        

            

# Params 
##########################################
R = foundOptimumR(warehouses,orders)
diMax = 10
qiMax = 10
##########################################
                


temp =  rangeOrdersPerInterest(warehouses,orders,dronesN)
# on transforme en un tableau a une seule dimension
orderSorted = []
for l in temp: 
    for e in l: orderSorted.append(e)

drones = []
for i in range(dronesN):
    drones.append(Drone(payload,i))

if(args.verbose==1):
    print(orderSorted)


#processDelivery(orderSorted,drones)

