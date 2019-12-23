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


DEFAULT_F = "/home/darkloner99/code/Hashcode/Hashcode/2016-qualif/qualification_round_2016.in/busy_day.in"
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

    def setProductsOrder(self,products: list):
        self.products = products
    
    def inOrder(self,i:int):
        return i in self.order
    
    def removeProduct(self,i):
        self.products[i] = 0
        self.q-=1

    def __str__(self):
        return "O_%d_%d_%d"%(self.x,self.y,self.q)

    def __repr__(self):
        return "O_%d_%d_%d"%(self.x,self.y,self.q)

    def __len__(self):
        return len([x for x in self.products if x==1])


class Drone:
    def __init(self,c,id):
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

    def load(self,object, q):
        if(object in self.items.keys()):
            self.items[object]+=q
            c-=c*items[object]
        else:
            self.items[object]=q
            c-=c*items[object]

    def unload(self,object,q):
        self.items[object]-=q
        c+=c*items[object]

    def getQuantity(self,object):
        if(object in self.items.keys()): return self.items[object]
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


# Params 
##########################################
R = 100


##########################################

if(args.verbose == 0):   
    print(warehouses)
    print(items)
    print(orders)


def distance(x1,y1,x2,y2):
    return sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)


def getOrderAtProximity(w,orders, r):
    # Retourne toutes les commandes dans un rayon r autour d'un entrepot.
    ordersAtProximity = []
    xw = w.x
    yw = w.y
    for order in orders:
        xo = order.x
        yo = order.y
        if(distance(xo,yo,xw,yw)<R): ordersAtProximity.append(order)
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

def foundBestInterestingDrone(drones:list,idP,order:Order):
    # Trouve le drone le plus intéressent pour aller faire une livraison
    pass


def deliverProduct(drone:Drone,Order:order,idP):
    # ici on gere aussi load , wait etc...
    pass

def dronesDispo(drones:list):
    # si temsp de simulation pour chaque drone > temps max alors return false
    pass




def processDelivery(orderSorted,drones):
    # Attention, il peut y avoir plusieurs fois la même commande dans la liste orderSorted
    while(len(orderSorted)> 0 and dronesDispo(drones)):
        order = orderSorted.pop()
        if(len(order)>0):
            for id,q in zip(order.products,range(itemN)):
                drone = foundBestInterestingDrone(drones,id,order)
                if(drone!=False):
                    deliverProduct(drone,Order,id)


                


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


processDelivery(orderSorted,drones)