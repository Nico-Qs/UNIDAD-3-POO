from ClaseCalefactorGas import CalefactorGas
from ClaseCalefactorElectrico import CalefactorElectrico
from ClaseCalefactor import Calefactor
import csv
import numpy as np
class ManejadorCalefactores:
    __calefactores: np.array

    def __init__(self):
        self.__calefactores=np.empty(0,dtype=Calefactor)

    def agregarCalefactor(self,calefactor):
        self.__calefactores = np.append(self.__calefactores,calefactor)

    def cargaElectricos(self):
        with open('calefactor-electrico.csv','r',encoding="utf8") as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader, None)
            for fila in reader:
                C=CalefactorElectrico(fila[0],fila[1],fila[2])
                self.agregarCalefactor(C)
            archivo.close()

    def cargaGas(self):
        with open('calefactor-a-gas.csv','r',encoding="utf8") as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                C=CalefactorGas(fila[0],fila[1],fila[2],fila[3])
                self.agregarCalefactor(C)
            archivo.close()

    def item_1(self):
        c=int(input("Ingrese el costo por metro al cubo: "))
        h=int(input("Ingrese la cantidad que se estima que consumira por hora: "))
        pos=-1
        min=99999999
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores[i]) is CalefactorGas:
                costo=(self.__calefactores[i].getCalorias()/1000)*c*h
                if costo < min:
                    min=costo
                    pos=i
        print("El calefactor a gas de menor consumo es el de marca {} y modelo {}.".format(self.__calefactores[pos].getMarca(),self.__calefactores[pos].getModelo()))
    def item_2(self):
        c=int(input("Ingrese el costo por metro al cubo: "))
        h=int(input("Ingrese la cantidad que se estima que consumira por hora: "))
        pos=-1
        min=99999999
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores[i]) is CalefactorElectrico:
                costo=(self.__calefactores[i].getPotencia()/1000)*c*h
                if costo < min:
                    min=costo
                    pos=i
        print("El calefactor electrico de menor consumo es el de marca {} y modelo {}.".format(self.__calefactores[pos].getMarca(),self.__calefactores[pos].getModelo()))