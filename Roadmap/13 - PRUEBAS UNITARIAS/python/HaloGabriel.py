import unittest

# EJERCICIO
# Crea una función que se encargue de sumar dos números y retornar
# su resultado.
# Crea un test, utilizando las herramientas de tu lenguaje, que sea
# capaz de determinar si esa función se ejecuta correctamente.

def sumar(num1: int, num2: int):
    if not isinstance(num1, (int, float)):
        raise ValueError(f'Error: {num1} no es un int o float.')
    if not isinstance(num2, (int, float)):
        raise ValueError(f'Error: {num2} no es un int o float.')
    return num1 + num2

class TestMaths(unittest.TestCase):

    def test_sumar_dos_enteros_positivos(self):
        suma = sumar(2, 3)
        self.assertEqual(suma, 5)

    def test_sumar_un_entero_negativo_y_un_entero_positivo(self):
        suma = sumar(-2, 3)
        self.assertEqual(suma, 1)

    def test_sumar_un_entero_positivo_y_un_entero_negativo(self):
        suma = sumar(2, -3)
        self.assertEqual(suma, -1)

    def test_sumar_dos_enteros_negativos(self):
        suma = sumar(-2, -3)
        self.assertEqual(suma, -5)

    def test_sumar_dos_decimales_positivos(self):
        suma = sumar(2.5, 3.5)
        self.assertEqual(suma, 6)

    def test_sumar_un_decimal_negativo_y_un_decimal_positivo(self):
        suma = sumar(-2.5, 3.5)
        self.assertEqual(suma, 1)

    def test_sumar_un_decimal_positivo_y_un_decimal_negativo(self):
        suma = sumar(2.5, -3.5)
        self.assertEqual(suma, -1)

    def test_sumar_dos_decimales_negativos(self):
        suma = sumar(-2.5, -3.5)
        self.assertEqual(suma, -6)

    def test_sumar_un_entero_positivo_y_un_decimal_positivo(self):
        suma = sumar(2, 3.5)
        self.assertEqual(suma, 5.5)

    def test_sumar_un_entero_negativo_y_un_decimal_positivo(self):
        suma = sumar(-2, 3.5)
        self.assertEqual(suma, 1.5)

    def test_sumar_un_entero_positivo_y_un_decimal_negativo(self):
        suma = sumar(2, -3.5)
        self.assertEqual(suma, -1.5)

    def test_sumar_un_entero_negativo_y_un_decimal_negativo(self):
        suma = sumar(-2, -3.5)
        self.assertEqual(suma, -5.5)

    def test_sumar_un_no_int_con_un_int(self):
        with self.assertRaises(ValueError):
            sumar("2", 3)

    def test_sumar_un_int_con_un_no_int(self):
        with self.assertRaises(ValueError):
            sumar(2, "3")

    def test_sumar_dos_no_int(self):
        with self.assertRaises(ValueError):
            sumar("2", "3")

# DIFICULTAD EXTRA (opcional):
# Crea un diccionario con las siguientes claves y valores:
# "name": "Tu nombre"
# "age": "Tu edad"
# "birth_date": "Tu fecha de nacimiento"
# "programming_languages": ["Listado de lenguajes de programación"]
# Crea dos test:
# - Un primero que determine que existen todos los campos.
# - Un segundo que determine que los datos introducidos son correctos.

data_dict = {
    'name': 'Gabriel',
    'age': 26,
    'birth_date': '19-09-2000',
    'programming_languages': ['Java', 'C#', 'Python']
}

class TestDictionaries(unittest.TestCase):

    def setUp(self): 
        self.data_dict = {
            'name': 'Gabriel',
            'age': 26,
            'birth_date': '19-09-2000',
            'programming_languages': ['Java', 'C#', 'Python']
        }

    def test_existen_campos_en_diccionario(self):
        self.assertIn('name', self.data_dict)
        self.assertIn('age', self.data_dict)
        self.assertIn('birth_date', self.data_dict)
        self.assertIn('programming_languages', self.data_dict)

    def test_valores_correctos_en_diccionario(self):
        self.assertEqual('Gabriel', data_dict['name'])
        self.assertEqual(26, data_dict['age'])
        self.assertEqual('19-09-2000', data_dict['birth_date'])
        self.assertEqual(['Java', 'C#', 'Python'], data_dict['programming_languages'])

unittest.main()