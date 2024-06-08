import unittest

data = {
    "name": "Diego",
    "age": "28",
    "birth_date": "10-03-1996",
    "programming_language": "Python",
}


def add(number1: float, number2: float):
    return number1 + number2


class TestAdd(unittest.TestCase):
    def test_suma(self):
        number1 = 2
        number2 = 3

        result = number1 + number2

        self.assertEqual(result, 5)


class TestData(unittest.TestCase):
    def test_fields(self):

        keys = data.keys()

        self.assertFalse("name" not in keys)
        self.assertFalse("age" not in keys)
        self.assertFalse("birth_date" not in keys)
        self.assertFalse("programming_language" not in keys)

    def test_data(self):
        self.assertEqual(data["name"], "Diego")
        self.assertEqual(data["age"], "28")
        self.assertEqual(data["birth_date"], "10-03-1996")
        self.assertEqual(data["programming_language"], "Python")


if __name__ == '__main__':
    unittest.main()
