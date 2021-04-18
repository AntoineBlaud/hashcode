import time

f = open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/Balance/3.in.saved", 'r')


def get_input():
    #return input().strip()
    return f.readline().strip()



def minPartition(S, n, pairs, S1=0, S2=0, lookup={}, distribution = {}):
 
    
    # end, we print the difference
    if n < 0:
        return abs(S1 - S2)
 
    # saved the current compute
    key = (n, S1)

    if key not in lookup:

        if n not in pairs:

            inc = minPartition(S, n - 1, pairs, S1 + S[n], S2, lookup, distribution)
            exc = minPartition(S, n - 1, pairs, S1, S2 + S[n], lookup, distribution)
        
        else:

            # get the second numbers
            pair = pairs[n]

            # if the second number(the pair) was already set before  we must put n in the second list
            if pair in distribution:

                if(distribution[pair] == False): # it have been put in L2
                    exc = inc = minPartition(S, n - 1, pairs, S1 + S[n], S2, lookup, distribution)
                else: 
                    inc = exc = minPartition(S, n - 1, pairs, S1, S2 + S[n], lookup, distribution)

            # on a pas encore ajouté la pair, on fait donc le meilleur choix
            else:

                distribution[n] = True # L1
                inc = minPartition(S, n - 1, pairs, S1 + S[n], S2, lookup, distribution)
                distribution[n] = False # L2
                exc = minPartition(S, n - 1, pairs, S1, S2 + S[n], lookup, distribution)

                distribution[n] = (inc == min(inc, exc))

        lookup[key] = min(inc, exc)
    return lookup[key]
 
 
if __name__ == '__main__':
 
    start = time.time()
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

    
 
    print(minPartition(S, len(S) - 1, pairs))
    print(time.time()-start)