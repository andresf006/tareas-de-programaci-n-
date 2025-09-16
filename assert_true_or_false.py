import unittest

def verdadero_o_falso():
    return True   # simplemente retornamos un True

class TestVerdaderooFalso(unittest.TestCase):
    def test_verdadero(self):
        self.assertTrue(verdadero_o_falso())   # pasa porq estamos  verificando q sea true

    def test_falso(self):
        self.assertFalse(not verdadero_o_falso())  # también debería pasar ya q esta negando el True 

if __name__ == "__main__":
    unittest.main()
