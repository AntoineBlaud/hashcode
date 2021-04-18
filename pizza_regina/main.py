
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

import random
import datetime
import tqdm


class data:
    def __init__(self, slices, x, y):

        self.slices = slices
        self.x = x
        self.y = y


class Pizza:
    def __init__(self, mapping, items, row_size,column_size):

        self.mapping = mapping
        self.items = items
        self.row_size = row_size
        self.column_size =column_size

    def split_pizza_into_map(self, row_lenght, column_lenght):
        # coupe la pizza en plusieurs "grosse part", la taille des parts est donné par row_lenght et column_lenght

        splited_mapping = []
        i, j, c_x, c_y = 0, 0, 0, 0

        while(i < self.row_size and j < self.column_size):
            mapp = []

            # append box per box
            for x in range(i, min(i+column_lenght, self.row_size)):
                for y in range(j, min(j+row_lenght, self.column_size)):

                    mapp.append(self.mapping[x * self.column_size + y])
                    c_x, c_y = x , y

            splited_mapping.append(mapp)

            j += row_lenght

            if(c_y == self.column_size-1):

                j = 0
                i += column_lenght

        return splited_mapping


def valid_slice(slice, pizza, min_ing):
    # check if n T and n M > min_ing

    x0, x1, y0, y1 = slice
    tomato, mushroom = 0, 0


    for x in range(x0, x1+1):

        for y in range(y0, y1+1):

            item = pizza.items[y][x]

            if(item == "T"):
                tomato += 1

            if(item == "M"):
                mushroom += 1

    if(tomato >= min_ing and mushroom >= min_ing):
        return True

    return False


'''
Cette fonction s'occupe de retourner toutes les découpe possible de part pour un mapping
il y a donc la même cellule dans plusieurs combinaisons de part 
Les combinaisons de part se base sur le critère de taille maximum et la quantité minimal d'ingrédient
'''


def find_valid_slices(mapping, min_ing, max_cell, pizza):

    # ici on liste les combinaisons en prenant en compte que la taille maximale
    slices = []
    y0, x0, item = mapping[0]
    y1, x1, item = mapping[len(mapping)-1]
    # pour chaque cellules dans la pizza
    for i0 in range(x0, x1 + 1):
        for j0 in range(y0, y1 + 1):
            # teste les combinaisons et ajoute les combinaisons valides
            for i1 in range(i0, min(x1+1, i0 + max_cell)):
                for j1 in range(j0, min(y1+1, j0+int(max_cell/(i1-i0+1)))):
                    slices.append((i0, i1, j0, j1))

    # maintenant on filtre en prenant aussi en compte le nombre minimal d'ingrédient
    return list(filter(lambda s: valid_slice(s, pizza, min_ing), slices))


def save(pizza, slices, file):

    out = data(slices, pizza.column_size, pizza.row_size)

    with open(file, "wb") as f:
        pickle.dump(out, f)

    return out


def show_pizza_output(data:  data):

    import matplotlib.pyplot as plt
    import numpy as np

    out = np.zeros((data.y, data.x, 3))

    for slices in data.slices:

        (x0, x1, y0, y1) = slices
        slice_color = [max(0.02, random.random()-0.2), max(0.1,
                                                       random.random()-0.2), max(0.1, random.random()-0.2)]

        for x in range(x0, x1 + 1):

            for y in range(y0, y1 + 1):

                out[y][x] = slice_color

    plt.imshow(out)
    plt.show()


'''
Trouve toutes les parts comportant la cellule aux coordonnées (x,y)
'''


def find_intersect(x, y, slices):

    intersect_slices = []

    for (x0, x1, y0, y1) in slices:
        if(x0 <= x <= x1 and y0 <= y <= y1):
            intersect_slices.append((x0, x1, y0, y1))

    return intersect_slices


def get_value_at_index(values, index):

    new_value = []
    for i in range(len(values)):
        if(i in index):
            new_value.append(values[i])
    return new_value


'''
Retourne les coordonnées rectangulaire de la zone (x0,x1,y0,y1)
'''
def mapping_coordonate(mapping):

    y0, x0, item = mapping[0]
    y1, x1, item = mapping[len(mapping)-1]
    return (x0, x1, y0, y1)


