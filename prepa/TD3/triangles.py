
import sys
import os
import time
import re
import functools
import random

#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD3/samples-C3_Triangles/3.in", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()



def compute_size(grid, i, j, length, width):
    n = 0
    while((i + n < length) and (j + n  < width) and (grid[i + n][j - n: j + n + 1] == ['.' for _ in range(2 * n + 1)])):
        n += 1
    return n



if __name__ == '__main__':
    length, width = map(int, get_input().split(" "))
    grid = [list(get_input())  for _ in range(length)]
    i, j, bigger_tr = 0, 0, 0
    while(i < length and j < width):

            for j in range(bigger_tr, width - bigger_tr):
                carac = grid[i][j]
                if carac == '.':
                        size = compute_size(grid, i, j, length, width)
                        if size > bigger_tr:
                                bigger_tr = size
            i += 1
    print(bigger_tr)



