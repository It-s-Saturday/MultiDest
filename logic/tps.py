from sys import maxsize as infinity
from itertools import permutations
import Node


def tps(graph, origin, destination):
    vertex = []
    for key in graph.keys():
        if key != origin:
            vertex.append(key)
    # print(vertex)

    path = infinity
    next_permutation = permutations(vertex)
    for permutation in next_permutation:
        print("curr perm:", permutation)
        current_cost = 0
        key = origin
        print(key)
        for j in permutation:
            print(graph[key])
            try:
                current_cost += graph[key].get(origin)
            except:
                continue
            key = j
        try:
            current_cost += graph[key].get(origin)
        except:
            continue
        path = min(path, current_cost)
    print(path)

