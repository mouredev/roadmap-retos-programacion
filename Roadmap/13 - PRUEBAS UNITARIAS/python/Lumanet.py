import unittest 

def suma(a, b):
  return a + b

class TestSuma(unittest.TestCase): # Heredamos de unittest.TestCase para poder hacer las pruebas
  def test_suma(self): # Creamos un método que empiece por test para que sea detectado
    self.assertEqual(suma(5, 7), 12) # Comprobamos que 5 + 7 = 12
    self.assertEqual(suma(5, -7), -2)
    self.assertEqual(suma(0, 0), 0)
    self.assertEqual(suma(3.5, 2.1), 5.6)
    self.assertEqual(suma(2, 2.1), 4.1)
    self.assertEqual(suma(2.5, 2.5), 5)
    
# if __name__ == '__main__':
#     unittest.main()
    
"""
DIFICULTAD EXTRA (opcional):
Crea un diccionario con las siguientes claves y valores:
"name": "Tu nombre"
"age": "Tu edad"
"birth_date": "Tu fecha de nacimiento"
"programming_languages": ["Listado de lenguajes de programación"]
Crea dos test:
- Un primero que determine que existen todos los campos.
- Un segundo que determine que los datos introducidos son correctos.
"""
import unittest

usuario = {
    "name": "Marcos",
    "age": 42,
    "birth_date": "02-20-1982",
    "programming_languages": ["Python", "PHP", "CSS", "JavaScript"]
}    

class Tests(unittest.TestCase):
    def test_campos(self):
        self.assertEqual(True if usuario["name"] else False, True) # Si el campo name existe, devolverá True
        self.assertEqual(True if usuario["age"] else False, True)
        self.assertEqual(True if usuario["birth_date"] else False, True)
        self.assertEqual(True if usuario["programming_languages"] else False, True)
        
    def test_tipo(self):
        self.assertEqual(type(usuario["name"]), str) # Comprobamos que el tipo de dato es el correcto
        self.assertEqual(type(usuario["age"]), int)
        self.assertEqual(type(usuario["birth_date"]), str)
        self.assertEqual(type(usuario["programming_languages"]), list)

if __name__ == '__main__': # Si ejecutamos el script directamente, se ejecutarán las pruebas
    unittest.main() # Ejecutamos las pruebas
