

#Operadores


#operadores aritmeticos

#suma
from test._test_multiprocessing import exception_throwing_generator


sum = 5 + 2
print(f"Sum: 5 + 2 = {sum}")
print(f"Sum: 5 + 2 = {(5 + 2)}")

#resta
Subtraction = 5 - 2
print(f"Subtraction: 5 - 2 = {Subtraction}")
print(f"Subtraction: 5 - 2 = {(5 - 2)}")


#multiplicación
Multiplication = 5 * 2
print(f"Multiplication: 5 * 2 = {Multiplication}")
print(f"Multiplication: 5 * 2 = {(5 * 2)}")

#división
Division = 5 / 2
print(f"Division: 5 / 2 = {Division}")
print(f"division: 5 / 2 = {(5 / 2)}")

#modulo
Modulo = 5 % 2
print(f"modulo: 5 % 2 = {Modulo}")
print(f"modulo: 5 % 2 = {(5 % 2)}")

#potencia
Power = 5 ** 2
print(f"potencia: 5 ** 2 = {Power}")
print(f"potencia: 5 ** 2 = {(5 ** 2)}") 

#exponente
Exponent = 5 // 2
print(f"Exponent: 5 ** 2 = {Exponent}")
print(f"Exponent: 5 ** 2 = {(5 ** 2)}")

#division entera
IntegerDivision = 5 // 2
print(f"Integer Division: 5 // 2 = {IntegerDivision}")
print(f"Integer Division: 5 // 2 = {(5 // 2)}")

#operadores de comparacion

"""
Aunque se represente con números,
es posible comparar variables, cadenas de texto, listas, etc.
"""

#igual
Equal = 5 == 2
print(f"Equal: 5 == 2 = {Equal}") 
print(f"Equal: 5 == 2 = {(5 == 2)}")

#diferente
Different = 5 != 2
print(f"Different: 5 != 2 = {Different}")
print(f"Different: 5 != 2 = {(5 != 2)}")

#mayor que
GreaterThan = 5 > 2
print(f"Greater Than: 5 > 2 = {GreaterThan}")
print(f"Greater Than: 5 > 2 = {(5 > 2)}")   

#menor que
LessThan = 5 < 2
print(f"Less Than: 5 < 2 = {LessThan}")
print(f"Less Than: 5 < 2 = {(5 < 2)}")

#mayor o igual que
GreaterThanOrEqual = 5 >= 2
print(f"Greater Than or Equal: 5 >= 2 = {GreaterThanOrEqual}")
print(f"Greater Than or Equal: 5 >= 2 = {(5 >= 2)}")    

#menor o igual que
LessThanOrEqual = 5 <= 2
print(f"Less Than or Equal: 5 <= 2 = {LessThanOrEqual}")
print(f"Less Than or Equal: 5 <= 2 = {(5 <= 2)}")

#operadores logicos 

"""Los operadores lógicos se utilizan para combinar condiciones y evaluar expresiones booleanas.
Los operadores lógicos más comunes son and, or y not."""

#and (dos condiciones deben ser iguales o verdaderas  para que se cumpla la condicion)

And = (5 > 2) and (2 < 3)
print(f"And: (5 > 2) and (2 < 3) = {And}")
print(f"And: (5 > 2) and (2 < 3) = {((5 > 2) and (2 < 3))}")

#or  (al menos una condicion debe ser verdadera para que se cumpla la condicion)

Or = (5 > 2) or (2 < 3)
print(f"Or: (5 > 2) or (2 < 3) = {Or}")
print(f"Or: (5 > 2) or (2 < 3) = {((5 > 2) or (2 < 3))}")
 
#not (invierte el resultado de la condicion)    

Not = not (5 > 2)
print(f"Not: not (5 > 2) = {Not}")
print(f"Not: not (5 > 2) = {(not (5 > 2))}")

#operadores de asignación

"""Los operadores de asignación se utilizan para asignar valores a variables.
El operador de asignación más común es el signo igual (=), pero también existen otros operadores que combinan la asignación con una operación aritmética."""

#asignación
#asignación simple
#asigna el valor especificado a la variable y esta asignacion se representa con el signo igual (=)

my_variable = 7
print(my_variable)

#asignación con suma
#le suma a la variable el valor especificado 

my_variable += 3
print(my_variable)

#asignación con resta
#le resta a la variable el valor especificado

my_variable -= 3
print(my_variable)

#asignación con multiplicación
#le multiplica a la variable el valor especificado

my_variable *= 2
print(my_variable)  

#asignación con división
#le divide a la variable el valor especificado
my_variable /= 2
print(my_variable)

#asignación con módulo
#le aplica el módulo a la variable con el valor especificado
my_variable %= 3
print(my_variable)

#asignación con potencia
my_variable **= 2
print(my_variable)  

#asignación con división entera
my_variable //= 2
print(my_variable)

#asignación con exponente
my_variable **= 2
print(my_variable)

#operadores de identidad

"""Los operadores de identidad se utilizan para comparar objetos y verificar si son el mismo objeto en memoria.
Los operadores de identidad más comunes son is e is not."""


mynewvariable = my_variable


#is (verifica si dos objetos son el mismo objeto en memoria) (no solo compara el valor, sino si son el mismo objeto en memoria)



print(f"is: my_variable is mynewvariable = {my_variable is mynewvariable}")


#is not (verifica si dos objetos no son el mismo objeto en memoria) (no solo compara si son mismo el valor, sino si no son el mismo objeto en memoria)

print(f"is not: my_variable is not mynewvariable = {(my_variable is not mynewvariable)}")


