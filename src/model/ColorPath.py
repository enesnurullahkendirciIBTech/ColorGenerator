class ColorPath:
    nextPath = None

    def __init__(self, name):
        self.name = name

    def setNextPath(self, nextPath):
        if self.nextPath is None:
            self.nextPath = nextPath
        else:
            self.nextPath.setNextPath(nextPath)
