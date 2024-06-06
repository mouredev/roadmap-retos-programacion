"""
EJERCICIO:
Crea una funcion que se encargue de sumar dos numeros y retornar su 
resultado.

Crea un test, utilizando las herramientas de tu lenguaje, que sea 
capaz de determinar si esa funcion se ejecuta correctamente.

DIFICULTAD EXTRA (opcional):
Crea un diccionario con las siguientes claves y valores:
"name": "Tu nombre"
"age": "Tu edad"
"birth_date": "Tu fecha de nacimiento"
"programming_languages": ["Listado de lenguajes de
programacion"]

Crea dos test:
- Un primero que determine que existen todos los campos.
- Un segundo que determine que los datos introducios son correctos.

by adra-dev
"""

"""
Ejercicio
"""

"""
Test unitarios:

En programacion, las pruebas o test unitarios son una forma de 
comprobar el correcto funcionamiento de una unidad de codigo. Son 
pruebas que debe superar el codigo para verificar su correcto 
funcionamiento.

La instruccion assert permite llevar a cabo estas pruebas. Si el 
resultado de la condicion booleana es True, el resultado del test es
positivo, mientras que si es False, se generara un a excepcion 
AssertionError indicando cual es la prueba que ha fallado

"""

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b

resultado = sum(3, 4)
assert resultado == 7

resultado = sum(3, -4)
assert resultado == -1

# resultado = sum(-3,+4)
# assert resultado == 0


"""
Test unitarios con unittest:
El uso de assert para comprobar nuestro codigo no suele ser muy 
efficiente, pues el programa parara en cuanto una de las condiciones
no se satisfaga. Esto obliga a ir corrigiendo cada problema antes de 
continuar con el resto de comprobaciones. Existen soluciones mas 
sofisticadas para la elaboracion de pruebas de unidad. La biblioteca 
unittest ofrece utilidades para la construccion de pruebas de unidad
como la automatizacion, desactivacion y configuracion de test, entre 
otras funcionalidades.
"""
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)    


"""
EXTRA
"""
from datetime import datetime, date


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
                    "name": "Adrian Rodriguez",
                    "age": 26,
                    "birth_date": datetime.strptime("12-02-98", "%d-%m-%y").date(),
                    "programming_languages": ["Python", "Rust"],
                }


    def data_fields(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)
    
    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)

unittest.main()