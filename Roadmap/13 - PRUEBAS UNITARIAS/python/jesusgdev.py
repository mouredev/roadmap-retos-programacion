'''
* EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
   su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
   capaz de determinar si esa función se ejecuta correctamente.
  
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
   - "name": "Tu nombre"
   - "age": "Tu edad"
   - "birth_date": "Tu fecha de nacimiento"
   - "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
   - Un primero que determine que existen todos los campos.
   - Un segundo que determine que los datos introducidos son correctos.
'''


import unittest  # 🧪 Módulo para hacer pruebas automáticas
from datetime import datetime, date  # 📆 Para manejar fechas de forma segura


# 📦 Diccionario con los datos personales
data = {
    "name": "Jesús García",
    "age": 41,
    "birth_date": "1984-03-25",
    "programming_languages": ["Python", "JavaScript", "Java"]
}


# ➕ Función que suma dos números y valida que sean correctos
def sum(a, b):
    # ⚠️ Verifica si ambos valores son números enteros o decimales
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    
    # ✅ Si todo está bien, retorna la suma
    return a + b


# 🧪 Clase de pruebas para la función sum
class TestSumar(unittest.TestCase):

    def test_sum(self):
        # ✅ Pruebas con valores válidos
        self.assertEqual(sum(2, 3), 5)           # 2 + 3 = 5
        self.assertEqual(sum(-1, -4), -5)        # -1 + (-4) = -5
        self.assertEqual(sum(-2, 5), 3)          # -2 + 5 = 3
        self.assertEqual(sum(2.5, 3.4), 5.9)     # 2.5 + 3.4 = 5.9

    def test_sum_types(self):
        # ❌ Pruebas con valores incorrectos: deben lanzar error
        with self.assertRaises(ValueError): sum("5", 4)
        with self.assertRaises(ValueError): sum(4, "5")
        with self.assertRaises(ValueError): sum("4", "5")
        with self.assertRaises(ValueError): sum(4, "a")
        with self.assertRaises(ValueError): sum(None, 5)

'''
Extra
'''

# ✅ Clase para comprobar la existencia de los campos y valores en nuestra data
class TestData(unittest.TestCase):

    # 🔧 Este método se ejecuta antes de cada test
    def setUp(self):
        self.data = {
            "name": "Jesús García",
            "age": 41,
            "birth_date": datetime.strptime("1984-03-25", "%Y-%m-%d").date(),
            "programming_languages": ["Python", "JavaScript", "Java"]
        }

    def test_if_data_field_exist(self):
        # 🔍 Verifica si cada campo existe en el diccionario
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_if_data_value_is_correct(self):
        # ✅ Verifica que cada campo tenga el tipo correcto
        self.assertIsInstance(self.data["name"], str)                # 👤 Nombre: texto
        self.assertIsInstance(self.data["age"], int)                 # 🔢 Edad: entero
        self.assertIsInstance(self.data["birth_date"], date)         # 📅 Fecha: tipo date
        self.assertIsInstance(self.data["programming_languages"], list)  # 💻 Lista de lenguajes


# ▶️ Ejecuta todas las pruebas cuando se ejecuta el archivo directamente
if __name__ == "__main__":
    unittest.main()

