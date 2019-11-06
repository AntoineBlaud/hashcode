import threading
import multiprocessing
from Score import Score
from ctypes import *
import json


class Algo():

    libc = CDLL("./lib.so")

    def __init__(self, input):
        self.input = input
    

    def resolve(self):
        self.input_part1 = self.input[:39999]
        self.input_part2 = self.input[40000:]

        p1 = multiprocessing.Process(target=self.glouton1,args = (self.input_part1,"data1/",))
        p2 = multiprocessing.Process(target=self.glouton1,args = (self.input_part2,"data2/",))

        p1.start()
        p2.start()
        score = Score("in.txt","out.txt")
        #score.start()


    def glouton1(self, input,path):
        
        dic = {"array": input}
        js = json.dumps(dic)
        f = open("data/"+path+"in.txt","w")
        f.write(js)
        f.close()
        self.libc.readJson(("data/"+path+"in.txt").encode('utf-8'))
        self.libc.glouton(("data/"+path).encode('utf-8'),"array".encode('utf-8'))
