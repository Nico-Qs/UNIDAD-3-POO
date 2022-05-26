from ClaseAparatos import Aparato
class Heladera(Aparato):
    __capacidadLit: int
    __freezer: bool
    __ciclica: bool

    def __init__(self,marca,model,col,pais,precio,capacidad,freezer,cicl):
        self.__capacidad = int(capacidad)
        self.__freezer = bool(freezer)
        self.__ciclica = bool(cicl)
        super().__init__(marca,model,col,pais,precio)

    def getCapacidadlit(self):
        return self.__capacidadLit

    def getFreezer(self):
        return self.__freezer

    def getCiclica(self):
        return self.__ciclica