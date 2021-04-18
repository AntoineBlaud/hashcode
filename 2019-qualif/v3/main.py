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

# better score  here : https://github.com/inaitana/hashcode-2019-qualification

if __name__ == '__main__':


    DEFAULT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2019-qualif\\qualification_round_2019.in\\b_lovely_landscapes.txt"
    OUTPUT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2019-qualif\\out\\b_lovely_landscapes.txt"

    parser = argparse.ArgumentParser(description='Compute hashcode :)')


    parser.add_argument('-i', '--filein', help='Input file',
                        default=DEFAULT_F, type=str)

    parser.add_argument('-o', '--fileout', help='Ouput file',
                        default=OUTPUT_F, type=str)

    parser.add_argument('-v', '--verbose', default=-1,
                        help='verbose mode', type=int)

    args = parser.parse_args()




def calculate_common_tags(p1, p2):

    score = 0
    for tag in p1:
        if(tag in p2):score += 1
    return score

# H1
def get_tags_in_simple_slide(photos, index):

    return photos[index][3]

# (V1,V2)


def get_tags_in_double_slide(photos, indexs):

    return photos[indexs[0]][3].union(photos[indexs[1]][3])


def get_tags_index(photos, index):

    if(type(index) is int):  # --> H slide
        return get_tags_in_simple_slide(photos, index)

    return get_tags_in_double_slide(photos, index)


def calculate_score(tags1: set, tags2: set):

    p = tags1.intersection(tags2)
    score1 = len(p)
    score2 = len(tags1) - len(p)
    score3 = len(tags2) - len(p)
    return min(score1, score2, score3)


def get_tags(photo):

    return photo[3:]


def get_id(photo):

    return photo[0]


def solve(photos_id,photos):

    slide = []
    pbar = tqdm.tqdm(total=len(photos_id))
    score = 0
    
    while(len(photos_id) > 1):
        photo_compared_id = photos_id.pop()
        photo_compared_tags = get_tags_index(photos, photo_compared_id)
        best_score = 0
        best_id = next(iter(photos_id))

        # entrée pair donc pas besoin de vérifier la taille
        for x in photos_id:
            photo_compared_id_2 = x
            photo_compared_tags_2 = get_tags_index(photos, photo_compared_id_2)
            s = calculate_score(photo_compared_tags, photo_compared_tags_2)
            if(s > best_score ):
                best_score  = s
                best_id = photo_compared_id_2

        slide.append(photo_compared_id)
        slide.append(best_id)
        
        photos_id.discard(best_id)
        pbar.update(2)
        score += best_score
        pbar.set_postfix(score=score)

    # append last photo
    if(len(photos_id) > 0):
        slide.append(photos_id[0])
        pbar.update(1)

    return slide



def solve_v(photos_id,photos):

    group_v = []
    pbar = tqdm.tqdm(total=len(photos_id))
    
    while(len(photos_id) > 1):
        photo_compared_id = photos_id.pop()
        photo_compared_tags = get_tags_index(photos, photo_compared_id)
        best_score = 1000
        best_id = next(iter(photos_id))

        # entrée pair donc pas besoin de vérifier la taille
        for x in photos_id:
            photo_compared_id_2 = x
            photo_compared_tags_2 = get_tags_index(photos, photo_compared_id_2)
            s = calculate_common_tags(photo_compared_tags, photo_compared_tags_2)
            if(s < best_score ):
                best_score  = s
                best_id = photo_compared_id_2
            if(best_score==0):
                break

        group_v.append((photo_compared_id,best_id))
        photos_id.discard(best_id)
        pbar.update(2)


    return group_v



if __name__ == "__main__":


    # read input data <-------------
    photos = []
    with open(args.filein) as f:
        videosN = int(re.sub("\n", "", f.readline()).split(" ")[0])
        for i in range(videosN):
            photos.append(
                list([i] + [str(x) for x in re.sub("\n", "", f.readline()).split(" ")]))


    # sort photo by type
    photos_H_id = []
    photos_V_id = []

    for p in photos:
        p_id = p[0]
        if p[1] == 'H':
            # append id
            photos_H_id.append(p_id)
        else: # (p[1]=='V')
            photos_V_id.append(p_id)



    # apply set on tags
    for p in photos:
        p[3] = set(get_tags(p))
        del p[4:]

    # on groupe par 2 les photos verticale ; regle: le moins de tags en commun
    photos_V_id = solve_v(set(photos_V_id),photos)
    # merge H and V
    photos_id = photos_H_id + photos_V_id

    
random.shuffle(photos_id)
# solve 
slide = solve(set(photos_id),photos)


# write output ----------------->
with open(args.fileout, "w") as f:
    f.write(str(len(slide))+"\n")
    for e in slide:
        if(type(e) == tuple):
            f.write(str(e[0])+" "+str(e[1])+"\n")
        else:
            f.write(str(e)+"\n")
