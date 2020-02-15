
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

# Profilers
######################################################################################
#from guppy import hpy
# h = hpy()
# h.heap()
######################################################################################

M = 100000

default_in = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\pizza regina\\in\\medium.in"
default_out = "out/exemple.out"

'''
Cette fonction s'occupe de retourner toutes les découpe possible de part pour un mapping
il y a donc la même cellule dans plusieurs combinaisons de part 
Les combinaisons de part se base sur le critère de taille maximum et la quantité minimal d'ingrédient
'''


def find_all_combination(mapping, min_ing, max_cell, pizza):

    # ici juste liste les combinaisons en prenant en compte que la taille maximal
    combinations_step1 = []
    combinations_step2 = []
    y0, x0, item = mapping[0]
    y1, x1, item = mapping[len(mapping)-1]
    # pour chaque cellules dans la pizza
    for i0 in range(x0, x1+1):
        for j0 in range(y0, y1+1):
            # teste les combinaisons et ajoute les combinaisons valides
            for i1 in range(i0, min(x1+1, i0+max_cell)):
                for j1 in range(j0, min(y1+1, j0+int(max_cell/(i1-i0+1)))):
                    combinations_step1.append((i0, i1, j0, j1))

    # maintenand on filtre en prenant aussi en compte le nombre minimal d'ingrédient
    for combination in combinations_step1:
        x0, x1, y0, y1 = combination
        tomato = 0
        mushroom = 0
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                item = pizza.items[y][x]
                if(item == "T"):
                    tomato += 1
                if(item == "M"):
                    mushroom += 1
        if(tomato >= min_ing & mushroom >= min_ing):
            combinations_step2.append(combination)
    return combinations_step2


def find_intersect(x, y, combinations):
    intersect_combinations = []
    for c in combinations:
        x0, x1, y0, y1 = c
        if(x0 <= x <= x1 and y0 <= y <= y1):
            intersect_combinations.append(c)

    return intersect_combinations


def get_value_at_index(values, index):
    new_value = []
    for i in range(len(values)):
        if(i in index):
            new_value.append(values[i])
    return new_value


def get_mapping_property(mapping):
    y0, x0, item = mapping[0]
    y1, x1, item = mapping[len(mapping)-1]
    return (x0, x1, y0, y1)


def solve_combination(combinations_in, mapping):

    x0, x1, y0, y1 = get_mapping_property(mapping)
    prob = pulp.LpProblem("Pizza_hashcode", pulp.LpMaximize)
    pslice = pulp.LpVariable.dicts(
        "slice", combinations_in, lowBound=0, upBound=1, cat=pulp.LpInteger)
    cells = pulp.LpVariable.dicts(
        "cell", [(m[0], m[1]) for m in mapping], lowBound=0, upBound=1, cat=pulp.LpInteger)

    prob += pulp.lpSum(cells)
    for (y, x), cell in cells.items():
        intersect = find_intersect(x, y, pslice.keys())
        prob += pulp.lpSum([v for (k, v) in pslice.items()
                            if k in intersect]) <= 1
        prob += pulp.lpSum([v for (k, v) in pslice.items()
                            if k in intersect]) == cell

    prob.solve()

    slice_out = []
    cell_out = {}
    for k, v in pslice.items():
        if(pulp.value(v) == 1):
            slice_out.append(k)
    for k, v in cells.items():
        cell_out[k] = pulp.value(v)

    return slice_out, cell_out


def save(pizza, slices, file):
    out = data(slices, pizza.columsN, pizza.rowsN)
    with open(file, "wb") as f:
        pickle.dump(out, f)


def join_part(slices_list):
    return reduce(lambda x, y: x+y, slices_list)


def compute_single_map(args):
    mapping, min_ing, max_cell, pizza, step = args
    combinations = find_all_combination(mapping, min_ing, max_cell, pizza)
    slice_out, cell_out = solve_combination(combinations, mapping)
    lock = multiprocessing.RLock()
    with lock:
        sys.stdout.write(str(step)+" done!   "+'\r')
        sys.stdout.flush()

    return slice_out


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Compute hashcode pizza regina')
    parser.add_argument('-i', '--filein', help='Input file',
                        default=default_in, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',
                        default=default_out, type=str)
    parser.add_argument('-v', '--verbose', default=-1,
                        help='verbose mode', type=int)
    args = parser.parse_args()

    mapping = []
    items = []
    slice_list = []
    with open(args.filein) as f:
        rows_N, colums_N, min_ing, max_cell = map(
            int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
        line = [list(re.sub("\n", "", f.readline()))for i in range(rows_N)]
        mapping = ([(i, j, line[i][j]) for i in range(rows_N)
                    for j in range(colums_N)])
        items = ([[line[i][j] for j in range(colums_N)]for i in range(rows_N)])

    pizza = Pizza(mapping, items, rows_N, colums_N)
    mappings = pizza.split_pizza_into_map(20, 20)
    p = multiprocessing.Pool(multiprocessing.cpu_count())
    print("Must compute %d steps" % len(mappings))
    slice_list = p.map(compute_single_map, [(
        m, min_ing, max_cell, pizza, i) for m in mappings for i in range(len(mappings))])
    p.close()
    p.join()
    slice_out = join_part(slice_list)
    save(pizza, slice_out, args.fileout)
