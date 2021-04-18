from collections import namedtuple
Result = namedtuple('Result',['length','shift_left','shift_right'])  

def comp(c):
    return {'A': 'T', 'T': 'A', 'C':'G', 'G': 'C'}[c]

def boucle(brin, reversed_brin):
    i=0
    while i < len(brin)/2 and i < len(reversed_brin)/2 and brin[i] == comp(reversed_brin[i]):
        i+=1
    return i

def find_longest(brin, reversed_brin, shift_left, shift_right):

    if len(brin) < max(shift_right, shift_left) or len(reversed_brin) < max(shift_right, shift_left) :
       return (0, shift_left, shift_right)

    b  = Result(boucle(brin, reversed_brin) , shift_left , shift_right)
    p1 = Result(*find_longest(brin[1:], reversed_brin[:-1], shift_left + 1, shift_right))
    p2 = Result(*find_longest(brin[:-1], reversed_brin[1:], shift_left, shift_right + 1))

    return sorted([p1 , p2 , b], reverse=True) [0]


def boucle3(brin):
    r = find_longest(brin, brin[::-1], 0, 0)
    print(r)
    print(brin +'->')
    if r.shift_left > 0:
        print(brin[:r.shift_left] +'|', end= "")
    print(brin[r.shift_left: r.shift_left + r.length], end="")
    print(' '*5 + brin[r.shift_left + r.length: len(brin) - r.shift_right - r.length])
    if r.shift_right > 0:
        print(brin[::-1][:r.shift_right] +'|', end= "")
    print(brin[::-1][r.shift_right: r.shift_right + r.length])
    print("-"*50)


boucle3('ATGTAATC')
boucle3('CGTATATGTAATC')
boucle3('CGTATATGTAATATC')
boucle3('CGTATACTGTACCCGATATC')
