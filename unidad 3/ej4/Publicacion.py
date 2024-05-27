class Publicacion:
    __titulo: str
    __categoria: str
    __precioBase: float
    def __init__(self, titulo, categoria, precioBase):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precioBase = precioBase
    def __str__(self):
        return "Titulo: " + self.__titulo + "\nCategoria: " + self.__categoria + "\nPrecio Base: " + str(self.__precioBase)
    def getTitulo(self):
        return self.__titulo
    def getCateg(self):
        return self.__categoria
    def getPrecioBase(self):
        return self.__precioBase
    def getImporteVenta(self):
        pass