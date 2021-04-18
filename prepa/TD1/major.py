import sys
import os
import time
import re
import functools
import random

if __name__ == '__main__':

    size_e,size_m = map(int,input().strip().split(" "))
    coeff = list(map(int,input().strip().split(" ")))

    best_e =""
    best_g = -1

    for student in range(size_e):

        average = 0
        inputs = input().strip()
        name,grades = inputs.split(" ")[0], list(map(int,inputs.split(" ")[1:]))
        
        for i,c in enumerate(coeff):
            average+=c*grades[i]

        average= average/len(grades)

        if(average>best_g):
            best_e = name
            best_g = average

        elif(average==best_g):
            best_e ="EX AEQUO"

    
    sys.stdout.buffer.write(best_e.encode())

        


  
