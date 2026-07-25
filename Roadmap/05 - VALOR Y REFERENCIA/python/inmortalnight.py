# 05 - VALOR Y REFERENCIA

# Asignación de variables por valor, se copia, tipo de dato primitivo

# int
valor1 = 10
valor2 = valor1
print("int: ", valor1, valor2, sep=" ")
valor2 = 20
print("int: ", valor1, valor2, sep=" ")
# float
valor1 = 10.5
valor2 = valor1
print("float: " , valor1, valor2, sep=" ")
valor2 = 20.5
print("float: " , valor1, valor2, sep=" ")
# boolean
valor1_1 = True
valor2_2 = valor1_1
print("boolean: " , valor1_1, valor2_2, sep=" ")
valor2_2 = False
print("boolean: " , valor1_1, valor2_2, sep=" ")
# string
valor1 = "Hola"
valor2 = valor1
print("string: " , valor1, valor2, sep=" ")
valor2 = "Adios"
print("string: " , valor1, valor2, sep=" ")


# Asignación de variables por referencia, usa el mismo espacio de memoria, tipo de dato complejo
# list
valor1 = [1, 2, 3]
valor2 = valor1
print("list: " , valor1, valor2, sep=" ")
valor2.append(4)
print("list: " ,  valor1, valor2, sep=" ")
# tuple
valor1 = (1, 2, 3)
valor2 = valor1
print("tuple: " ,  valor1, valor2, sep=" ")
# dict
valor1 = {"a": 1, "b": 2}
valor2 = valor1
print("dict: " ,  valor1, valor2, sep=" ")
valor1["a"] = 3
print("dict: " ,  valor1, valor2, sep=" ")
# set
valor1 = {1, 2, 3}
valor2 = valor1
print("set: " ,  valor1, valor2, sep=" ")
valor1.add(4)
print("set: " ,  valor1, valor2, sep=" ")
# frozenset
valor1 = frozenset({1, 2, 3})
valor2 = valor1
print("frozenset: " ,  valor1, valor2, sep=" ")
# bytearray
valor1 = bytearray(b"abc")
valor2 = valor1
print("bytearray: " ,  valor1, valor2, sep=" ")
valor1[0] = 100
print("bytearray: " ,  valor1, valor2, sep=" ")


# EXTRA 
''' * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
    def1(a,b), 2 parametros
    def2(a,b), '''

# Funcion por valor
def program1(a:int, b: int) -> tuple:
    temp = a
    a = b
    b = temp
    return a, b
value1 = 10
value2 = 20
print("value1", value1, "value2", value2)
value3, value4 = program1(value1, value2)
print("value1", value1, "value2", value2)
print("value3", value3, "value4", value4)

# Funcion por referencia
def program2(a:list, b: list) -> tuple:
    a, b = b, a
    return a, b
value1 = [10, 20]
value2 = [20, 30]
print("value1", value1, "value2", value2)
value3, value4 = program2(value1, value2)
print("value1", value1, "value2", value2)
print("value3", value3, "value4", value4)

'''Explicación: 
En ambos casos, lo que se trabaja y se cambia son los variables locales dentro de las funciones. 
Aunque salga un error al cambiar por referencia, no afectará a las variables originales. 
En el caso de que se quiera cambiar el valor de las variables originales, 
se deberá convertir las variables locales en datos compuestos; 
listas a[:], b[:] = b[:], a[:].'''