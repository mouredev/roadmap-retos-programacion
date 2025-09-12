# 13 - PRUEBAS UNITARIAS
import unittest
from datetime import datetime as dt
# SooHav.py
# python -m unittest -v tests

# Ejercicio


def suma(a: float, b: float) -> float:
    return a + b


resultado1 = suma(3, 4)
resultado2 = suma(3.5, 4.5)
resultado3 = suma(3, 4.5)

print(resultado1)
print(resultado2)
print(resultado3)

# Forma simple de testear
assert (suma(3, 4) == 7.0)
assert (suma(3.5, 4.5) == 8.0)
assert (suma(3, 4.5) == 7.5)


class TestSuma(unittest.TestCase):

    def test_suma_enteros(self):
        # Verifica que la suma de 1 y 2 sea igual a 3
        self.assertEqual(suma(1, 2), 3.0)
        # Verifica que la suma de -1 y 1 sea igual a 0
        self.assertEqual(suma(-1, 1), 0.0)
        # Verifica que la suma de 0 y 0 sea igual a 0
        self.assertEqual(suma(0, 0), 0.0)

    def test_suma_decimales(self):
        # Verifica que la suma de 1.5 y 2.5 sea igual a 4.0
        self.assertAlmostEqual(suma(1.5, 2.5), 4.0)
        self.assertAlmostEqual(suma(-1.5, 1.5), 0.0)


# Difiicultad Extra
def crear_diccionario(nombre, edad, fecha_nacimiento, lenguajes):
    info = {
        "nombre": nombre,
        "edad": edad,
        "fecha_nacimiento": fecha_nacimiento,
        "lenguajes": lenguajes
    }
    return info


info = crear_diccionario("Sofia", 46, "26-02-1978", ["Python", "R"])
print(info)


class TestCrearDiccionario(unittest.TestCase):

    def test_crear_diccionario(self):
        nombre = "Sofia"
        edad = 46
        fecha_nacimiento = "26-02-1978"
        lenguajes = ["Python", "R"]
        info = crear_diccionario(nombre, edad, fecha_nacimiento, lenguajes)
        # Verifica que el resultado es un diccionario
        self.assertIsInstance(info, dict)

    def test_existencia_campos(self):
        nombre = "Sofia"
        edad = 46
        fecha_nacimiento = "26-02-1978"
        lenguajes = ["Python", "R"]
        info = crear_diccionario(nombre, edad, fecha_nacimiento, lenguajes)
        # Verifica que 'nombre' está presente en el diccionario
        self.assertIn("nombre", info)
        self.assertIn("edad", info)
        self.assertIn("fecha_nacimiento", info)
        self.assertIn("lenguajes", info)

    def test_datos_correctos(self):
        nombre = "Sofia"
        edad = 46
        fecha_nacimiento = "26-02-1978"
        lenguajes = ["Python", "R"]
        info = crear_diccionario(nombre, edad, fecha_nacimiento, lenguajes)
        self.assertIsInstance(info["nombre"], str)
        self.assertIsInstance(info["edad"], int)
        self.assertIsInstance(dt.strptime(
            info["fecha_nacimiento"], "%d-%m-%Y"), dt)
        self.assertIsInstance(info["lenguajes"], list)


# Ejecucion de pruebas
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
