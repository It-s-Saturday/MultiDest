# grab list of inputs from an expandable form (max 5 to start)
    # ignore empty inputs
    # try and confirm lookup, maybe directly reference google api to confirm location
        # above solution should not require any error handling

# each list element then is represented as a node that needs to check distance to each other node
    # based on distance and time

#

class Node:
    def __init__(self, name):
        self.name = name
        self.distance_from_origin = None
        self.distances_to_others = []
        self.distance_to_destination = None

        self.isOrigin = None
        self.isDestination = None

    def setAsOrigin(self):
        self.isOrigin = True

    def setAsDestination(self):
        self.isDestination = True

    def unsetAsOrigin(self):
        self.isOrigin = False

    def unsetAsDestination(self):
        self.isDestination = False

    def getName(self):
        return self.name

    def getDistanceFromOrigin(self):
        return self.distance_from_origin

    def getDistancesToOthers(self):
        return self.distances_to_others

    def getDistanceToDestination(self):
        return self.distance_to_destination

    def __str__(self):
        return "Node:" + self.name


origin = ["Home"]
destination = ["CFA"]

points = ["school", "LJ"]

travel = {}


travel[Node(origin[0])] = 0

for point in points:

    travel[Node(point)] = None

travel[Node(destination[0])] = len(points) + 1

for key in travel.keys():
    print(key)
