import unittest  #importamos la libreria unittest
 
def division ():
    return 1/3 #hacemos una division inexacta

class TestAlmostequal(unittest.TestCase):  #llamamos a la clase unittest.TestCase
    def testalmostequal(self):             #definimos el metodo testalmostequal
        self.assertAlmostEqual(division(),0.333, places = 3) #comprobamos que la division es casi igual a 0.333 con 3 decimales 
 
if __name__ == '__main__':  
    unittest.main() 
