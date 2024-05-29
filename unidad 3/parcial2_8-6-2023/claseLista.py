import csv
from Casa import Casa
from Departamento import Departamento
from claseNodo import Nodo


class Lista:
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
    def agregarInmuebleAlComienzo(self,inmu):
        nodo = Nodo(inmu)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo 
        self.__actual=nodo
        self.__tope+=1
    def insertarInmuebles(self):
        archi1 = open("deptos.csv")
        archi2 = open("casas.csv")
        reader1 = csv.reader(archi1, delimiter=";")
        reader2 = csv.reader(archi2, delimiter=";")
        band1 = True
        band2 = True
        for fila in reader1:
            if band1:
                band1 = False
            else:
                depto = Departamento(fila[0], fila[1], float(fila[2]), int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]))
                self.agregarInmuebleAlComienzo(depto)
        archi1.close()        
        for fila in reader2:
            if band2:
                band2 = False
            else:
                casa = Casa(fila[0], fila[1], float(fila[2]), float(fila[3]))
                self.agregarInmuebleAlComienzo(casa)
        archi2.close()

    def agregarAlFinal(self, inmu):
        nodo = Nodo(inmu)
        if self.__comienzo is None:
            # Si la lista está vacía, el nuevo nodo se convierte en el primer nodo.
            self.__comienzo = nodo
        else:
            # Si la lista no está vacía, recorre hasta el final.
            aux = self.__comienzo
            while aux is not None:
                anterior = aux
                aux = aux.getSiguiente()
            # Una vez que encuentra el final de la lista (aux es None), el nodo anterior se enlaza con el nuevo nodo.
            anterior.setSiguiente(nodo)
        # Actualiza el nodo actual al comienzo de la lista.
        self.__actual = self.__comienzo
        # Incrementa el contador de nodos en la lista.
        self.__tope += 1
        # Mensaje de confirmación.
        print("Agregado exitosamente!\n")
    def informeDeptos(self, xcant):
        band=False
        for inmu in self:
            if isinstance(inmu, Departamento):
                if inmu.get_cantH() < xcant:
                    print(f"""
                        Localidad: {inmu.getLocalidad()}
                        Direccion: {inmu.getDireccion()}
                        Sup cubierta: {inmu.getSupC()}
                        Monoblock: {inmu.get_nroM()}
                        Nro depto: {inmu.get_nroD()}
                        Piso: {inmu.get_piso()}
                        Importe de venta: {inmu.getImporteVenta()}\n""")
                    band=True
        if band is False:
            print(f"No existen deptos con menos de {xcant} habitaciones")
    def informeCasas(self):
        for inmu in self:
            if isinstance(inmu, Casa):
                print(f"""
                    Direccion: {inmu.getDireccion()}
                    Sup cubierta: {inmu.getSupC()}
                    Importe de venta: {inmu.getImporteVenta()}""")
       

