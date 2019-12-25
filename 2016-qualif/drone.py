import sys
import os
import time
import argparse
import re
from copy import copy,deepcopy
from math import *
from random import *
from guppy import hpy; h=hpy()


'''
@ Loic: ajuster R (rayon) suivant nombre de drone et valeur incluses
        scoring 
'''

######################################################################################

######################################################################################

DEFAULT_F = "/home/darkloner99/code/Hashcode/Hashcode/2016-qualif/qualification_round_2016.in/redundancy.in"
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
        for i in range(itemN-len(products)):
            self.products.append(0)

    
    def loadProduct(self,i:int,q:int):
        if(self.products[i] - q >=0): self.products[i]-=q;return True
        return False
    def unloadProduct(self,idP,q):
        self.products[idP]+=q

    def getQ(self,idP):
        return self.products[idP]
    def __str__(self):
        return "W_%d_%d"%(self.x,self.y)

    def __repr__(self):
        return "W_%d_%d"%(self.x,self.y)

    def __len__(self):
        t = 0
        for x in self.products: t+=x
        return t




class Order:
    def __init__(self,x,y,q,id):
        self.x = x
        self.y = y
        self.q = q
        self.id = id
        self.completed = False

    def setProductsOrder(self,products: list):
        self.products = [0 for x in range(itemN)]
        for x in products:
           self.products[x]+=1
    
    def inOrder(self,i:int):
        return i in self.products
    
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
        if(idP in self.items.keys()):
            self.items[idP]+=q
            self.c-=q*items[idP]
        else:
            self.items[idP]=q
            self.c-=items[idP]

    def unload(self,idP,q):
        self.items[idP]-=q
        self.c+=q*items[idP]

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
    d  = sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    if(int(d) == d): return d
    return int(d)+1


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
        if((len(ordersPerWuniq)/len(orders))>0.8 and (len(ordersPerW)/len(orders))<=1.4):
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



def foundClosestWharehouseContainingItem(drone, order,warehouses, idP, q):
    # Retourne l'entrepot le plus sur la route contenant la maximun d'item voulu
    # Ici meilleur entrepot mais qui n'a pas tout les élements
    bestQ0D = columnsN + rowsN
    bestQ0Q = 0
    bestQ0 = warehouses[randint(0,len(warehouses)-1)]
    # Ici meilleur entrepot avec assez de produit en stock 
    bestQ1D = columnsN + rowsN
    bestQ1 = warehouses[randint(0,len(warehouses)-1)]
    for w in warehouses:
        d = distance(w.x,w.y,drone.x,drone.y) + distance(w.x,w.y,order.x,order.y) + drone.Tavailable
        # Si dans l'entrepot il y a une quantité suffisante et la distance est meilleur
        if(w.getQ(idP)>=q and bestQ1D>d):
            bestQ1D = d
            bestQ1 = w

        # Sinon on enregistre la meilleur solution
        if(w.getQ(idP)>=bestQ0Q  and bestQ0D>d):
            bestQ0D = d
            bestQ0 = w
            bestQ0Q = w.getQ(idP)

    # Ici pareil que pour drone modifier
    if(bestQ1!=False):
        return bestQ1,bestQ1D
    return bestQ0, bestQ0D


def foundClosestWharehouseOnTheRoad(drone:Drone,order:Order,warehouses):
    # Retourne l'entrepot le plus sur la route
    best = warehouses[randint(0,warehouseN-1)]
    bestd = distance(drone.x,drone.y,best.x,best.y) + distance(best.x,best.y,order.x,order.y)
    for w in warehouses:
        d = distance(drone.x,drone.y,w.x,w.y) + distance(w.x,w.y,order.x,order.y)
        if( d<bestd and len(w)>0):
            best = w
            bestd = d
    return best,bestd



def foundBestInterestingDrone(drones,order,idP,q,warehouses):
    # Retourne le drone le plus intéressent 
    global diMax
    distances =  {}
    xo = order.x
    yo = order.y
    i = 0
    for drone in drones:
        xd = drone.x
        yd = drone.y
        d = rowsN + columnsN
        # Quantité du produit dans le drone
        qInDrone = drone.inDrone(idP)
        # Si la quantité de produit dans le drone est suffisante
        if(qInDrone>=q):
            d = distance(xo,yo,xd,yd)  + drone.Tavailable
        else:
            w,q2 = foundClosestWharehouseContainingItem(drone,order,warehouses,idP,q-qInDrone)
            if(q2>=q):
                d = distance(xo,yo,w.x,w.y) + distance(w.x,w.y,drone.x,drone.y) + drone.Tavailable

        distances[i] = (d, i)
        i+=1

    droneSorted = dict(sorted(distances.items(), key=lambda t: t[1][0]))
    best = list(droneSorted.keys())

    (di, i) = distances[best[0]]
    if(di<diMax):
        return drones[i]
    return False


