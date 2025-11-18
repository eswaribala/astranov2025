class Region:
    def __init__(self, code="I1", name="India"):
        self.__code = code
        self.__name = name
    def show(self):
        return f"Region[code={self.__code}, name={self.__name}]"