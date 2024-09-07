"""* EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""
#Librería para testing
import  unittest
from datetime import datetime, date 

#Función a testear
def sumar(a , b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Se recibe algo que no es entero o decimal')
    return a + b 

class TestSumar(unittest.TestCase): #Clase obligatoria para que se ejecuten los test
    #Para crear una función de test, debemos crear una función en la que su nombre debe comenzar por test
    def test_sumar(self):        
        self.assertEqual(sumar(5, 5), 10) #Función assert para testing y pruebas        
        self.assertEqual(sumar(4, 5), 9)
        self.assertEqual(sumar(-5, -5), -10)
        
    def test_sumar_tipos(self):        
        with self.assertRaises(ValueError): # Test para el tipado de los argumentos
            sumar("2", 5)
        
        with self.assertRaises(ValueError):
            sumar(2, "5")
        
        with self.assertRaises(ValueError):
            sumar("2", "5")

#EXTRA

class TestDatos(unittest.TestCase):
    
    def setUp(self): #Función perteneciente a la clase unittest que permite almacenar valores para usarlos posteriomente en los tests
        self.datos = {
            'name':'Juan Jesús Tenreiro Rodríguez',
            'age': 56,
            'birth_date':datetime.strptime("01-05-1968", "%d-%m-%Y").date(),
            'programming_languajes':['Python', 'Java', 'JavaScript', 'PHP', 'Cobol']
        }  
    
    def test_existe_todos_los_campos(self):
        self.assertIn('name', self.datos)
        self.assertIn('age', self.datos)
        self.assertIn('birth_date', self.datos)
        self.assertIn('programming_languajes', self.datos)
        
    def test_datos_correctos(self):
        self.assertIsInstance(self.datos['name'], str)
        self.assertIsInstance(self.datos['age'], int)
        self.assertIsInstance(self.datos['birth_date'], date)
        self.assertIsInstance(self.datos['programming_languajes'], list)
        
unittest.main() #ejecuta todos los test_ 