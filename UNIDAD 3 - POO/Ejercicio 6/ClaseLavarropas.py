from ClaseAparatos import Aparato
class Lavarropa(Aparato):
    __capacidad: int
    __velocidad: int
    __ct_program: int
    __tipo_de_carga: str

    def __init__(self,marca,model,col,pais,precio,capacidad,velocidad,ct,tipo):
        self.__capacidad = int(capacidad)
        self.__velocidad = int(velocidad)
        self.__ct_program = int(ct)
        self.__tipo_de_carga = tipo
        super().__init__(marca,model,col,pais,precio)

    def getCapacidad(self):
        return self.__capacidad

    def getVelocidad(self):
        return self.__velocidad

    def getCtprogram(self):
        return self.__ct_program

    def getTipo(self):
        return self.__tipo_de_carga