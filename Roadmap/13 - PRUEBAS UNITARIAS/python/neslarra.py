"""
 Crea una función que se encargue de sumar dos números y retornar
 su resultado.
 Crea un test, utilizando las herramientas de tu lenguaje, que sea
 capaz de determinar si esa función se ejecuta correctamente.

 DIFICULTAD EXTRA (opcional):
 Crea un diccionario con las siguientes claves y valores:
 "name": "Tu nombre"
 "age": "Tu edad"
 "birth_date": "Tu fecha de nacimiento"
 "programming_languages": ["Listado de lenguajes de programación"]
 Crea dos test:
 - Un primero que determine que existen todos los campos.
 - Un segundo que determine que los datos introducidos son correctos.
"""

print(f"== Explicación {'=' * 30}\n")

print(f"""
import unittest
from datetime import datetime

# Creo una función sumar que suma dos números PERO devuelve "raise" si alguna de las entradas NO es numérica.
def sumar(num1, num2):
    if not all([bool(x.__class__.__name__ in ('int', 'float')) for x in (num1, num2)]):
        raise ValueError("Todos los argumentos deben ser numéricos.")
    return num1 + num2

# Creo una clase TestSumar ("Test" DEBE ser el prefijo) la cual hereda de unitest.TestCase
class TestSumar(unittest.TestCase):

    # Creo una función que realice los test que deben salir OK ("test_" DEBE ser el prefijo).
    def test_sumar_returns(self):
        self.assertEqual(sumar(1, 1), 2)
        self.assertEqual(sumar(1, -1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(1.5, 0.5), 2)
        self.assertEqual(sumar(1, -1.5), -0.5)

    # Creo una función que realice los test que salen por "raise" ("test_" DEBE ser el prefijo).
    def test_sumar_raises(self):
        with self.assertRaises(ValueError):
            sumar("a", 1)
        with self.assertRaises(ValueError):
            sumar("1", 1)
        with self.assertRaises(ValueError):
            sumar("1", "1")
        with self.assertRaises(ValueError):
            sumar("", 1)

# Ejecuto unitest.main() que automáticamente correrá todas los tests declaradas.
if __name__ == '__main__':
    unittest.main()

# Devuelve
Ran 2 tests in 0.009s

OK

Si alguno de los test no ejecutara OK, entonces devolvería AssertionError indicando cuál falló.

""")

print(f"== Dificultad Extra {'=' * 30}\n")

import unittest
from datetime import datetime

mi_data = {"nombre": "neslarra", "edad": 59, "fecha_nacimiento": datetime(1965, 3, 23), "lenguajes": ["python", "sql", "bash"]}


class TestMiData(unittest.TestCase):

    def test_keys(self):
        claves = mi_data.keys()
        self.assertTrue("nombre" in claves)
        self.assertTrue("edad" in claves)
        self.assertTrue("fecha_nacimiento" in claves)
        self.assertTrue("lenguajes" in claves)

    def test_values_type(self):
        self.assertIsInstance(mi_data["nombre"], str)
        self.assertIsInstance(mi_data["edad"], int)
        self.assertIsInstance(mi_data["fecha_nacimiento"], datetime)
        self.assertIsInstance(mi_data["lenguajes"], list)

# Ejecuto unitest.main() que automáticamente correrá todas los tests declaradas.
if __name__ == '__main__':
    unittest.main()
