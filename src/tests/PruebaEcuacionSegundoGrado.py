import math
import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado


class PruebaEcuacionSegundoGrado(unittest.TestCase):

    def test_solucionESG_parametrosNumericos_raicesReales(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        parametroA = 3
        parametroB = -5
        parametroC = 1

        RaizEsperada1 = "1.43"
        RaizEsperada2 = "0.23"

        # Do
        ecuacionSegundoGrado.definirParametros(parametroA, parametroB, parametroC)
        RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

        # Assert
        self.assertEqual(RaizEsperada1, RaizActual1)
        self.assertEqual(RaizEsperada2, RaizActual2)


    def test_solucionESG_parametrosNoNumericos_lanzaException(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            ecuacionSegundoGrado.definirParametros("3.1", "5.2", "c")

