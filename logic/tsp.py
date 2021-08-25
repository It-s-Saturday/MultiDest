from sys import maxsize as infinity
from itertools import permutations
from contextlib import suppress


def tsp(graph, origin, destination):
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
            with suppress(KeyError):
                temp_c = graph[path[i]][path[i + 1]]
                # print(temp_c, "added")
                c += temp_c
            i += 1

        if cost == min(cost, c):
            continue
        else:
            cost = min(cost, c)
            out_path = path
            print("cost set to {} | path set to {}".format(cost, out_path))
    print(out_path)
    print(str(cost) + "mins")
