from sys import maxsize as infinity
from itertools import permutations
import Node


def tps(graph, origin, destination):  # LOOKING FOR 22
    print(graph)
    path = infinity
    for i in permutations(graph):
        cost = 0
        if i[0] != origin or i[-1] != destination:
            continue
        # implement linked-listesque methodology


