#13 PRUEBAS UNITARIAS
"""
/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "nombre": "Tu nombre"
 * "edad": "Tu edad"
 * "fecha_de_nacimiento": "Tu fecha de nacimiento"
 * "lenguajes_de_programacion": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */
"""
import unittest


# Función que suma dos números y devuelve el resultado
def suma_2(a: int, b: int) -> int:
    """
    Suma dos números y devuelve el resultado.
    """
    return a + b

# Clase de pruebas unitarias para la función suma_2
class TestSuma(unittest.TestCase):

    # Prueba para verificar la suma de números positivos
    def test_suma_positiva(self):
        """
        Prueba la suma de números positivos.
        """
        self.assertEqual(suma_2(5, 5), 10)

    # Prueba para verificar la suma de números positivos y negativos
    def test_sume_negativa(self):
        """
        Prueba la suma de un número positivo y otro negativo.
        """
        self.assertEqual(suma_2(-1, -5), -6)

# Función que crea un diccionario con información personal
def crear_diccionario(nombre, edad, fecha_nacimiento, lenguajes_de_programacion):
    """
    Crea un diccionario con información personal.
    """
    return {
        "nombre": nombre,
        "edad": edad,
        "fecha_de_nacimiento": fecha_nacimiento,
        "lenguajes_de_programacion": lenguajes_de_programacion
    }

# Clase de pruebas unitarias para la función crear_diccionario
class TestDatosPersonales(unittest.TestCase):

    # Prueba para verificar la existencia de todos los campos en el diccionario
    def test_existencia_campos(self):
        """
        Prueba la existencia de todos los campos en el diccionario.
        """
        datos = crear_diccionario("Santiago", 14, "2010-01-20", ["Python", "Arduino"])
        self.assertTrue("nombre" in datos)
        self.assertTrue("edad" in datos)
        self.assertTrue("fecha_de_nacimiento" in datos)
        self.assertTrue("lenguajes_de_programacion" in datos)

    # Prueba para verificar los tipos de datos de los campos en el diccionario
    def test_campos_correctos(self):
        """
        Prueba los tipos de datos de los campos en el diccionario.
        """
        datos = crear_diccionario("Santiago", 14, "2009-03-26", ["Python", "Arduino"])
        self.assertIsInstance(datos["nombre"], str)
        self.assertIsInstance(datos["edad"], int)
        self.assertIsInstance(datos["fecha_de_nacimiento"], str)
        self.assertIsInstance(datos["lenguajes_de_programacion"], list)
        # Aquí podrías validar también los tipos de datos dentro de la lista de lenguajes de programación

if __name__ == '__main__':
    unittest.main()