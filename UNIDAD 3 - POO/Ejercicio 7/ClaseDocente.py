from ClasePersonal import Personal
class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str

    def __init__(self, **kwargs):
        self.__carrera = kwargs["carrera"]
        self.__cargo = kwargs["cargo"]
        self.__catedra = kwargs["catedra"]
        super().__init__(**kwargs)


    def getTipoAgente(self):
        return (self.__class__.__name__)

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getCuil(),
                    apellido= self.getApellido(),
                    nombre= self.getNombre(),
                    sueldo= self.getSueldo(),
                    anti= self.getAnti(),
                    carrera = self.__carrera,
                    cargo = self.__cargo,
                    catedra = self.__catedra,
                )
            )
            return d
