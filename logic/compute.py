# grab list of inputs from an expandable form (max 5 to start)
# ignore empty inputs
# try and confirm lookup, maybe directly reference google api to confirm location
# above solution should not require any error handling

# each list element then is represented as a node that needs to check distance to each other node
# based on distance and time

# assume (for now) that going and back is equal (which it sometimes isn't)

import Node
import djikstra


def createOrigin(name: str) -> Node:
    origin = Node.Node(name)
    origin.setIndex(0)
    origin.setAsOrigin()
    return origin


def createDestination(name: str, num_stops: int) -> Node:
    destination = Node.Node(name)
    destination.setIndex(num_stops + 1)
    destination.setAsDestination()
    return destination


def lookup_time(start: Node, end: Node) -> int:  # fill with actual lookup
    if start.getName() == "Home" and end.getName() == "school":
        return 7
    elif start.getName() == "Home" and end.getName() == "LJ":
        return 6

    elif start.getName() == "school" and end.getName() == "Home":  # duplicate
        return 7
    elif start.getName() == "school" and end.getName() == "LJ":  # duplicate
        return 9
    elif start.getName() == "school" and end.getName() == "CFA":
        return 9

    elif start.getName() == "LJ" and end.getName() == "Home":
        return 6
    elif start.getName() == "LJ" and end.getName() == "school":  # duplicate
        return 9
    elif start.getName() == "LJ" and end.getName() == "CFA":
        return 6

    elif start.getName() == "CFA" and end.getName() == "school":
        return 9
    elif start.getName() == "CFA" and end.getName() == "LJ":
        return 6



travel = {}
stops = ["school", "LJ"]

originNode = createOrigin("Home")

destinationNode = createDestination("CFA", len(stops))

travel[originNode] = originNode.getIndex()

list_of_stops = []
for stop in stops:
    temp = Node.Node(stop)
    travel[temp] = None
    list_of_stops.append(temp)

travel[destinationNode] = destinationNode.getIndex()

# for key in travel.keys():
#     print(key.__str__(), travel[key])


nodes = ()
for node in travel.keys():
    nodes = nodes + (node.getName(),)

distances = {}

# for each key in the dictionary, call lookup on key and all other keys in the dict and populate it
# outer dict maps single source to n targets
# inner dict gives distances TO n targets
for key in travel.keys():
    curr_key_dict = {}
    for other in travel.keys():
        if key != other:
            if key.getIsOrigin() and other.getIsDestination() or key.getIsDestination() and other.getIsOrigin():
                continue
            curr_key_dict[other.getName()] = lookup_time(key, other)
    distances[key.getName()] = curr_key_dict

# distances = {
#     'B': {'A': 5, 'D': 1, 'G': 2},
#     'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
#     'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
#     'G': {'B': 2, 'D': 1, 'C': 2},
#     'C': {'G': 2, 'E': 1, 'F': 16},
#     'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
#     'F': {'A': 5, 'E': 2, 'C': 16}}
print(node.__str__() for node in nodes)
print(distances)
print(nodes)
print(djikstra.dijkstra(nodes, distances))
