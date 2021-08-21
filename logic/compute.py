# grab list of inputs from an expandable form (max 5 to start)
# ignore empty inputs
# try and confirm lookup, maybe directly reference google api to confirm location
# above solution should not require any error handling

# each list element then is represented as a node that needs to check distance to each other node
# based on distance and time

# assume (for now) that going and back is equal (which it sometimes isn't)

import Node
import djikstra
import djikstra2
import tps


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
    if start.getName() == "home" and end.getName() == "school":
        return 7
    elif start.getName() == "home" and end.getName() == "LJ":
        return 6

    elif start.getName() == "school" and end.getName() == "home":  # duplicate
        return 7
    elif start.getName() == "school" and end.getName() == "LJ":  # duplicate
        return 9
    elif start.getName() == "school" and end.getName() == "CFA":
        return 9

    elif start.getName() == "LJ" and end.getName() == "home":
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

originNode = createOrigin("home")

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
                continue  # this is here because the point is that you MUST go to other places before the destination
            curr_key_dict[other.getName()] = lookup_time(key, other)
        else:
            curr_key_dict[key.getName()] = 0
    distances[key.getName()] = curr_key_dict

# print(distances)
# print(nodes)
print(tps.tps(distances, originNode.getName(), destinationNode.getName()))
