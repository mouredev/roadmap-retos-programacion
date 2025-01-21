"""

        Operadores

"""


## Operadores aritméticos

print (f"suma: 25 + 30 es {25 + 30}")
print (f"resta: 25 - 30 es {25 - 30}")
print (f"multiplicación: 25 * 30 es {25 * 30}")
print (f"división: 25 / 30 es {25 / 30}")    
print (f"módulo: 25 % 30 es {25 % 30}")
print (f"potencia: 25 ** 30 es {25 ** 30}")
print (f"división entera: 25 // 30 es {25 // 30}")       
print (f"raíz cuadrada: 25 ** 0.5 es {25 ** 0.5}")

## Operadores lógicos

print (f"AND: 3 + 5 == 8 and 8 + 3 == 11 es {3 + 5 == 8 and 8 + 3 == 11}")
print (f"OR: 3 + 5 == 11 or 8 + 3 == 11 es {3 + 5 == 11 or 8 + 3 == 11}")
print (f"NOT: not 3 + 5 == 11 es {not 3 + 5 == 11}")

## Operadores de comparación

print (f"igual: 25 == 30 es {25 == 30}")
print (f"distinto: 25 != 30 se {25 != 30}")
print (f"mayor: 25 > 30 es {25 > 30}")
print (f"menor: 25 < 30 es {25 < 30}")
print (f"mayor o igual: 25 >= 30 es {25 >= 30}")
print (f"menor o igual: 25 <= 30 es {25 <= 30}")
print (f"comparación de cadenas: 'hola cadena 1' == 'hola cadena 2' es {'hola cadena 1' == 'hola cadena 2'}")
print (f"comparación de cadenas: 'hola cadena 1' != 'hola cadena 2' es {'hola cadena 1' != 'hola cadena 2'}")
print (f"comparación de cadenas: 'hola cadena 1' > 'hola cadena 2' es {'hola cadena 1' > 'hola cadena 2'}")
print (f"comparación de cadenas: 'hola cadena 1' < 'hola cadena 2' es {'hola cadena 1' < 'hola cadena 2'}")  
print (f"comparación de cadenas: 'hola cadena 1' >= 'hola cadena 2' es {'hola cadena 1' >= 'hola cadena 2'}")
print (f"comparación de cadenas: 'hola cadena 1' <= 'hola cadena 2' es {'hola cadena 1' <= 'hola cadena 2'}")   
print (f"comparación de listas: [1, 2, 3] == [5, 6, 7] es {[1, 2, 3] == [5, 6, 7]}")
print (f"comparación de listas: [1, 2, 3] != [5, 6, 7] es {[1, 2, 3] != [5, 6, 7]}")
print (f"comparación de listas: [1, 2, 3] > [5, 6, 7] es {[1, 2, 3] > [5, 6, 7]}") 
print (f"comparación de listas: [1, 2, 3] < [5, 6, 7] es {[1, 2, 3] < [5, 6, 7]}")
print (f"comparación de listas: [1, 2, 3] >= [5, 6, 7] es {[1, 2, 3] >= [5, 6, 7]}")
print (f"comparación de listas: [1, 2, 3] <= [5, 6, 7] es {[1, 2, 3] <= [5, 6, 7]}")



## Operadores de bits

a= 25 # 11001
b= 30 # 11110
print (f"AND: 25 & 30 es {a & b}") # 11000
print (f"OR: 25 | 30 es {a | b}") # 11111
print (f"XOR: 25 ^ 30 es {a ^ b}") # 00111
print (f"NOT: ~25 es {~a}") 
print (f"Desplazamiento a la izquierda: 25 << 2 es {a << 2}") # 1100100
print (f"Desplazamiento a la derecha: 25 >> 2 es {a >> 2}") # 110


## Operadores de pertenencia

print (f"pertenencia: 'o' in 'drolo18' es {'o' in 'drolo18'}")  
print (f"pertenencia: 'b' not in 'drolo18' es {'b' not in 'drolo18'}")

## Operadores de asignación

my_number = 25 # asignación
print (my_number)   
my_number += 2 # suma y asignación
print (my_number)
my_number -= 2 # resta y asignación
print (my_number)
my_number *= 2 # multiplicación y asignación
print (my_number)
my_number /= 2 # división y asignación
print (my_number)
my_number %= 2 # módulo y asignación
print (my_number)
my_number **= 2 # potencia y asignación
print (my_number)
my_number //= 1 # división entera y asignación
print (my_number)

## Operadores de identidad

my_new_number  = 1.0
print (f"identidad: my_new_number is my_number es {my_new_number is my_number}")
print (f"identidad: my_new_number is not my_number es {my_new_number is not my_number}")

my_new_number = my_number   
print (f"identidad: my_new_number is my_number es {my_new_number is my_number}")
print (f"identidad: my_new_number is not my_number es {my_new_number is not my_number}")

"""
Estructuras de control
"""

# condicionales

my_string = "juan"

if my_string == "drolo18":
    print ("my_string es 'drolo18'")
elif my_string == "pedro":
    print ("my_string es 'Pedro'")
else:
    print ("my_string no es ni 'drolo18' ni 'Pedro'")


# interactivas

for i in range(25):
    print (i)

i = 0
while i < 25:
    print (i)
    i += 1

# manejo de excepciones

try:
    print (10 / 1) 
except: 
    print ("se ha producido un error")
finally:
    print ("finalizado el manejo de excepciones")   

"""
Extra
"""     

for number in range(1, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0: 
         print (number)  
