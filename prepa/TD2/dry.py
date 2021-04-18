import sys
import os
import time
import re
import functools
import random

#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/DryLand/1.in", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()


def check_dry(mapping, i , j):

    for x in range(max(i-1,0),min(i+2,n)):
        for y in range(max(j-1,0),min(j+2,m)):
            if(mapping[x][y] =='#'):
                return False
    return True

    
if __name__ == '__main__':

    n, m = map(int,get_input().split(" "))

    mapping = []

    for _ in range(n):
        mapping.append(list(get_input()))

    cpt = 0
    for i,line in enumerate(mapping):
        for j,v in enumerate(line):

            if(v != '#' and check_dry(mapping,i,j)):
                cpt+=1
                


    print(cpt)
    
