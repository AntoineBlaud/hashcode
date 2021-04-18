import sys
import os
import time
import re
import functools
import random

#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD3/samples-A3_Color_Median/1.in", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()

def convert(color):
    return  0.2126*int(color[1:3],16) + 0.7152*int(color[3:5],16) + 0.0722*int(color[5:7],16)


if __name__ == '__main__':

    colors = list(get_input().split(" "))
    brightness = map(convert,colors)

    results = sorted(zip(brightness,colors))
    results = zip(*results)
    brightness,colors = [ list(tuple) for tuple in  results]
    print(colors[int(len(colors)/2)])
