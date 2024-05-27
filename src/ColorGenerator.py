
import json
import copy

from src.model.ColorPath import ColorPath
from src.model.ColorModel import ColorModel

class ColorGenerator:
    def start(self):
         with open('resources/tokens.json') as model:
             tokens = json.load(model)
             for index, (key, subdict) in enumerate(tokens.items()):
                 colorPath = ColorPath(key)
                 self.__find(subdict, colorPath)

    def __find(self, subdict, colorPath):
        print(subdict)
        print(colorPath)
        if '$type' in subdict and subdict['$type'] == "color":
            self.__prepareColor(subdict, colorPath)
        else:
            for childKey, childs in subdict.items():
                colorPathCopy = copy.deepcopy(colorPath)
                childPath = ColorPath(childKey)
                colorPathCopy.setNextPath(childPath)
                self.__find(childs, colorPathCopy)

    def __prepareColor(self, subdict, colorPath):
        print(subdict)
        with open('resources/basecolors.json') as model:
            baseColors = json.load(model)
            value = subdict['$value'].replace("{", "").replace("}", "")
            colorNames = value.split(".")
            color = baseColors
            for index, colorName in enumerate(colorNames):
                color = color[colorName]
            color = color['$value']
            colorModel = ColorModel()
            colorModel.createAssets(color, colorPath)









