import os
import json

from src.data import ColorPathNode
from src.utility.XCAssetsMaker import XCAssetsMaker


class DirectoryMaker:
    path = "/Users/volkan/Desktop/Test/"

    def __init__(self, theme, isDark):
        self.theme = theme
        self.isDark = isDark

    def createAssets(self, colorName, colorPathNode):
        self.__createRootFolder()
        self.__createPath(self.__getRootPath(), colorName, colorPathNode, "")

    def __createRootFolder(self):
        if not os.path.exists(self.__getRootPath()):
            os.makedirs(self.__getRootPath())
            self.__addInfoJson(self.__getRootPath())

    def __createPath(self, filePath, colorName, colorPathNode, assetName):
        if colorPathNode.nextPath is None:
            assetName = self.theme['prefix'] + assetName + colorPathNode.name + ".colorset"
            filePath = filePath + "/" + assetName
        else:
            filePath = filePath + "/" + colorPathNode.name
            assetName += colorPathNode.name + "_"

        if not os.path.exists(filePath):
            os.makedirs(filePath)
            if colorPathNode.nextPath is not None:
                self.__addInfoJson(filePath)

        if colorPathNode.nextPath is not None:
            self.__createPath(filePath, colorName, colorPathNode.nextPath, assetName)
        else:
            XCAssetsMaker().create(filePath, colorName, self.isDark)
            self.__generateColorSwiftFile(assetName)

    def __getRootPath(self):
        return self.path + "/" + self.theme['name'] + ".xcassets"

    def __addInfoJson(self, path):
        info = {
            "info": {
                "author": "xcode",
                "version": 1
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
