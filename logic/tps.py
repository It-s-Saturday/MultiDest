from sys import maxsize as infinity
from itertools import permutations
import Node


def tps(graph, origin, destination):  # LOOKING FOR 22
    evaluate = []
    for permutation in permutations(graph):
        if permutation[0] != origin or permutation[-1] != destination:
            continue
        # implement linked-listesque methodology
        evaluate.append(permutation)
    print(evaluate)
    cost = infinity
    for path in evaluate:
        i = 0
        c = 0
        while path[i] != path[-1]:
            c += graph[path[i]][path[i+1]]
            i += 1
        cost = min(cost, c)
        print("\n")
    print(cost)

