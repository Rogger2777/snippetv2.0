import math
import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado


class PruebaEcuacionSegundoGrado(unittest.TestCase):

    def test_solucionESG_parametrosNoNumericos_lanzaException(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            ecuacionSegundoGrado.definirParametros("3.1", "5.2", "c")


    def test_solucionESG_parametrosNoNumericos_lanzaException_subTest(self):
        ecuacionSegundoGrado = EcuacionSegundoGrado()

        items = (
            {"Case": "Caso 01", "a": "a", "b":  "b", "c": "c"},
            {"Case": "Caso 02", "a": "a", "b": 1, "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "aa", "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "3,1", "c": 1},
        )

        for item in items:
            with self.subTest(item["Case"]):
                self.assertTrue(True)
                with self.assertRaises(ValueError):
                    ecuacionSegundoGrado.definirParametros(item["a"], item["b"], item["c"])
