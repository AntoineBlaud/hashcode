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

    # inputfile1 = Input("qualification_round_2019.in/b_lovely_landscapes.txt")
    # array1 = inputfile1.fileToArray(removeItem={1}, ignoreLine={0}).array

    # statarray1  = Stat(array1,2,removeItemIndepth2={0,1})

    # r = Random()
    # shuffle(array1)
    # a1 = Algo(array1)
    # a1.resolve()

    a = [["Brique 2"],["Brique 2",["Brique 3"]],"Brique 1",518181]
    d = {"antoine0:":16, "maman":15};
    b = "Hellp"
    f = open("t.json","w")
    json.dump({"tab":a,"valeur":b,"dic":d},f)

    







