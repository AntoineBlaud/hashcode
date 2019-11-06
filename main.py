import os
import sys
import multiprocessing
import threading
from Input import Input
from Stats import Stat
from random import *
from algo import Algo
import json

if __name__ == '__main__':
    #multiprocessing.set_start_method('spawn', True)
    inputfile1 = Input("/home/darkloner99/code/Hashcode/Hashcode2019/qualification_round_2019.in/b_lovely_landscapes.txt")
    array1 = inputfile1.fileToArray(removeItem={1}, ignoreLine={0}).array

    statarray1  = Stat(array1,2,removeItemIndepth2={0,1})

    r = Random()
    shuffle(array1)
    a1 = Algo(array1)
    a1.resolve()


    







