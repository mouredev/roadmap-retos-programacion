'''
/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
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
'''
#Importamos la librería necesaria para hacer el test
import unittest

#Creamos la función suma 
def suma (numero1, numero2):
    return numero1 + numero2

#Creamos la clase de prueba que hereda de unittest.TestCase
class TestSuma(unittest.TestCase):
    #Definimos los métodos deben de empezar por "test_"
    def test_suma_positiva(self):
        numero1 = 3
        numero2 = 2

        resultado= suma(numero1,numero2)
        #Utilizamos afirmaciones (asertions) para verificar el valor esperado "5"
        self.assertEqual(resultado,5)


#Ejecutamos las pruebas
if __name__ == '__main__': #Verificamos si el script se está ejecutando como un programa principal
    unittest.main()


#Dificultad EXTRA

#Creamos el diccionario
alexdevrep = {
    "nombre": "Alejandro",
    "edad": "24",
    "Fecha de nacimiento": "22-07-1999",
    "Lenguajes de programación": ["Python","JavaScript","Java"]
}

#Creamos la función que nos comprueba las claves
def claves():
    claves_list =[]
    for clave in alexdevrep:
        claves_list.append(clave)
    return claves_list
    
#Creamos la función que nos devuelve los valores
def valor ():
    valor_list=[]
    for clave in alexdevrep:
        valor = alexdevrep[clave]
        valor_list.append(valor)
    return valor_list
    
#Creamos los test unitarios 
class Test(unittest.TestCase):
    def test_campos(self):
        claves_dict= claves()
        self.assertEqual(claves_dict,['nombre', 'edad', 'Fecha de nacimiento', 'Lenguajes de programación'])
        
        
    
    def test_datos(self):
        datos_dict=valor()
        self.assertEqual(datos_dict,['Alejandro', '24', '22-07-1999', ['Python', 'JavaScript', 'Java']])
        
#Ejecutamos los test
if __name__ == '__main__':
    unittest.main()

