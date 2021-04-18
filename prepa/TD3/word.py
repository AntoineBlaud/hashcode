import sys
import os
import time
import re
import functools
import random

#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD3/samples-B3_WordSearch/1.in", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()


def column(matrix, i):
    return [row[i] for row in matrix]

def row(matrix, i):
    return matrix[i]

def isPalindrome(s):
    return s == s[::-1]


if __name__ == '__main__':
    n,m = map(int,get_input().split(" "))
    word = list(get_input())
    word_len = len(word)
    words = [list(get_input())  for _ in range(n)]
    cpt = 0
    for i in range(n):
        for j in range(m - word_len + 1):
                right = row(words,i)[j:j + word_len]
                if word == right: cpt+=1


    for i in range(0, n - word_len + 1):
        for j in range(m):
                down = column(words,j)[i:i + word_len]
                if word == down: cpt+=1

   

    for i in range(n - 1, 0, -1):
        for j in range(m, m-word_len, -1):
                left = row(words,i)[j:j - word_len-1:-1]
                if word == left: cpt+=1


    for i in range(n, n - word_len, -1):
        for j in range(m-1, 0, -1):
                up = column(words,j)[i:i - word_len-1:-1]
                if word == up: cpt+=1

    print(cpt)





            




    