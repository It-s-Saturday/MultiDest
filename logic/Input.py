class Input:


    def __init__(self):
        self.fromHTML = []

    def getChoice(self):
        return self.fromHTML[0]

    def getMethod(self):
        return self.fromHTML[1]

    def getOrigin(self):
        return self.fromHTML[0]

    def getStops(self):
        return self.fromHTML[1, -2] # from first element to second to last

    def getDest(self):
        return self.fromHTML[-1]

    def __str__(self):
        out = "Choice: " + self.getChoice()
        out += "\nMethod " + self.getMethod()
        out += "\nOrigin: " + self.getOrigin()
        out += "\nStops: " + self.getStops()
        out += "\nDestination: " + self.getDest()
        return out