import unittest

class TestIdentidad(unittest.TestCase):
    def test_misma_referencia(self): #aca decimos q a y b son igules en memoria, no solo en contenido
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)  # apuntan al mismo objeto en memoria, a es b

    def test_distinta_referencia(self): #aca decimos q a y b son distintos en memoria, aunque tengan el mismo contenido
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertIsNot(a, b)  #aunque tienen mismo contenido, NO son el mismo objeto, a no es b

if __name__ == "__main__":
    unittest.main()
