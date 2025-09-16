import unittest
def numero_prueba():
    return 18

class TestNumeroPrueba(unittest.TestCase):
    def test_numero_prueba(self):
        self.assertIsInstance(18, float) #miramos q 18 no es float, por lo tanto el test falla


if __name__ == '__main__':
    unittest.main() 
