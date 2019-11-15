from Node import Node
from Server import Server
from IO import IO
import random
from copy import *
import time


EXEMPLE_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/a_example.in"
NARROW_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/b_narrow.in"
BIG_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/f_big.in"
SERVERS = Server(2)

def evalQuality(node):
    '''
    Evalue la qualite d'un noeud(decisif)
    '''
    return 1/(node.packs["deadline"])*5

def dada(data):
    '''
    Recherche les noeuds les plus interessents
    '''

    #Default choice
    best_choice = []
    best_choice.append(data[len(data) - 1])
    #Point counter
    best_pt = evalQuality(data[len(data) - 1])
    for node in data:
        single = evalQuality(node)
        if((best_pt - best_pt*0.1)<single):
            best_pt = single
            best_choice.append(node)

    a = random.choice(best_choice)
    b = deepcopy(a)
    data.remove(a)
    return b

def narrow_construct(target):
    #sauvegarder
    #division process
    #evaluer
    SERVERS.start(target)
    pass



if __name__== '__main__':
     #multiprocessing.set_start_method('spawn', True)
     start = time.time()
     io = IO(EXEMPLE_IN)
     targets = io.getData()
     size = len(targets)
     for i in range(0,size):
         #Select Best choice
        target = targets[i]
        print(str(i)+" /"+str(size))
        narrow_construct(target)

     total = time.time() - start
     print("Elapsed: "+ str(total))
     print("OK")

    

