import sys
import os
import time
import re
import functools
import random

#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/DivisionGame/2.in", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()




def compute(n, p):
    # joueur suivant 
    nextp = (p+1)%2
    # si vide alors on retourne l'autre joueur 
    if(n==0):
        return nextp
    #sinon on joue
    n-=1
    # si je joueur courant peut gagner avec une de ces trois possibilité alors il la joue et c'est toujours lui le winner
    if(compute(int(n/3),nextp) == p):
        return p
    if(compute(int(n/2),nextp) == p):
        return p
    if(compute(int(n/7),nextp == p)):
        return p

    #sinon c'est l'autre joueur qui prend la tête
    return nextp

    



if __name__ == '__main__':

    n = int(get_input())
    winner = compute(n, 0)
    if(winner == 0):
        print("First player")
    else:
        print("Second player")

    
