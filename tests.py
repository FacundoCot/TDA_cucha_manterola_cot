
import unittest
import analizar_rivales
import parsing

ARCH1 = "Archivos_ejemplos/3 elem.txt"
ARCH2 = "Archivos_ejemplos/10 elem.txt"
ARCH3 = "Archivos_ejemplos/100 elem.txt"
ARCH4 = "Archivos_ejemplos/10000 elem.txt"

ESP1 = 10
ESP2 = 29
ESP3 = 5223
ESP4 = 497886735


class TestRivales(unittest.TestCase):

    def test_caso_1(self):
        rivales = parsing.parsing(ARCH1)
        obtenido = analizar_rivales.tiempo_minimo(rivales)
        self.assertEqual(obtenido, ESP1)

    def test_caso_2(self):
        rivales = parsing.parsing(ARCH2)
        obtenido = analizar_rivales.tiempo_minimo(rivales)
        self.assertEqual(obtenido, ESP2)

    def test_caso_3(self):
        rivales = parsing.parsing(ARCH3)
        obtenido = analizar_rivales.tiempo_minimo(rivales)
        self.assertEqual(obtenido, ESP3)

    def test_caso_4(self):
        rivales = parsing.parsing(ARCH4)
        obtenido = analizar_rivales.tiempo_minimo(rivales)
        self.assertEqual(obtenido, ESP4)


if __name__ == "__main__":
    unittest.main()