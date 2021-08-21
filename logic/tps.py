from sys import maxsize as infinity
from itertools import permutations

def tps(graph, origin, destination):
    out_path = []
    evaluate = []
    for permutation in permutations(graph):
        if permutation[0] != origin or permutation[-1] != destination:
            continue
        evaluate.append(permutation)
    # print(evaluate)
    cost = infinity
    for path in evaluate:
        i = 0
        c = 0
        while path[i] != path[-1]:
            c += graph[path[i]][path[i+1]]
            i += 1
        if cost == min(cost, c):
            continue
        else:
            cost = min(cost, c)
            out_path = path
    print(path)
    print(cost)

