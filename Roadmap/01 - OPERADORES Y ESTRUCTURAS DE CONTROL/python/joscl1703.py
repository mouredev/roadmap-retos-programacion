'''
EJERCICIO 1: OPERADORES Y ESTRUCTURAS DE CONTROL
'''

# Operadores aritméticos
print("OPERADORES ARITMÉTICOS")
print(f"Suma 12 + 5 = {12 + 5}")
print(f"Resta 10 - 3 = {10 - 3}")
print(f"Multiplicación 4 * 6 = {4 * 6}")
print(f"División 15 / 3 = {15 / 3}")
print(f"Módulo 10 % 3 = {10 % 3}")
print(f"Potencia 2 ** 3 = {2 ** 3}")
print(f"División entera 17 // 3 = {17 // 3}")

#Operadores de comparación
print("\nOPERADORES DE COMPARACIÓN")
print(f"Igual a 6 ==6: {6 == 6}")
print(f"Diferente de 14 != 10: {14 != 10}")
print(f"Mayor que 9 > 4: {9 > 4}")
print(f"Menor que 2 < 5: {2 < 5}")
print(f"Mayor o igual que 7 >=5: {7 >= 5}")
print(f"Menor o igual que 1 <= 3: {1 <= 3}")

#Operadores lógicos
print("\nOPERADORES LÓGICOS")
print(f"AND && 18 + 9 = 27 and 5 * 3 = 15: {18 + 9 == 27 and 5 * 3 == 15}")
print(f"OR // 10 - 2 == 8 or 14 + 5 == 16: {10 - 2 == 8 or 14 + 5 == 16}")
print(f"NOT ! 7 // 3 == 2: {not 7 // 3 == 2}")

#Operadores de asignación
print("\nOPERADORES DE ASIGNACIÓN")
my_number = 17
print(my_number)
my_number += 4 #Suma y asignación
print(my_number)
my_number -= 2 #Resta y asignación
print(my_number)
my_number *= 2 #Multiplicación y asignación
print(my_number)
my_number /= 4 #División y asignación
print(my_number)
my_number %= 2 #Módulo y asignación
print(my_number)
my_number **= 3 #Potencia y asignación
print(my_number)
my_number //= 2 #División entera y asignación
print(my_number)




#Operadores de identidad
print("\nOPERADORES DE IDENTIDAD")
my_List = [1, 4, 5]
my_List2 = [1, 4, 5]
print(my_List is my_List2)
print(my_List is not my_List2) 

#Operadores de pertenencia
print("\nOPERADORES DE PERTENENCIA")
mis_frutas = ["manzana", "pera", "uva"]
print(f"¿En mis frutas poseo una naranja?: {'naranja' in mis_frutas}")
print(f"¿En mis frutas no poseo una sandía?: {'sandía' not in mis_frutas}")

#Operadores de bits
print("\nOPERADORES DE BITS")
a = 5 #0101
b = 3 #0011

print(f"AND: a & b = {a & b}")
print(f"OR: a | b = {a | b}")
print(f"XOR: a ^ b = {a ^ b}")
print(f"NOT: ~a = {~a}")
print(f"Desplazamiento a la izquierda: a << 1 = {a << 1}")
print(f"Desplazamiento a la derecha: b >> 1 = {b >> 1}")

"""
ESTRUCTURAS DE CONTROL
"""

#Condicionales
print("\nESTRUCTURAS DE CONTROL CONDICIONALES")
mi_prueba = "Taller"
if mi_prueba == "Examen":
    print("¡Es un examen!")
elif mi_prueba == "Tarea":
    print("¡Es una tarea!")
else:
    print("No es un examen ni una tarea.")

#Bucles o iterativas
print("\nESTRUCTURAS DE CONTROL ITERATIVAS")

for i in range(12):
    print(i)

i = 0

while i < 5:
    print(i)
    i += 1

#Manejo de excepciones
print("\nESTRUCTURAS DE CONTROL DE EXCEPCIONES")
try:
    print(17 / 2)
except:
    print("Se ha producido un error, no es posible dividir entre cero.")
finally:
    print("Se ha finalizado el manejo de excepciones.")