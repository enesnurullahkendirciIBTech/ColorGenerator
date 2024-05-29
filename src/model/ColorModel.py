import os
import json

from src.model.ColorPath import ColorPath
from src.model.ColorAssetsModel import ColorAssetsModel

class ColorModel:
    path = "/Users/volkansonmez/Desktop/test"

    def __init__(self, theme, isDark):
        self.theme = theme
        self.isDark = isDark

    def createAssets(self, colorName, colorPath):
        self.__createRootFolder()
        self.__createPath(self.__getRootPath(), colorName, colorPath, "")

    def __createRootFolder(self):
        if not os.path.exists(self.__getRootPath()):
            os.makedirs(self.__getRootPath())
            self.__addInfoJson(self.__getRootPath())

    def __createPath(self, filePath, colorName, colorPath, assetName):
        if colorPath.nextPath is None:
            assetName = self.theme['prefix'] + assetName + colorPath.name + ".colorset"
            filePath = filePath + "/" + assetName + colorPath.name + ".colorset"
        else:
            filePath = filePath + "/" + colorPath.name
            assetName += colorPath.name + "_"

        if not os.path.exists(filePath):
            os.makedirs(filePath)
            if colorPath.nextPath is not None:
                self.__addInfoJson(filePath)

        if colorPath.nextPath is not None:
            self.__createPath(filePath, colorName, colorPath.nextPath, assetName)
        else:
            ColorAssetsModel().create(filePath, colorName, self.isDark)
            self.__generateColorSwiftFile(assetName)

    def __getRootPath(self):
        return self.path + "/" + self.theme['name'] + ".xcassets"

    def __addInfoJson(self, path):
        info = {
                "info" : {
                     "author" : "xcode",
                     "version" : 1
                }
         }
        filePath = path + "/Contents.json"
        if not os.path.exists(filePath):
            with open(filePath, 'w') as contents:
                json.dump(info, contents)


    def __generateColorSwiftFile(self, assetName):
        if self.isDark:
            colorName = assetName
            if colorName.startswith("daf_"):
                colorName = colorName[len("daf_"):]
                if colorName.endswith(".colorset"):
                    colorName = colorName[:-len(".colorset")]

            if assetName.endswith(".colorset"):
                assetName = assetName[:-len(".colorset")]
            colorGenerated = f"public var {colorName}: UIColor {{   \nR.color.{assetName}()~ \n}}"

            filePath = self.__getRootPath() + "/" + self.theme['name']
            with open(filePath, "a") as file:
                file.write("\n" + colorGenerated)