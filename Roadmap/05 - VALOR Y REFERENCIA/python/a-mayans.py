""" 
Paso por valor: Se crea una copia local de la variable dentro de la función. 
Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro de la función le afectarán también fuera. 
"""

# Ejemplo de asignacion de variables: Por valor( tipos primitivos: int, float, boolean, strings y tuplas -> son inmutables )
value1 = 27
value2 = value1 # asignacion por valor
print(value2)
# modificacion de la variable
value2 = 13

print(value1) # la variable 'value1' no se ve afectada
print(value2) # la variable 'value2' tiene un valor diferente


# Ejemplo de asignacion de variables: Por referencia ( de estructuras: listas, sets, diccionarios -> son mutables )
lista1 = [14,18,21]
lista2 = lista1 # asignacion por variable
print(lista1)
print(lista2)
# modificacion de la variable
lista2[2] = 20

print(lista1) # como ambas variables apuntan a la misma direccion en memoria, las dos se ven afectadas
print(lista2)


# Funcion con paso por Valor
def modificar_valor(value):
    value = 27 * 3
    print(f'Valor dentro de la funcion: {value}')

# Ejemplo con un entero ( tipo primitivo )
value = 5
modificar_valor(value)
print(f'Fuera de la función: {value}')

# Funcion con paso por Referencia
def modificar_lista(lista):
    lista[0] = 13
    print(f'Dentro de la funcion: {lista}')

# Ejemplo con una lista ( objeto mutable )
lista3 = [1, 2, 3]
modificar_lista(lista3)
print(f'Fuera de la función: {lista3}')


# DIFICULTAD EXTRA (opcional):

# Crear variables para pasar como parametros
param_valor1 = 2727
param_valor2 = (13, 'Alex', True)
param_referencia1 = [1,2,3,4]
param_referencia2 = {'name': 'Carolina', 'age': 30, 'occupation': 'maestra'}

# Imprimimos valores originales
print(f'Valor original del valor 1: {param_valor1}')
print(f'Valor original del valor 2: {param_valor2}')
print(f'Valor original de la referencia 1: {param_referencia1}')
print(f'Valor original de la referencia 2: {param_referencia2}')

# Crear funcion con parametros de paso por valor
def cambio_valores(param_valor1, param_valor2):
    # cambiar valores
    param_valor1, param_valor2 = param_valor2, param_valor1
    # retornarlos
    return param_valor1, param_valor2

result_param_valor1, result_param_valor2 = cambio_valores(param_valor1, param_valor2)
print(f'Despues de la funcion: Valor 1: {result_param_valor1} - Valor 2: {result_param_valor2}')
print(f'Comprobando el valor original del valor 1: {param_valor1}')
print(f'Comprobando el valor original del valor 2: {param_valor2}')


# Crear funcion con parametros de paso por referencia
def cambio_referencias(param_referencia1, param_referencia2):
    # cambio valores
    param_referencia1, param_referencia2 = param_referencia2, param_referencia1
    # retornarlos
    return param_referencia1, param_referencia2

result_param_referencia1, result_param_referencia2 = cambio_referencias(param_referencia1, param_referencia2)
print(f'Despues de la funcion: Valor referencia 1: {result_param_referencia1} - Valor referencia 2: {result_param_referencia2}')
print(f'Comprobando el valor original de la referencia 1: {param_referencia1}')
print(f'Comprobando el valor original de la referencia 2: {param_referencia2}')