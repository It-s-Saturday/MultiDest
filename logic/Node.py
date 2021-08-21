import sys


class Node:
    def __init__(self, name: str):
        self.name = name
        self.index = -1

        self.distance_from_origin = sys.maxsize
        self.distances_to_others = []
        self.distance_to_destination = sys.maxsize

        self.isOrigin = None
        self.isDestination = None

    def getIndex(self) -> int:
        return self.index

    def setIndex(self, index: int) -> None:
        self.index = index

    def setAsOrigin(self) -> None:
        self.isOrigin = True

    def getIsOrigin(self) -> bool:
        return self.isOrigin

    def setAsDestination(self) -> None:
        self.isDestination = True

    def getIsDestination(self) -> bool:
        return self.isDestination

    def unsetAsOrigin(self) -> None:
        self.isOrigin = False

    def unsetAsDestination(self) -> None:
        self.isDestination = False

    def getName(self) -> str:
        return self.name

    def getDistanceFromOrigin(self) -> int:
        return self.distance_from_origin

    def setDistanceFromOrigin(self, distance: int):
        self.distance_from_origin = distance

    def getDistancesToOthers(self) -> list:
        return self.distances_to_others

    def setDistancestoOthers(self, distances: list):
        self.distances_to_others = distances

    def getDistanceToDestination(self) -> int:
        return self.distance_to_destination

    def setDistanceToDestination(self, distance: int):
        self.distance_to_destination = distance

    def __str__(self):
        return "Node:" + self.getName()
