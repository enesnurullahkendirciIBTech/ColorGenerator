import json
import copy

from src.data.ColorPathNode import ColorPathNode
from src.utility.DirectoryMaker import DirectoryMaker


class ColorGenerator:

    def start(self):
        with open('resources/BaseColors.json') as baseColorsData:
            baseColors = json.load(baseColorsData)
            themes = baseColors["baseColors"]

            for theme in themes:
                themeInformation = theme['theme']
                basedColors = theme['colors']
                with open('resources/Tokens.json') as model:
                    tokens = json.load(model)
                    lightTokens = tokens['light']
                    for index, (key, subdict) in enumerate(lightTokens.items()):
                        colorPathNode = ColorPathNode(key)
                        self.__find(subdict, colorPathNode, basedColors, themeInformation, False)

                    darkTokens = tokens['dark']
                    for index, (key, subdict) in enumerate(darkTokens.items()):
                        colorPathNode = ColorPathNode(key)
                        self.__find(subdict, colorPathNode, basedColors, themeInformation, True)

    def __find(self, subdict, colorPath, basedColors, theme, isDark):
        print(subdict)
        print(colorPath)
        if '$type' in subdict and subdict['$type'] == "color":
            self.__prepareColor(subdict, colorPath, basedColors, theme, isDark)
        else:
            for childKey, childs in subdict.items():
                colorPathCopy = copy.deepcopy(colorPath)
                childPath = ColorPathNode(childKey)
                colorPathCopy.setNextPath(childPath)
                self.__find(childs, colorPathCopy, basedColors, theme, isDark)

    def __prepareColor(self, subdict, colorPathNode, basedColors, theme, isDark):
        print(subdict)
        basedColorsCopy = copy.deepcopy(basedColors)
        value = subdict['$value'].replace("{", "").replace("}", "")
        colorNames = value.split(".")
        color = basedColorsCopy
        for index, colorName in enumerate(colorNames):
            color = color[colorName]
        color = color['$value']
        directoryMaker = DirectoryMaker(theme, isDark)
        directoryMaker.createAssets(color, colorPathNode)