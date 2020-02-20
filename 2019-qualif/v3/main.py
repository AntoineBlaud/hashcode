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


if __name__ == '__main__':

    DEFAULT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2019-qualif\\qualification_round_2019.in\\b_lovely_landscapes.txt"
    OUTPUT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2019-qualif\\out\\b_lovely_landscapes.txt"

    parser = argparse.ArgumentParser(
        description='Compute hashcode pizza regina')
    parser.add_argument('-i', '--filein', help='Input file',
                        default=DEFAULT_F, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',
                        default=OUTPUT_F, type=str)
    parser.add_argument('-v', '--verbose', default=-1,
                        help='verbose mode', type=int)
    args = parser.parse_args()

    photos = []
    with open(args.filein) as f:
        videosN = int(re.sub("\n", "", f.readline()).split(" ")[0])
        for i in range(videosN):
            photos.append(list([i] + [str(x) for x in re.sub("\n", "", f.readline()).split(" ")]))


def calculate_common_tags(p1, p2):
    score = 0
    for tag in p1:
        if(tag in p2): score += 1
    return score


# H1
def get_tags_in_H_slide(photos,index):
    return photos[index][3]

# (V1,V2)
def get_tags_in_V_slide(photos,indexs):
    return photos[indexs[0]][3].union(photos[indexs[1]][3])

def get_tags(photos,index):
    if(type(index) is int): #--> H slide
        return get_tags_in_H_slide(photos,index)

    return get_tags_in_V_slide(photos,index)

def calculate_score(tags1:set,tags2:set):
    p = tags1.intersection(tags2)
    score1 = len(p)
    score2 = len(tags1) - len(p)
    score3 = len(tags2) -len(p)
    return min(score1,score2,score3)



# sort photo by type
photosH = [];photosV = [];
for photo in photos:
    if photo[1] == 'H':
        photosH.append(photo[0])
    else:
        photosV.append(photo)

# on groupe par 2 les photos verticales qui ont le moins de tags en commun
photosVBy2 = []
pbar = tqdm.tqdm(total = len(photosV))
while(len(photosV) > 0):
    photo1 = photosV[0]
    bestChoice = 1
    bestScore = calculate_common_tags(photo1[3:],photosV[bestChoice][3:])
    for i in range(1,min(4000,len(photosV))):
        photo2 = photosV[i]
        common = calculate_common_tags(photo1[3:],photo2[3:])
        if(common<bestScore):
            bestScore = common
            bestChoice = i
    
    photosVBy2.append(((photo1[0],photosV[bestChoice][0])))
    del photosV[0]
    del photosV[bestChoice-1]
    pbar.update(2)

photosIndexs = photosH + photosVBy2
for photo in photos:
    photo[3] = set(photo[3:])
    del photo[4:]

def solve(photosIndexs):
    slide = []
    pbar = tqdm.tqdm(total = len(photosIndexs))
    FinalScore = 0
    random.shuffle(photosIndexs)
    while(len(photosIndexs)>1):
        photo1 = photosIndexs[0]
        photo1Tags = get_tags(photos,photo1)
        points = 0
        best = 1
        # entrée pair donc pas besoin de vérifier la taille
        for i in range(1,min(20000,len(photosIndexs))):
            photo2 = photosIndexs[i]
            photo2Tags = get_tags(photos,photo2)
            s = calculate_score(photo1Tags,photo2Tags)
            if(s > points):
                points = s
                best = i


    
        slide.append(photo1)
        slide.append(photosIndexs[best])
        del photosIndexs[0]
        del photosIndexs[best-1]
        pbar.update(2)
        FinalScore+=points
        pbar.set_postfix(score=FinalScore)

    if(len(photosIndexs)>0):
        slide.append(photosIndexs[0])
        pbar.update(1)
    

    with open(args.fileout,"w") as f:
        f.write(str(len(slide))+"\n")
        for e in slide:
            if(type(e)==tuple):
                f.write(str(e[0])+" "+str(e[1])+"\n")
            else:
                f.write(str(e)+"\n")


solve(photosIndexs)
    






        
            
