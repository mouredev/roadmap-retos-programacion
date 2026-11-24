import unittest

"""
UNIT TEST
"""


def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)

    def test_sum_all_asserts(self):
        # Equality
        self.assertEqual(sum(1, 2), 3)
        self.assertNotEqual(sum(1, 2), 99)

        # Truth
        self.assertTrue(sum(1, 1) == 2)
        self.assertFalse(sum(1, 1) == 99)

        # Identity
        result = sum(1, 2)
        self.assertIs(result, result)
        self.assertIsNot(result, sum(500, 500))  # large ints are not cached

        # None
        self.assertIsNone(None)
        self.assertIsNotNone(sum(1, 2))

        # Membership
        self.assertIn(sum(1, 2), [1, 2, 3])
        self.assertNotIn(sum(1, 2), [10, 20, 30])

        # Type
        self.assertIsInstance(sum(1, 2), int)
        self.assertNotIsInstance(sum(1, 2), str)

        # Comparison
        self.assertGreater(sum(5, 1), 5)
        self.assertGreaterEqual(sum(5, 0), 5)
        self.assertLess(sum(1, 1), 5)
        self.assertLessEqual(sum(1, 1), 2)

        # Approximate equality (floats)
        self.assertAlmostEqual(sum(0.1, 0.2), 0.3, places=1)
        self.assertNotAlmostEqual(sum(0.1, 0.2), 0.9, places=1)

        # Sequences and collections
        self.assertSequenceEqual([1, 2], [1, 2])
        self.assertListEqual([sum(1, 1)], [2])
        self.assertTupleEqual((sum(1, 2),), (3,))
        self.assertSetEqual({sum(1, 2)}, {3})
        self.assertDictEqual({"result": sum(1, 2)}, {"result": 3})

        # Multiline strings
        self.assertMultiLineEqual("a\nb", "a\nb")

        # Regex
        self.assertRegex(str(sum(1, 2)), r"\d+")
        self.assertNotRegex(str(sum(1, 2)), r"[a-z]")

        # Exceptions
        with self.assertRaises(ValueError):
            sum("a", 1)
        with self.assertRaisesRegex(ValueError, "enteros o decimales"):
            sum("a", 1)


"""
    EXTRA EXERCISE
"""

from datetime import date, datetime


class TestProfile(unittest.TestCase):
    def setUp(self):
        self.profile = {
            "name": "Sergio Cardo",
            "age": 35,
            "birth_date": datetime.strptime("1991-02-20", "%Y-%m-%d").date(),
            "programming_languages": ["Python", "C#", "PHP"],
        }

    def test_fields_exist(self):
        self.assertIn("name", self.profile)
        self.assertIn("age", self.profile)
        self.assertIn("birth_date", self.profile)
        self.assertIn("programming_languages", self.profile)

    def test_data_is_correct(self):
        self.assertIsInstance(self.profile["name"], str)
        self.assertGreater(len(self.profile["name"]), 0)
        self.assertIsInstance(self.profile["age"], int)
        self.assertGreater(self.profile["age"], 0)
        self.assertIsInstance(self.profile["birth_date"], date)
        self.assertLess(self.profile["birth_date"], date.today())
        self.assertIsInstance(self.profile["programming_languages"], list)
        self.assertGreater(len(self.profile["programming_languages"]), 0)


unittest.main()
