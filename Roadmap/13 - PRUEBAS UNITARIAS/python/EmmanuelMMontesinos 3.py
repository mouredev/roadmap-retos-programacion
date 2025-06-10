"""/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 */"""

# Ejercico Base

def suma(a,b):
    return a + b

def test(funcion,resultado):
    if resultado == funcion:
        print("Suma: Correcto")
    else:
        print(f"Suma Error: {funcion} != {resultado}")
        
# Prueba
test(suma(2,2),4)
test(suma(2,2),5)

# Ejercicio Extra

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
"""

diccionario = {
    "name":"Emmanuel",
    "age" : 33,
    "birth_date" : "17/05/999",
    "programming_languages" : ["Python","Bash"]
    }

def test_campos(dic:dict):
    keys = list(dic.keys())
    campos = ["name","age","birth_date","programming_languages"]
    if keys == campos:
        print("Campos: Correcto")
        
    else:
        for n in range(len(campos)):
            if keys[n] != campos[n]:
                print(f"Error Campos: {keys[n]} != {campos[n]}")
        
def test_datos(dic:dict):
    values = list(dic.values())
    campos = ["Emmanuel",33,"17/05/999",["Python","Bash"]]
    if values == campos:
        print("Datos: Correcto")
        
    else:
        for n in range(len(campos)):
            if values[n] != campos[n]:
                print(f"Error Datos: {values[n]} != {campos[n]}")
    

# Pruebas
test_campos(diccionario)
test_datos(diccionario)