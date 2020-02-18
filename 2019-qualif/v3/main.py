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
import numpy as np
import random
import matplotlib.pyplot as plt
import datetime
import tqdm


if __name__ == '__main__':

    DEFAULT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2019-qualif\\qualification_round_2019.in\\a_example.txt"
    OUTPUT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2019-qualif\\out\\a_example.txt"

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

def get_tags_in_common(p1,p2):
    tags = []
    for tag in p1[2:]:
        if(tag in p2[2:]): tags.append(tag)


def calcule_tags_in_1_but_not_in_2(p1, p2):
    score = 0
    for tag in p1:
        if(tag not in p2): score += 1
    return score


def calcule_tags_in_2_but_not_in_1(p1, p2):
    score = 0
    for tag in p2:
        if(tag not in p1):score+=1
    return score

# H1
def get_tags_in_H_slide(photos,index):
    return photos[index][2:]

# (V1,V2)
def get_tags_in_V_slide(photos,indexs):
    return get_tags_in_common(photos[indexs[0]],photos[indexs[1]])

def get_tags(photos,index):
    if(type(index) is int): #--> H slide
        return get_tags_in_H_slide(photos,index)

    return get_tags_in_V_slide(photos,index)

def calculate_score(tags1,tags2):
    score1 = calcule_tags_in_1_but_not_in_2(tags1,tags2)
    score2 = calcule_tags_in_2_but_not_in_1(tags1,tags2)
    score3 = calculate_common_tags(tags1,tags2)



# sort photo by type
photosH = [];photosV = [];
for photo in photos:
    if photo[1] == 'H':
        photosH.append(photo[0])
    else:
        photosV.append(photo)

# on groupe par 2 les photos verticales qui ont le moins de tags en commun
photosVBy2 = []
while(len(photosV) > 0):
    photo1 = photosV[0]
    bestChoice = 1
    bestScore = calculate_common_tags(photo1[2:],photosV[bestChoice][2:])
    for i,photo2 in enumerate(photosV[1:]):
        common = calculate_common_tags(photo1[2:],photo2[2:])
        if(common<bestScore):
            bestScore = common
            bestChoice = i
    
    photosVBy2.append(((photo1[0],photosV[bestChoice][0])))
    del photosV[0]
    del photosV[bestChoice-1]

photosIndexs = photosH + photosVBy2

pbar = tqdm.tqdm(total = len(photosIndexs))
while(len(photosIndexs)>0):
    photo1 = photosIndexs[0]
    photo1Tags = get_tags(photos,photo1)
    points = 0
    # entrée pair donc pas besoin de vérifier la taille
    for photo2 in photosIndexs[1:]:
        photo2Tags = get_tags(photos,photo2)




        
            
