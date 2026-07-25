#  * EJERCICIO:
#  * Crea una función que se encargue de sumar dos números y retornar
#  * su resultado.
#  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
#  * capaz de determinar si esa función se ejecuta correctamente.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un diccionario con las siguientes claves y valores:
#  * "name": "Tu nombre"
#  * "age": "Tu edad"
#  * "birth_date": "Tu fecha de nacimiento"
#  * "programming_languages": ["Listado de lenguajes de programación"]
#  * Crea dos test:
#  * - Un primero que determine que existen todos los campos.
#  * - Un segundo que determine que los datos introducidos son correctos.

# Creacion de la funcion que suma 
def sumar(a,b):
    return a+b

print(sumar(20,50))

import unittest

# Clase que corre los test para sumar
class TestSumar(unittest.TestCase):
    def test_suma_correcta(self):
        self.assertEqual(sumar(3,2),5) # Introduccion de la funcion sumar y el resultado esperado
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(0,0),0)


# DIFICULTAD EXTRA:

mi_dicc = {'name':'Julio',
           'age':'23',
           'birth_date':'04/02/2002',
           'programming_languajes':'Python'}

class Testdicc(unittest.TestCase):
    def test_todos_existen(self): # ---> Recordatorio importante: Todas las funciones deben llevar
        self.assertNotEqual(mi_dicc['name'],'') # "test_" en el nombre para que se ejecuten
        self.assertNotEqual(mi_dicc['age'],'')
        self.assertNotEqual(mi_dicc['birth_date'],'')
        self.assertNotEqual(mi_dicc['programming_languajes'],'')
    
    def test_todos_correctos(self):
        self.assertEqual(mi_dicc['name'],'Julio')
        self.assertEqual(mi_dicc['age'],'23')
        self.assertEqual(mi_dicc['birth_date'],'04/02/2002')
        self.assertEqual(mi_dicc['programming_languajes'],'Python')
        
if __name__ =="__main__":
    unittest.main()
