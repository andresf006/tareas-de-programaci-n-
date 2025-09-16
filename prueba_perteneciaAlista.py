import unittest

def lista_prueba_pares():
    return [2, 4, 6, 8, 10]

class TestListaPares(unittest.TestCase):
    def test_numero_en_lista(self):
        lista = lista_prueba_pares()
        self.assertIn(4, lista)   # pasa porque 4 sí está en la lista
        self.assertIn(5, lista)  # no pasa porq 5 no es par, no esta en la lista
       


if __name__ == '__main__':
    unittest.main() 
