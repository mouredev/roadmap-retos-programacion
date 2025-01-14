# Asignación por valor
number: int = 10
second_number = number
print(f"La variable original number vale {number}")
print(f"La variable por valor second_number vale {second_number}")

# Ahora le incrementamos 1 a second_number
second_number += 1
print(f"El valor de second_number ahoora es {second_number}")
print(f"y la variable original number vale {number}")


# Asignación por referencia
number_list = [1, 2, 3, 4, 5]
second_number_list = number_list
print(f"La lista original number_list es: {number_list}")
print(f"La segunda lista por referencia second_number_list es: {second_number_list}")
# Agregaamos un elmento a la segunda lista
second_number_list.append(6)
# Ahora revisamos ambas listas
print("Ahora revisamos ambas listas")
print(f"La lista original number_list es: {number_list}")
print(f"La segunda lista por referencia second_number_list es: {second_number_list}")


def per_value(number: int):
    print(f"El valor del parametro original es: {number}")
    number = 15
    print("Modificamos el parametro original asignando 15")
    print(f"El valor modificado del parametro original ahora es: {number}")


def per_reference(list_numbers: list):
    print(f"El valor del parametro original es: {list_numbers}")
    list_numbers.append(15)
    print("Modificamos el parametro original agregando 15 a la lista")
    print(f"El valor modificado del parametro original ahora es: {list_numbers}")
    print("Ahora creamos una nueva lista por referecia")
    other_list_numbers = list_numbers
    other_list_numbers.append(16)
    print("Agregamos el elmeento 16 a la nueva lista y vemos las 2 listas")
    print(f"El valor del parametro original es: {list_numbers}")
    print(f"El valor de la nueva lista es: {other_list_numbers}")


# Extra
def parameters_per_value(number_one: int, number_two: int) -> tuple:
    temporal_number = number_two
    number_two = number_one
    number_one = temporal_number

    return number_one, number_two


def parameters_per_reference(list_one: list, list_two: list) -> tuple:
    temporal_list = list_two
    list_two = list_one
    list_one = temporal_list

    return list_one, list_two


if __name__ == "__main__":
    per_value(12)
    per_reference([10, 11, 12, 13, 14])
    number = 16
    other_number = 12
    number_x, number_y = parameters_per_value(number, other_number)
    print("parametros por vaor")
    print(f"Los argumentos originales son: {number}, {other_number}")
    print(f"Las variables son: {number_x}, {number_y}")
    one_list = [16, 17, 18, 19, 20]
    other_list = [12, 13, 14, 15]
    list_x, list_y = parameters_per_reference(one_list, other_list)
    print("Parametros por referencia")
    print(f"Los argumentos originales son: {one_list}, {other_list}")
    print(f"Las variables son: {list_x}, {list_y}")
