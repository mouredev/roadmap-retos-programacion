import unittest

# ------ Ejercicio

def sum(a: int, b: int) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números enteros o decimales")    
    
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(3, 4), 7)
        self.assertEqual(sum(-3, 4), 1)
        self.assertEqual(sum(3, -4), -1)
        self.assertEqual(sum(8.9, 12.1), 21)
        self.assertEqual(sum(15, 91.9), 106.9)
        self.assertEqual(sum(-8, -12), -20)


    def test_sum_type(self):
        with self.assertRaises(TypeError):
            sum("2", 6)

        with self.assertRaises(TypeError):
            sum(2, "6")

        with self.assertRaises(TypeError):
            sum(None, 6)

        with self.assertRaises(TypeError):
            sum(6, None)

        with self.assertRaises(TypeError):
            sum([], ())


# ------ Extra

my_dict = {
    "name": "Yair Cañas",
    "age": 24,
    "birth_date": "03/01/2000",
    "programming_languages": ["Python", "C", "C++", "Java", "Matlab"]
}


class TestDict(unittest.TestCase):

    def test_keys(self):
        self.assertIn("name", my_dict)
        self.assertIn("age", my_dict)
        self.assertIn("birth_date", my_dict)
        self.assertIn("programming_languages", my_dict)


    def test_values(self):
        self.assertIsInstance(my_dict["name"], str)
        self.assertIsInstance(my_dict["age"], int)
        self.assertIsInstance(my_dict["birth_date"], str)
        self.assertIsInstance(my_dict["programming_languages"], list)


unittest.main()
