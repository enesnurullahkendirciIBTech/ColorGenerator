import json

from src.model.RGBModel import RGBModel

class ColorAssetsModel:

    def create(self, path, color):
        rgbModel = None
        if "#" in color:
            rgbModel = self.__getColorFromHex(color)
        else:
            rgbModel = self.__getColorFromRgb(color)

        print(color)
        self.__writeColor(path, rgbModel)

    def __getColorFromHex(self, hexColor):
        hexColor = hexColor.lstrip('#')
        red = int(hexColor[0:2], 16) / 255.0
        green = int(hexColor[2:4], 16) / 255.0
        blue = int(hexColor[4:6], 16) / 255.0
        alpha = 1.0
        if len(hexColor) == 8:
            alpha = int(hexColor[6:8], 16) / 255.0
        return RGBModel(red, green, blue, alpha)

    def __getColorFromRgb(self, color):
        values = color.split("(")[1].split(")")[0].split(", ")

        red = float(values[0]) / 255.0
        green = float(values[1]) / 255.0
        blue = float(values[2]) / 255.0
        alpha = float(values[3])
        return RGBModel(red, green, blue, alpha)

    def __writeColor(self, path, rgbModel):
        with open('resources/ExampleColor.json') as data:
            jsonModel = json.load(data)

            print(jsonModel)
            for item in jsonModel["colors"]:
                if "appearances" in item:
                    for appearance in item["appearances"]:
                        if appearance["value"] != "dark":
                            print("Dark olmayan appearance:", appearance)
                else:
                    components = item['color']['components']
                    components["alpha"] = rgbModel.getAlphaValue()
                    components["red"] = rgbModel.getRedValue()
                    components["blue"] = rgbModel.getBlueValue()
                    components["green"] = rgbModel.getGreenValue()

                    item['color']['components'] = components

                    print(jsonModel)
                    with open(path + "/Contents.json", 'w') as contentInfo:
                        json.dump(jsonModel, contentInfo)




