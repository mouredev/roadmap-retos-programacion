import unittest
"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""

def add(n1, n2):
    if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
        raise TypeError("Args must be integer or float numbers")
    return n1 + n2


class TestAddMethod(unittest.TestCase):
    def test_postivite(self):
        self.assertEqual(add(10, 2), 12)
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(5, -3), 2)

    
    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, 3), -2)

    def test_str(self):
        with self.assertRaises(TypeError):
            add("5", 2)
        with self.assertRaises(TypeError):
            add(5, "2")
        with self.assertRaises(TypeError):
            add("5", "2")

# if __name__ == "__main__":
#     unittest.main()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""

info = dict(name="duban", age=25, birth_date="unknown", 
            programming_languages=["Python", "Java"])


class TestDictValues(unittest.TestCase):

    def setUp(self):
        """
        Setting before each proof.
        Create the dictionary 'info' with the proof data
        """

        self.info = dict(
            name="duban",
            age=25,
            birth_date="unknown",
            programming_languages=["Python", "Java"]
        )

    def tearDown(self):
        """
        Clean after each proof.
        Reset the dictionary (optional in this case but util that we need release space)
        """
        self.info = None
    

    def test_keys_required(self):
        """
        Verify that dictionary info contain the required keys
        """
        keys_required = {"name", "age", "birth_date", "programming_languages"}
        self.assertTrue(keys_required.issubset(self.info.keys()))

    def test_data_types(self):
        """
        Verify that dictionary values are correct 
        """
        self.assertIsInstance(self.info["name"], str, "The name must be string")
        self.assertIsInstance(self.info["age"], int, "The age must be integer")
        self.assertIsInstance(self.info["birth_date"], str, "The birth date must be string")
        self.assertIsInstance(self.info["programming_languages"], list, "The programming languages must be list")

    def test_programming_languages_noempty(self):
        """
        Verify that list is not empty
        """
        self.assertGreater(len(self.info["programming_languages"]), 0, "The programming languages" +
                        "list must contain values")
        
    def test_programming_lang_content(self):
        """
        Verify the content of programming languages list
        """
        for language in self.info["programming_languages"]:
            self.assertIsInstance(language, str, f"The language {language} is not string")

    def test_data_correct(self):
        """
        Verify that each dictionary values are correct 
        """
        self.assertEqual(self.info["name"], "duban", "The name is not correct")
        self.assertEqual(self.info["age"], 25, "The age is not correct")
        self.assertEqual(self.info["birth_date"], "unknown", "The birth date is not correct")
        self.assertEqual(self.info["programming_languages"], ["Python", "Java"], 
                        "The programming languages are not correct")


if __name__ == "__main__":
    unittest.main()