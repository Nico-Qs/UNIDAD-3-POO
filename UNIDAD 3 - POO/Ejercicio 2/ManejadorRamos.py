from ManejadorFlores import ManejaFlores
from ClaseRamo import Ramo
class ManejadorRamos:
    __lista: list[Ramo]
    __instancia: ManejaFlores
    def __init__(self):
        self.__lista=[]
        self.__instancia=ManejaFlores()
    def agregar_Venta(self):
        tamaños=["Pequeño","Mediano","Grande"]
        t=int(input("Ingrese un tamaño de ramo: 1 - Pequeño, 2 - Mediano, 3 - Grande: "))
        R=Ramo(tamaños[t-1])
        self.__instancia.mostrar_flores()
        F = int(input("Ingrese un numero de flor 0 para terminar: "))
        while F != 0:
            if F > -1 and F <= self.__instancia.get_Ct():
                R.agregar_flor(self.__instancia.get_flor(F-1))
            else:
                print("Numero incorrecto ingrese nuevamente")
            F = int(input("Ingrese un numero de flor 0 para terminar: "))
        self.__lista.append(R)
    def calcula_Max(self):
        for i in range(len(self.__lista)):
            Maximos = [0] * self.__instancia.get_Ct()
            for j in range(len(Maximos)):
                ct=self.__lista[i].ct_flores(j+1)
                Maximos[j]=ct
            Maxx=max(Maximos)
            print("----5 Flores mas pedidas para el ramo {} de tamaño: {}----".format(i+1,self.__lista[i].getTam()))
            for k in range(len(Maximos)):
                if Maximos[k] == Maxx:
                    self.__instancia.mostrar_flor(k)
        """
        #Itera solo hasta las 5 flores maximas
        i=0
        j=0
        while i<len(Maximos) and j<=5:
            if Maximos[i] == max:
                print("--Nombre: {}--".format(self.__instancia.mostrar_flor(i)))
                j+=1
            i+=1
        """
    def tipoDeRamo(self):
        tip=input("Ingrese un tipo de ramo(Pequeño-Mediano-Grande): ").lower()
        print("Flores vendidas en los ramos de tipo: {}".format(tip))
        for i in range(len(self.__lista)):
            if self.__lista[i].getTam().lower() == tip:
                print("------Ramo: {}, Tamaño: {}------".format(i + 1, tip))
                print("--Flores--")
                self.__lista[i].flores_porTam()