import threading
import multiprocessing
from ctypes import *
import json


class Algo():

    libc = CDLL("/home/darkloner99/code/Hashcode/Hashcode/lib.so")

    def __init__(self, input, path):
        self.input = input
        self.path = path
    

    def resolve(self):
        self.input_part1 = self.input[:len(input)/2-1]
        self.input_part2 = self.input[len(input)/2:]

        p1 = multiprocessing.Process(target=self.glouton,args = (self.input_part1,"P1/",))
        p2 = multiprocessing.Process(target=self.glouton,args = (self.input_part2,"P2/",))

        p1.start()
        p2.start()


    def glouton(self, input,custom_p):
        
        dic = {"DATA": input}
        js = json.dumps(dic)
        f = open(self.path+custom_p+"in.txt","w")
        f.write(js)
        f.close()
        self.libc.readJson((self.path+custom_p+ "in.txt").encode('utf-8'))
        self.libc.config((self.path+custom_p).encode('utf-8'), "DATA".encode('utf-8'))
        self.libc.mainHVV()
