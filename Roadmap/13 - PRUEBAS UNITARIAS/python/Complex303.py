"""
Pruebas Unitarias
"""
# Pruebas unitarias: Son pruebas que se aplican a funciones o métodos individuales de un programa para verificar que funcionan correctamente de manera aislada.

import unittest  # Librería estándar de Python para pruebas unitarias.
from datetime import datetime, date # Importamos datetime y date para trabajar con fechas


def sumar(a, b):
    # Verificamos que ambos argumentos sean números (int o float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser números")
    # Retornamos la suma de a y b
    return a + b

# Definimos una clase de prueba que hereda de unittest.TestCase
# Esta clase contendrá nuestros métodos de prueba 
# nota:  En unittest, cualquier método dentro de una clase que herede de unittest.TestCase será reconocido como un test solo si su nombre comienza con test_. Si no usa ese prefijo, unittest lo ignorará y no lo ejecutará.
class TestSum(unittest.TestCase):

        def test_sum(self):
            # Comprobamos que sumar(5,4) devuelve 9
            self.assertEqual(sumar(5, 4), 9)
            # Otros casos de prueba con diferentes combinaciones
            self.assertEqual(sumar(-2, 1), -1)
            self.assertEqual(sumar(0, 0), 0)
            self.assertEqual(sumar(-1, -1), -2)
            self.assertEqual(sumar(1.5, 2.5), 4.0)
            self.assertEqual(sumar(1, -1), 0)

            
        # Comprobamos que la función devuelve un error si los argumentos no son números
        # En este caso, usamos assertRaises para verificar que se lanza una excepción ValueError
        def test_sum_invalid(self):
            # Verificamos que si se pasan valores inválidos, se lance ValueError
            with self.assertRaises(ValueError):
                sumar("5", 3)
            with self.assertRaises(ValueError):
                sumar(5, "3")
            with self.assertRaises(ValueError):
                sumar("5", "3")
            with self.assertRaises(ValueError):
                sumar(None, 3)
            with self.assertRaises(ValueError):
                sumar(5, None)
            with self.assertRaises(ValueError):
                sumar(None, None)
            with self.assertRaises(ValueError):
                sumar("a", 3)
            with self.assertRaises(ValueError): 
                sumar(5, "b")
#Se usa assertEqual para comparar resultados y assertRaises para validar excepciones esperadas.

#Esto permite que los tests solo se ejecuten cuando el script se corre directamente y no si se importa desde otro archivo.            
# if __name__ == '__main__':
#     unittest.main()




"""* DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos."""





# Creamos una clase de prueba que hereda de unittest.TestCase
class TestData(unittest.TestCase):

    # Este método se ejecuta antes de cada test, para preparar datos comunes
    def setUp(self): 
        # Creamos un diccionario con datos ficticios de ejemplo
        self.data = {
            "name": "Complex303",  # Cadena
            "age": 2,  # Entero
            # Convertimos la cadena "01-01-16" a objeto date usando strptime y date()
            "birth_date": datetime.strptime("01-01-16", "%d-%m-%y").date(),
            # Lista de lenguajes de programación
            "programming_languages": ["Python", "Java", "C#"]
        }
        
    # Primer test: verifica que las claves existan en el diccionario
    def test_fields_exist(self):
        self.assertIn("name", self.data)  # Verifica que "name" exista en self.data
        self.assertIn("age", self.data)   # Verifica que "age" exista en self.data
        self.assertIn("birth_date", self.data)  # Verifica que "birth_date" exista
        self.assertIn("programming_languages", self.data)  # Verifica que "programming_languages" exista

    # Segundo test: valida que cada valor tenga el tipo de dato correcto
    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)  # Que "name" sea cadena
        self.assertIsInstance(self.data["age"], int)  # Que "age" sea entero
        self.assertIsInstance(self.data["birth_date"], date)  # Que "birth_date" sea un objeto date
        self.assertIsInstance(self.data["programming_languages"], list)  # Que "programming_languages" sea lista


unittest.main()


# setUp(self): se ejecuta antes de cada test. Aquí inicializas los datos de prueba.

# assertIn(clave, diccionario): verifica que la clave exista en el diccionario.

# assertIsInstance(valor, tipo): verifica que el valor sea de un tipo específico.

# unittest.main(): ejecuta todos los métodos que comienzan con test_.