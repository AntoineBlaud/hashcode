import os
import sys
import multiprocessing
import threading
from IO import IO
from Stats import Stat
from random import *
from algo import Algo
import json

LOVELY_LANDSCAPES_PATH = "/home/darkloner99/code/Hashcode/Hashcode/qualification_round_2019.in/b_lovely_landscapes.txt"
MEMORABLE_MOMENTS_PATH = "/home/darkloner99/code/Hashcode/Hashcode/qualification_round_2019.in/c_memorable_moments.txt"
SHINY_SELFIES_PATH = "/home/darkloner99/code/Hashcode/Hashcode/qualification_round_2019.in/e_shiny_selfies.txt"
SET_PICTURE_PATH = "/home/darkloner99/code/Hashcode/Hashcode/qualification_round_2019.in/d_pet_pictures.txt"

LOVELY_LANDSCAPES_OUT_PATH = "/home/darkloner99/code/Hashcode/Hashcode/Score/lovely"
SET_PICTURE_OUT_PATH = "/home/darkloner99/code/Hashcode/Hashcode/Score/set_picture"
SHINY_OUT_PATH = "/home/darkloner99/code/Hashcode/Hashcode/Score/shiny"

PROCESS_PATH = "/home/darkloner99/code/Hashcode/Hashcode/Process"


def resolve():
    
    io = IO(SET_PICTURE_PATH)

    DATA = io.fileToArray(removeItem={1}, ignoreLine={0}).array
    STATS  = Stat(DATA,2,removeItemIndepth2={0,1})

    shuffle(DATA)
    ALGO = Algo(DATA)
    ALGO.resolve()


def compileOutputH():
    if os.path.exists(LOVELY_LANDSCAPES_OUT_PATH+ "/out.txt"):
        os.remove(LOVELY_LANDSCAPES_OUT_PATH + "/out.txt")
    p1 = os.listdir(LOVELY_LANDSCAPES_OUT_PATH)
    p1 = [(LOVELY_LANDSCAPES_OUT_PATH +"/"+ p) for p in p1]
    out = LOVELY_LANDSCAPES_OUT_PATH + "/out.txt"
    io = IO("");
    io.compileOutputH(p1,out)

def compileOutputV():
    if os.path.exists(SHINY_OUT_PATH  + "/out.txt"):
        os.remove(SHINY_OUT_PATH + "/out.txt")
    p1 = os.listdir(SHINY_OUT_PATH)
    p1 = [(SHINY_OUT_PATH +"/"+ p) for p in p1]
    out = SHINY_OUT_PATH + "/out.txt"
    io = IO("");
    io.compileOutputV(p1,out)

def compileOutputHVV():
    if os.path.exists(SET_PICTURE_OUT_PATH + "/out.txt"):
        os.remove(SET_PICTURE_OUT_PATH + "/out.txt")
    p1 = os.listdir(SET_PICTURE_OUT_PATH)
    p1 = [(SET_PICTURE_OUT_PATH +"/"+ p) for p in p1]
    out = SET_PICTURE_OUT_PATH + "/out.txt"
    io = IO("");
    io.compileOutputHVV(p1,out)


if __name__ == '__main__':
    #multiprocessing.set_start_method('spawn', True)
    compileOutputH()




