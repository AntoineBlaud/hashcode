import sys
import os
import time
import re
import functools
import random

#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/AllSums/2.in", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()


def find_fragments(done,borneinf,bornesup):

    temp = []

    for x in range(borneinf,bornesup+1):
        for y in range(borneinf,bornesup+1)[::-1]:
            if((x,y) in done):
                temp.append((done[(x,y)],x, y))
                resinf, ressup = find_fragments(done,borneinf, x), find_fragments(done, y+1, bornesup)
                if(len(resinf)> 0):
                    temp+=(resinf)
                if(len(ressup)>0):
                    temp+=(ressup)
                return temp

    return temp
                    

    
if __name__ == '__main__':

    n,ns = map(int,get_input().split(" "))
    array = list(map(int,get_input().split(" ")))

    done = {}

    for _ in range(ns):
        borneinf, bornesup = map(int,get_input().split(" "))

        res = 0

        fragments = find_fragments(done,borneinf,bornesup)
        fragments = sorted(fragments, key=lambda f : f[1])

        if(len(fragments)==0):
            res = sum(array[borneinf:bornesup+1])
            done[(borneinf,bornesup)] = res
            print(res)

    
        else:
            current = borneinf
            for fragment in fragments:
                score,binf,bsup = fragment
                if(binf>current):
                    res+=sum(array[current:binf])
                res+=score
                current = bsup + 1
                done[(borneinf,bsup)] = res
            if(current<=bornesup):
                res+=sum(array[current:bornesup+1])
            print(res)





