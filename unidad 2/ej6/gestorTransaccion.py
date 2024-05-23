import csv

from classTransaccion import Transaccion


class GestorTransaccion:
    __transacciones: list
    def __init__(self):
        self.__transacciones = []
    def agregarTransaccion(self):
        archivo = open("transaccionesBilletera.csv")
        reader = csv.reader(archivo)
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                num = int(fila[0])
                cbu = int(fila[1])
                imp = float(fila[2])
                tipo = fila[3]
                unaTransac = Transaccion(cbu, num, imp, tipo)
                self.__transacciones.append(unaTransac)
        archivo.close()
    def getImpTransaccionesPorCBU(self, cbu):
        acum = 0
        for tr in self.__transacciones:
            if tr.getCBU() == cbu:
                acum += tr.getImporte()
        return acum

