from Node import Node
from Server import Server
from IO import IO
import random
<<<<<<< HEAD
import operator


EXEMPLE_IN = "/home/bertolottoloic/Code/hashcode/2019-final/final_round_2019.in/a_example.in"
NARROW_IN = "/home/bertolottoloic/Code/hashcode/2019-final/final_round_2019.in/b_narrow.in"

=======
from copy import *
import time


EXEMPLE_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/a_example.in"
NARROW_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/b_narrow.in"
BIG_IN = "/home/darkloner99/code/Hashcode/Hashcode/2019-final/final_round_2019.in/f_big.in"
>>>>>>> 8b943755bda4148e7e2a95b541bbdc328aa1a735
SERVERS = Server(2)

def urgent_evalQuality(node):
    '''
    Evalue la qualité d'un noeud(décisif) suivant la deadline, le nombre de points et le nombre de targets incluent dans la target (c5 c3)
    '''
    if(node.target):
        return node.packs["points"]*2 + (1/(node.packs["deadline"]))*1000*node.packs["points"]
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
<<<<<<< HEAD
        single = manytar_evalQuality(node)
        tmp_pt = best_pt
        if node not in best_choice:
            if((best_pt*0.9)<single):
                best_pt = single
                best_choice[node] = best_pt
    best_choice = sorted(best_choice.items(), key=operator.itemgetter(1), reverse=True)
    return best_choice[random.randint(1,5)][0]
=======
        single = evalQuality(node)
        if((best_pt - best_pt*0.1)<single):
            best_pt = single
            best_choice.append(node)

    a = random.choice(best_choice)
    b = deepcopy(a)
    data.remove(a)
    return b
>>>>>>> 8b943755bda4148e7e2a95b541bbdc328aa1a735

def narrow_construct(target):
    #sauvegarder
    #division process
    #evaluer
    SERVERS.start(target)
    pass



if __name__== '__main__':
     #multiprocessing.set_start_method('spawn', True)
<<<<<<< HEAD
     io = IO(NARROW_IN)
     targets = io.getData()
     target = bestNode(targets)
     c=4

    
     
=======
     start = time.time()
     io = IO(EXEMPLE_IN)
     targets = io.getData()
     size = len(targets)
     for i in range(0,size):
         #Select Best choice
        target = targets[i]
        print(str(i)+" /"+str(size))
        narrow_construct(target)
>>>>>>> 8b943755bda4148e7e2a95b541bbdc328aa1a735

     total = time.time() - start
     print("Elapsed: "+ str(total))
     print("OK")

    

