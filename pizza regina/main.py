from guppy import hpy
import sys
import os
import time
import argparse
import re
from copy import copy
import pulp 


# Profilers
######################################################################################
h = hpy()
h.heap()
######################################################################################

M = 100000

default_in = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\pizza regina\\in\\example.in"
default_out= "out/exemple.out"





class Pizza:
    def __init__(self,mapping,items,i,j):
        self.mapping = mapping
        self.items = items
        self.rowsN = i
        self.columsN = j

    # coupe la pizza en plusieurs "grosse part", la taille des parts est donné par row_lenght et column_lenght
    def split_pizza_into_map(self,row_lenght,column_lenght):
        splited_mapping = []; i=0; j=0;cursorX=0;cursorY=0
        while(i<rows_N and j<colums_N):
            new_mapping = []
            for x in range(i,min(i+column_lenght,self.rowsN)):
                for y in range(j,min(j+row_lenght,self.columsN)):
                    new_mapping.append(self.mapping[x*self.columsN+y])
                    cursorX = x
                    cursorY = y
            j+=row_lenght;
            if(cursorY == self.columsN-1):
                j = 0
                i+= column_lenght
            splited_mapping.append(new_mapping)
        return splited_mapping




'''
Cette fonction s'occupe de retourner toutes les découpe possible de part pour un mapping
il y a donc la même cellule dans plusieurs combinaisons de part 
Les combinaisons de part se base sur le critère de taille maximum et la quantité minimal d'ingrédient
'''
def find_all_combination(mapping):

    #ici juste liste les combinaisons en prenant en compte que la taille maximal
    combinations_step1 = []
    combinations_step2 = []
    y0,x0,item = mapping[0]
    y1,x1,item = mapping[len(mapping)-1]
    # pour chaque cellules dans la pizza
    for i0 in range(x0,x1+1):
        for j0 in range(y0,y1+1):
            # teste les combinaisons et ajoute les combinaisons valides
            for i1 in range(i0,min(x1+1,i0+max_cell)):
                for j1 in range(j0,min(y1+1,j0+int(max_cell/(i1-i0+1)))):
                    combinations_step1.append((i0,i1,j0,j1))

    # maintenand on filtre en prenant aussi en compte le nombre minimal d'ingrédient
    for combination in combinations_step1:
        x0,x1,y0,y1 = combination
        tomato = 0
        mushroom = 0
        for x in range(x0,x1+1):
            for y in range(y0,y1+1):
                item = pizza.items[y][x]
                if(item=="T"): tomato+=1
                if(item=="M"): mushroom+=1
        if(tomato>=min_ing & mushroom>=min_ing):
            combinations_step2.append(combination)
    return combinations_step2

def find_intersect(x,y,combinations):
    intersect_combinations = []
    for c in combinations:
        x0,x1,y0,y1 = c
        if(x0<=x<=x1 and y0<=y<=y1): intersect_combinations.append(c)

    return intersect_combinations

def get_value_at_index(values,index):
    new_value = []
    for i in range(len(values)):
        if(i in index):
            new_value.append(values[i])
    return new_value

def get_mapping_property(mapping):
    y0,x0,item = mapping[0]
    y1,x1,item = mapping[len(mapping)-1]
    return (x0,x1,y0,y1)




def solve_combination(combinations_in,mapping):

    x0,x1,y0,y1 = get_mapping_property(mapping)
    prob = pulp.LpProblem("Pizza hashcode", pulp.LpMaximize)
    pslice = pulp.LpVariable.dicts("slice",combinations_in,lowBound=0,upBound=1,cat=pulp.LpInteger)
    cells = pulp.LpVariable.dicts("cell",[(m[0],m[1]) for m in mapping],lowBound=0,upBound=1,cat=pulp.LpInteger)

    prob+=pulp.lpSum(cells)
    for (y,x),cell in cells.items():
            intersect = find_intersect(x,y,pslice.keys())
            prob+=pulp.lpSum([v for (k,v) in pslice.items() if k in intersect])<=1
            prob+=pulp.lpSum([v for (k,v) in pslice.items() if k in intersect])==cell
            print("ok")
    prob.solve()
    for k,v in pslice.items():
        print(str(k)+"==>"+str(pulp.value(v)))
    for k,v in cells.items():
        print(str(k)+"==>"+str(pulp.value(v)))
    






parser = argparse.ArgumentParser(description='Compute hashcode pizza regina')
parser.add_argument('-i', '--filein', help='Input file', default=default_in, type=str)
parser.add_argument('-o', '--fileout', help='Ouput file', default=default_out, type=str)
parser.add_argument('-v', '--verbose', default=-1,
                    help='verbose mode', type=int)
args = parser.parse_args()

mapping = []
items = []
with open(args.filein) as f:
    rows_N,colums_N,min_ing,max_cell = map(int,[int(x) for x in re.sub("\n","",f.readline()).split(" ")])
    line = [list(re.sub("\n","",f.readline()))for i in range(rows_N)]
    mapping = ([(i,j,line[i][j]) for i in range(rows_N) for j in range(colums_N)])
    items = ([[line[i][j] for j in range(colums_N) ]for i in range(rows_N)])

pizza = Pizza(mapping,items,rows_N,colums_N)
#test
mappings = pizza.split_pizza_into_map(2,3)

combinations = find_all_combination(pizza.mapping)
a = find_intersect(0,0,combinations)
solve_combination(combinations,pizza.mapping)



#fonction qui pour chaque carré retourne toute les part possible afin de mettre leur somme à 1