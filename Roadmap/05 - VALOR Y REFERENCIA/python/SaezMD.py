#05 VALOR Y REFERENCIA
"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
"""


#Values by value
valA = 1
valB = 3 * 4
valC = 'Pythonista'

a, b, c = 1, 2, 3
a = b = c = 12

#by Value:
a = 1
b = 12.5
c = "hello"
d = False

#by ref:
x = ["a", "b", "c"]
y = {"a": 0, "b": 1, "c": 2}


#Function by value:
x = 10
def function(entry):
    entry = 0
function(x)

print(x) # 10

#Function by ref:
x = [10, 20, 30]
def function(entrada):
    entrada.append(40)

function(x)
print(x) # [10, 20, 30, 40]


"""
 * DIFICULTAD EXTRA (opcional):
 Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna 
 a dos variables diferentes a las originales. A continuación, imprime el valor de las
 variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 Comprueba también que se ha conservado el valor original en las primeras.
"""

val01 = 12
val02 = "Home"
print(id(val01), id(val02))

def function01(value1, value2)-> str:
    """function to check values not changed"""
    temp01= value1
    temp02= value2
    value1 = temp02
    value2 = temp01
    
    return value1, value2

exit01, exit02 = function01(val01, val02)

print(val01, val02)
print(id(val01), id(val02))
print()
print(exit01, exit02)
print(id(exit01), id(exit02))


ref01 = ["car", "ramp"]
ref02 = {"jan":12, "feb": 10}
print(id(ref01), id(ref02))

def function02(ref1, ref2)-> str:
    """function to check references yes changed"""
    temp01= ref1
    temp02= ref2
    ref1 = temp02
    ref2 = temp01

    return ref1, ref2

exit03, exit04 = function02(ref01, ref02)

print(ref01, ref02)
print(id(ref01), id(ref02))
print()
print(exit03, exit04)
print(id(exit03), id(exit04))



