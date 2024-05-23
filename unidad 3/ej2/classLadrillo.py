class Ladrillo:
    __id: int
    __alto: 7
    __ancho: 15
    __largo: 25
    __cantidad: int
    __kgMatPrima: float
    __costo: float
    __materiales: list
    def __init__(self, id, cantidad, kgMat, costo):
        self.__id = id
        self.__cantidad = cantidad
        self.__kgMatPrima = kgMat
        self.__costo = costo
        self.__materiales = []
    def getId(self):
        return self.__id
    def getCostoUnit(self):
        return self.__costo
    def addMaterial(self, xmat):
        exito = False
        if xmat not in self.__materiales:
            self.__materiales.append(xmat)
            exito = True
        return exito
    def actualizarCosto(self):
        for mat in self.__materiales:
            self.__costo += mat.getCostoAdicional()
        
    def getCostoTotal(self):
        return self.__costo * self.__cantidad
    def listarMateriales(self):
        if len(self.__materiales) > 0:
            for mat in self.__materiales:
                print(f"Material: {mat.getMaterial()} - Costo: {mat.getCostoAdicional()} - Caracteristicas: {mat.getCaracteristicas()}")
        else:
            print("Ladrillo tradicional")
    def getMateriales(self):
        ret = ""
        if len(self.__materiales) > 0:
            for mat in self.__materiales:
                ret += str(mat.getMaterial())
        return ret
    def getCostosAdicionales(self):
            ret=""
            if len(self.__materiales)>0:
                for mat in self.__materiales:
                    ret+=str(mat.getCostoAdicional())
            return ret