import sys
import os
import time
import argparse
import re
from copy import copy



def compute_upperbound(score,cabAvailableT,vx,vy,ridesArr:list,candidate):
    upperBound = score
    for rides in ridesArr:
        xe,ye,xs,ys,st,end,ID = map(int,rides)
        if(ID not in candidate):
            P = abs(xs-xe) + abs(ys-ye)
            Pbefore = max(cabAvailableT + abs(xe-vx) + abs(ye-vy),st)
            # Si le vehicule peut respecter la deadline
            if(Pbefore+P<=end ): 
                upperBound+=P*distanceFee+constantFee
                # Si il peut respecter le bonus
                if(Pbefore==st): upperBound+=bonusV
    return upperBound



def compute_rides(vx,vy,cabAvailableT,rides):
    score = 0
    xe,ye,xs,ys,st,end,ID = map(int,rides)
    P = abs(xs-xe) + abs(ys-ye)
    Pbefore = max(cabAvailableT + abs(xe-vx) + abs(ye-vy),st)
    # Si le vehicule peut respecter la deadline
    newCabAvailableT = Pbefore+P 
    if(newCabAvailableT<=end): 
        score =P*distanceFee+constantFee
        # Si il peut respecter le bonus
        if(Pbefore<=st): score+=bonusV
    return score



def a(vx,vy,cabAvailableT,rides):
    score = 0
    xe,ye,xs,ys,st,end,ID = map(int,rides)
    P = abs(xs-xe) + abs(ys-ye)
    Pbefore = max(cabAvailableT + abs(xe-vx) + abs(ye-vy),st)
    # Si le vehicule peut respecter la deadline
    newCabAvailableT = Pbefore+P
    if(cabAvailableT<=end): 
        score = P*distanceFee+constantFee
        # Si il peut respecter le bonus
        if(Pbefore==st): score+=bonusV
    return score,newCabAvailableT,xs,ys

def solve_cab(ridesArr):

    queue = []
    bestScore = 0
    bestCandidate = []
    shapeX = len(ridesArr)
    upperboundArr = []

    if(shapeX>1):
        for rides in ridesArr:
            score = compute_rides(0,0,0,rides)
            if(score>0):
                xe,ye,xs,ys,st,end,ID = map(int,rides)
                score,cabAvailableT,xs,ys = a(0,0,0,rides) 
                r = [score,cabAvailableT,xs,ys]
                candidate = [];candidate.append(r);candidate.append([ID])
                queue.append(candidate)
                u = compute_upperbound(score,cabAvailableT,xs,ys,ridesArr,candidate[1]);upperboundArr.append(u)
                if(args.verbose==1): print(candidate)
    else:
        score = compute_rides(0,0,0,ridesArr[0])
        if(score>0):
            xe,ye,xs,ys,st,end,ID = map(int,ridesArr[0])
            score,cabAvailableT,xs,ys = a(0,0,0,ridesArr[0])  
            r = [score,cabAvailableT,xs,ys]
            candidate = [];candidate.append(r);candidate.append([ID])
            if(args.verbose==1): print(candidate)
            return score,candidate


    while(len(queue)>0):
        nextE = upperboundArr.index(max(upperboundArr))
        candidate = queue.pop(nextE)
        scorep,cabAvailableT,vx,vy = map(int,candidate[0][0:4])
        courses = candidate[1]
        u = compute_upperbound(scorep,cabAvailableT,vx,vy,ridesArr,candidate[1])
        upperboundArr.remove(u)
        MAX = max(upperboundArr)
        if(len(queue)==0):
            return scorep,candidate

        for r in ridesArr:
            xe,ye,xs,ys,st,end,ID = map(int,r)
            if(ID not in courses):
                score = compute_rides(vx,vy,cabAvailableT,r)
                if(score>0):
                    score,cabAvailableT2,xs,ys =  a(vx,vy,cabAvailableT,r)
                    score+=scorep
                    newCandidate = []
                    newCandidate.append([score,cabAvailableT2,xs,ys])
                    newCandidate.append(courses + [ID])
                    u = compute_upperbound(score,cabAvailableT2,xs,ys,ridesArr,newCandidate[1])
                    if(score>bestScore):
                        bestScore = score
                        bestCandidate = newCandidate
                    if(u > bestScore):
                        queue.append(newCandidate)
                        upperboundArr.append(u)

                    if(score>=MAX):
                        return  score,newCandidate
    return (0,False)

                        
def writeOut(carArr,SCORE):
    f = open(OUTPUT_F,"w")
    print(str(SCORE), file=f)
    for car in carArr:
        for e in car:
            print(str(e),file=f,end=" ")
        print("",file=f)
                    


######################################################################################


######################################################################################


defaultFile = "/home/darkloner99/code/Hashcode/Hashcode/2018-qualif/in/input2.in"
OUTPUT_F = "/home/darkloner99/code/Hashcode/Hashcode/2018-qualif/out/results.txt"

parser = argparse.ArgumentParser(description='Compute hashcode 2018 ride')
parser.add_argument('-f','--file',help='Input file',default=defaultFile,type=str)
parser.add_argument('-v','--verbose',default=-1,help='verbose mode',type=int)
args = parser.parse_args()



with open(args.file,"r") as f:
    rowsN,columsN,vehiculesN,ridesN,bonusV,constantFee,distanceFee,steps =  [int(x) for x in f.readline().strip().split(" ")]
    size = int(ridesN/0.4*vehiculesN)
    ridesArr = []
    for i in range(ridesN):
        # xe,ye,xs,ys,st,end
        ridesArr.append([int(x) for x in f.readline().strip().split(" ")] + [i])
        
if(args.verbose==0): print(ridesArr)



#Ici faire une boucle pur chaque vehicule et supprimer les courses prises
SCORE = 0
carArr = []
ridesArr = ridesArr[0:30]

for car in range(vehiculesN):
    if(len(ridesArr)>0):
        score,candidate = solve_cab(ridesArr)
        if(candidate==False):
            pass
        else:
            carArr.append([car] + candidate[1])
            SCORE+=score
            ridesArr = [ride for ride in ridesArr if ride[6] not in candidate[1]]
    sys.stdout.write("%d %d/%d       \r"%(SCORE,ridesN-len(ridesArr),ridesN))
    sys.stdout.flush()
    writeOut(carArr,SCORE)

print(SCORE)










