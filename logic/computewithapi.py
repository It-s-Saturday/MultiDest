# grab list of inputs from an expandable form (max 5 to start)
# ignore empty inputs
# try and confirm lookup, maybe directly reference google api to confirm location
# above solution should not require any error handling

# each list element then is represented as a node that needs to check distance to each other node
# based on distance and time

# assume (for now) that going and back is equal (which it sometimes isn't)
from contextlib import suppress

import Node
# import djikstra
# import djikstra2
from pathlib import Path
import googlemaps

from logic import maps, tsp

DRIVING = "driving"
WALKING = "walking"
BIKING = "bicycling"
TRANSIT = "transit"
DURATION = "duration"
DISTANCE = "distance"


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


def parseMeasurementFromAPI(toParse: str) -> int:  # returns time in minutes or distance in miles
    string = toParse.split(' ')
    cumulative_time = 0  # time in minutes
    cumulative_distance = 0  # distance in miles
    for i in range(0, len(string), 2):
        try:
            time_val = int(string[i])
        except:
            time_val = float(string[i])
        unit = string[i + 1]
        if "day" in unit:
            cumulative_time += time_val * 24 * 60
        elif "hour" in unit:
            cumulative_time += time_val * 60
        elif "min" in unit:
            cumulative_time += time_val
        elif unit == "ft":
            cumulative_time += time_val / 5280
        elif unit == "mi":
            cumulative_time += time_val
        else:
            raise Exception("Unhandled time_unit greater than day or distance greater then mile")
    return cumulative_time



def parseForMethod(input):
    if "driv" in input.lower():
        print("Method set to: Driving")
        return DRIVING
    elif "walk" in input.lower():
        print("Method set to: Walking")
        return WALKING
    elif "bi" in input.lower():
        print("Method set to: Bicycle")
        return BIKING
    elif "tra" in input.lower():
        print("Method set to: Transit")
        return TRANSIT
    else:
        print("{} not recognized, setting to: Driving".format(input))
        return DRIVING


def parseForChoice(input):
    if "ti" in input.lower():
        print("Choice set to: time")
        return DURATION
    elif "dis" in input.lower():
        print("Choice set to: distance")
        return DISTANCE
    else:
        print("{} not recognized, setting to: Time".format(input))
        return DURATION

def compute(distances: list):
    travel = {}

    stops = []
    timeOrDistance = parseForChoice(input("What would you like the time or distance?"))

    while True:
        pull_stops = input("Pull stops from file?")
        if "n" in pull_stops:
            originNode = createOrigin(input("Enter origin address or name: "))
            num_stops = int(input("How many stops between origin and destination?: "))
            print("Where are you stopping?")
            for i in range(num_stops):
                stops.append(input("Stop address or name: "))
                print(stops)
            destinationNode = createDestination(input("Enter destination address or name: "), len(stops))
            break
        elif "y" in pull_stops:
            filename = input("Enter file path: ")
            file = open(filename, encoding='utf-8-sig')
            line_num = 0
            for line in file.readlines():
                if line_num == 0:  # first line
                    originNode = createOrigin(line)
                    line_num += 1
                    continue
                stops.append(line.strip())
                print(line, "added:", stops)
                line_num += 1
                print(line_num)
            print("{} removed".format(stops[-1]))
            stops.remove(stops[-1])
            print(stops)
            destinationNode = createDestination(line, len(stops))  # last line (hopefully)
            break
        else:
            print("Unknown input, please try again.")

    method = parseForMethod(input("Finally, how will you be travelling?"))

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
            print(key, other.getName())
            if key != other:
                if key.getIsOrigin() and other.getIsDestination() or key.getIsDestination() and other.getIsOrigin():
                    continue  # this is here because the point is that you MUST go to other places before the destination
                # travel = [keya: valub]
                # travel = [valub: keya]
                # skip if travel[key] == other and travel[other] == key and walking

                # with suppress(KeyError):
                #     if method == WALKING and key.getName() in distances[other.getName()]:
                #         print("skipped")
                #         continue
                curr_key_dict[other.getName()] = parseMeasurementFromAPI(
                    maps.lookup(key.getName(), other.getName(), method, timeOrDistance))
            else:
                curr_key_dict[key.getName()] = 0
            # print(curr_key_dict)
        distances[key.getName()] = curr_key_dict
        print(distances)
        # print(distances)
    tsp.tsp(distances, originNode.getName(), destinationNode.getName(), timeOrDistance)

    # travelling salesman problem
