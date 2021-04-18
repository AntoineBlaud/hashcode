import collections
import operator
import math

BT = collections.namedtuple("BT", ["value", "left", "right"])
NNRecord = collections.namedtuple("NNRecord", ["point", "distance"])


# source: wikipedia + https://johnlekberg.com/blog/2020-04-17-kd-tree.html
def SED(X, Y):
    return sum((i-j)**2 for i, j in zip(X, Y))

def kdtree(points):
    k = len(points[0])
    
    def build(*, points, depth):
        if len(points) == 0:
            return None
        
        points.sort(key=operator.itemgetter(depth % k))
        middle = len(points) // 2
        
        return BT(
            value = points[middle],
            left = build(
                points=points[:middle],
                depth=depth+1,
            ),
            right = build(
                points=points[middle+1:],
                depth=depth+1,
            ),
        )
    
    return build(points=list(points), depth=0)


def find_nearest_neighbor(tree, point):
 
    k = len(point)
    
    best = NNRecord(point=tree.value, distance=math.inf)
    def search(tree, depth):
        nonlocal best
        
        if tree is None:
            return
        
        distance = SED(tree.value, point)
        if distance > 0.0001 and distance < best.distance :
            best = NNRecord(point=tree.value, distance=distance)
        
        axis = depth % k
        diff = point[axis] - tree.value[axis]
        if diff <= 0:
            close, away = tree.left, tree.right
        else:
            close, away = tree.right, tree.left
        search(tree=close, depth=depth+1)
        if diff**2 < best.distance:
            search(tree=away, depth=depth+1)
    
    search(tree=tree, depth=0)
    return best.point

def locate_min(a):
    smallest = min(a)
    return smallest, [index for index, element in enumerate(a) 
                      if smallest == element]


def nearest_neighbor_kdtree( query_points, reference_points):
    """Use a k-d tree to solve the "Nearest Neighbor Problem"."""
    tree = kdtree(reference_points)
    #query_points.sort( key=lambda tup: (tup[0],tup[1]))
    done = set()
    closest = []
    while(len(query_points) > 0):
        query_p = query_points.pop()
        if(query_p not in done):
            r = find_nearest_neighbor(tree=tree, point=query_p)
            done.add(r)
            done.add(query_p)
            closest.append((query_p, r))

    distances =  list(map(lambda x: SED(x[0], x[1]), closest))
    minimums = locate_min(distances)

    closest_index = [ (reference_points.index(x0),reference_points.index(x1)) for (x0, x1) in closest]
    closest_index = [(min(x0, x1), max(x0,x1)) for (x0, x1) in closest_index ]

    closest_index = [closest_index[m] for m in minimums[1]]
    closest_index.sort(key=lambda tup: (tup[0],tup[1]))
    x1, x2 = closest_index [0][0], closest_index [0][1]
    return minimums[0], x1, x2
    

size = int(input())
reference_points = [tuple(map(int, input().split(" "))) for _ in range(size)]
query_points = reference_points[:]
print(*nearest_neighbor_kdtree(query_points,reference_points))

