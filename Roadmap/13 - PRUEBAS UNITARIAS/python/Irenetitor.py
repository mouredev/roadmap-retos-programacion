from datetime import datetime, date
import unittest


#Exercise



def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("The arguments must be of type int or float.")
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 9), 8)
        self.assertEqual(add(2.6, 4.5), 7.1)
        self.assertEqual(add(6.4, 2), 8.4)

    def test_type_add(self):
        with self.assertRaises(TypeError):
            add("3", 7)
        with self.assertRaises(TypeError):
            add(5, "6")
        with self.assertRaises(TypeError):
            add("9", "8")



if __name__ == "__main__":
    unittest.main()

#Extra Exercise



class testUser_data(unittest.TestCase):
    def setUp(self) -> None:
        self.user_data = {
            "name": "Juan",
            "age": 29,
            "birth_date": datetime.strptime("23-02-1996", "%d-%m-%y").date(),
            "languages": ["Python", "JavaScript", "Java"]
        }

    def test_exist_fields(self):
        self.assertIn("name", self.user_data)
        self.assertIn("age", self.user_data)
        self.assertIn("birth_date", self.user_data)
        self.assertIn("languages", self.user_data)

    def test_user_gitdata_correct(self):
        self.assertIsInstance(self.user_data["name"], str)
        self.assertIsInstance(self.user_data["age"], int)
        self.assertIsInstance(self.user_data["birth_date"], date)
        self.assertIsInstance(self.user_data["languages"], list)


if __name__ == "__main__":
    unittest.main()