
import sys
import os
import time
import re
import functools
import random



f = open("C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\prepa\\TD1\\samples-E1_Cartes\\2.in", 'r')


def get_input():
    #return input().strip()
    return f.readline().strip()



def rotate(cards, index):

    index = len(cards) - index - 1
    # invert card face
    for i, (x, y) in enumerate( cards[index:] ):

        j = index + i
        if(cards[j][1] == 'V'):
            cards[j] = (cards[j][0], 'R')

        else:
            cards[j] = (cards[j][0], 'V')

    # then invert number(with their card face)
    cards = cards[:index] + cards[index:][::-1]
    return cards









if __name__ == '__main__':

    ncard = int(get_input())

    cards_in = get_input().split(" ")

    cards_v = [int(x) for i, x in enumerate(cards_in) if i % 2 == 0]

    cards_V_T = []

    for i, c in enumerate(cards_v):
        cards_V_T.append((c, cards_in[i*2+1]))

    max_i = random.randint(1,6)
    cards_V_T_cut = cards_V_T[:max_i]

    for i in range(random.randint(1, 9)):
        cards_V_T_cut = rotate(cards_V_T_cut,random.randint(1,max_i))

    print(cards_V_T_cut)
    

    # print(pancake_sort(cards_v),end='')
