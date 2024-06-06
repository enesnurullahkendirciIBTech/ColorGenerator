import os

from src.utility.XCAssetsMaker import XCAssetsMaker
from src.utility.CamelCaseConvertor import CamelCaseConverter

class ThemeProtocolMaker:
    path = "/Users/volkan/Desktop/Test/"

    def generateColorProtocol(self, colorPathNode):
        self.__createPath(self.path, colorPathNode, "")

    def __createPath(self, filePath, colorPathNode, assetName):
        if colorPathNode.nextPath is None:
            assetName = assetName + colorPathNode.name + ".colorset"
            filePath = filePath + "/" + assetName
        else:
            filePath = filePath + "/" + colorPathNode.name
            assetName += colorPathNode.name + "_"

        if colorPathNode.nextPath is not None:
            self.__createPath(filePath, colorPathNode.nextPath, assetName)
        else:
            self.__generateToColorName(assetName)

    def __generateToColorName(self, assetName):
       colorName = assetName
       if colorName.endswith(".colorset"):
           colorName = colorName[:-len(".colorset")]

       colorName = CamelCaseConverter.toCamelCase(colorName)
       colorGenerated = f"var {colorName}: UIColor {{ get }}\n"

       filePath = self.path + "/ThemeProtocol"
       with open(filePath, "a") as file:
          file.write("\n" + colorGenerated)