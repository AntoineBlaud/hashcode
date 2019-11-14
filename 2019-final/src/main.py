from Node import Node
from Server import Server
from IO import IO
import random




EXEMPLE_IN = "/home/bertolottoloic/Code/hashcode/2019-final/final_round_2019.in/a_example.in"
NARROW_IN = "/home/bertolottoloic/Code/hashcode/2019-final/final_round_2019.in/b_narrow.in"

SERVERS = Server(2)

def evalQuality(node):
    '''
    Evalue la qualité d'un noeud(décisif) suivant la deadline, le nombre de points et le nombre de targets incluent dans la target (c5 c3)
    '''
    return 1/(node.pack["deadline"])*5

def narrow(data):
    '''
    Recherche les noeuds les plus intéressents
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

    return random.choice(best_choice)

def narrow_construct(target):
    #sauvegarder
    #division process
    #evaluer
    pass



if __name__== '__main__':
     #multiprocessing.set_start_method('spawn', True)
     io = IO(EXEMPLE_IN)
     targets = io.getData()
    
     for i in range(0,len(targets)-1):
         #Select Best choice
        target = narrow(targets)
        targets.remove(target)
        narrow_construct(target)

    

