import unittest

def sumar(num1, num2):
  return num1 + num2

class TestSum(unittest.TestCase):
  def test_1(self):
    resultado = sumar(1, 2)
    self.assertEqual(resultado, 3)

# DIFICULTAD EXTRA

user = {
    "name": "Chape",
    "age": 27,
    "birth_date": "1997-06-02",
    "programming_languages": ["js", "ts", "py"]
}

class TestDict(unittest.TestCase):
    def test_check_all_keys(self):
        self.assertIn("name", user)
        self.assertIn("age", user)
        self.assertIn("birth_date", user)
        self.assertIn("programming_languages", user)
    
    def test_check_values(self):
        self.assertEqual(user["name"], "Andres")
        self.assertEqual(user["age"], 27)
        self.assertEqual(user["birth_date"], "1997-06-02",)
        self.assertEqual(user["programming_languages"], ["js", "ts", "py"])


if __name__ == '__main__':
    unittest.main()

