# 13 Unit Tests
import doctest


def sum(num_1: int, num_2: int) -> int:
    # """
    # Doctest
    # >>> sum(1,2)
    # 3
    # """

    # Check types
    if not isinstance(num_1, int | float) or not isinstance(num_2, int | float):
        raise ValueError("Params must be int or float")

    return num_1 + num_2

# Run doctest
# doctest.testmod()

# Using unittest
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        expected_result = 7
        result = sum(3,4)

        self.assertEqual(expected_result, result)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("1", "2")

# Run unnittest
