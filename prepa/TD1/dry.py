import sys
import os
import time
import re
import functools
import random

if __name__ == '__main__':

    size = int(input().strip())

    for i in range(size):
        nexts = input().strip()

        if(i==0):
            minimum = nexts

        else:
            
            if(len(minimum) > len(nexts)):
                minimum = nexts     

            elif(len(minimum)==len(nexts) and nexts < minimum):
                minimum = nexts   

    sys.stdout.buffer.write(minimum.encode())
