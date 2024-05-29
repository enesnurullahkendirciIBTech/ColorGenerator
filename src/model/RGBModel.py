class RGBModel:
    def __init__(self, red, green, blue, alpha):
        self.alpha = alpha
        self.green = green
        self.blue = blue
        self.red = red

    def getRedValue(self):
        return f"{self.red:.3f}"

    def getGreenValue(self):
        return f"{self.green:.3f}"

    def getBlueValue(self):
        return f"{self.blue:.3f}"

    def getAlphaValue(self):
        return f"{self.alpha:.3f}"