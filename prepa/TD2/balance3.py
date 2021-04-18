import math



#f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/Balance/3.in.saved", 'r')


def get_input():
    return input().strip()
    #return f.readline().strip()





def check_parent(queue,previous, num, pair):

    psum, ppair, parent, pindex, pairN = previous

    while(parent >= 0):
        if(ppair == pair):
            return False
        psum,ppair,parent,pindex, pairN = queue[parent]
    return True


def min_partition(S, pairs):


    sumS = sum(S)
    goal = int(sumS/2) 
  
    # somme, pair(si couple), parent , index de la donnée, pairN
    queue = [(0, None, -1, -1, 0)]

    for i,num in enumerate(S):

        size = len(queue)
        for j in range(size):

           
            psum, pair, parent, pindex, pairN =  previous = queue[j]
            newsum = num + psum

            if i in pairs:
                pair = pairs[i]
                if check_parent(queue,previous,i,pair) and (newsum <= goal):
                    queue.append((newsum, i, j, i+1, pairN+1))

            elif(newsum <= goal):
                queue.append((newsum, None, j, i+1, pairN))


    best = 0
    for  psum, pair, parent, pindex, pairN in queue:
        if(pairN==len(pairs)/2 and psum-best>0):
            best  = psum
        
    return abs(sumS-2*best)
        





if __name__ == '__main__':
 
    pairs_index = []
    # Input: a set of items
    n, m = map(int, get_input().split(" "))
    if(m > 0):
        pairs_index = list(map(int, get_input().split(" ")))
    else:
        get_input()
    S = list(map(int, get_input().split(" ")))

    pairs = {}
    i = 0
    while i < (len(pairs_index)):
        n1, n2  = pairs_index[i], pairs_index[i+1]
        pairs[n1], pairs[n2] = n2, n1
        i+=2

    print(min_partition(S,pairs))

    
 
