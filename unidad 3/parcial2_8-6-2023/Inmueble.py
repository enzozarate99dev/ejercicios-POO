import abc
from abc import ABC
class Inmueble(ABC):
    __localidad: str
    __direccion: str
    __supC: float
    def __init__(self, localidad, direccion, supC):
        self.__localidad = localidad
        self.__direccion = direccion
        self.__supC = supC
    def __str__(self):
        return f"Localidad: {self.__localidad} - "   + f"Direccion: {self.__direccion} - "  + f"Superficie: {self.__supC} - " 
    def getLocalidad(self):
        return self.__localidad
    def getDireccion(self):
        return self.__direccion
    def getSupC(self):
        return self.__supC
    @abc.abstractmethod
    def getPrecioConstruccion(self):
        pass
    def getImporteVenta(self):
        return self.getSupC() * 15 * self.getPrecioConstruccion()