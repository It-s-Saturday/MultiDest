def dijkstra(nodes, distances) -> dict:
    unvisited = {node: None for node in nodes}
    print(unvisited)
    visited = {}
    current = nodes[0]  # starting point
    currentDistance = 0  # cumulative distance
    unvisited[current] = currentDistance
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance  # add onto cumulative distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance  # "score" of the neighbor in relation to current
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:  # check to see and end if unvisited has been exhausted
            break
        candidates = [node for node in unvisited.items() if node[1]]  # sets to remaining kv pairs in unvisited
        print(candidates)
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
    return visited
