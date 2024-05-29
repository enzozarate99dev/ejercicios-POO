from Inmueble import Inmueble


class Casa(Inmueble):
    __supTerreno: float
    def __init__(self, localidad, direccion, supC, supT):
        super().__init__(localidad, direccion, supC)
        self.__supTerreno = supT
    def __str__(self):
        return super().__str__() + f"Superficie terreno: {self.__supTerreno}" 
    def getSupT(self):
        return self.__supTerreno
    def getPrecioConstruccion(self):
        return self.getSupT() * 1.8 * 20000