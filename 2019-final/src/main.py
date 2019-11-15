from Node import Node
from Server import Server
from IO import IO
import random
from copy import *
import time
import operator
import sys
import os

URGENT_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/c_urgent.in"
EXEMPLE_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/a_example.in"
NARROW_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/b_narrow.in"
BIG_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/f_big.in"
TYPICAL_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/d_typical.in"
INTRIGUING_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/e_intriguing.in"
# Pas encore initialiser
SERVERS = None


def urgent_evalQuality(node):
    '''
    Evalue la qualité d'un noeud(décisif) suivant la deadline, le nombre de points et le nombre de targets incluent dans la target (c5 c3)
    '''
    if(node.target):
        return node.packs["points"]*2 + node.packs["deadline"]
    return 0

def manytar_evalQuality(node):
    '''
    Evalue la qualité d'un noeud(décisif) en fonction des dépendances avec d'autres noeuds(décisif)
    '''
    if(len(node.childrens)==0):
        return urgent_evalQuality(node)
    points = 0
    for node1 in node.childrens.values():
        points += manytar_evalQuality(node1)
    return points + urgent_evalQuality(node) 


def bestNode(data):
    '''
    Recherche les noeuds les plus interessents
    '''

    #Default choice
    best_choice = {}
    best_pt = manytar_evalQuality(data[0])
    best_choice[data[0]] = best_pt
    #Point counter
    for node in data:
        single = manytar_evalQuality(node)
        tmp_pt = best_pt
        if node not in best_choice:
            if((best_pt*0.9)<single):
                best_pt = single
                best_choice[node] = best_pt
    best_choice = sorted(best_choice.items(), key=operator.itemgetter(1), reverse=True)
    rINT = random.randint(0,min(4,len(data)))
    rChOICE = deepcopy(best_choice[rINT][0])
    best_choice.remove(best_choice[rINT])
    return rChOICE

def construct(target:Node):
    '''
    Try to add the target 
    '''
    points_before = SERVERS.evalTotalPoint()
    SERVERS.start(target)
    points_after = SERVERS.evalTotalPoint() 
    if(points_after == points_before):
        SERVERS.restore("backup_level_2.json")
    



if __name__== '__main__':
    #multiprocessing.set_start_method('spawn', True)
    start = time.time()
    # Load data
    io = IO(INTRIGUING_IN)
    targets = io.getData()
    SERVERS = Server(io.NavailableServers)
    size = len(targets)
    MAX_POINT = 0
    BEST_SERVER = 0
    # NULL
    SERVERS.backup("backup_level_1.json")
    targets_copy = deepcopy(targets)

    for x in range(0,10):
        for y in range(0,size):
            ### CHANGER ICI
            target = targets[size - y - 1]
            construct(target)
            sys.stdout.write(str(y)+"/"+str(size)+ "  " + str(SERVERS.evalTotalPoint())+"\r")
            sys.stdout.flush()
        # Eval points
        CUR_POINT = SERVERS.evalTotalPoint()
        if(CUR_POINT > MAX_POINT):
            MAX_POINT = CUR_POINT
            BEST_SERVER  = x
            SERVERS.backup("backup_level_3.json")

        # SET ALL TO 0
        SERVERS.restore("backup_level_1.json")
        targets = deepcopy(targets_copy)
        print(str(x)+"/10" +  "  Points: " + str(CUR_POINT))

    SERVERS.restore("backup_level_3.json")
    print("END")
# Print elapsed time
    total = time.time() - start
    print("Elapsed: "+ str(total))

    

