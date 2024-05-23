import csv

from classReparacion import Reparacion

class GestorReparacion:
    __lista_rep: list

    def __init__(self):
        self.__lista_rep = []

    def cargarRep(self):
        archivo = open("reparaciones.csv")
        reader = csv.reader(archivo, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                pat = fila[0]
                reparacion = fila[1]
                repuesto = fila[2]
                pr = float(fila[3])
                pmo = float(fila[4])
                estado = fila[5]
                unaRep = Reparacion(pat,reparacion,repuesto,pr,pmo,estado)
                self.__lista_rep.append(unaRep)
        archivo.close()
    
    def buscarReparaciones(self, xpat):
        indices = []
        for indice in range(len(self.__lista_rep)):
            if xpat == self.__lista_rep[indice].getPatente():
                indices.append(indice)
        return indices

    def getReparacionPorIndice(self, indice):
        return self.__lista_rep[indice]

    
