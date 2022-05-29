class Personal:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldob: float
    __anti: str

    def __init__(self, **kwargs):
        self.__cuil = kwargs["cuil"]
        self.__apellido = kwargs["apellido"]
        self.__nombre = kwargs["nombre"]
        self.__sueldob = kwargs["sueldo"]
        self.__anti = kwargs["anti"]

    def __gt__(self, other):
        return self.__nombre > other.__nombre
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldo(self):
        return self.__sueldob

    def getAnti(self):
        return self.__anti