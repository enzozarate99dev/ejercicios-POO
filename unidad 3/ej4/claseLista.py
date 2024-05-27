import csv
from AudioLibro import Audiolibro
from Libro import Libro
from claseNodo import Nodo


class ListaPublicaciones:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo = None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def getTope(self):
        return self.__tope
    def agregarPublicacion(self,publicacion):
        nodo = Nodo(publicacion)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual=nodo
        self.__tope+=1
    def cargarPublicaciones(self):
        band1 = False
        archi1 = open("librosimpresos.csv")
        reader1 = csv.reader(archi1, delimiter=";")
        for fila in reader1:
            if band1 == False:
                band1 = True
            else:
                titulo = fila[0]
                categoria = fila[1]
                precioBase = float(fila[2])
                autor = fila[3]
                fechaE = fila[4]
                cantPaginas = int(fila[5])
                libro = Libro(titulo, categoria, precioBase, autor, fechaE, cantPaginas)
                self.agregarPublicacion(libro)
        archi1.close()
        band2 = False
        archi2 = open("audiolibros.csv")
        reader2 = csv.reader(archi2, delimiter=";")
        for fila in reader2:
            if band2 == False:
                band2 = True
            else:
                titulo = fila[0]
                categoria = fila[1]
                precioBase = float(fila[2])
                tiempoR = int(fila[3])
                narrador = fila[4]
                audiolibro = Audiolibro(titulo, categoria, precioBase, tiempoR, narrador)
                self.agregarPublicacion(audiolibro)
        archi2.close()
    def listarDatosPubli(self):
        aux = self.__comienzo
        while aux!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()
    
    def mostrarTipoPublicacion(self, pos):
        ret = 0
        if pos < self.getTope():
            aux = self.__comienzo
            for i in range(pos):
                aux = aux.getSiguiente()
            if isinstance(aux.getDato(), Libro):
                ret = 1
            elif isinstance(aux.getDato(), Audiolibro):
                ret = 2
        else:
            print("Posicion fuera del rango")
        return ret
    def mostrarCantDeTipos(self):
        cantL=0
        cantA=0
        aux = self.__comienzo
        while aux is not None:
            publi = aux.getDato()
            if isinstance(publi, Libro):
                cantL+=1
            elif isinstance(publi, Audiolibro):
                cantA+=1
            aux = aux.getSiguiente()
        print(f"Cantidad de Libros: {cantL}")
        print(f"Cantidad de Audiolibros: {cantA}")
   
    def informeVentas(self):
        for publi in self:
            print(f"Titulo: {publi.getTitulo()}")
            print(f"Categoria: {publi.getCateg()}")
            print(f"Importe de Venta: {publi.getImporteVenta()}\n")
        
