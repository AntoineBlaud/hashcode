import time
import math
import sys
import os
import random
import threading
from numba import *
import numpy as np
import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)

#@jit(nopython=True,parallel=True)
@profile
def test(size:int,c):
    for a in range(1,size):
        for b in range(1,size):
            c[1][b] = b
    return c


s = time.time()
c = np.ones((3,100**2))
b =  test(100,c)
print(str(time.time()-s))