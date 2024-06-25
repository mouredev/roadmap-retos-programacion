###############################################################################
## EJERCICIO
###############################################################################
import unittest


def add(x:int, y:int) ->int:
    return x + y


class tests(unittest.TestCase):
    def test_add(self):
        result = add(3,2)
        self.assertEqual(result, 5)
    def test_add2(self):
        result = add(3,3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
    


###############################################################################
## DIFICULTAD EXTRA
###############################################################################
import unittest

dictionary = {
    "name": "Daniel San",
    "age": 35,
    "birth_date": "04-04-1989",
    "programming_languages": ["Python", "SQL", "CSS", "JavaScript"]
}
       

class Tests(unittest.TestCase):
    def test_every_field(self):
        self.assertEqual(True if dictionary["name"] else False, True)
        self.assertEqual(True if dictionary["age"] else False, True)
        self.assertEqual(True if dictionary["birth_date"] else False, True)
        self.assertEqual(True if dictionary["programming_languages"] else False, True)
        
    def test_type_field(self):
        self.assertEqual(type(dictionary["name"]), str)
        self.assertEqual(type(dictionary["age"]), int)
        self.assertEqual(type(dictionary["birth_date"]), str)
        self.assertEqual(type(dictionary["programming_languages"]), list)


if __name__ == '__main__':
    unittest.main()
