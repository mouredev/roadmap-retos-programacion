def sum(a, b):
    return a + b

data = {
    'name': 'Diego',
    'age': 28,
    'birth_day': '1996-11-08',
    'programming_languages': ['Python', 'Javascript', 'Swift']
}

import unittest
from idiegorojas import sum

'''
    * unittest.TestCase: Es la clase base para crear pruebas. Cada método que comienza con test_ es una prueba individual.
    * self.assertEqual: Es un método que verifica si dos valores son iguales. Si no lo son, la prueba falla.
    * unittest.main(): Ejecuta todas las pruebas definidas en la clase.
'''


class TestSumar(unittest.TestCase):
    def test_sumar_numeros_positivos(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum(0, 0), 0)

    def test_sumar_tipo(self):
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


if __name__ == '__main__':
    unittest.main()


# Extra

import unittest
from idiegorojas import data

class TestDict(unittest.TestCase):

    def test_existe_campos(self):
        campos_requerido = ['name', 'age', 'birth_day', 'programming_languages']
        for field in campos_requerido:
            self.assertIn(field, data)
    
    def test_tipo_dato_correcto(self):
        self.assertIsInstance(data['name'], str)
        self.assertIsInstance(data['age'], int)
        self.assertIsInstance(data['birth_day'], str)
        self.assertIsInstance(data['programming_languages'], list)

    def test_valores_correctos(self):
        self.assertEqual(data['name'], 'Diego')
        self.assertEqual(data['age'], 28)
        self.assertEqual(data['birth_day'], '1996-11-08')
        self.assertIn('Python', data['programming_languages'])
        self.assertIn('Javascript', data['programming_languages'])
        self.assertIn('Swift', data['programming_languages'])


if __name__ =='__main__':
    unittest.main()