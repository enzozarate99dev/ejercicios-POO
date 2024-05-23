class Reparacion:
    __patente: str
    __reparacion: str
    __repuesto: str
    __precioR: float
    __precioMO: float
    __estado: str
    def __init__(self, patente, reparacion, repuesto, precioR, precioMO, estado):
        self.__patente = patente
        self.__reparacion = reparacion
        self.__repuesto = repuesto
        self.__precioR = precioR
        self.__precioMO = precioMO
        self.__estado = estado
    def getPatente(self):
        return self.__patente
    def getReparacion(self):
        return self.__reparacion
    def getRepuesto(self):
        return self.__repuesto
    def getPrecioR(self):
        return self.__precioR
    def getPrecioMO(self):
        return self.__precioMO
    def getEstado(self):
        return self.__estado
    def calcularSubTotal(self):
        return self.__precioR + self.__precioMO