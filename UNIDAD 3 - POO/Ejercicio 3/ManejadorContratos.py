
import datetime
from ClaseContrato import Contrato
import numpy as np
class ManejadorContratos:
    __cantidad: int
    __contratos: np.array
    __dimension: int
    __incremento: int

    def __init__(self, dim=1, inc=1):
        self.__contratos = np.empty(dim, dtype=Contrato)
        self.__dimension = dim
        self.__incremento = inc
        self.__cantidad = 0

    def agregarContrato(self, contrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = contrato
        self.__cantidad += 1

    def mostrarcontratos(self):
        for i in range(self.__cantidad):
            print(self.__contratos[i])

    def verificar_si_hay_contrato(self,jugador,equipo):
        band=False
        i=0
        while i<self.__cantidad and not band:
            if self.__contratos[i].getJugador().getNombre() == jugador.getNombre() and self.__contratos[i].getEquipo().getNombre() == equipo.getNombre():
                band=True
            i+=1
        return band

    def es_vigente(self,contrato):
        band=False
        fecha_actual=datetime.date.today()
        fecha_in=contrato.getFechain()
        fecha_fin=contrato.getFechafin()
        if fecha_actual >= fecha_in and fecha_fin <= fecha_fin:
            band=True
        return band
    def busca_contrato_vigente(self,jugador):
        i = 0
        pos = -1
        band=False
        while i < self.__cantidad and not band:
            player=self.__contratos[i].getJugador()
            if player.getDNI() == jugador.getDNI():
                pos=i
                band=True
            i+=1
        return pos
    def consulta_jugadores_contratados(self,jugador):
        b = self.busca_contrato_vigente(jugador)
        vigente = self.es_vigente(self.__contratos[b])
        if b!=-1 and vigente:
            equipo=self.__contratos[b].getEquipo()
            print("El jugador buscado posee un contrato vigente")
            print("Jugador: {}, Equipo: {}, Fecha de finalizacion de contrato: {}".format(jugador.getNombre(),equipo.getNombre(),self.__contratos[b].getFechafin()))
        else:
            print("El jugador ingresado no posee un contrato vigente")

    def consulta_contratos_de_un_equipo(self,equipo):
        band=False
        for i in range(self.__cantidad):
            fecha_actual=datetime.date.today()
            vence_6_meses=fecha_actual + datetime.timedelta(days=365/2)
            fecha_fin=self.__contratos[i].getFechafin()
            team=self.__contratos[i].getEquipo()
            if team.getNombre() == equipo.getNombre():
                if fecha_fin >= fecha_actual and fecha_fin <= vence_6_meses:
                    jugador=self.__contratos[i].getJugador()
                    print("Jugador: [{}], su contrato vence en {} mes/meses".format(jugador,fecha_fin.month - fecha_actual.month))
                    band=True
        if not band:
            print("El equipo, {} no posee contratos que tiene una fecha de vencimiento dentro de los proximos 6 meses".format(equipo.getNombre()))

    def importe_de_contratos(self,equipo):
        total=0.0
        for i in range (self.__cantidad):
            team=self.__contratos[i].getEquipo()
            if team.getNombre() == equipo.getNombre():
                if self.es_vigente(self.__contratos[i]):
                    total+=self.__contratos[i].getPago()
        print("El equipo, {} paga mensualmente a sus jugadores en conceptos de contrato una cantidad de {} pesos".format(equipo.getNombre(),total))

    def crear_archivo(self):
        with open('Contratos.csv', 'w') as archivo:
            archivo.write('DNI del jugador;Nombre del equipo;Fecha de inicio;Fecha de finalizacion;Pago mensual\n')
            for contrato in self.__contratos:
                jugador=contrato.getJugador()
                equipo=contrato.getEquipo()
                archivo.write(
                    jugador.getDNI() + ";" +
                    equipo.getNombre() + ";" +
                    str(contrato.getFechain()) + ";" +
                    str(contrato.getFechafin()) + ";" +
                    str(contrato.getPago()) + "\n")
            print("--Archivo generado correctamente--")