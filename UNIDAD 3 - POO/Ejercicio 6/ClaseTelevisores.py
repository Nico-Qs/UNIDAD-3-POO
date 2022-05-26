from ClaseAparatos import Aparato
class Televisor(Aparato):
    __tipo_pantalla: str
    __pulgadas: str
    __tipo_definicion: str
    __conexion_internet: bool

    def __init__(self,marca,model,col,pais,precio,tipo_pant,pulgad,tipo_def,conexion):
        self.__tipo_pantalla = tipo_pant
        self.__pulgadas = pulgad
        self.__tipo_definicion = tipo_def
        self.__conexion_internet = bool(conexion)
        super().__init__(marca,model,col,pais,precio)

    def getTipopant(self):
        return self.__tipo_pantalla

    def getPulgadas(self):
        return self.__pulgadas

    def getTipodefi(self):
        return self.__tipo_definicion

    def getConexion(self):
        return self.__conexion_internet