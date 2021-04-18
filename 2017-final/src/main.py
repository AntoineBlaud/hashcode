import os
import sys
import pulp
import numpy as np
import re
import argparse
import collections
import time
import random

parser = argparse.ArgumentParser(description='Hashcode 2017-----final')
parser.add_argument("-v",action='store', dest='verbose',help='enable verbose')
args = parser.parse_args()
 
CHARLESTON_IN= "/home/darkloner99/code/Hashcode/Hashcode/2017-final/final_round_2017.in/charleston_road.in"
OPERA_IN = "/home/darkloner99/code/Hashcode/Hashcode/2017-final/final_round_2017.in/opera.in"
HIGH_IN = "/home/darkloner99/code/Hashcode/Hashcode/2017-final/final_round_2017.in/lets_go_higher.in"
LONDON_IN = "/home/darkloner99/code/Hashcode/Hashcode/2017-final/final_round_2017.in/rue_de_londres.in"
TEST_IN = "/home/darkloner99/code/Hashcode/Hashcode/2017-final/final_round_2017.in/test.In"
CHARLESTON_ROUTER_OUT ="/home/darkloner99/code/Hashcode/Hashcode/2017-final/out/charleston_router.out"
CHARLESTON_TARGET_OUT ="/home/darkloner99/code/Hashcode/Hashcode/2017-final/out/charleston_target.out"
LONDON_OUT = "/home/darkloner99/code/Hashcode/Hashcode/2017-final/out/rue_de_londres.out"
HIGH_OUT="/home/darkloner99/code/Hashcode/Hashcode/2017-final/out/lets_go_higher.out"
OPERA_OUT = "/home/darkloner99/code/Hashcode/Hashcode/2017-final/out/opera.out"

f = open(OPERA_IN,"r")
M=100000
rowsN, columsN, radius = map(int,[int(x) for x in re.sub("\n","",f.readline()).split(" ")])
backboneP, routerP, budget =  map(int,[int(x) for x in re.sub("\n","",f.readline()).split(" ")])
backboneX, backboneY = map(int,[int(x) for x in re.sub("\n","",f.readline()).split(" ")])
# Reserver un budget pour les routeur et un budget pour les cables
# Trouver compromis entre budget, nombre de cellule qui capte pour avoir meilleur score possible
routerBudget = ((100-3*radius*backboneP)/100)*budget
mapping=[]
for i in range(rowsN):
    line = re.sub("\n","",f.readline());mapping.append([])
    for j in range(columsN):
        if(line[j]=="-"): temp = 0
        if(line[j]=="."): temp = 1
        if(line[j]=="#"): temp = 2
        mapping[i].append(temp)
f.close()

def reset_output_file(file):
    f = open(file,"w");f.close()

def write_output(fileRouter,mapping):
    def convert(i:int):
        '''
        Convertie de entier a string
        '''
        if(i==0): return "-"
        if(i==1): return "."
        if(i==2): return "#"
        if(i==3): return "r"

    def write_router_output(file,mapping):
        '''
        Ecrit la solution du placement des routeurs
        '''
        rowsN = len(mapping); columsN = len(mapping[0]);f = open(file,"w")
        for i in range(rowsN):
            for j in range(columsN):
                f.write(convert(mapping[i][j]))
            f.write("\n")
        f.close()
    write_router_output(fileRouter,mapping)


