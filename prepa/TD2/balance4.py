import pulp


def get_input():
    return input()


def solve(S,pairs,n):

    prob = pulp.LpProblem("Balance", pulp.LpMinimize)
    sumset1 = pulp.LpVariable.dicts("S1",S,lowBound=0, upBound=1, cat=pulp.LpInteger)
    sumset2 = pulp.LpVariable.dicts("S2",S,lowBound=0, upBound=1, cat=pulp.LpInteger)


    prob +=pulp.lpSum([(S[i]*(sumset1[S[i]]-sumset2[S[i]]) for i in range(n))])
    prob +=pulp.lpSum([(S[i]*(sumset1[S[i]]-sumset2[S[i]]) for i in range(n))]) >=0

    for i in range(n):
        prob +=pulp.lpSum([sumset2[S[i]] + sumset1[S[i]] ]) == 1 

    for e in pairs:
        prob+=pulp.lpSum([sumset1[S[e]] + sumset1[S[pairs[e]]]]) == 1
        prob+=pulp.lpSum([sumset2[S[e]] + sumset2[S[pairs[e]]]]) == 1

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    res = 0
    for i in range(n):
        res+=(pulp.value(sumset1[S[i]]) - pulp.value(sumset2[S[i]])) * S[i]
    

    print(int(abs(res)));



if __name__ == '__main__':
 

    pairs_index = []
    # Input: a set of items
    n, m = map(int, get_input().split(" "))
    if(m > 0):
        pairs_index = list(map(int, get_input().split(" ")))
    else:
        get_input()

    S,pairs = list(map(int, get_input().split(" "))),{}
    i = 0
    while i < (len(pairs_index)):
        n1, n2  = pairs_index[i], pairs_index[i+1]
        pairs[n1] = n2
        i+=2

    solve(S,pairs,n)

    