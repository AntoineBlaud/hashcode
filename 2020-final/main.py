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
import math






# trouver les meilleurs socles en fonctione de la proximité(moyenne des scores)




# prendre une zone et faire une moyenne
# score fonction avec distance, score, temps à faire, proche du début, sortie proche de la moyenne (naturel puis IA)
# pour chaque étapes maintenir la liste des cases infranchissable (et les prendre en compte pour la distance en prenant en compte les étapes suivantes (car le circuit évolue))
# fonction calcul distance (avec étapes infranchissable)
# fonction zone importante
# fonction affichage 
# limiter la zone d'action
# pour bras 1 faire etape 1 puis passer au bras 2 , etc.... , couper les étapes en sout étapes avec une liste des infranchissable(deja dit plus haut)
# affichage graphique


    # x1 - x
    #y1 - y
    # tourne x en dernier
    #tourne x en premier
    # essaye entre
    #change de point




class Arm:
    
    def __init__(self, idm, x , y):

        self.id = idm
        self.x = x
        self.y = y
        self.steps = 0
        self.armx = x
        self.army = y



def score_density(tasks_data):

    mapp = [[0 for i in WIDTH] for j in LENGTH]

    for tasks in tasks_data:
        i,score,assembly,assembly_data = tasks

        for x,y in tasks:
            mapp[x][y]+=score
    
    return mapp


def mapping_average(mapping):

    avg, i = 0, 0

    for line in mapping:

        for v in line:
            avg += v;
            i += 1
    
    return avg



def select_mountpoint(tasks_data, mount_points_data):
    
    global PARAM_COEFF,PARAM_RATIO,mount_points

    selected_mountpoint = []
    mapping = score_density(tasks_data)
    average = mapping_average(mapping)
    ratio = int(WIDTH*LENGTH/(PARAM_RATIO*MOUNT_POINTS))

    # Pour le nombre de mountpoints disponible trouve le meilleur emplacement suivant les zones de densité de points
    for _ in range(MOUNT_POINTS):

        # trouve la boxe avec la plus grand valeur 
        x, y, maxm = 0, 0, 0

        for i,line in enumerate(mapping):

            for j,v in enumerate(line):
                if(v > maxm):
                    x, y = i,j
                    maxm = v

        # ajoute le mounpoint le plus proche
        selected_mountpoint.append(find_neareast_mountpoint(mount_points_data,selected_mountpoint,x,y))

        #reduit la valeur de la zone afin de placer les mountpoint aussi à d'autre endroid
        m = int(math.sqrt(ratio))
        m = m - m % 2
        for x1 in range(x-m/2,x+m/2):

            for y1 in range(y-m/2,y+m/2):
                mapping[x1][y1]-=average*PARAM_COEFF;
        
    return select_mountpoint
        
        





def eval_task(tasks, arm):
    pass



def apply_task(arm, task):
    pass


def compute_min_distance(pointA, pointB):
    pass

def find_best_startingpoint(arm,points):
    pass


def compute_best_path(start, points):
    pass



def path_distance(arm , task):

    points = task[2][:]
    start, d1 = find_best_startingpoint()
    points.remove(start)
    points, d2 = compute_best_path(start, points)

    return d1 + d2


    






def is_available_arms(arms):

    for arm in arms:
        if(is_available_arm(arm)):
            return True

    return False

def is_available_arm(arm):
    return arm.step < STEPS

def find_next_arm(arms,previous_index):

    for arm in arms[previous_index:]:
        if(is_available_arm(arm)):
            return arm,arms.index(arm)
    for arm in arms:
        if(is_available_arm):
            return arm,arms.index(arm)

    return None
    
def find_near_tasks(tasks_data, arm, step):
    selected = []

    for task in tasks_data:
        if(distance_score(arm,task,step) < 10*PARAM_NEAR):
            selected.append(task)

    return selected


def distance_score(arm, tasks, step):

    cpt = 0
    xtot,ytot = 0, 0

    for (x,y) in tasks[2] :
        xtot+=x
        ytot+=y
    
    xtot/=cpt
    ytot/=cpt
    return math.sqrt((arm.armx - xtot)**2 + (arm.army - ytot)**2)
    



   


def solve(tasks_data , arms):

    previous_index = 0

    while(is_available_arms(arms)):
        arm,previous_index = find_next_arm(arms,previous_index)
        near_tasks = find_near_tasks(tasks_data,arm,arm.step)


           # find best task
        score = 0
        selected_task = near_tasks[0]
        completed = False
        banlist = []

        while(not completed):

            for task in near_tasks:
                v = eval_task(task, arm)
                if(v > score):
                    selected_task, score = task, v
            try:
                apply_task(arm,selected_task)
                tasks_data.remove(selected_task)
                completed = True
            except e:
                banlist.append(selected_task)
                if(len(near_tasks) ==0):
                    raise Exception("banlist full")
            


if __name__ == '__main__':

    FILE = "a_example"
    DEFAULT_F = "2020-final/in/" + FILE + ".txt"
    OUTPUT_F = "2020-final/out/" + FILE + ".txt"
    parser = argparse.ArgumentParser(description='Hashcode 2020 qualif')
    parser.add_argument('-i', '--filein', help='Input file',default=DEFAULT_F, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',default=OUTPUT_F, type=str)
    parser.add_argument('-v', '--verbose', default=-1,help='verbose mode', type=int)
    args = parser.parse_args() 


mount_points_data = []
tasks_data = []
steps_impassable_square = [] #ajouter les mount_point


PARAM_RATIO = 2
PARAM_COEFF = 1
PARAM_NEAR = 5


with open(args.filein) as f:
    WIDTH, LENGTH, arms, MOUNT_POINTS, tasks, STEPS = map(int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])

    for i in range(MOUNT_POINTS):
        x,y = map(int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
        mount_points_data.append((i,x,y))

    for i in range(tasks):
        score, assembly = map(int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
        assembly_data_temp = [int(x) for x in re.sub("\n", "", f.readline()).split(" ")]
        assembly_data = []
        j = 0

        for _ in range(int(len(assembly_data_temp)/2)):
            assembly_data.append((assembly_data_temp[j],assembly_data_temp[j+1]))
            j+=2

        tasks_data.append((i,score,assembly,assembly_data))


selected_mountpoint = select_mountpoint(tasks_data,mount_points_data)


arms = []

for selected in selected_mountpoint:
    idm, x , y = selected
    arms.append( Arm(idm, x , y) )


solve(tasks_data,arms)
            



