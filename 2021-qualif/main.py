import sys
import os
import time
import argparse
import re
from copy import copy, deepcopy
import pulp
from functools import reduce
import pickle
import multiprocessing
import random
import datetime
import math
import tqdm
# import matplotlib.pyplot as plt

if __name__ == '__main__':

    DEFAULT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2021-qualif\\in\\e.txt"
    OUTPUT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2021-qualif\\out\\e.txt"

    parser = argparse.ArgumentParser(description='Compute hashcode 2021')
    parser.add_argument('-i', '--filein', help='Input file',default=DEFAULT_F, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',default=OUTPUT_F, type=str)
    parser.add_argument('-v', '--verbose', default=-1,help='verbose mode', type=int)
    args = parser.parse_args()


    # map(int, [int(x) for x in re.sub("\\n", "", f.readline()).split(" ")])
    # [int(x) for x in re.sub("\\n", "", f.readline()).split(" ")]
    # [str(x) for x in re.sub("\\n", "", f.readline()).split(" ")]
    with open(args.filein) as f:
        duration, intersectionsN, streetsN, carsN, bonusN = map(int, [int(x) for x in re.sub("\\n", "", f.readline()).split(" ")])
        streets = []
        intersections = {i:[] for i in range(intersectionsN)}
        cars = []
        for _ in range(streetsN):
            streets.append(tuple(f.readline().strip().split(" ")))
        for i in range(streetsN):
            (B, E, streetname, L) = streets[i]
            streets[i] = (int(B), int(E) ,str(streetname), int(L))
            intersections[int(E)].append(streetname)
        for _ in range(carsN):
            cars.append(f.readline().strip().split(" "))
        for i in range(carsN):
            cars[i][0] = int(cars[i][0])
    

    scoreboard = {x[2]:0 for x in streets}
    cycles = {i:[] for i in range(intersectionsN)}
    
    for car in cars:
        for x in car[1:]:
            scoreboard[x]+=1

    for i,intersec in enumerate(cycles.values()):
        incoming = intersections[i]
        scores = [scoreboard[name] for name in incoming]
        minj = 0
        for j,x in enumerate(scores):
            if(x > 1):
                cycles[i].append(1)
            else:
                intersections[i].remove(intersections[i][j-minj])
                minj+=1
    
    for i in range(intersectionsN):
        cycle, intersec =  cycles[i], intersections[i]
        if(len(cycle) == 0):
            del cycles[i]
            del intersections[i]
        

    
    with open(args.fileout, "w") as f: 
        f.write(str(len(cycles))+"\n")
        for i in cycles.keys():
            cycle = cycles[i]
            f.write(str(i) + "\n")
            f.write(str(len(cycle))+"\n")
            streetname = intersections[i]

            for name,value in zip(streetname,cycle):
                f.write(name + " " + str(value)+"\n")








        






