#Operadores aritméticos

print(f"Suma 10 + 5 = {10 + 5}")
print(f"Resta 10 - 5 = {10 - 5}")
print(f"Multiplicación 10 * 5 = {10 * 5}")
print(f"División 10 / 5 = {10 / 5}")
print(f"División Entera 10 // 4 = {10 // 4}")
print(f"Modulo 10 % 4 = {10 % 4}")
print(f"Exponenciales 10 ** 5 = {10 ** 5}")

#Operadores de Comparación 
#Los operadores de comparación nos van a dar resultados "True or False"

print(f"Igualdad: 10 == 5 es {10 == 5}")   
print(f"Desiguladad: 10 != 5 es {10 != 5}")  
print(f"Mayor que: 10 > 5 es {10 > 5}")
print(f"Menor que: 10 < 5 es {10 < 5}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 5 es {10 <= 5}") 

#Operadores lógicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")

#Operadores de asignación
#Los usamos en conjunto con el valor de las variables

my_number = 10 # El operador de asignación es "=", lo estoy utilizando para establecer que my_number es igual a 10.
print(my_number)
my_number += 5 # Suma y asignación. Al valor de my_number le sume 5.
print(my_number)
my_number -= 5 # Resta y asignación. Al valor de my_number le reste  5.
print(my_number) 
my_number *= 5 # Multiplicación y asignación. Al valor de my_number le multiplique por  5.
print(my_number) 
my_number /= 2 # División y asignación. Al valor de my_number lo dividí por  2.
print(my_number) 
my_number //= 3 # División entera y asignación. Al valor de my_number lo dividí de forma entera por  3. División sin decimales.
print(my_number)
my_number %= 3 # Módulo y asignación. Al valor de my_number lo calcule el resto de forma entera por  5. (8 // 3 = 3+3 da 6 la diferencia es 2)
print(my_number) 
my_number **= 5 # Exponente y asignación. Al valor de my_number lo multiplique exponencialmente por  5.
print(my_number)

# Operadores de identidad
# Sirven para comparar el valor de la posición de memoria.

my_new_number = my_number
print(my_new_number)
print(f"my_number is my_new_number es {my_number is my_new_number}") # IS se usa para igualdad
print(f"my_number is not my_new_number es {my_number is not my_new_number}") # IS NOT se usa para desigualdad

# Operadores de pertenencia

print(f"'a' in 'nacho' es {'a' in 'nacho'}") # true (in se utiliza para corrobar que PERTENECE)
print(f"'p' in 'nacho' es {'p' in 'nacho'}") # false

print(f"'p' not in 'nacho' es {'p' not in 'nacho'}") # true (not in se utiliza para corroborar que NO PERTENECE)

my_variable1 = "AprendiendoPhyton"
print(f"'Aprendiendo' in 'my_variable1' is {'Aprendiendo' in my_variable1}")

# Operadores de bit
a = 10
b = 3
print(f"AND: 10 & 3 = {10 & 3}") #1010
print(f"OR: 10 | 3 = {10 | 3}") #1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001
print(f"NOT: ~10 = {~10}") #1010
print(f"Desplazamiento a la derecha 10 >> 2 = {10 >> 2}") #0010
print(f"Desplazamiento a la izquierda 10 << 2 = {10 << 2}") #10100

"""
Estructuras de control
"""

# Condicionales

my_string = "nacho"

if my_string == "nacho":
    print("my_string es 'nacho'")
elif my_string == "ignacio":
    print("my_string is 'ignacio'")
else:
    print("my_string no es 'nacho'")

# Iterativas
# Ejecuta lo que se encuentra dentro del bucle. Recorre una escructura determinada.

for n in range(10):
    print(n)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
# La finalidad es que la aparición de un error en el código, ese error no destruya el funcionamiento del mismo. Es una especie de cortafuegos que impide que el error tire abajo el programa.


try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range (10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)


