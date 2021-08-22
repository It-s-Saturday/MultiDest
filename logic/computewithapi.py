# grab list of inputs from an expandable form (max 5 to start)
# ignore empty inputs
# try and confirm lookup, maybe directly reference google api to confirm location
# above solution should not require any error handling

# each list element then is represented as a node that needs to check distance to each other node
# based on distance and time

# assume (for now) that going and back is equal (which it sometimes isn't)

import Node
# import djikstra
# import djikstra2
import tps
import googlemaps

from logic import maps


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

def parseTimeFromAPI(toParse: str) -> int: # returns time in minutes

    string = toParse.split(' ')
    cumulative_time = 0  # time in minutes
    for i in range(0, len(string), 2):
        time_val = int(string[i])
        unit = string[i + 1]
        if "day" in unit:
            cumulative_time += time_val * 24 * 60
        elif "hour" in unit:
            cumulative_time += time_val * 60
        elif "min" in unit:
            cumulative_time += time_val
        else:
            raise Exception("Unhandled time_unit greater than day")
    return cumulative_time


travel = {}

num_stops = int(input("How many stops between origin and destination?: "))
stops = []

originNode = createOrigin(input("Enter origin address or name: "))

print("Where are you stopping?")
for i in range(num_stops):
    stops.append(input("Stop address or name: "))
    print(stops)

destinationNode = createDestination(input("Enter destination address or name: "), len(stops))


travel[originNode] = originNode.getIndex()

list_of_stops = []
for stop in stops:
    temp = Node.Node(stop)
    travel[temp] = None
    list_of_stops.append(temp)

travel[destinationNode] = destinationNode.getIndex()

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
            curr_key_dict[other.getName()] = parseTimeFromAPI(maps.lookup(key.getName(), other.getName()))
        else:
            curr_key_dict[key.getName()] = 0
    distances[key.getName()] = curr_key_dict
tps.tps(distances, originNode.getName(), destinationNode.getName())

# Origin: Kean University
# Random Stops:
# 3 Golf Dr, Kenilworth, NJ
# Warinanco Park, Roselle, NJ
# 1561 Morris Ave, Union, NJ
# Destination:
# 154 Summit St Newark NJ


