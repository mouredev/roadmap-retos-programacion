# -- exercise
def sum_numbers(a: int, b: int) -> int:
    return a + b


# -- extra challenge
class DataDict:
    def __init__(
        self,
        name: str,
        age: int,
        birth_date: str,
        programming_languages: list[str] = [],
    ) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

    def get_values_dict(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "birth_date": self.birth_date,
            "programming_languages": self.programming_languages,
        }


# -- test
"""
crate a file named tests.py and add the following code
run the tests by executing `python tests.py` or `python -m unittest tests.py`
"""
from main import sum_numbers, DataDict
import unittest


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(1, 2), 3)
        self.assertEqual(sum_numbers(2, 2), 4)
        self.assertEqual(sum_numbers(3, 3), 6)
        self.assertEqual(sum_numbers(4, 4), 8)
        self.assertEqual(sum_numbers(5, 5), 10)


class TestDataDict(unittest.TestCase):
    data = DataDict(
        name="qwik",
        age=22,
        birth_date="00/11/2002",
        programming_languages=["Python", "JavaScript", "TypeScript"],
    )

    def test_data_dict(self):
        self.assertEqual(
            self.data.get_values_dict(),
            {
                "name": "qwik",
                "age": 22,
                "birth_date": "00/11/2002",
                "programming_languages": ["Python", "JavaScript", "TypeScript"],
            },
        )

    def test_data_dict_values(self):
        self.assertEqual(self.data.name, "qwik")
        self.assertEqual(self.data.age, 22)
        self.assertEqual(self.data.birth_date, "00/11/2002")
        self.assertEqual(
            self.data.programming_languages, ["Python", "JavaScript", "TypeScript"]
        )


if __name__ == "__main__":
    unittest.main()
