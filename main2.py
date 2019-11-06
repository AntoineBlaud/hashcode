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
    f = open("Hashcode/Score/lovely/part2.txt","r");
    dic = json.load(f)
    arr = dic["array"]
    scoreVV(arr)
   



    
