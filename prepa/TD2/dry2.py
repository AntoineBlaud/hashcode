import sys
import os
import time
import re
import functools
import random

f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/samples-E2_DryIslands/2.in", 'r')


def get_input():
    #return input().strip()
    return f.readline().strip()



def apply_dry(mapping, i , j):

    for x in range(max(i-1,0),min(i+2,n)):
        for y in range(max(j-1,0),min(j+2,m)):
            if(mapping[x][y] =='.'):
                mapping[x][y] = 0


def check_bound(mapping,p1,p2):

    return (p1 < len(mapping) and p2 < len(mapping[0]) and p1 >= 0 and p2 >= 0)


def set_zone(mapping, i ,j):

    
    rangexy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    queue = []
    queue.append((i, j))

    while(len(queue) > 0):

        i, j = queue.pop()
        for x, y in rangexy:
            p1, p2 = x + i, y + j

            if check_bound(mapping,p1,p2) :

                if mapping[p1][p2] == '.':
                    mapping[p1][p2] = 1
                    queue.append((p1, p2))




    
if __name__ == '__main__':

    mapping = []

    # get input 
    n, m = map(int,get_input().split(" "))
    for _ in range(n):
        mapping.append(list(get_input()))


    # find and transform wet zone 
    for i, line in enumerate(mapping):
        for j, v in enumerate(line):
            if(v == '#'):
                apply_dry(mapping,i,j)
                

 
    #  find and count zone
    cpt = 0
    for i, line in enumerate(mapping):
        for j, v in enumerate(line):

            if v == '.':
                set_zone(mapping,i,j)
                cpt+=1

    print(cpt)
              



