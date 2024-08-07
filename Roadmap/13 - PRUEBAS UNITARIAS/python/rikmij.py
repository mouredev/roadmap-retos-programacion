import unittest

def suma(n1, n2):
    return n1 + n2

class ProbarSuma(unittest.TestCase):
    def test_suma(self):
        prueba = suma(3, 7)
        self.assertEqual(prueba, 10)

# "\n", "*"*9, " EJERCICIO EXTRA ", "*"*9

dicc_presentarse = {"name":"Rick", "age":"26", "birth_date":"21/07/1997", "programming languages":["Python, Kotlin"]}

class TestDicc(unittest.TestCase):
    def test_all_fills(self):
        self.assertIn("Rick", dicc_presentarse["name"])
        self.assertIn("26", dicc_presentarse["age"])
        self.assertIn("21/07/1997", dicc_presentarse["birth_date"])
        self.assertIn("Python, Kotlin", dicc_presentarse["programming languages"])
    
    def test_correct_datas(self):
        self.assertIs(type(dicc_presentarse["name"]), str)
        self.assertIs(type(dicc_presentarse["age"]), str)
        self.assertIs(type(dicc_presentarse["birth_date"]), str)
        self.assertIs(type(dicc_presentarse["programming languages"]), list)


if __name__ == "__main__":
    unittest.main()
