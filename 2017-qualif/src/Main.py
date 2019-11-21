import numpy as np
from Process import *

TEST_IN = '/home/bertolottoloic/Code/hashcode/2017-qualif/streaming/test.txt'

def main():
    io = IO(TEST_IN)
    io.getData()
    print("OK")

main()