#operadores de pertenencia

"""Los operadores de pertenencia se utilizan para verificar si un valor está presente en una secuencia, como una lista, tupla o cadena de texto.
Los operadores de pertenencia más comunes son in y not in."""   

#in (verifica si un valor está presente en una secuencia)

my_list = [1, 2, 3, 4, 5]
print(f"in: 3 in my_list = {3 in my_list}")  

#not in (verifica si un valor no está presente en una secuencia)
print(f"not in: 7  not in my_list = {7 not in my_list}")

# Ejemplo con combinación de operadores lógicos
print(f"Ejemplo: (3 in my_list) and (6 not in my_list) = {(3 in my_list) and (6 not in my_list)}")

#operadores de bits

"""Los operadores de bits se utilizan para realizar operaciones a nivel de bits en números enteros.
Los operadores de bits más comunes son &, |, ^, ~, << y >>."""




a = 10 #1010
b = 3  #0011

# AND bit a bit
bitwise_and =  10  & 3
print(f"Bitwise AND: 10 & 3 = {bitwise_and}") 

"""lo opera en binario comparando los valores en este formato, por ejemplo en este caso seria
1010
0011
----
0010 = 2 en decimal"""

# OR bit a bit
bitwise_or = 10 | 3
print(f"Bitwise OR: 10 | 3 = {bitwise_or}")

"""Tambien comparará bit a bit y si al menos uno de los valoes es 1 dará a a 1, por ejemplo
 1010
 0011
 ----
 1011 = 11 en decimal"""


# XOR bit a bit
bitwise_xor = 10 ^ 3
print(f"Bitwise XOR: 10 ^ 3 = {bitwise_xor}")

""" Tambien los comparará pero solo si son diferentes el resultado será 1 ny si no lo son será 0
1010
0011
----
1001 en decimal 9"""

# NOT bit a bit
bitwise_not = ~10
print(f"Bitwise NOT: ~10 = {bitwise_not}")   

""" Este los que realizará será invertir todos los bits de los numeros que comparará, negando bit a bipor asi decirlo

00001010
(~10): = -(10 + 1) = 
1010
----
0101 lo que sería -11 en decimal """

#Desplazamiento a la derecha (>>)
right_shift = 10 >> 2
print(f"right shift: 10 >> 2 = {right_shift}")  

"""lo que hará sera dezplazar todos los bits a la derecha, por ejemplo
1010
>>>>
0010 = 2 en decimal (10//2² = 2.5 pero como se manejan enteros al usar este tipo de operadores pasa a ser = 2)
"""

 #Desplazamiento a la izquierda (<<)
left_shift = 10 << 2
print(f"left shift: 10 << 2 = {left_shift}")  


"""lo que hará sera desplazar a la izquierda todos los bits por ejemplo
1010
<<<<
101000 = 40 en decimal (10**2² = 40 )"""

#the end of operators

#Estructuras de control

"""Las estructuras de control son bloques de código que permiten tomar decisiones y ejecutar diferentes acciones según ciertas condiciones. 
Las estructuras de control más comunes son las condicionales (if, elif, else) y los bucles (for, while)."""

"""Estructuras de control condicionales;
estas estructuras de control condicionales permiten ejecutar bloques de código basados en condiciones específicas."""


#Condicional if

"""La estructura if evalúa una condición y ejecuta un bloque de código si la condición es verdadera."""

#la condicional elif 

"""evalúa si una condición es verdadera y, si lo es, ejecuta el bloque de código indentado debajo de ella."""

#la condicional else
"""else se ejecuta si ninguna de las condiciones anteriores es verdadera."""

my_string = "Kriptum"
if my_string == "Paprika":
    print("La variable my_string es igual a 'Paprika'")
elif my_string == "Ivan":
    print("La variable my_string es igual a 'Ivan'")
else:
    print("La variable my_string no es igual a 'Paprika'")

#Condicionales iterativas

"""Las estructuras de control iterativas permiten repetir un bloque de código varias veces.
Las estructuras de control iterativas más comunes son los bucles for y while."""

#Bucle for

"""El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena de texto) y ejecutar un bloque de código para cada elemento de la secuencia."""

for i in range(10):
    print(f"{i} es un número en el rango de 0 a 9")

#Bucle while

"""El bucle while se utiliza para repetir un bloque de código mientras se cumpla una condición."""
i = 0
while i < 10:
    print(f"{i} es un número en el rango de 0 a 9")
    i += 1

#manejo de excepciones

"""El manejo de excepciones permite capturar y manejar errores que pueden ocurrir durante la ejecución del código.
La estructura try-except se utiliza para manejar excepciones en Python."""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: La división por cero no es permitida.")
except:
    print("Error: Ocurrió un error inesperado.")
finally:
    print("This the end of the try-except block.")

    """
    Posibles errores que puedes capturar con except:
- ValueError: cuando alguien ingresa texto en vez de un número
- TypeError: si haces operaciones incompatibles
- KeyError: al acceder a un diccionario con una clave que no existe
- IndexError: al acceder a una posición inválida en una lista
- ZeroDivisionError: si hay división entre cero
- FileNotFoundError: al trabajar con archivos que no existen
- Exception: para capturar errores generales que no anticipaste
- ImportError: al intentar importar un módulo que no existe
"""





#Fin de las estructuras de control





#ejercicio extra

"""
Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 """

for ejercicio_extra in range(10, 56):
    if ejercicio_extra % 2 == 0 and ejercicio_extra != 16 and ejercicio_extra % 3 != 0:
        print(ejercicio_extra)