import sys
import os
import time
import argparse
import re
from copy import copy, deepcopy
import pulp
from functools import reduce
import pickle
import multiprocessing
import random
import datetime
import tqdm
# import matplotlib.pyplot as plt


#########################################################
# Lire 3 fois le problème
# Communiquer afin de bien être d'accord sur ce qu'il faut faire (le sujet du problème)
# Mettre sujet sur téléphone

# Voir ensemble algo:
#   - complexité
#   - structure de données à utiliser
#   - structure principale du code (étapes importantes)
#   - Performances (travailler avec des index, faire des listes et dictionnaire constant, optimiser la boucle appelée le plus de fois)
#   - les différentes input
#   - analogie avec un ancien problème ou autre
#
# Checkpoint:
#   toute les 30 minutes
#
#
#########################################################
if __name__ == '__main__':

    DEFAULT_F = ""
    OUTPUT_F = ""

    parser = argparse.ArgumentParser(description='Hashcode 2020 qualif')
    parser.add_argument('-i', '--filein', help='Input file',
                        default=DEFAULT_F, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',
                        default=OUTPUT_F, type=str)
    parser.add_argument('-v', '--verbose', default=-1,
                        help='verbose mode', type=int)
    args = parser.parse_args()

    # map(int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
    # [int(x) for x in re.sub("\n", "", f.readline()).split(" ")]
    # [str(x) for x in re.sub("\n", "", f.readline()).split(" ")]

    # Input process
    with open(args.filein) as f:
        pass

    # output process
    with open(args.fileout) as f:
        pass
