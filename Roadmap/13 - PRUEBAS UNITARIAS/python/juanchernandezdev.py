### Python Unit Testing ###\
import unittest
  
def sum(num1, num2):
  return num1 + num2


class TestAddFunction(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(sum(5, 5), 10)
    self.assertEqual(sum(5, 3), 8)
    self.assertEqual(sum(2, 2), 4)
    self.assertEqual(sum(10, 45), 55)
    self.assertEqual(sum(5, -5), 0)

  def test_add_large_numbers(self):
    self.assertEqual(sum(45000, 20000), 65000)

    
#! Optional Challenge
my_info = {
  'name': 'John',
  'age': 37,
  'birth_date': '23/12/1986',
  'programming_languages': ['JavaScript', 'Python']
}

def get_info(info):
  return info

class TestMyInfoDict(unittest.TestCase):
  
  def test_dict_fields(self):
    fields = ['name', 'age', 'birth_date', 'programming_languages']
    result = get_info(my_info)
    
    for field in fields:
      self.assertTrue(field in result, f'Missing field: {field}')
      
  def test_dict_fields(self):
    values = ['John', 37, '23/12/1986', ['JavaScript', 'Python']]
    result = get_info(my_info)
    for value in values:
      self.assertTrue(value in result.values(), f'Value is not correct: {value}')
    
if __name__ == '__main__':
    unittest.main()
    