def makeDeliver(drone:Drone,order:Order,w,idP,q):

    # Ici on vide le drone de tout les items qui ne sont pas dans la commande
    for k,v in drone.items.items():
        if(not order.inOrder(k)):
            drone.unload(k,v)
            w.unloadProduct(k,v)
    
    # On remplit le drone de l'item voulu en priorité
    for i in range(q):
        inWarehouse = w.getQ(idP)
        if(inWarehouse > q):
            if(drone.c > items[idP]):
                drone.load(idP,1)
                w.loadProduct(idP,1)

    # Ensuite on remplit d'autre article de la commande 
    for v,k in zip(order.products,range(itemN)):
        for i in range(v):
            if(drone.c > items[k] and drone.inDrone(k)<=v):
                    drone.load(k,1)
                    if(w.getQ(k)>0):
                        w.loadProduct(idP,1)
    
    # Ensuite on remplit le drone d'item qui ne sont pas dans la commande mais qui sont dans l'entrepot
    for v,k in zip(w.products,range(itemN)):
        for i in range(v):
            if(drone.c > items[k] and drone.inDrone(k)<=M):
                    drone.load(k,1)
                    w.loadProduct(k,1)

    # Ici on livre
    for k,v in drone.items.items():
        for i in range(v): 
            if(order.products[k]>0):
                drone.unload(k,1)
                order.removeProduct(k,1)




def deliverProduct(drone:Drone,order:Order,warehouses,idP,q):
    # ici le drone est deja choisi, on choisi donc maintenand l'entrepot
    global SCORE
    di = distance(drone.x,drone.y,order.x,order.y)
    qd = drone.inDrone(idP)
    wc,dc = foundClosestWharehouseOnTheRoad(drone,order,warehouses)
    if(q-qd>0):
        wp,dp = foundClosestWharehouseContainingItem(drone,order,warehouses,idP,q-qd)
        if(dp < curveCoeff*dc):
            wc,dc = wp,dp

    drone.Tavailable+=dc
    makeDeliver(drone,order,wc,idP,q-qd)
    drone.x  = order.x
    drone.y = order.y

    if(len(order)==0 and order.completed==False):
        order.completed = True
        SCORE+= ((turnN-drone.Tavailable)/turnN)*100
            

        
def dronesDispo(drones:list):
    # si temps de simulation pour chaque drone > temps max alors return false
    for drone in drones:
        if(drone.Tavailable<turnN):
            return True

def calculateAverageProductOrder(orderSorted):
    x = 0
    i = 0
    for order in orderSorted:
        for item in order.products:
            if(item>0):
                i+=1
                x+=item
    return int(x/i) +  1




def process(orderSorted,drones,warehouses):
    # Attention, il peut y avoir plusieurs fois la même commande dans la liste orderSorted
    while(len(orderSorted)> 0 and dronesDispo(drones)):
        order = orderSorted.pop()
        # Si la commande a encore des articles
        if(not order.completed):
            for i in range(0,Pass):
                for idP,q in zip(range(itemN),order.products):
                    if(q>0):
                        # Recuperer drone le plus interessant pour livrer 
                        drone = foundBestInterestingDrone(drones,order,idP,q,warehouses)
                        # Si la livraison est interessente
                        if(drone!=False):
                            deliverProduct(drone,order,warehouses,idP,q)



        

# Params 
##########################################
R = foundOptimumR(warehouses,orders)
SCORE = 0
diMax = 0
Pass = 0
curveCoeff = 0
SIMUL_TIME = 100

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

# moyenne produit
M = calculateAverageProductOrder(orderSorted)

# Regler Params pour trouver le meilleur 
for i in range(SIMUL_TIME):
    diMax = randint(5,turnN)
    Pass = randint(1,10)
    curveCoeff =  randint(2,20)
    
    process(deepcopy(orderSorted),deepcopy(drones),deepcopy(warehouses))
    print("Score:%d  R:%d diMax:%d pass: %d curveCoeff: %d"%(SCORE,R,diMax,Pass,curveCoeff))
    SCORE = 0

