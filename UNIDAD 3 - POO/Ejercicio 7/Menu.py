import os
from ObjectEncoder import ObjectEncoder
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDocenteInvestigador import DocenteInvestigador
from ManejaInterfaz import ManejaInterface
from ClaseLista import Lista
class Menu:
    __claseLista: Lista

    def __init__(self):
        self.__claseLista=Lista()

    def mostrar(self):
        print("1 - Crear archivo .json si es que no existe")
        print("2 - Insertar un agente en la colección en una posición determinada.\n3 - Agregar un agente a la colección.")
        print("4 - Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
        print("5 - Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("6 - Mostrar la marca de todos los lavarropas que tienen carga superior .\n7 - Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.")
        print("8 - Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.")

    def cargaJson(self,jsonF):
        objeto1 = Docente(cuil="20-3454506-8", apellido="Perez", nombre="Nicolas", sueldo=89000, anti=3,carrera="LCC", cargo="JTP", catedra="Sistemas de Informacion")
        objeto2 = Investigador(cuil="15-324235-5", apellido="Dominguez", nombre="Juan", sueldo=120000, anti=2,area="Computacional", tipo="Cientifica")
        objeto3 = PersonalApoyo(cuil="12-456543-4", apellido="Castro", nombre="Maria", sueldo=140000, anti=2,categoria="I")
        objeto4 = DocenteInvestigador(programa="I", importe=25000, cuil="18-3446706-8", apellido="Lopez",nombre="Marcos", sueldo=89000, anti=3, catedra="EyFCI", carrera="LCC",cargo="Jefe de Catedra", area="Estructuras", tipo="Teorica")
        d = objeto1.toJson()
        d1 = objeto2.toJson()
        d2 = objeto3.toJson()
        d3 = objeto4.toJson()
        lista = [d, d1, d2, d3]
        jsonF.guardarJSONArchivo(lista, "Personal.json")

    def menuOp(self):
        try:
            jsonF = ObjectEncoder()
            jsonF.decodificarDiccionario(self.__claseLista)
            manejaInterfaz = ManejaInterface()
        except:
            print("Necesita crearse el archivo, puede ingresar la opcion 1 del programa")
        self.mostrar()
        op=int(input("Ingrese una opcion 0 para terminar: "))
        while op != 0:
            os.system('cls')
            if op == 1:
                self.cargaJson(jsonF)
                jsonF.decodificarDiccionario(self.__claseLista)
                manejaInterfaz = ManejaInterface()

            elif op == 2:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 3:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 4:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 5:
                self.__claseLista.listado_ordenador_porNombre()

            elif op == 6:
                self.__claseLista.cuentaAgenteInvestigadores()

            elif op == 7:
                for dato in self.__claseLista:
                    print(dato.getTipoAgente())

            elif op == 8:
                print()#self.__claseLista.almacenaJson(jsonF)
            self.mostrar()
            op = int(input("Ingrese una opcion 0 para terminar: "))
            os.system('cls')