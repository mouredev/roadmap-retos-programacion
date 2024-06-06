import os, unittest
os.system('cls')
#os.system('clear')
from datetime import date
"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
"""


def sum_two_numbers(num1:int,num2:int)->int:
    return num1+num2
print(sum_two_numbers(15,85))

class TestSum(unittest.TestCase):
    def test_positive_sum(self):
        self.assertEqual(sum_two_numbers(3, 9), 12) # Verifica si la suma de 3 y 5 es igual a 8

    def test_negative_sum(self):
        self.assertFalse(sum_two_numbers(-1, 1), 0) #En la mayoría de los casos se puede usar indistintamente asserEqual o assertTrue
# pero en este caso concreto al ser cero el resultado propuesto para la operación dará fallo y habrá que testearlo con assertEqual o assertFalse

    def test_float_sum(self):
        self.assertTrue(sum_two_numbers(2.5,7.3),9.8)
    
    def test_type_int_return(self):
        self.assertEqual(type(sum_two_numbers(0,0)), int)#Tambien se puede testear si el tipo de dato que devuelve es el correcto
    
    def test_type_float_return(self):
        self.assertEqual(type(sum_two_numbers(0.0,0.0)), float)
    

# if __name__ == '__main__': 
#     unittest.main() #Con este condicional ejecutamos los test anteriores al mismo y termina la ejecución de todo el programa

""" * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos."""
print(type(date(1974,12,26)))

my_personal_dict = {
   "name": "Jesus",
   "age": 49,
   "birth_date": date(1974,12,26),
   "programming_languages": ["Python", "Java", "Javascript"]
}

def check_values(dict:dict):
    my_list = []
    [my_list.append(v) for v in dict.values()]
    return my_list


class TestDict(unittest.TestCase):
    def test_exist_items(self):
        self.assertTrue(len(my_personal_dict),4)

    def test_type_values(self):
        self.assertEqual(type(check_values(my_personal_dict)), list)
        self.assertEqual(type(check_values(my_personal_dict)[0]), str)
        self.assertEqual(type(check_values(my_personal_dict)[1]), int)
        self.assertEqual(type(check_values(my_personal_dict)[2]), date)
        self.assertEqual(type(check_values(my_personal_dict)[3]), list)
        self.assertEqual(type(check_values(my_personal_dict)[3][0]), str)
        self.assertEqual(type(check_values(my_personal_dict)[3][1]), str)
        self.assertEqual(type(check_values(my_personal_dict)[3][2]), str)
         

if __name__ == '__main__':
    unittest.main()
























# class TestEjemplos(unittest.TestCase):
#     def setUp(self):
#         print("Entra setUp")
#     def tearDown(self):
#         print("Entra tearDown")

#     def test_1(self):
#         print("Test: test_1")
#     def test_2(self):
#         print("Test: test_2")
# if __name__ == '__main__':
#     unittest.main()
