"""	
13 - PRUEBAS UNITARIAS
Autor de la solución: Oriaj3	
Teoría:	
Las pruebas unitarias son una técnica de programación que consiste en crear
pequeños fragmentos de código que verifican el correcto funcionamiento de
otro fragmento de código. Estos fragmentos de código se conocen como tests.

Las pruebas unitarias son una parte fundamental de la metodología de
desarrollo ágil, ya que permiten detectar errores de forma temprana y
asegurar que los cambios realizados en el código no afecten su funcionamiento.

En la mayoría de los lenguajes de programación, existen herramientas y
bibliotecas que facilitan la creación y ejecución de pruebas unitarias.
Estas herramientas permiten definir los tests, ejecutarlos y verificar
que el código se comporta como se espera.

En Python, una de las bibliotecas más utilizadas para realizar pruebas
unitarias es unittest. Esta biblioteca proporciona una serie de clases
y métodos que permiten crear y ejecutar tests de forma sencilla.
"""
import unittest
from datetime import datetime, date

"""
/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
"""
def sumar2(a: int, b: int) -> int:
    """
    Suma dos números y devuelve el resultado.
    """
    return a + b

# Clase de pruebas unitarias para la función sumar2
class TestSumar(unittest.TestCase):
    
        # Prueba para verificar la suma de números positivos
        def test_suma_positiva(self):
            """
            Prueba la suma de números positivos.
            """
            self.assertEqual(sumar2(5, 5), 10)
    
        # Prueba para verificar la suma de números positivos y negativos
        def test_sume_negativa(self):
            """
            Prueba la suma de un número positivo y otro negativo.
            """
            self.assertEqual(sumar2(-1, -5), -6)
            
        # Prueba para verficiar la suma de un número positivo y otro negativo
        def test_suma_positiva_negativa(self):
            """
            Prueba la suma de un número positivo y otro negativo.
            """
            self.assertEqual(sumar2(5, -5), 0)
        
        # Prueba para verificar la suma de 0 con 0 
        
        
""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */
"""

# Diccionario con los datos personales
datos_personales = {
    "name": "Jairo",
    "age": 24,
    "birth_date": datetime.strptime("01-03-93", "%d-%m-%y").date(),
    "programming_languages": ["Python", "Java", "C++"],
}

# Clase de pruebas unitarias para los datos personales
class TestDatosPersonales(unittest.TestCase):
    #Prueba para verificar que existen todos los campos
    def test_campos(self):
        """
        Prueba que existen todos los campos en el diccionario.
        """
        self.assertIn("name", datos_personales)
        self.assertIn("age", datos_personales)
        self.assertIn("birth_date", datos_personales)
        self.assertIn("programming_languages", datos_personales)
    
    def test_datos_correctos(self):
        """
        Prueba que los datos introducidos son correctos.
        """
        self.assertIsInstance(datos_personales["name"], str)
        self.assertIsInstance(datos_personales["age"], int)
        self.assertIsInstance(datos_personales["birth_date"], date)
        self.assertIsInstance(datos_personales["programming_languages"], list)
        for language in datos_personales["programming_languages"]:
            self.assertIsInstance(language, str)
        
# Ejecutar las pruebas unitarias
if __name__ == '__main__':
    unittest.main()