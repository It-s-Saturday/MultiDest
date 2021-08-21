from sys import maxsize
from itertools import permutations




# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        # print("curr perm:", i)
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        print(k)
        for j in i:
            # print("j:", j)
            # print("Key:", k)
            # print("Graph[key]:", graph[k])

            current_pathweight += graph[k][j]
            # print("cost:", current_pathweight)
            k = j
            # print('\n')
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


# Driver Code
if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))