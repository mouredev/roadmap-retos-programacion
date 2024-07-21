# --- 13-Pruebas Unitarias ---
# --- Javier Molina ---

# --- Pruebas Unitarias ---
import unittest
def suma(a: int, b: int):
    return a + b

class TestSuma(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(1, 1), 2)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(-4, 2), -2)

# --- Ejercicio Extra ---

data = {
    "name": "Javier",
    "age": 22,
    "birth_date": "2001-10-20",
    "programming_languages": ["Python, JavaScript"]
    }

class TestDictionary(unittest.TestCase):

    def test_dict_fields(self):
        self.assertIn("name", data)
        self.assertIn("age", data)
        self.assertIn("birth_date", data)
        self.assertIn("programming_languages", data)
        
    def test_dict_values(self):
        self.assertEqual(data["name"], "Javier")
        self.assertEqual(data["age"], 22)
        self.assertEqual(data["birth_date"], "2001-10-20")
        self.assertEqual(data["programming_languages"], ["Python, JavaScript"])
        
    
if __name__ == '__main__':
    unittest.main()