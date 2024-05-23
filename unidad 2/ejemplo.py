import numpy as np
from math import sqrt

"""class Punto:
    __x: int
    __y: int
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    def __str__(self):
        return '({}, {})'.format(self.__x, self.__y)
    def setX(self, v):
        self.__x = v
    def getX(self):
        return self.__x
    def setY(self, v):
        self.__y = v
    def getY(self):
        return self.__y
    def mostrarDatos(self):
        print("(x,y) = (",self.__x,',', self.__y,")")
    def mover(self, x, y):
        self.setX(x)
        self.setY(y)
    def distanciaEuclidea(self, otroPunto):
        distancia = sqrt((otroPunto.__x-self.__x)**2+(otroPunto.__y-self.__y)**2)
        return distancia


class arregloNumPy:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __puntos: np.ndarray
    def __init__(self, dimension, incremento=5):
        self.__puntos = np.empty(dimension, dtype=Punto)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarPunto(self, unPunto):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__puntos.resize(self.__dimension)
        self.__puntos[self.__cantidad]=unPunto
        self.__cantidad += 1
    def getUnPunto(self, indice):
        return self.__puntos[indice]
    def mostrarPuntos(self):
        for i in range(self.__cantidad):
            self.__puntos[i].mostrarDatos()
    def calcularDistanciasP0(self, unPunto):
        for i in range(self.__cantidad):
            distancia = unPunto.distanciaEuclidea(self.__puntos[i])
            print('Distancia del punto {} al punto {} es {}'.format(unPunto, self.__puntos[i], distancia))


    def testArregloPuntos(self):
        p1 = Punto(4, 5)
        p2 = Punto(3, 4)
        p3 = Punto(-9, 5)
        p4 = Punto(3, 2)
        p5 = Punto(1, 7)
        self.agregarPunto(p1)
        self.agregarPunto(p2)
        self.agregarPunto(p3)
        self.agregarPunto(p4)
        self.agregarPunto(p5)

if __name__ == '__main__':
    arregloPuntos = arregloNumPy(3,10)
    arregloPuntos.testArregloPuntos()
    punto0 = arregloPuntos.getUnPunto(0)
    arregloPuntos.calcularDistanciasP0(punto0)
    arregloPuntos.mostrarPuntos() """

class CuentaCorriente:
    __cuil: str
    __nombreYApellido: str
    __saldo: float
    def __init__(self, cuil, nya, saldo):
        self.__cuil = cuil
        self.__nombreYApellido = nya
        self.__saldo = saldo 

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")
    def transferir(self, other, monto):
        if self.__saldo >= monto:
            self.retirar(monto)	
            other.depositar(monto)
        else:
            print("Saldo insuficiente para realizar la transferencia")
    
    def __lt__(self, other):
        return self.__saldo < other.__saldo
     
    

class arregloNumPy:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __cuentas: np.ndarray
    def __init__(self, dimension, incremento=5):
        self.__cuentas = np.empty(dimension, dtype=CuentaCorriente)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarCuenta(self, unaCta):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__cuentas.resize(self.__dimension)
        self.__cuentas[self.__cantidad]=unaCta
        self.__cantidad += 1
    
    def ordenar(self):
        self.__cuentas = np.sort(self.__cuentas)

    def test(self):
        cuenta1 = CuentaCorriente('20-41774509-3', 'Enzo Zarate', 55000)
        cuenta2 = CuentaCorriente('20-12345678-3', 'Juan Perez', 1500)
        cuenta3 = CuentaCorriente('27-12345679-5', 'Maria Martinez', 8000)
        self.agregarCuenta(cuenta1)
        self.agregarCuenta(cuenta2)
        self.agregarCuenta(cuenta3)
        cuenta1.transferir(cuenta2, 2000)


if __name__ == '__main__':
    arrayCtas = arregloNumPy(3)
    arrayCtas.test()
    arrayCtas.ordenar()