# #05 VALOR Y REFERENCIA
'''
EJERCICIO
- Muestra ejemplos de asignación de variables "por valor" y "por referencia". según
  su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y
  "por referencia", y como se comportan en cada caso en el momento de ser modificadas.
'''

# Paso de dato por valor
'''
Si usamos un párametro pasado por valor, se creará una copia  local de la variable, lo que implica que cualquier
modificación sobre la misma no tendrá efecto sobre la original
'''
x = 10

def funcion(entrada):
    entrada = 0

funcion(x)
print(x)

# Paso de dato por referencia
'''
Con una variable pasada como referencia, se actuará directamente sobre la variable pasada, por lo que las
modificaciones afectarán a la variable original.
'''
x = [10, 20, 30]

def funcion(entrada):
    entrada.append(40)

funcion(x)
print(x)

# DIFICULTAD EXTRA
print("\n----------------------------------------------------")
print("EXTRA DIFFICULT")
'''
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
'''

# Por valor
var1 = 10
var2 = 20

def valor(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2

var3, var4 = valor(var1, var2)

print(f"{var1}, {var2}")
print(f"{var3}, {var4}")

# Por referencia
list_a = [10, 20]
list_b = [30, 40]

def referencia(var1: list, var2: list):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2

list_c, list_d = referencia(list_a, list_b)
print(f"{list_a}, {list_b}")
print(f"{list_c}, {list_d}")
