import unittest
"""Ejercicio"""

#Pruebas de test con pytest

def suma(a,b):
    return a+b

def test_suma ():
    assert suma(10,10) == 20
    assert suma(5,-10) == -5

#Pruebas de test con unitest

def rest (x,y):
    return x-y

class Testrest(unittest.TestCase):
    def test_rest(self):
        self.assertEqual(rest(2, 3), -1)

if __name__ == '__main__':
    unittest.main()

"""Extra"""

my_dict = {
    'name' : "Angel",
    'age' : 20,
    'birth_date' : "19-07-2006",
    'lenguages' : ["c#", "python"]
}



class Test_values (unittest.TestCase):

    def test_keys(self):
        keys= {'name', 'age','birth_date', 'lenguages'}
        self.assertEqual(set(my_dict.keys()), keys)
    def test_type (self):
        self.assertIsInstance(my_dict.get('age'), int)
        self.assertIsInstance(my_dict.get('name'), str)
        self.assertIsInstance(my_dict.get('birth_date'), str)
        self.assertIsInstance(my_dict.get('lenguages'), list)
    def test_value(self):
        self.assertEqual(my_dict.get('name') ,"Angel")
        self.assertEqual(my_dict.get('age') ,20)
        self.assertEqual(my_dict.get('birth_date'), "19-07-2006")
        self.assertCountEqual(my_dict.get('lenguages'),["c#", "python"])
        



if __name__ == '__main__':
    unittest.main()