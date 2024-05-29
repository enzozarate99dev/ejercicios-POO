from Inmueble import Inmueble


class Departamento(Inmueble):
    __cantH: int
    __nroM: int
    __nroD: int
    __piso: int
    def __init__(self, localidad, direccion, supC, cantH, nroM, nroDm, piso):
        super().__init__(localidad, direccion, supC)
        self.__cantH = cantH
        self.__nroM = nroM
        self.__nroD = nroDm
        self.__piso = piso
    def __str__(self):
        return super().__str__() + f"Cant habitaciones: {self.__cantH} - "  + f"Nro monoblock: {self.__nroM} - " + f"Nro depto: {self.__nroD} - " + f"Piso: {self.__piso} - "
    def get_cantH(self):
        return self.__cantH
    def get_nroM(self):
        return self.__nroM
    def get_nroD(self):
        return self.__nroD
    def get_piso(self):
        return self.__piso
    def getPrecioConstruccion(self):
        return self.get_cantH() * 17000