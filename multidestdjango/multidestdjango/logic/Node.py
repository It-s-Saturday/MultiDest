
class Node:
    def __init__(self, name: str):
        self.name = name
        self.index = -1
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

    def getName(self) -> str:
        return self.name

    def __str__(self):
        return "Node:" + self.getName()
