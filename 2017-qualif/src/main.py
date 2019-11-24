import numpy as np
from Process import *
from tests import test_server_score,test_knapstack
import random


TEST_IN = "/home/darkloner99/code/Hashcode/Hashcode/2017-qualif/qualification_round_2017.in/streaming/exemple.in"


# Start_Point here
def main():
    # Get Input
    io = IO(TEST_IN)
    io.getData()
    data = Data(io)
    process = Process(data)
    test_knapstack()
main()
