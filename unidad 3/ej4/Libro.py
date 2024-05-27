from datetime import datetime
from Publicacion import Publicacion


class Libro(Publicacion):
    __autor: str
    __fechaE: str
    __cantPaginas: int
    def __init__(self, titulo, categoria, precioBase, autor, fechaE, cantPaginas):
        super().__init__(titulo, categoria, precioBase)
        self.__autor = autor
        self.__fechaE = fechaE
        self.__cantPaginas = cantPaginas
    def __str__(self):
        return super().__str__() + "\nAutor: " + self.__autor + "\nFecha de edicion: " + self.__fechaE + "\nCantidad de paginas: " + str(self.__cantPaginas) + "\n"
    def getImporteVenta(self):
        anoEd = int(self.__fechaE.split('-')[0])
        anoAct = datetime.now().year
        imp = self.getPrecioBase() - self.getPrecioBase() * (0.01 * (anoAct - anoEd))
        return imp
       
