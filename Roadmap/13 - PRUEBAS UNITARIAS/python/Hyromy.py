import unittest # libreria para test

def sumar(x, y):
    number = (int, float)
    if not isinstance(x, number) or not isinstance(y, number):
        raise TypeError("Los parametros deben ser numeros")

    return x + y

""" class Test(unittest.TestCase): # clase para pruebas
    def test_sum_int(self): # caso de prueba
        self.assertEqual(sumar(0, 0), 0) # prueba
        self.assertEqual(sumar(5, 6), 11) # otra prueba
        self.assertEqual(sumar(-7, 2), -5)
        self.assertEqual(sumar(6, -2), 4)
        self.assertEqual(sumar(-5, -7), -12)

    def test_sum_float(self): # otro caso de prueba
        self.assertEqual(sumar(4.3, 0.46), 4.76)
        self.assertEqual(sumar(346.0, 4), 350.0)
        self.assertEqual(sumar(43, 43.4), 86.4)

    #pruebas negativas
    def test_sum_negative(self):
        with self.assertRaises(TypeError): # esperando que la prueba falle
            sumar("7", 5)
        with self.assertRaises(TypeError):
            sumar(7, "5.7")
        with self.assertRaises(TypeError):
            sumar("a", "5.7")
 """
#unittest.main() # ejecutar las pruebas

# ---- DIFICULTAD EXTRA ----
diccionario = {
    "name": "Hyromy",
    "age": 19,
    "birth_date": "04/12/2004",
    "programming_languages": [
        "JavaScript",
        "Java",
        "PHP",
        "Python"
    ]
}

def check_keys(data:dict):
    keys = ["name", "age", "birth_date", "programming_languages"]
    for i in data:
        if i not in keys:
            raise KeyError(f"Clave {i} no existe")
    
def check_values(data:dict):
    if not isinstance(data["name"], str):
        raise ValueError("Valor de clave 'name' no valida")
    
    if not isinstance(data["age"], int):
        raise ValueError("Valor de clave 'age' no valida")

    date_data = data["birth_date"].split("/")
    try:
        for i in date_data:
            i = int(i)
            if not isinstance(i, int) or i < 0:
                raise ValueError("Valor de clave 'birth_date' no valida")
    except:
        raise ValueError("Valor de clave 'birth_date' no valida")

    for i in data["programming_languages"]:
        if not isinstance(i, str) or len(i) == 0:
            raise ValueError("Valor de clave 'programming_languages' no valida")

class Extra(unittest.TestCase):
    def test_check_keys_positive(self):
        self.assertEqual(check_keys(diccionario), None)

    def test_check_values_positive(self):
        self.assertEqual(check_values(diccionario), None)

    def test_check_keys_negative(self):
        with self.assertRaises(KeyError):
            check_keys({"hola":"xd"})

    def test_check_values_negative(self):
        with self.assertRaises(ValueError):
            data_test = diccionario.copy()
            data_test["birth_date"] = "20/may/2343"
            check_values(data_test)

unittest.main()