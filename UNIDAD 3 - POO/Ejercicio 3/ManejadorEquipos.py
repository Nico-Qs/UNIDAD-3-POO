import numpy as np
from ClaseEquipo import Equipo
import csv
class ManejadorEquipos:
    __equipos : np.array
    __cantidad : int
    __dimension : int
    __incremento : int

    def __init__(self,dim=10,inc=2):
        self.__equipos=np.empty(dim,dtype=Equipo)
        self.__dimension=dim
        self.__incremento=inc
        self.__cantidad=0

    def agregarEquipo(self,equipo):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__equipos.resize(self.__dimension)
        self.__equipos[self.__cantidad]=equipo
        self.__cantidad+=1

    def mostrarEquipos(self):
        for i in range(self.__cantidad):
            print(self.__equipos[i])

    def cargarEquipos(self):
        archivo=open("Equipos.csv")
        reader=csv.reader(archivo,delimiter=";")
        fila=next(reader)
        cantidad=int(fila[0])
        for i in range(cantidad):
            fila=next(reader)
            E=Equipo(fila[0],fila[1])
            self.agregarEquipo(E)
        archivo.close()

    def buscaEquipo(self,nombre):
        i=0
        pos=-1
        band=False
        while i<self.__cantidad and not band:
            equipo=self.__equipos[i]
            if equipo.getNombre() == nombre:
                pos=i
                band=True
            i+=1
        if i>self.__cantidad:
            print("Equipo '{}' no encontrado...".format(nombre))
        return pos

    def getEquipo(self,pos):
        return self.__equipos[pos]
