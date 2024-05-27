from Publicacion import Publicacion


class Audiolibro(Publicacion):
    __tiempoR: int
    __narrador: str
    def __init__(self, titulo, categoria, precioBase, tiempoR, narrador):
        super().__init__(titulo, categoria, precioBase)
        self.__tiempoR = tiempoR
        self.__narrador = narrador
    def __str__(self):
        return super().__str__() + "\nTiempo de reproduccion: " + str(self.__tiempoR) + "\nNarrador: " + str(self.__narrador)
    def getImporteVenta(self):
        imp = self.getPrecioBase() + self.getPrecioBase()*0.1
        return imp