def process_router(mapping,router_budget,maxSeconds=None):

    global routerP
    global radius
    max_router = int(router_budget/float(routerP))
    rowsN = len(mapping)
    columsN = len(mapping[0])
    mapping_router=[]
    mapping_router = [(i,j) for i in range(rowsN) for j in range(columsN)]
    prob = pulp.LpProblem("2017-final", pulp.LpMaximize)
    targetcell = [(x,y) for x in range(rowsN) for y in range(columsN)]
    targetcell_receive=  [(x,y,z) for x in range(rowsN) for y in range(columsN) for z in range((2*radius+1)*(2*radius+1))]
    # 0 = ne capte pas,  1 = capte
    targetcell = pulp.LpVariable.dicts("TargetCell", targetcell,lowBound=0, upBound=1, cat=pulp.LpInteger)
    targetcell_receive = pulp.LpVariable.dicts("TargetCellReceive", targetcell_receive,lowBound=0, upBound=1, cat=pulp.LpInteger)
    # 0 = rien, 1 = router
    mapping_router = pulp.LpVariable.dicts("MappingRouter", mapping_router,lowBound=0, upBound=1, cat=pulp.LpInteger)
    # Variable de décision pour le IF
    omega = [(i,j) for i in range(0,rowsN) for j in range(columsN)]
    omega = pulp.LpVariable.dicts("Omega", omega,lowBound=0, upBound=1, cat=pulp.LpInteger)


    # Maximiser le score (cellule qui capte)
    prob+=pulp.lpSum([targetcell[(x,y)] for x in range(rowsN) for y in range(columsN)])
    #   CONTRAINTES
    # Limiter le budget
    prob+=pulp.lpSum([mapping_router[(x,y)] for x in range(rowsN) for y in range(columsN)]) <= max_router
    # Routeur ne peut pas être placer dans les murs
    prob+=pulp.lpSum([mapping_router[(x,y)] for x in range(rowsN) for y in range(columsN) if mapping[x][y]==2 ]) ==0
    # Toutes les cellules non intéressentes valent 0
    prob+=pulp.lpSum([targetcell[(x,y)] for x in range(rowsN) for y in range(columsN) if mapping[x][y]==0]) == 0
    prob+=pulp.lpSum([targetcell[(x,y)] for x in range(rowsN) for y in range(columsN) if mapping[x][y]==2]) == 0

    #Retourne 1 si un mur bloque le passage des ondes entre la targetcell et le répeteur
    def check_wall(ti,tj,ri,rj):
        for j in range(min(rj,tj),max(rj,tj)+1):
            if(mapping[ri][j]==2): return 1
            if(mapping[ti][j]==2): return 1
        for i in range(min(ti,ri),max(ti,ri)+1):
            if(mapping[i][rj]==2): return 1
            if(mapping[i][tj]==2): return 1
        return 0    

    # target cell recoit ou non le signal
    # pour chaque mapping_router dans x-r,y-r
    # si (mapping_router==1 et pas de mur entre la cellule et le routeur alors entre alors la cellule = 1)
    # pour vérifier si il y a un mur entre, on parcourt la diagonale (n incrémente +1 puis +1 et si on arrive a max on incrémente le deuxieme qui n'a pas finit)
    for i in range(rowsN):
        for j in range(columsN):
            # Les cellules sur les cotées n'ont pas forcément autour de cellues autour que celles
            # au milieu
            # Ici on vérifie qu'il y a un répeteur pas loin et pas de murs entre
            z=0
            for xr in range(-radius,radius+1):
                for yr in range(-radius,radius+1):
                    if(i+xr<0 or i+xr>=rowsN or j+yr<0 or j+yr>=columsN): 
                        prob+=pulp.lpSum(targetcell_receive[(i,j,z)]) ==0
                        # On vérifier qu'il n'y a pas de murs
                    elif(check_wall(i,j,i+xr,j+yr)==0):
                        #-x+y >=0
                        # si mapping_router==1 alors targetcell_receive==1
                        # si mapping_router==0 alors targetcell_receive==0
                        prob+=pulp.lpSum([-mapping_router[(i+xr,j+yr)] +targetcell_receive[(i,j,z)]]) ==0
                    # Si il y a un mur alors la cellules ne recoit pas
                    else:prob+=pulp.lpSum(targetcell_receive[(i,j,z)]) ==0
                    z+=1
            # Si dans une seule sur les radius*radius possibilés on capte, alors on capte
            # <=> si la somme des receveurs >=1 then targetcell = 1 else targetcell = 0
            #https://math.stackexchange.com/questions/2500415/how-to-write-if-else-statement-in-linear-programming/2501007
            prob+=pulp.lpSum([targetcell_receive[(i,j,z)] for z in range((2*radius+1)*(2*radius+1))]) >=1 - M*(1-omega[(i,j)])
            prob+=pulp.lpSum([targetcell_receive[(i,j,z)] for z in range((2*radius+1)*(2*radius+1))]) <=1 + M*(omega[(i,j)])
            prob+=pulp.lpSum(1-M*(1-omega[(i,j)])) <= targetcell[(i,j)]
            prob+=pulp.lpSum(1+M*(1-omega[(i,j)])) >= targetcell[(i,j)]
            prob+=pulp.lpSum(0-M*(omega[(i,j)])) <= targetcell[(i,j)]
            prob+=pulp.lpSum(0+M*(omega[(i,j)])) >= targetcell[(i,j)]

    prob.solve(pulp.PULP_CBC_CMD(maxSeconds=maxSeconds))
    # Compute Score 
    score = 0
    for i in range(rowsN):
        for j in range(columsN):
            if(int(pulp.value(mapping_router[(i,j)]))==1): mapping[i][j] = 3
            if(int(pulp.value(targetcell[(i,j)]))==1): score+=1
    return (mapping,score)


def compute(mapping):
    global routerP;global radius;global routerBudget

    sectionX = 2*radius;sectionY = 4*radius
    crossingX = int(rowsN/sectionX);crossingY = int(columsN/sectionY)
    customerN=0
    for x in range(0,len(mapping)): customerN += mapping[x].count(1)
    x=0;y=0;SCORE = 0
    mapping = np.asarray(mapping)
    TOTAL=0

    print("\n---- Starting router resolution ----\n")
    startingTime = time.time()
    while (x<crossingX):
        while(y<crossingY):
            mapp =  mapping[x*sectionX:min((x+1)*sectionX,rowsN),y*sectionY:min((y+1)*sectionY,columsN)]
            # compute budget for the step
            customerX = 0;score = 0
            # convertir pour numpy
            for c in range(0,len(mapp)): customerX +=  mapp[c].tolist().count(1)
            #coeff =  (((customerX/customerN)*(budget*((100-3*backboneP*radius)/100))))
            coeff=1.1
            stepBudget= (customerX*coeff//(2*radius*2*radius))*routerP
            if(stepBudget>=routerP and (TOTAL+stepBudget)<routerBudget):
                TOTAL+=stepBudget
                (mapp,score) = process_router(mapp,stepBudget,5)
                mapping[x*sectionX:min((x+1)*sectionX,rowsN),y*sectionY:min((y+1)*sectionY,columsN)] = mapp
            SCORE+=score;y+=1
            sys.stdout.write(" %s/%s\r"%(y*sectionY,columsN));sys.stdout.flush()


        x+=1;y=0;print("\nstep %d terminated,  estimated score: %d, cost: %d, elapsed_time %d" % (x, SCORE, TOTAL,time.time()-startingTime))
        # Write output
        write_output(OPERA_OUT,mapping[:x*sectionX])

def stats(mapping):

    global routerP; global radius
    customerN=0
    for x in range(0,len(mapping)): customerN += mapping[x].count(1)
    routerN = customerN/(2*radius)**2
    pRouter = routerN*routerP
    print("routerN: %d  router total P: %d"%(routerN,pRouter))
    

compute(mapping)
#stats(mapping)


print("end")

# Adapter router_buget/crossing
# Calculer meilleur rapport entre budget et nombre de répeteur
