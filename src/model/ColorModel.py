import os
import json

from src.model.ColorPath import ColorPath
from src.model.ColorAssetsModel import ColorAssetsModel

class ColorModel:
    path = "/Users/volkansonmez/Desktop/test"
    root = "Colors.xcassets"

    def createAssets(self, colorName, colorPath):
        self.__createRootFolder()
        self.__createPath(self.__getRootPath(), colorName, colorPath)

    def __createRootFolder(self):
        if not os.path.exists(self.__getRootPath()):
            os.makedirs(self.__getRootPath())
            self.__addInfoJson(self.__getRootPath())

    def __createPath(self, filePath, colorName, colorPath):
        filePath = filePath + "/" + colorPath.name
        if not os.path.exists(filePath):
            os.makedirs(filePath)
            if colorPath.nextPath is not None:
                self.__addInfoJson(filePath)

        if colorPath.nextPath is not None:
            self.__createPath(filePath, colorName, colorPath.nextPath)
        else:
            ColorAssetsModel().create(filePath, colorName)

    def __getRootPath(self):
        return self.path + "/" + self.root

    def __addInfoJson(self, path):
        info = {
                "info" : {
                     "author" : "xcode",
                     "version" : 1
                }
         }
        filePath = path + "/Contents.json"
        with open(filePath, 'w') as contents:
            json.dump(info, contents)

