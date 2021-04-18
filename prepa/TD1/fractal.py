import sys
import os
import time
import re
import functools
import random



def print_arr(pattern, results, i, j):

    for x in range(len(pattern[0])):

        for y in range(len(pattern)):

            results[i+y][j+x] = pattern[y][x]

    return results



if __name__ == '__main__':



    size_e = int(input().strip())

    f1 = "┌┐\n" \
         "└┘"

    f2 = "┌┐┌┐\n"\
         "└┌┐┘\n"\
         "┌└┘┐\n"\
         "└┘└┘"



    if(size_e == 1):
        sys.stdout.buffer.write(f1.encode())

    elif(size_e == 2):
        sys.stdout.buffer.write(f2.encode())

    else:
        dim = 2
        results = [list(s) for s in f2.split('\n')]
        while(dim!=size_e):
            new_results = [[' ' for x in range(len(results[0])*2)] for y in range(len(results)*2)]
            
            middle_y = len(results)
            middle_x = len(results[0])

            print_arr(results,new_results,0,0)
            print_arr(results,new_results,0,middle_x)
            print_arr(results,new_results,middle_y,0)
            print_arr(results,new_results,middle_y,middle_x)
            print_arr(results,new_results,int(middle_y/2),int(middle_x/2))
            results = new_results.copy()
            dim+=1

    

        for i,x in enumerate(results):
            results[i] = ''.join(map(str, results[i])) + '\n'
        
        results[-1] = results[-1][:-1]
        
        results = ''.join(map(str, results))
        sys.stdout.buffer.write(results.encode())




    

  