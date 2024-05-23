import csv

from classCliente import Cliente
from gestorReparacion import GestorReparacion

class GestorCliente:
    __lista_clientes: list

    def __init__(self):
        self.__lista_clientes = []

    def cargarClientes(self):
        archivo = open("clientes.csv")
        reader = csv.reader(archivo, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                dni = int(fila[0])
                apellido = fila[1]
                nom = fila[2]
                tel = int(fila[3])
                pat = fila[4]
                vehiculo = fila[5]
                estado = fila[6]
                unCliente = Cliente(dni,apellido,nom,tel,pat,vehiculo,estado)
                self.__lista_clientes.append(unCliente)
        archivo.close()

    def buscarCliente(self, xdni):
        band = False
        valorRet = None
        indice = 0
        while not band and indice < len(self.__lista_clientes):
            if xdni == self.__lista_clientes[indice].getDni():
                band = True
                valorRet = indice
            else:
                indice += 1
        return valorRet
    def getCliente(self, indice):
        return self.__lista_clientes[indice]
    def __eq__(self, other):
        return self.getDni() == other.getDni()





    
