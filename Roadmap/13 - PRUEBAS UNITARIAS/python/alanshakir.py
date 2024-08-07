"""
/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */
"""
import unittest

def sumar_valores(valor_a, valor_b):
    return(valor_a + valor_b)

class TestPruebas(unittest.TestCase):
    def test_1(self):
        resultado = sumar_valores(3, 8)
        self.assertEqual(resultado, 11)
        

#Extra

my_dict = {"name": "alan ramirez",
           "age": 39,
           "birth_date": "20-01-1985",
           "programming_languages": ["Python", "Java", "C"]
}

class TestDict(unittest.TestCase):
    def test_all_values(self):
        self.assertIn("name", my_dict)
        self.assertIn("age", my_dict)
        self.assertIn("birth_date", my_dict)
        self.assertIn("programming_languages", my_dict)
    
    def test_is_corect(self):
        self.assertIsInstance(my_dict["name"], str)
        self.assertIsInstance(my_dict["age"], int)
        self.assertIsInstance(my_dict["birth_date"], str)
        self.assertIsInstance(my_dict["programming_languages"], list)

if __name__ == "__main__":
    unittest.main()
