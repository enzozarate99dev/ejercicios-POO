import csv
import numpy as np
from classCuenta import Cuenta
from gestorTransaccion import GestorTransaccion

class GestorCuenta:
    __cuentas: np.ndarray

    def __init__(self):
        self.__cuentas = np.empty(0, dtype=Cuenta)

    def agregarCuenta(self):
        archivo = open("cuentasBilletera.csv")
        reader = csv.reader(archivo)
        band = True
        for fila in reader:
            if band:
                "saltar cabecera"
                band = not band
            else:
                apellido = fila[0]
                nombre = fila[1]
                dni = int(fila[2])
                telefono = int(fila[3])
                saldo = float(fila[4])
                cbu = int(fila[5])
                unaCuenta = Cuenta(apellido, nombre, dni, telefono, saldo, cbu)
                self.__cuentas = np.append(self.__cuentas, unaCuenta)
        archivo.close()
    
    def actualizarSaldoPorTransacciones(self, monto):
        for cuenta in self.__cuentas:
            cuenta.setSaldo(monto)

    
    def buscarCuenta(self, xdni):
        band = False
        valorRet = None
        indice = 0
        while not band and indice < len(self.__cuentas):
            if xdni == self.__cuentas[indice].getDNI():
                band = True
                valorRet = indice
            else:
                indice += 1
        return valorRet
    
    def getUnaCuenta(self, indice):
        self.__cuentas[indice].mostrar()

    def mostrarCuentas(self):
        for cuenta in self.__cuentas:
            cuenta.mostrar()
    def setPorcAnual(self, xp):
        # El indice 0 es indiferente, igualmente se modifica para todas las instancias
        self.__cuentas[0].setPorcAnual(xp)


