
import sys
import os
import time
import argparse
import re
from copy import copy
import pulp
from functools import reduce
import pickle
import multiprocessing
from Pizza import Pizza
from Data import data


if __name__ == '__main__':
    default_in = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\pizza regina\\in\\medium.in"
    parser = argparse.ArgumentParser(description='Compute hashcode pizza regina')
    parser.add_argument('-i', '--filein', help='Input file',default=default_in, type=str)

    args = parser.parse_args()

    mapping = []
    items = []
    with open(args.filein) as f:
        rows_N, colums_N, min_ing, max_cell = map(int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
        line = [list(re.sub("\n", "", f.readline()))for i in range(rows_N)]
        mapping = ([(i, j, line[i][j]) for i in range(rows_N) for j in range(colums_N)])
        items = ([[line[i][j] for j in range(colums_N)]for i in range(rows_N)])

    pizza = Pizza(mapping, items, rows_N, colums_N)

    with open("object", "rb") as f:
        data = pickle.load(f)
        score=0
        print("Nombre de parts: %d"%len(data.slices))
        cells = {}
        for s in data.slices:
            (x0, x1, y0, y1) = s
            area = 0; tomatoes = 0;mushrooms = 0;
            for x in range(x0, x1+1):
                for y in range(y0, y1+1):
                    if(pizza.items[y][x]=='T'):tomatoes+=1
                    if(pizza.items[y][x]=='M'):mushrooms+=1
                    area+=1
                    # Vérification de l'unicité d'une cellule
                    if((y,x) in cells.keys()):
                         print('\033[93m'+"Error !! Cell in multiple slice"+'\033[0m')
                    cells[(y,x)] = ""

            if(area<=max_cell and tomatoes>=min_ing and mushrooms >=min_ing):
                score+=area

        print('\033[94m'+"Score: "+str(score)+'\033[0m')

                    
        
    
