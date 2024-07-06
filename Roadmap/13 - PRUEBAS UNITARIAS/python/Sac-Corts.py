### Ejercicio ###
import unittest

def sumar(a, b):
    return a + b

class TestSumar(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

#unittest.main()

### Ejercicio Extra ###

data = {
    "name" : "Isaac Cortés",
    "age" : 22,
    "birth_date" : 21/10/2001,
    "programming_languages" : ["Python", "JavaScript", "Java"]
}

class TestData(unittest.TestCase):

    def test_field(self):
        self.assertIn("name", data)
        self.assertIn("age", data)
        self.assertIn("birth_date", data)
        self.assertIn("programming_languages", data)

    def test_correct_data(self):
        self.assertEqual(data["name"], "Isaac Cortés")
        self.assertEqual(data["age"], 22)
        self.assertEqual(data["birth_date"], 21/10/2001)
        self.assertListEqual(data["programming_languages"], ["Python", "JavaScript", "Java"])

unittest.main()


