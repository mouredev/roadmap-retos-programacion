#13 - Pruebas unitarias
"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea capaz de determinar si esa función se ejecuta correctamente.
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
"""

def sum_numbers(num1:float, num2:float)-> float:

    total = num1 + num2
    return total

print(sum_numbers(1,2))

assert sum_numbers(7,0) == 7, f"sum is correct"
assert sum_numbers(7,13) == 20, f"sum is correct"
#assert sum_numbers(7,33) == 7, f"sum is NOT correct, the correct is: 40"

#EXTRA
dictPersonal = {"name": "Saul Saez",
                "age": 12,            
                "birth_date": "20/12/2013",
                "programming_languages": ["Python", "Golang", "VBA", "JavaScript"]              
                 }

countKeys = 0 

for key, value in dictPersonal.items():
    assert value != "", f"The key: {key} is empty."
    countKeys += 1

assert countKeys == 4, "Keys should be 4."
assert len(dictPersonal) == 4, "Keys should be 4."

assert type(dictPersonal["name"]) == str, f"Name should be a: str"
assert type(dictPersonal["age"]) == int, f"Age should be an: int"
assert type(dictPersonal["birth_date"]) == str, f"Birth_date should be a: str"
assert type(dictPersonal["programming_languages"]) == list, f"Programming_languages should be a: list"
