
import json
import copy

from src.model.ColorPath import ColorPath
from src.model.ColorModel import ColorModel

class ColorGenerator:
    def start(self):
        with open('resources/basecolors.json') as baseColorsData:
            baseColors = json.load(baseColorsData)
            themes = baseColors["baseColors"]

            for theme in themes:
                themeInformation = theme['theme']
                basedColors = theme['colors']
                with open('resources/tokens.json') as model:
                    tokens = json.load(model)
                    lightTokens = tokens['light']
                    for index, (key, subdict) in enumerate(lightTokens.items()):
                        colorPath = ColorPath(key)
                        self.__find(subdict, colorPath, basedColors, themeInformation, False)

                    darkTokens = tokens['dark']
                    for index, (key, subdict) in enumerate(darkTokens.items()):
                        colorPath = ColorPath(key)
                        self.__find(subdict, colorPath, basedColors, themeInformation, True)

    def __find(self, subdict, colorPath, basedColors, theme, isDark):
        print(subdict)
        print(colorPath)
        if '$type' in subdict and subdict['$type'] == "color":
            self.__prepareColor(subdict, colorPath, basedColors, theme, isDark)
        else:
            for childKey, childs in subdict.items():
                colorPathCopy = copy.deepcopy(colorPath)
                childPath = ColorPath(childKey)
                colorPathCopy.setNextPath(childPath)
                self.__find(childs, colorPathCopy, basedColors, theme, isDark)

    def __prepareColor(self, subdict, colorPath, basedColors, theme, isDark):
        print(subdict)

        basedColorsCopy = copy.deepcopy(basedColors)
        value = subdict['$value'].replace("{", "").replace("}", "")
        colorNames = value.split(".")
        color = basedColorsCopy
        for index, colorName in enumerate(colorNames):
            color = color[colorName]
        color = color['$value']
        colorModel = ColorModel(theme, isDark)
        colorModel.createAssets(color, colorPath)









