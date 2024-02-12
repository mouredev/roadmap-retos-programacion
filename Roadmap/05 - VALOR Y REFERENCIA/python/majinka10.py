# Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...

entero = 10
flotante = 3.1415
booleano = True
cadena = 'Hola'

def cambiar_valor_simple(dato):
    if type(dato) == int:
        dato = 20
    elif type(dato) == float:
        dato += 3
    elif type(dato) == bool:
        dato = False 
    elif type(dato) == str:
        dato += 'Python!'

cambiar_valor_simple(entero)
print(entero)
cambiar_valor_simple(flotante)
print(flotante)
cambiar_valor_simple(booleano)
print(booleano)
cambiar_valor_simple(cadena)
print(cadena)

print('Caso en el que podemos modificar (con return)')
def por_dos(dato):
    return dato * 2

print(por_dos(entero))
print(por_dos(flotante))
print(por_dos(cadena))
print(por_dos(booleano))


#Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...

print('\nPara tipos de datos compuestos')

lista = [2, 5, 6]
diccionario = {'Hola': 3, 'Python': 2, 'Adios': 6}
conjunto = {3, 2, 1}

def cambiar_valor_compuesto(compuesto):
    if type(compuesto) == dict:
        for clave in diccionario.keys():
            compuesto[clave] *= 2
    elif type(compuesto) == set:
        conjunto.add(5)
    else:
        for i, numero in enumerate(compuesto):
            compuesto[i] *= numero

cambiar_valor_compuesto(lista)
print(lista)
cambiar_valor_compuesto(diccionario)
print(diccionario)
cambiar_valor_compuesto(conjunto)
print(conjunto)

print('Caso en el que NO podemos modificar (pasando una copia a la función)')
lista2 = [2, 5, 6]
diccionario2 = {'Hola': 3, 'Python': 2, 'Adios': 6}
conjunto2 = {3, 2, 1}
cambiar_valor_compuesto(lista2[:])
print(lista2)
cambiar_valor_compuesto(diccionario2.copy())
print(diccionario2)
cambiar_valor_compuesto(conjunto2.copy())
print(conjunto2)

# Ejercicio EXTRA
print('\nEjercicio EXTRA')

parametro1 = 'Hola'
parametro2 = 5

def intercambio_valor(parametro1, parametro2):
    auxiliar = parametro1
    parametro1 = parametro2
    parametro2 = auxiliar
    return parametro1, parametro2

not_parametro1, not_parametro2 = intercambio_valor(parametro1, parametro2) 

print(f"Variables originales: {parametro1, parametro2}.")
print(f"Variables nuevas: {not_parametro1, not_parametro2}.")

parametro3 = [9, 0, 3]
parametro4 = {'Uno': 1, 'Dos': 2, 'Tres': 3}

def intercambio_referencia(parametro1, parametro2):
    auxiliar = parametro1
    parametro1 = parametro2
    parametro2 = auxiliar
    return parametro1, parametro2

not_parametro3, not_parametro4 = intercambio_referencia(parametro3, parametro4) 

print(f"Variables originales: {parametro3, parametro4}.")
print(f"Variables nuevas: {not_parametro3, not_parametro4}.")