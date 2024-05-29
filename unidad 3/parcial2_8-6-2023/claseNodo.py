from Inmueble import Inmueble


class Nodo:
    __inmueble: Inmueble
    __siguiente: object
    def __init__(self, inmueble):
        self.__inmueble = inmueble
        self.__siguiente = None
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__inmueble
   