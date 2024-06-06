# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * PRUEBAS UNITARIAS
# -----------------------------------
# - Verifican que las unidades individuales de código (como 
#   funciones, métodos o clases) funcionen como se espera.
# - Mas info: https://ellibrodepython.com/python-testing

#____________________________________
# * EJERCICIO #1
"""
* Crea una función que se encargue de sumar dos números y retornar
  su resultado.
* Crea un test, utilizando las herramientas de tu lenguaje, que sea
  capaz de determinar si esa función se ejecuta correctamente.
"""

import unittest

def sum(a: float, b: float) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return (a + b)
    else:
        return(None)
    
class TestSum(unittest.TestCase):
    def test_sum_correct(self):
        self.assertEqual(sum(5, 2), 7)
        self.assertEqual(sum(2.50, 1.25), 3.75)
        self.assertEqual(sum(-2, 1), -1)
        self.assertEqual(sum(0, 0), 0)

    def test_sum_isNone(self):
        self.assertIsNone(sum(1, "2"))
        self.assertIsNone(sum("a", "b"))

    def test_sum_incorrect(self):
        self.assertNotEqual(sum(1, 3), 5)

    def test_sum_error_handling(self):
        with self.assertRaises(TypeError):
            sum(10)

#____________________________________
# * EJERCICIO #2
"""
* Crea un diccionario con las siguientes claves y valores:
  - "name": "Tu nombre"
  - "age": "Tu edad"
  - "birth_date": "Tu fecha de nacimiento"
  - "programming_languages": ["Listado de lenguajes de programación"]
* Crea dos test:
  - Un primero que determine que existen todos los campos.
  - Un segundo que determine que los datos introducidos son correctos.
"""    

dict_user = {
    "name": "Ken",
    "age": 121,
    "birth_date": "1903-03-19",
    "prog_langs": ["cs", "py", "vb", "rs", "js"]
}

class TestDict(unittest.TestCase):
    def test_dic_key_existence(self):
        self.assertIn("name", dict_user)
        self.assertIn("age", dict_user)
        self.assertIn("birth_date", dict_user)
        self.assertIn("prog_langs", dict_user)
    
    def test_dic_value_types(self):
        self.assertIsInstance(dict_user["name"], str)
        self.assertIsInstance(dict_user["age"], int)
        self.assertIsInstance(dict_user["birth_date"], str)
        self.assertIsInstance(dict_user["prog_langs"], list)

    def test_dic_value_content(self):
        self.assertEqual(dict_user["name"], "Ken")
        self.assertEqual(dict_user["age"], 121)
        self.assertEqual(dict_user["birth_date"], "1903-03-19")
        self.assertListEqual(
            dict_user["prog_langs"], 
            ["cs", "py", "vb", "rs", "js"]
        )
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

