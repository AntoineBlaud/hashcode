from functools import reduce
import math


def seek(list):
    return list[len(list) - 1]

def merge_list(list):
    merge = []
    for p in list:
        if p not in merge:
            merge.append(p)
    return merge
    

def main():
    size = int(input())
    points = [tuple(map(int, input().split(" "))) for _ in range(size)]
    p_lr = []
    p_rl = []
    # on parcours du plus petit x vers le plus grand 
    points = sorted(points)
    for i in range(0 , size):
        while len(p_lr) > 0 and (seek(p_lr)[1] < points[i][1]) :
            p_lr.pop()
        p_lr.append(points[i])
    if len(p_lr) > 0 and (seek(p_lr)[1] < points[i][1]):
            p_lr.pop()

    # on parcours du plus grand x vers le plus petit
    points = sorted(points, reverse=True)
    for i in range(0 , size):
        while len(p_rl) > 0 and (seek(p_rl)[1] > points[i][1] ):
            p_rl.pop()
        p_rl.append(points[i])
    if len(p_lr) > 0 and (seek(p_lr)[1] < points[i][1]) :
            p_lr.pop()

    # on fusionne en supprimant les doublons
    wrap = merge_list(p_lr + p_rl)
    length = 0
    wrap.append(wrap[0])
    for i in range(len(wrap) - 1):
        p0, p1 = wrap[i], wrap[i + 1]
        length += math.sqrt(math.pow(p1[0] - p0[0], 2) + math.pow(p1[1] - p0[1], 2))
    print(round(length))


if __name__ == '__main__':
    main()