'''
Résout la disposition des parts de manière optimal
'''
def solve_combination(slices_in, mapping):

    x0, x1, y0, y1 = mapping_coordonate(mapping)

    prob = pulp.LpProblem("Pizza_hashcode", pulp.LpMaximize)

    # 0 or 1 slice
    pslice = pulp.LpVariable.dicts(
        "slice", slices_in, lowBound=0, upBound=1, cat=pulp.LpInteger)

    # 0 or 1 cell
    cells = pulp.LpVariable.dicts(
        "cell", [(m[0], m[1]) for m in mapping], lowBound=0, upBound=1, cat=pulp.LpInteger)

    # maximizes cells number
    prob += pulp.lpSum(cells)

    for (y, x), cell in cells.items():

        slices_intersected = find_intersect(x, y, pslice.keys())

        # slice that use one or more cell in commum are limited by 1 per group
        prob += pulp.lpSum([v for (k, v) in pslice.items()
                            if k in slices_intersected]) <= 1

        # if we take on of the slice then the cell value is 1
        prob += pulp.lpSum([v for (k, v) in pslice.items()
                            if k in slices_intersected]) == cell

    prob.solve()

    slice_out, cell_out  = [], {}

    for k, v in pslice.items():

        if(pulp.value(v) == 1):
            slice_out.append(k)

    for k, v in cells.items():
        cell_out[k] = pulp.value(v)

    return slice_out, cell_out


'''
Transforme une liste de liste en liste
'''
def join_slices(slices):
    return reduce(lambda l1, l2: l1 + l2, slices)


'''
Exécute l'algorithme de résolution sur une map(grand part):  one step 
'''

def compute_single_map(args):

    mapping, min_ing, max_cell, pizza, step = args
    # Trouve toutes les combinaisons de part valide
    slices = find_valid_slices(mapping, min_ing, max_cell, pizza)
    # Sélectionne les part de manière à maximiser le nombre de cellules
    slice_out, cell_out = solve_combination(slices, mapping)
    # Affiche la fin de l'étape
    lock = multiprocessing.RLock()

    with lock:
        sys.stdout.write('#')

    return slice_out


if __name__ == '__main__':

    DEFAULT_IN = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\pizza_regina\\in\\small.in"
    DEFAULT_OUT = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\pizza_regina\\out\\small.in"

    parser = argparse.ArgumentParser(
        description='Compute hashcode pizza regina')
    parser.add_argument('-i', '--filein', help='Input file',
                        type=str, default=DEFAULT_IN)
    parser.add_argument('-o', '--fileout', help='Ouput file',
                        type=str, default=DEFAULT_OUT)
    parser.add_argument('-x', '--rect_size_x',
                        help='Rectangular size X (used to cutting the pizza in smaller slice)', type=int, default=10)
    parser.add_argument('-y', '--rect_size_y',
                        help='Rectangular size Y (used to cutting the pizza in smaller slice)', type=int, default=10)
    parser.add_argument('-v', '--verbose', default=-1,
                        help='verbose mode', type=int)
    args = parser.parse_args()

    print("Start at: " + str(datetime.datetime.now()))
    mapping = []
    items = []
    slice_list = []
    with open(args.filein) as f:
        rows_size,column_size, min_ing, max_cell = map(
            int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
        line = [list(re.sub("\n", "", f.readline()))for i in range(rows_size)]
        mapping = ([(i, j, line[i][j]) for i in range(rows_size)
                    for j in range(column_size)])
        items = ([[line[i][j] for j in range(column_size)]for i in range(rows_size)])

    pizza = Pizza(mapping, items, rows_size,column_size)
    print("Splitting pizza.....")
    mappings = pizza.split_pizza_into_map(args.rect_size_x, args.rect_size_y)
    
    print("Starting solving slice (can take a very long time, depends rect_size_x,rect_size_y and pizza size !)...")
    print("Must compute %d steps" % len(mappings))

    proc = multiprocessing.Pool(multiprocessing.cpu_count())
    slice_list = proc.map(compute_single_map, [(
       mapp, min_ing, max_cell, pizza, i) for mapp, i in zip(mappings, range(len(mappings)))])

    # for _ in tqdm.tqdm(proc.imap_unordered(compute_single_map, [(
    #    mapp, min_ing, max_cell, pizza, i) for mapp, i in zip(mappings, range(len(mappings)))]),total=len(mappings)):
    #     pass

    proc.close()
    proc.join()

    # slice_list = [compute_single_map((mapp, min_ing, max_cell, pizza, i))
    #               for mapp, i in zip(mappings, range(len(mappings)))]
    slice_out = join_slices(slice_list)
    print("Writing output file in pickle format")
    data = save(pizza, slice_out, args.fileout)
    print("finish at: " + str(datetime.datetime.now()))

    #show_pizza_output(data)
