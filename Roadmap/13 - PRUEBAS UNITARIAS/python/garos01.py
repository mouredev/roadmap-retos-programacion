import unittest


def suma(a, b):

    return a + b


class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-5, -3), -8)


if __name__ == "__main__":
    unittest.main()

# Ejercicio ectra


datos_personales = {
    "name": "Oscar Garzon",
    "age": 29,
    "birth_date": "11-09-1994",
    "programming_languages": ["Python", "JavaScript"],
}


class TestDatosPersonales(unittest.TestCase):
    def test_campos_existen(self):
        self.assertIn("name", datos_personales)
        self.assertIn("age", datos_personales)
        self.assertIn("birth_date", datos_personales)
        self.assertIn("programming_languages", datos_personales)

    def test_datos_correctos(self):
        self.assertIsInstance(datos_personales["name"], str)
        self.assertIsInstance(datos_personales["age"], int)
        self.assertIsInstance(datos_personales["birth_date"], str)
        self.assertIsInstance(datos_personales["programming_languages"], list)
        for lang in datos_personales["programming_languages"]:
            self.assertIsInstance(lang, str)


if __name__ == "__main__":
    unittest.main()
