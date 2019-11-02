import threading
import multiprocessing
from Score import Score
from ctypes import *


class Algo():

    libc = CDLL("./lib.so")

    def __init__(self, input):
        self.input = input
    

    def resolve(self):
        self.input_part1 = self.input[:39999]
        self.input_part2 = self.input[40000:]

        p1 = multiprocessing.Process(target=self.glouton1,args = (self.input_part1,))
        p2 = multiprocessing.Process(target=self.glouton1,args = (self.input_part2,))

        p1.start()
        #p2.start()
        score = Score("int.txt","out.txt")
        score.start()


    def glouton1(self, input):

        d = "filename"
        #self.libc.glouton.argstypes = [c_char_p,c_int]
        s#t = create_string_buffer(b'Test')
        #self.libc.glouton("Test".encode('utf-8'), 0)
