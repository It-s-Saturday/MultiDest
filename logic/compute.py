# grab list of inputs from an expandable form (max 5 to start)
# ignore empty inputs
# try and confirm lookup, maybe directly reference google api to confirm location
# above solution should not require any error handling

# each list element then is represented as a node that needs to check distance to each other node
# based on distance and time

#
import Node

travel = {}

originNode = Node.Node("Home")
originNode.setAsOrigin()

destinationNode = Node.Node("CFA")
destinationNode.setAsDestination()

stops = ["school", "LJ"]

travel[originNode] = 0

list_of_stops = []
for stop in stops:
    temp = Node.Node(stop)
    travel[temp] = None
    list_of_stops.append(temp)

travel[destinationNode] = len(stops) + 1

for key in travel.keys():
    print(key.__str__(), travel[key])
