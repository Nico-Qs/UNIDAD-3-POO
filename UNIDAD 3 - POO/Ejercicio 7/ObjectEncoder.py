from pathlib import Path
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDocenteInvestigador import DocenteInvestigador
import json
class ObjectEncoder(object):

    def decodificarDiccionario(self,lista):
        diccionario = self.leerJSONArchivo("Personal.json")
        for elem in diccionario:
            if '__class__' not in elem:
                print("No se encuentra el diccionario")
            else:
                class_name=elem['__class__']
                class_=eval(class_name)
                if class_name == "Docente":
                    atributos = elem['__atributos__']
                    H = class_(**atributos)
                    lista.insertarFinal(H)
                elif class_name == "Investigador":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.insertarFinal(T)
                elif class_name == "DocenteInvestigador":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.insertarFinal(T)
                elif class_name == "PersonalApoyo":
                    atributos = elem['__atributos__']
                    L = class_(**atributos)
                    lista.insertarFinal(L)

    def retornarObjeto(self, tipo):
        if tipo == "docente":
            objeto = Docente(cuil="15-1823791-2", apellido="Ortiz", nombre="Juan", sueldo=50000, anti=10, carrera="LSI",cargo="JTP", catedra="Programacion Orientada a Objetos")
        elif tipo == "investigador":
            objeto = Investigador(cuil="20-1923192-3", apellido="Dominguez", nombre="Carlos", sueldo=120000, anti=2,area="Computacional", tipo="Cientifica")
        elif tipo == "personal apoyo":
            objeto = PersonalApoyo(cuil="12-456543-4", apellido="Pereyra", nombre="Maria", sueldo=70000, anti=1,categoria="I")
        elif tipo == "docente investigador":
            objeto = DocenteInvestigador(programa="I", importe=25000, cuil="18-3446706-8", apellido="Lopez", nombre="Juan Cruz", sueldo=90000, anti=4, catedra="EyFCI", carrera="LCC",cargo="Jefe de Catedra", area="Estructuras", tipo="Teorica")
        else:
            objeto = None

        return objeto
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)