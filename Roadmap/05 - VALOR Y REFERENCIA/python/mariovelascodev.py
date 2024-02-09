
#Paso por valor
num1 = 6
num2 = num1 #En la variable num2 se crea una copia del valor de la variable num1
num2 *= 5 #Modificamos solo el valor de la variable num2
print(num1)
print(num2)

#Paso por referencia
lista1 = [23, 42, 56]
lista2 = lista1 #En la variable lista2 se comparte la misma referencia de memoria del objeto de lista1
lista2.pop() #Al eliminar un valor de lista2 tambien se borra de lista1 ya que tienen la misma referencia de memoria
print(lista1)
print(lista2)


#Ejemplos de funciones con variables
numero = 12
numero_flotante = 3.8
cadena = "Hola Mundo"
lista = [2, 5, "texto"]
conjunto = set([5, 6, 7, 8])
diccionario = {
    "id": 1,
    "nombre": "Mario",
    "alias": "mariovelascodev"
}

def entrada(arg):
    arg = "¡Python mola!"
    print(f"Valor de la variable dentro de la función: {arg}")

def entrada1(arg):
    arg.pop()
    print(f"Valor de la variable dentro de la función: {arg}")

def entrada2(arg):
    arg.popitem()
    print(f"Valor de la variable dentro de la función: {arg}")    

print("----PASO POR VALOR----\n")
print("El paso por valor crea una copia local de la variable, \nlo que implica que cualquier modificación sobre la misma\nno tenga efecto sobre la original.\n")
print(f"Valor de la variable \"numero\" fuera de la función: {numero}")
entrada(numero)
print(f"Valor de la variable \"numero\" fuera de la función: {numero}")
print("\n")

print(f"Valor de la variable \"numero_flotante\" fuera de la función: {numero_flotante}")
entrada(numero_flotante)
print(f"Valor de la variable \"numero_flotante\" fuera de la función: {numero_flotante}")
print("\n")

print(f"Valor de la variable \"cadena\" fuera de la función: {cadena}")
entrada(cadena)
print(f"Valor de la variable \"cadena\" fuera de la función: {cadena}")


print("\n----PASO POR REFERENCIA----\n")
print("El paso por referencia, actua directamente sobre la variable pasada,\npor lo que las modificaciones afectarán a la variable original.\n")
print(f"Valor de la variable \"lista\" fuera de la función: {lista}")
entrada1(lista)
print(f"Valor de la variable \"lista\" fuera de la función: {lista}")
print("\n")

print(f"Valor de la variable \"conjunto\" fuera de la función: {conjunto}")
entrada1(conjunto)
print(f"Valor de la variable \"conjunto\" fuera de la función: {conjunto}")
print("\n")

print(f"Valor de la variable \"diccionario\" fuera de la función: {diccionario}")
entrada2(diccionario)
print(f"Valor de la variable \"diccionario\" fuera de la función: {diccionario}")
print("\n")

print("\n----EXTRA----\n")

a = 5
b = "Python"

def intercambio_valor(param1, param2):
    #Intercambio el valor de las dos variables entre ellas, creando una variable para almacenar el valor del param1 para poder darselo a param2
    valor_temporal = param1
    param1 = param2
    param2 = valor_temporal

    #Retorno el valor de los parámetros
    return param1, param2

#Añadimos a las nuevas variables el valor retornado de la función
nuevo_a, nuevo_b = intercambio_valor(a, b)

print("PASO POR VALOR\n")
print(f"Valor de la variable a: {a}")
print(f"Valor de la variable b: {b}")
print(f"Valor de la variable nuevo_a: {nuevo_a}")
print(f"Valor de la variable nuevo_b: {nuevo_b}")

#Comprobamos que no modificamos las variables originales
nuevo_a = "JS"
nuevo_b += 8
print(f"Valor de la variable nuevo_a: {nuevo_a}")
print(f"Valor de la variable nuevo_b: {nuevo_b}")
print(f"Valor de la variable a: {a}")
print(f"Valor de la variable b: {b}")

lista_numeros = [1, 30, 256]
lista_string = ["Python", "Hola mundo", "Mario"]
def intercambio_referencia(param1, param2):
    #Creamos una copia de las lista de los dos parámetros, para no afectar a las listas originales
    copia_param1 = param1.copy()
    copia_param2 = param2.copy()
    #Intercambio el valor de los parámetros con las copias de lista
    param1 = copia_param2
    param2 = copia_param1

    #Retorno el valor de los parámetros
    return param1, param2

#Añadimos a las nuevas variables el valor retornado de la función
nueva_lista_numeros, nueva_lista_string = intercambio_referencia(lista_numeros, lista_string)

#Comprobamos que no modificamos las variables originales
nueva_lista_numeros.append(255)
nueva_lista_string.pop()

print("\nPASO POR REFERENCIA\n")
print(f"Valor de la variable lista_numeros: {lista_numeros}")
print(f"Valor de la variable lista_string: {lista_string}")
print(f"Valor de la variable nueva_lista_numeros: {nueva_lista_numeros}")
print(f"Valor de la variable nueva_lista_string: {nueva_lista_string}")
print(f"Valor de la variable lista_numeros: {lista_numeros}")
print(f"Valor de la variable lista_string: {lista_string}")
