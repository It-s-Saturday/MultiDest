# grab list of inputs from an expandable form (max 5 to start)
# ignore empty inputs
# try and confirm lookup, maybe directly reference google api to confirm location
# above solution should not require any error handling

# each list element then is represented as a node that needs to check distance to each other node
# based on distance and time

# assume (for now) that going and back is equal (which it sometimes isn't)

from . import maps, tsp, Node

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
    cumulative = 0
    for i in range(0, len(string), 2):
        try:
            time_val = int(string[i])
        except:
            time_val = float(string[i])
        unit = string[i + 1]
        if "day" in unit:
            cumulative += time_val * 24 * 60
        elif "hour" in unit:
            cumulative += time_val * 60
        elif "min" in unit:
            cumulative += time_val
        elif unit == "ft":
            cumulative += time_val / 5280
        elif unit == "mi":
            cumulative += time_val
        else:
            raise Exception("Unhandled metric greater than day or distance greater then mile")
    return cumulative


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


def compute(i_choice: str, i_method: str, i_origin: str, i_destination: str,
            i_stops: list[str]):
    """This method parses user input from views.py and populates appropriate dictionaries before sending it to tsp.py"""

    travel = {}
    # TODO: get rid of empty elements from distances
    for entry in i_stops:
        if  entry.strip() == "":
            i_stops.remove(entry)
    if len(i_stops) <= 1:
        raise Exception("Invalid text Input")


    stops = []
    choice = i_choice

    originNode = createOrigin(i_origin)
    for i in range(len(i_stops)):
        if i == 0 or i == len(i_stops) - 1:
            continue
        stops.append(i_stops[i])  # otherwise, add it to stops
    destinationNode = createDestination(i_destination, len(stops))

    method = parseForMethod(i_method)

    travel[originNode] = originNode.getIndex()

    list_of_stops = []
    for stop in stops:
        temp = Node.Node(stop)
        travel[temp] = None
        list_of_stops.append(temp)

    travel[destinationNode] = destinationNode.getIndex()

    # nodes = ()
    # for node in travel.keys():
    #     nodes = nodes + (node.getName(),)

    distances = {}

    # for each key in the dictionary, call lookup on key and all other keys in the dict and populate it
    # outer dict maps single source to n targets
    # inner dict gives distances to n targets
    for key in travel.keys():
        curr_key_dict = {}
        for other in travel.keys():
            print(key, other.getName())
            if key != other:
                if key.getIsOrigin() and other.getIsDestination() or key.getIsDestination() and other.getIsOrigin():
                    continue  # this is here because the point is that you MUST go to other places before the destination
                # travel = [keya: valub]
                # travel = [valub: keya]

                curr_key_dict[other.getName()] = parseMeasurementFromAPI(
                    maps.lookup(key.getName(), other.getName(), method, choice))
            else:
                curr_key_dict[key.getName()] = 0
        distances[key.getName()] = curr_key_dict
        # print(distances)
    tsp.tsp(distances, originNode.getName(), destinationNode.getName(), i_choice)
