import unittest

def suma():  # función bajo prueba
    return 4 + 6 #retorna 10 

class TestSumaFunction(unittest.TestCase): # clase de prueba
    def test_suma(self):  # método de prueba
        self.assertEqual(suma(), 10)  # ahora sí llamamos a la función

if __name__ == "__main__":
    unittest.main()
