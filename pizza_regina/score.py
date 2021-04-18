
import sys
import os
import time
import argparse
import re
import pickle

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate score')
    parser.add_argument('-i', '--filein', help='Input file', type=str)
    parser.add_argument('-s', '--solution', help='Solution file', type=str)
    args = parser.parse_args()

    mapping = []
    items = []
    with open(args.filein) as f:
        rows_N, colums_N, min_ing, max_cell = map(int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
        line = [list(re.sub("\n", "", f.readline()))for i in range(rows_N)]
        mapping = ([(i, j, line[i][j]) for i in range(rows_N) for j in range(colums_N)])
        items = ([[line[i][j] for j in range(colums_N)]for i in range(rows_N)])

    pizza = Pizza(mapping, items, rows_N, colums_N)
    with open(args.solution, "rb") as f:
        data = pickle.load(f);score=0;cells = {};
        print("Nombre de parts: %d"%len(data.slices))
        for s in data.slices:
            (x0, x1, y0, y1) = s
            area = 0; tomatoes = 0;mushrooms = 0;
            for x in range(x0, x1+1):
                for y in range(y0, y1+1):
                    if(pizza.items[y][x]=='T'):tomatoes+=1
                    if(pizza.items[y][x]=='M'):mushrooms+=1
                    # Vérification de l'unicité d'une cellule
                    if((y,x) in cells.keys()):
                         print('\033[93m'+"Error !! Cell in multiple slice"+'\033[0m')
                    cells[(y,x)] = ""
                    area+=1
            
            if(area<=max_cell and tomatoes>=min_ing and mushrooms >=min_ing):
                score+=area

        print('\033[94m'+"Score: "+str(score)+'\033[0m')

                    
        
    
