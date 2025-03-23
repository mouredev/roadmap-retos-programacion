"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""
import unittest

def sumar(a, b) ->int :
    if not isinstance(a,(int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los números deben ser enetros o decimales.")
    return a + b



class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(2,6), 8)
        self.assertEqual(sumar(-2,-5), -7)
        self.assertEqual(sumar(-2,5), 3)
        self.assertEqual(sumar(2.3,5), 7.3)
        self.assertEqual(sumar(2.5,2.5), 5)
        self.assertEqual(sumar(0,0), 0)

    def test_type_sum(self):
        with self.assertRaises(ValueError):
            sumar("3","2")
        with self.assertRaises(ValueError):
            sumar("2",2)
        with self.assertRaises(ValueError):
            sumar(3,"2")
        with self.assertRaises(ValueError):
            sumar("r",2)
        with self.assertRaises(ValueError):
            sumar(3,None)

if __name__ == "__main__":
    unittest.main()


