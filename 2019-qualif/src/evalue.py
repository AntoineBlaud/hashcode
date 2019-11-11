import os
import sys
import multiprocessing
import threading
from random import *
import json

def scoreVV(arr):
    S  = 0;
    x = 0;

    while(x<len(arr)-1):
        arr_temp = arr[x][2:]
        arr_temp2= arr[x+1][2:] 
        for e in arr_temp:
            if(e in arr_temp2):
                S+=1
        x+=1
    print(S)


def scoreVH(arr):
    S = 0;
    x=0;
    while(x<len(arr)-4):
        H = arr[x][2:]
        V = arr[x+1][2:] + arr[x+2][2:]
        H =list(dict.fromkeys(H))
        V=list(dict.fromkeys(V))
        for e in H:
            if(e in V):
                S+=1

        H = arr[x+3][2:]
        H =list(dict.fromkeys(H))
        for e in H:
            if(e in V):
                S+=1
        x+=3;
    return S
        



def scoreHH(arr):
    S  = 0;
    x = 0;

    while(x<len(arr)-4):
        arr_temp = arr[x][2:] + arr[x+1][2:]
        arr_temp2= arr[x+2][2:] + arr[x+3][2:]
        arr_temp =list(dict.fromkeys(arr_temp))
        arr_temp2 =list(dict.fromkeys(arr_temp2))
        for e in arr_temp:
            if(e in arr_temp2):
                S+=1

        x+=2
    print(S)

def isDuplicate(arr):
    
    recept = []
    for x in range(0,len(arr)):
        n = arr[x][0];
        if(n in recept):
            print("ERROR")
        else:
            recept.append(n)




if __name__ == '__main__':
    #f = open("Hashcode/Score/lovely/part2.txt","r");
    f = open("data/data2/saved.txt","r");
    dic = json.load(f)
    arr = dic["array"]
    print(scoreVH(arr))
   



    
