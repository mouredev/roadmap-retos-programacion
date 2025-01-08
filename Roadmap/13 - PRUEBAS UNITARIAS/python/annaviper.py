import pytest

"""EJERCICIO"""


def sum_two_numbers(num1: int, num2: int) -> int:
	if isinstance(num1, int) & isinstance(num2, int):
		return num1 + num2
	raise ValueError("Numbers have to be integers.")


class TestSum:
	@pytest.mark.parametrize("num1,num2,expected", [
		(0, 1, 1),
		(5, 5, 10),
		(3, -1, 2)
	])
	def test_sum_two_numbers(self, num1, num2, expected):
		assert sum_two_numbers(num1, num2) == expected

	def test_raises_value_error(self):
		with pytest.raises(ValueError):
			sum_two_numbers("", 3)


"""DIFICULTAD EXTRA"""

data = {
	'name': 'anna',
	'age': 36,
	'birth_date': "13 de octubre",
	'programming_languages': ['Python', 'Kotlin']
}


class TestDictionary:
	def test_all_keys_exist(self):
		# using set instead of list so the order doesn't matter
		keys = {'name', 'age', 'birth_date', 'programming_languages'}
		assert set(data.keys()) == keys

	def test_values_are_correct(self):
		values = ['anna', 36, '13 de octubre', ['Python', 'Kotlin']]
		assert list(data.values()) == values
