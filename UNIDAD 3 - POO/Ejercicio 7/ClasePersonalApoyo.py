from ClasePersonal import Personal
class PersonalApoyo(Personal):
    __categoria: str

    def __init__(self, **kwargs):
        self.__categoria = kwargs["categoria"]
        super().__init__(**kwargs)

    def __repr__(self):
        return repr(__class__)

    def getTipoAgente(self):
        return (self.__class__.__name__)

    def getCategoria(self):
        return self.__categoria

    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getCuil(),
                    apellido= self.getApellido(),
                    nombre= self.getNombre(),
                    sueldo= self.getSueldo(),
                    anti= self.getAnti(),
                    categoria = self.__categoria
                )
            )
            return d