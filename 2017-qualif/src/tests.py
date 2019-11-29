import numpy as np


import line_profiler
import atexit

profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)


def knapSack(W, wt, val, n):
    K = np.zeros((n + 1, W + 1), dtype=np.int32)

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


def test_knapstack():
    a = np.empty((10010,), dtype=np.int32)
    for i in range(0, 10000):
        a = np.concatenate([a[:10], a[11:]])
        a = np.delete(a, 10)

    a = []
    for i in range(0, 20000):
        a.append(i)
    for i in range(0, 10000):
        del a[10]



