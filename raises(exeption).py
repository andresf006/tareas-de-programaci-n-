import unittest

def exepcion():
    return 123 / 0   # aquí hacemos una division q da como resultado 0

class TestExepcion(unittest.TestCase):
    def test_excepcion(self):
        with self.assertRaises(ZeroDivisionError):  # esperamos que esta excepción ocurra, usamos zeroDivisionError porque esperamos q la division de 0
            exepcion()  # al ejecutarse, lanza ZeroDivisionError y pasa a la exepcion 
            
            
if __name__ == '__main__':
    unittest.main()
