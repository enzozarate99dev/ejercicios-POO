import unittest 
from Casa import Casa
from Departamento import Departamento

class TestInmuebles(unittest.TestCase):
    def setUp(self):
        self.__depto = Departamento(localidad="Loc", direccion="Dir", supC=100, cantH=1, nroM=2, nroDm=3, piso=4)
        self.__casa = Casa(localidad="Loc", direccion="Dir", supC=200, supT=300)
    def test_precioConstDepto(self):
        self.assertEqual(self.__depto.getPrecioConstruccion(),1*17000)
    def test_precioConstCasa(self):
        self.assertEqual(self.__casa.getPrecioConstruccion(),300*1.8*20000)
    def test_importeVentaDepto(self):
        impEsperadoDepto = 100 * 15 * self.__depto.getPrecioConstruccion()
        self.assertEqual(self.__depto.getImporteVenta(), impEsperadoDepto)
    def test_importeVentaCasa(self):
        impEsperadoCasa = 200 * 15 * self.__casa.getPrecioConstruccion() 
        self.assertEqual(self.__casa.getImporteVenta(), impEsperadoCasa)

if __name__=='__main__':
    unittest.main()