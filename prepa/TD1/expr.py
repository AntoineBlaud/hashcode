import sys
import os
import time
import re
import functools
import random

from fractions import Fraction


#f = open("C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\prepa\\TD1\\samples-D1_Expression\\2.in",'r')

def get_input():
    return input().strip().split(" ")
    #return f.readline().strip().split(" ")


def is_op(op):

    if(op=='+' or op=='-' or op=='*' or op=='/' ):
        return True

    return False
        


def op(stack):

    buffer = []
    while(len(stack) >0):

        op = stack.pop()
        if(is_op(op)):
            try:
                opa = Fraction(buffer.pop())
                opb = Fraction(buffer.pop())
            except:
                return None

            if(op=='+'):
                op = opa+opb

            if(op=='-'):
                op = opb-opa

            if(op=='*'):
                op = opa*opb

            if(op=='/'):
                if(opa==0.0):
                    return None
                op = opb/opa      

            buffer.append(op) 
        
        else:
            buffer.append(op)


    if(len(buffer)>1):
        return None

    return buffer.pop()

if __name__ == '__main__':

    stack = []
    stack.append(get_input()[::-1])
    stack.append(get_input()[::-1])


    r_1 = op(stack[0])
    r_2 = op(stack[1])
    print(r_1==r_2)



