class CamelCaseConverter:

    @staticmethod
    def toCamelCase(snake_str):
        snake_str = snake_str.replace('-', '_')
        components = snake_str.split('_')
        return components[0].lower() + ''.join(x.title() for x in components[1:])