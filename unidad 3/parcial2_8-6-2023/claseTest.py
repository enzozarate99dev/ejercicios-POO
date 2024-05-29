import unittest 
from Casa import Casa
from Departamento import Departamento

class TestInmuebles(unittest.TestCase):
    def test_importeVenta(self):
        depto = Departamento(localidad="Loc", direccion="Dir", supC=100, cantH=1, nroM=2, nroDm=3, piso=4)
        casa = Casa(localidad="Loc", direccion="Dir", supC=200, supT=300)

        precioConstDepto = 1*17000
        precioConstCasa = 300*1.8*20000

        impEsperadoDepto = 100 * 15 * precioConstDepto
        impEsperadoCasa = 200 * 15 * precioConstCasa 
        
        self.assertEqual(depto.getImporteVenta(), impEsperadoDepto)
        self.assertEqual(casa.getImporteVenta(), impEsperadoCasa)