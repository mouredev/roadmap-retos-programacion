#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RETO 3 ROADMAP 2024

EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

AUTOR: CRISTIAN
"""

"""
Las estructuras soportadas por python son las siguientes: las listas, las tuplas y los diccionarios
LISTAS: van siempre entre corchetes ( [] ) y son modificables, por lo que se pueden borrar y escribir todos los
datos que queramos
TUPLAS: van siempre entre paréntesis () y no son modificables, es decir, las operaciones contrarias de una lista
CONJUNTOS O SETS: Un conjunto es una colección no ordenada de elementos únicos. Se define mediante llaves {}.
DICCIONARIOS: Un diccionario es una colección de pares clave-valor. Permite acceder a los valores a través de las claves. Se define mediante llaves {}.
CADENAS O STRINGS: Una cadena es una secuencia de caracteres. Se puede definir mediante comillas simples (') o dobles ("). 
"""

#Estas son las operaciones que se pueden realizar con una lista
mi_lista=["cristian", "aitor", "alexia", "juan", 23, 34, 76]
#INSERCIÓN
mi_lista.append("CFGS Desarrollo de aplicaciones web")
print("Esto es una simulación de agregación de elementos a una lista: \n", mi_lista)
#BORRADO
del mi_lista[2]
print("Esto es una simulación de borrado de elementos de una lista: \n", mi_lista)
#ACTUALIZACIÓN
mi_lista[5] = 545
print("Esto es una simulación de actualización de una lista: \n", mi_lista)
#ORDENACIÓN: para mostrar la ordenación, se va a usar una lista de números
lista_numeros = [455,234,3,567,34,7,5,766,58]
lista_numeros.sort()
print("Lista de números ordenada: \n", lista_numeros)

print("----------------------------------------------------------------------")

#Las tuplas son inmutables, lo que no permite la modificación de datos, por ello, solo se pueden realizar 
#las siguientes operaciones
#CREACIÓN DE TUPLAS
mi_tupla=("dani", "cristian", "sergio", 23, 547, 5678)
print("Aquí tenemos nuestra tupla: \n", mi_tupla)
#ACCESO DE DATOS
print("Este es el dato con indice 1 de nuestra tupla: " ,mi_tupla[1])
#CONCATENACIÓN
tupla_concatenada= mi_tupla + (56,345,7897)
print("Esta es una tupla concatenada con otra: \n", tupla_concatenada)
#REPETICIÓN DE ELEMENTOS
tupla_repetida = mi_tupla * 3
print("Esta es nuestra tupla repetida 3 veces: \n", tupla_repetida)
#COMPROBAR LONGITUD DE TUPLA
print("Esta es la longitud de nuestra tupla: ", len(mi_tupla)) 
#ITERACIÓN A TRAVES DE UNA TUPLA: para ello, vamos a imprimir en cada línea, los elementos de las tupla
print("Esto es una simulación de iteración de las tuplas: ")
for i in mi_tupla:
    print(i, "\n")

print("----------------------------------------------------------------------")


#En cuanto a los conjuntos, se pueden realizar las siguientes operaciones:
#CREACIÓN
conjunto_vacio = set()
conjunto_con_elementos = {1, 2, 3, 'a', 'b'}
print("Esto es un conjunto: ", conjunto_con_elementos)
#ADICIÓN
conjunto = {1, 2, 3}
conjunto.add(4)
print("Añadimos un elemento al conjunto: " , conjunto)
#ELIMINACIÓN
conjunto.remove(2)
print("Eliminamos el 2 del conjunto: ", conjunto)
#Verificación de Pertenencia
pertenece_3 = 3 in conjunto
print(pertenece_3)
#Comprobación de Subconjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {1, 2}
es_subconjunto = conjunto2.issubset(conjunto1)
print("¿Es subconjunto?: ", es_subconjunto)
#Comprobación de Igualdad
conjunto1 = {1, 2, 3}
conjunto2 = {3, 2, 1}
son_iguales = conjunto1 == conjunto2
print("¿Son iguales los conjuntos?: ", son_iguales)

print("----------------------------------------------------------------------")


#Estas son las operaciones que se pueden realizar con los diccionarios
#Creación de diccionarios
diccionario_vacio = {}
diccionario_con_elementos = {'clave1': 'valor1', 'clave2': 42, 'clave3': [1, 2, 3]}
#Acceso a valores por clave
diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ejemplo'}
edad = diccionario['edad']  # Valor: 25
#Añadir o modificar elementos
diccionario = {'nombre': 'Juan', 'edad': 25}
diccionario['ciudad'] = 'Ejemplo'  # Añadir un nuevo par clave-valor
diccionario['edad'] = 26  # Modificar el valor de una clave existente
#Eliminar elementos
diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ejemplo'}
del diccionario['ciudad']  # Eliminar el elemento con clave 'ciudad'
#Operaciones de diccionarios
diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ejemplo'}

diccionario_copia = diccionario.copy()  # Crear una copia del diccionario
diccionario.clear()  # Eliminar todos los elementos del diccionario

claves = diccionario.keys()  # Obtener las claves del diccionario
valores = diccionario.values()  # Obtener los valores del diccionario
#Iteración a través de un diccionario
diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ejemplo'}

for clave in diccionario:
    print(clave, diccionario[clave])  # Iterar a través de las claves y valores

for clave, valor in diccionario.items():
    print(clave, valor)  # Iterar a través de pares clave-valor
#Verificación de pertenencia de claves
diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ejemplo'}
tiene_clave = 'ciudad' in diccionario  # Valor: True

print("----------------------------------------------------------------------")


#Estas son las operaciones que se pueden realizar con las cadenas o strings
#CONCATENACIÓN
cadena1 = "Hola"
cadena2 = " Mundo"
concatenacion = cadena1 + cadena2  # Valor: "Hola Mundo"
#REPETICIÓN
cadena = "Hola"
repetida = cadena * 3  # Valor: "HolaHolaHola"
#ACCESO A CARACTERES POR ÍNDICE
cadena = "Python"
tercer_caracter = cadena[2]  # Valor: "t"
#LONGITUD
cadena = "Python"
longitud = len(cadena)
#SLICING
cadena = "Python"
subcadena = cadena[1:4]  # Valor: "yth" 
#MÉTODO FIND
cadena = "Python es divertido"
posicion = cadena.find("es")  # Valor: 7
#MÉTODO REPLACE
cadena = "Hola Mundo"
nueva_cadena = cadena.replace("Hola", "Adiós")  # Valor: "Adiós Mundo"
#MÉTODO UPPER Y LOWER
cadena = "Hola Mundo"
minusculas = cadena.lower()  # Valor: "hola mundo"
mayusculas = cadena.upper()  # Valor: "HOLA MUNDO"
#MÉTODO SPLIT
cadena = "Python,es,lenguaje,de,programación"
lista_subcadenas = cadena.split(",")  # Valor: ['Python', 'es', 'lenguaje', 'de', 'programación']
#MÉTODO STRIP
cadena = "Python,es,lenguaje,de,programación"
lista_subcadenas = cadena.split(",")  # Valor: ['Python', 'es', 'lenguaje', 'de', 'programación']
#MÉTODO STARTSWITH Y ENDSWITH
cadena = "Hola Mundo"
comienza_con_hola = cadena.startswith("Hola")  # Valor: True
termina_con_mundo = cadena.endswith("Mundo")  # Valor: True

