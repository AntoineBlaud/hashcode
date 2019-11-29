import numpy as np
from Process import *
import random


TEST_IN = "/home/darkloner99/code/Hashcode/Hashcode/2017-qualif/qualification_round_2017.in/streaming/exemple.in"
KITTEN_IN = "/home/darkloner99/code/Hashcode/Hashcode/2017-qualif/qualification_round_2017.in/streaming/kittens.in.txt"

# Start_Point here
def main():

    io = IO(KITTEN_IN)
    io.getData()
    data = Data(io)
    process = Process(data)
    print("Starting finding solution...")
    process.dynamic_start()
    print("ok")

main()
