import sys
import os
import time
import argparse
import re
from copy import copy, deepcopy
from functools import reduce
import pickle
import multiprocessing
import random
import datetime
import math
import tqdm

# import matplotlib.pyplot as plt

if __name__ == '__main__':

    DEFAULT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2021-qualif\\in\\d.txt"
    OUTPUT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2021-qualif\\out\\d.txt"

    parser = argparse.ArgumentParser(description='Compute hashcode 2021')
    parser.add_argument('-i', '--filein', help='Input file',
                        default=DEFAULT_F, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',
                        default=OUTPUT_F, type=str)
    parser.add_argument('-v', '--verbose', default=-1,
                        help='verbose mode', type=int)
    args = parser.parse_args()

    with open(args.filein) as f:
        duration, intersectionsN, streetsN, carsN, bonusN = map(
            int, [int(x) for x in re.sub("\\n", "", f.readline()).split(" ")])
        streets = []
        intersections = {i: [] for i in range(intersectionsN)}
        cars = []
        for _ in range(streetsN):
            streets.append(tuple(f.readline().strip().split(" ")))
        for i in range(streetsN):
            (B, E, streetname, L) = streets[i]
            streets[i] = (int(B), int(E), str(streetname), int(L))
            intersections[int(E)].append(streetname)
        for _ in range(carsN):
            cars.append(f.readline().strip().split(" "))
        for i in range(carsN):
            cars[i][0] = int(cars[i][0])


def write_output(cycles, intersections):
    with open(args.fileout, "w") as f:
        f.write(str(len(cycles))+"\n")
        for i in cycles.keys():
            cycle = cycles[i]
            f.write(str(i) + "\n")
            f.write(str(len(cycle))+"\n")
            streetname = intersections[i]
            for name, value in zip(streetname, cycle):
                f.write(name + " " + str(value)+"\n")

streets_end = {street[2]: street[1] for street in streets}
streets_len = {street[2]: street[3] for street in streets}
traffic = {x[2]: 0 for x in streets}
cycles = {i: [] for i in range(intersectionsN)}

# compute traffic 
for car in cars:
    for x in car[1:]:
        traffic[x] += 1


def clean(cycles, intersections):
    new_cycles = {i: [] for i in cycles.keys()}
    for i in cycles.keys():
        minj = 0
        for j, x in enumerate(cycles[i]):
                if x > 0:
                    new_cycles[i].append(x)
                else:
                    intersections[i].remove(intersections[i][j-minj])        
                minj += 1

    cycles = new_cycles
    for i in cycles.keys():
        cycle, intersec = cycles[i], intersections[i]
        if len(cycle) == 0 :
            del cycles[i]
            del intersections[i]

    return cycles, intersections



def compute_score(cycles, intersections, cars, streets):

    global duration, intersectionsN, streetsN, carsN, bonusN

    end = {}
    intersection_crossed= {t:[] for t in range(duration * 2)}
    cars_location = {i: (0, car[1], 1) for i, car in enumerate(cars)}

    def get_waiting_time(time, cycle, intersection, street):
        current_time = 0
        current_street = intersection[0]
        i, j = 0, 0
        if(cycle[intersection.index(street)] == 0):
            return None
        while(current_time < time or current_street != street):
            current_time += 1
            i += 1
            if(i >= cycle[j]):
                j = (j + 1) % len(cycle)
                i = 0
                current_street = intersection[j % len(cycle)]
        return (current_time - time)

    for _ in range(duration):
        for i in cars_location.keys():
            car = cars_location[i]
            if i not in end and car[0] < duration:
                time, street, street_index = car[0], car[1],  car[2]
                intersection = streets_end[street]
                next_street = cars[i][street_index + 1]
                waiting_time = get_waiting_time(time, cycles[intersection], intersections[intersection], street)
                if waiting_time == None:
                     cars_location[i] =  1000000, street, street_index
                     continue
                time = time +  waiting_time
                if intersection in intersection_crossed[time]:
                    cars_location[i] = time + 1, street, street_index
                    continue

                else:
                    intersection_crossed[time].append(intersection)
                    cars_location[i] = car = time + streets_len[next_street], next_street, street_index + 1

                # check end
                if car[2] == len(cars[i]) - 1 and car[0] < duration:
                    end[i] = duration - car[0] + bonusN

    if(len(end) == 0):
        return 0
    return reduce(lambda a, b: a + b , end.values())
     

 

def solve():
    for i, intersec in enumerate(cycles.values()):
        incoming = intersections[i]
        scores = [traffic[name] for name in incoming]
        minj = 0
        for j, x in enumerate(scores):
            if x > 0:
                cycles[i].append(int(int(math.pow(x, 1/3))*1.29))
            else:
                intersections[i].remove(intersections[i][j-minj])
                minj += 1
    for i in range(intersectionsN):
        cycle, intersec = cycles[i], intersections[i]
        if len(cycle) == 0 :
            del cycles[i]
            del intersections[i]

    return cycles, intersections


def improve(cycles, intersections, cars, streets):
    
    current_score = compute_score(cycles, intersections, cars, streets)
    pbar = tqdm.tqdm(total = len(cycles))

    for i in cycles.keys():
        pbar.update(1)
        pbar.set_description("score %d" % current_score)
        for j in range(len(cycles[i])):
            if(len(cycles[i]) > 1):
                saved = intersections[i][:]
                for _ in range(min(len(cycles[i])*2, 10)):
                    random.shuffle(intersections[i])
                    new_score = compute_score(cycles, intersections, cars, streets)
                    if(new_score < current_score):
                        intersections[i] = saved
                    else:
                        current_score = new_score
                    pbar.set_description("score %d" % current_score)

    return cycles, intersections
        

cycles, intersections = solve()
cycles, intersections = improve(cycles, intersections, cars, streets)
cycles, intersections = clean(cycles,intersections)
write_output(cycles, intersections)
