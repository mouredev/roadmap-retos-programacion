'''
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 '''

'''
DEFINICIÓN:
Parámetros por referencia y valor, son aquellos parámetros que al entrar en una función se comportan de una determinada
forma, ya sea creando una copia de una variable y operando sobre ella (por valor) o bien operando directamente sobre el valor
original y modificando la variable (por referencia)

Si bien los objetos que se obtienen en una variable original por referencia y el valor que resulta despues de entrar a una función
parecieran ser diferentes lo cierto es que son el mismo, ya que comparten la misma dirección en la memoria, esto lo podemos notar si
usamos la función "id()" que nos entrega el valor de memoria de cada objeto

'''

#Las modificaciones de variables pueden variar dependiendo del tipo de dato, estos se dividen en mutables e inmutables

'''
Tipos Mutables: Si permiten ser modificados una vez creados (datos pasados por referencia)
(Estos tipos de datos el programa interpreta que no vale la pena crear una copia ya que pueden ser
muy grandes, por ello se actua directamente sobre la dirección de memoria del elemento)

- Listas
- Bytearray
- Diccionarios
- Conjuntos
'''

'''
Tipos Inmutables: No permiten ser modificados una vez creados (datos pasados por valor)

- Booleanos
- Integgers(Enteros)
- Float(Flotantes)
- Strings(Cadenas)
- Tuplas
- Range
- Bytes
'''

print("------- EJEMPLOS DE DATOS POR VALOR ------- ")

# ----> Ejemplo_1: Entero
print("------- Ejemplo: Entero ------- ")
#---------------------------------

value_1 = 70 #Variable pasada por Valor (tipo de dato Int)
print(id(value_1))
print(f"Valor original: {value_1}") #Variable Original de tipo Integger

def doouble(intValue):
    doubleValue = intValue * 2
    return doubleValue

p1 = doouble(value_1)

print(f"Copia pasada por función: {p1}") #Copia local de la variable procesada dentro de la función (aumentada al doble)
#print(id(p1)) #Dirección en memoria de la copia local
print(f"Valor original(No cambia): {value_1}")
#print(id(value_1)) #Dirección en memoria de la variable original


# ----> Ejemplo_2: Tuplas (Recordar que para poder modificar tuplas primero debemos transformarlas a listas)
print("------- Ejemplo: Tupla -------")
#---------------------------------

tupla_1 = ("Hola", "Como", "Estas")

def removeItem(t):
    list_t = list(t)
    for e in list_t:
        if e == "Hola":
            list_t.remove(e)
    t = tuple(list_t)
    return t

resultado = removeItem(tupla_1)

print(f"Elemento tupla_1 original: {tupla_1}") # Al tratarse de un dato inmutable el valor original no se modifica
print(f"Elemento tupla_1 modificado en la función: {resultado}") # Lo que si se modifica es la copia local que pasamos a la función


# ----> Ejemplo_3: String
print("------- Ejemplo: Cadena -------")
#---------------------------------

string_1 = "Cadena 1"

def upperString(s):
    newString = s.upper()
    return newString

resultado_s = upperString(string_1)
print(f"Copia pasada por función: {resultado_s}")
print(f"Valor original (sin modificar): {string_1}")


print("------- EJEMPLOS DE DATOS POR REFERENCIA ------- ")

# ----> Ejemplo_1: Lista
print("------- Ejemplo: Lista -------")
#---------------------------------

list_1 = [1,3,5,7,9] #Variable pasada por referencia (tipo de dato list)

print(f"{list_1} lista sin modificaciones")
print(id(list_1)) #Dirección en la memoria de la lista

def numbersDoubles(lista):
    for i in range(len(lista)):
        itemDouble = lista[i] * 2
        lista.append(itemDouble)
    return lista

p2 = numbersDoubles(list_1)

print(list_1) #Lista original, referenciada en la función numbersDoubles -> Al ser pasada por referencia tenemos que el valor original a sido modificado

print(p2) #Lista final, resultado de la aplicación de métodos en la función -> Este valor es otro "objeto" al que se le ha asignado la misma dirección de list_1
print(id(p2)) #Dirección en la memoria de la lista pasada por la función es la misma que la de la lista original

print(type(list_1))

'''
Las listas al pasar por referencia por una función se modifica el contenido de esta de manera permanente, pero mantiene la misma dirección en la memoria
que la lista original, las variables antiguas de la lista eventualmente es borrada del programa
'''


# ----> Ejemplo_2: Lista (revisar este ejemplo)
print("------- Ejemplo: Lista 2 -------")
#---------------------------------

lista_2 = [23, 43, 53, 12, 54]
print(id(lista_2))

def deletList(l):
    l = [] #Con esta linea "vaciamos la lista"
    return l

print(id(deletList(lista_2)))


# ----> Ejemplo_3: Diccionarios
print("------- Ejemplo: Diccionario -------")
#---------------------------------

diasPorMes = {
    "Enero": 31,
    "Febrero": 29,
    "Marzo": 31,
    "Abril": 30,
    "Mayo": 31,
    "Junio": 30,
    "Julio": 31,
    "Agosto": 31,
    "Septiembre": 30,
    "Octubre": 31,
    "Noviembre": 30,
    "Diciembre": 31
}

print(diasPorMes)
print(id(diasPorMes)) #Dirección de la variable #1669176227520

def meses(dictionary):
    print(id(dictionary)) #Dirección de la variable #1669176227520
    for i in dictionary:
        if dictionary[i] == 31:
            print(f"{i} tiene 31 días")
            #print(f"{diasPorMes.get(i)} tiene 31 días")
        elif dictionary[i] <= 30:
            print(f"{i} es el mes más corto")
            dictionary.update({"Febrero": 0})
        else:
            continue

meses(diasPorMes)
print(meses(diasPorMes))
print(id(meses(diasPorMes))) #Dirección de memoria del resultado del diccionario pasado por la función ha sido modificada #140710946191352
print(id(diasPorMes)) #Dirección de la variable #1669176227520


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 '''

#PARAMETROS POR VALOR

variable_1 = "cadena"
variable_2 = (23, 43, 12, 54, 65)

def programa_1(v1, v2):
    var_aux = v1
    copia_v1 = v2
    copia_v2 = var_aux
    return copia_v1, copia_v2

test_1 = programa_1(variable_1, variable_2)
print(f"Copia Variable 1 (editada): {test_1[0]}, Variable 1 original: {variable_1}")
print(f"Copia Variable 2 (editada): {test_1[1]}, Variable 2 original: {variable_2}")


#PARAMETROS POR REFERENCIA

variable_3 = [23, 43, 15, 31, 12, 32]
variable_4 = {
    "Lord of the Rings": 3,
    "Harry Potter": 8,
    "Pirates of the Caribean": 5,
    "Transformers": 7,
}

def programa_2(v3, v4):
    var_aux_2 = v3
    copia_v3 = v4
    copia_v4 = var_aux_2
    return copia_v3, copia_v4

test_2 = programa_2(variable_3, variable_4)

print(f"Variable 3 pasada por referencia: {test_2[0]}, Variable 3 original: {variable_3}")
print(f"Variable 4 pasada por referencia: {test_2[1]}, Variable 4 original: {variable_4}")
