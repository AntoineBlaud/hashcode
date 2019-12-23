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
        self.products.remove(i)
        self.q-=1

    def __str__(self):
        return "O_%d_%d_%d"%(self.x,self.y,self.q)

    def __repr__(self):
        return "O_%d_%d_%d"%(self.x,self.y,self.q)


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


def processDelivery(orderSorted,dronesN):
    for order in orderSorted:
        pass




temp =  rangeOrdersPerInterest(warehouses,orders,dronesN)
# on transforme en un tableau a une seule dimension
ordersSorted = []
for l in temp: 
    for e in l: ordersSorted.append(e)







if(args.verbose==1):
    print(ordersSorted)