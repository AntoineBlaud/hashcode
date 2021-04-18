

MAX_DEPTH = 1000

def fiboword(w1, w2, n):
    size_l = [None] * MAX_DEPTH 
    size_l[0] = len(w1)
    size_l[1] = len(w2)
    for i in range(2, MAX_DEPTH ):
        size_l[i] = int(size_l[i-1] + size_l[i-2]) 
    for size in reversed(size_l[3:]):
        if(size < n):
             n-=size

    inf_word = ""
    while(len(inf_word) - 1 < n):
        inf_word = w2 + w1
        w1 = w2
        w2 = inf_word
    return inf_word[n]

w1, w2, n = input().split(" ")
n = int(n)
print(fiboword(w1,w2,n))