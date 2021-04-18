import itertools
from math import sqrt
# https://gist.github.com/mlalevic/6222750
def length(x , y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def solve_tsp_dynamic(points):
    # calc all lengths
    all_distances = [[length(x, y) for y in points] for x in points]
    # initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0, idx+1])
         for idx, dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                # this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
                B[(S, j)] = min([(A[(S-{j}, k)][0] + all_distances[k][j],
                                  A[(S-{j}, k)][1] + [j]) for k in S if k != 0 and k != j])
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res


size = int(input())
reference_points = [tuple(map(int, input().split(" "))) for _ in range(size)]

print(round(solve_tsp_dynamic(reference_points)[0]))
