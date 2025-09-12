'''
Operadores
'''

#Operadores aritméticos
print(f"Suma:15 + 5 = {15 + 5}")
print(f"Resta:250 - 30 = {250 - 30}")
print(f"Multiplicación:2*3 = {2 * 3}")
print(f"División: 10/30 = {10 / 3}")
print(f"Módulo: 10%30 = {10 % 30}")
print(f"Exponente: 5**2 = {5 ** 2}")
print(f"División entera: 10//30 = {10 // 3}")

#Operadores de comparación
print(f"Igualdad: Juan == Puan = {'Juan' == 'Juan'}")
print(f"Igualdad: Juan != Pedro = {'Juan' != 'Pedro'}")
print(f"Mayor que: 8 > 9 = {8 > 9}")
print(f"Menor que: 8 < 9 = {8 < 9}")
print(f"Mayor que: 8 >= 8 = {8 >= 8}")
print(f"Menor que: 8 <= 12 = {8 <= 2}")

#Operadores lógicos
print(f"AND &&: 3 == 3 and 8 < 10 es { 3 == 3 and 8 < 10}")
print(f"OR ||: 3 > 3 or 2 > 1 es {3 > 3 or 2 > 1}")
print(f"NOT !: not 3 + 3 == 9 es {not 3 + 3 == 9}")

#Operadores de asignación
my_data = 'Hola' #Asignación
print(my_data)
my_data += ' mouredev' #Contenar "suma" y asignación
print(my_data) 
new_data = 10 #Asignación y asignación
print(new_data)
new_data -= 5 #Resta y asignación
print(new_data)
new_data *= 5 #Multiplicación y asignación
print(new_data)
new_data /= 5 #División y asignación
print(new_data)
new_data %= 3 #Módulo y asignación
print(new_data)
new_data **= 5 #Módulo y asignación
print(new_data)
new_data //= 3 #División entera y asignación
print(new_data)

#Operadores de identidad
my_new_data = new_data
print(f"my_new_data is new_data es {my_new_data is new_data}")
print(f"my_new_data is not new_data es {my_new_data is not new_data}")

#Operadores de pertenencia
print(f" 'a' in 'carlos' = {'a' in 'carlos'}")
print(f" 'e' not in 'carlos' = {'e' not in 'carlos'}")

#Operadores de bit
x = 10 #1010
y = 3 #0011
print(f"AND: 10 & 3 = {10 & 3}") #0010 que es 2
print(f"OR: 10 | 3 = {10 | 3}") #1011 que es 11
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001 que es 9
print(f"NOT: ~10 = {~10}") # que es -11
print(f"Desplazamiento a la derecha: 10>>2 = {10>>2}") #0010 que es 2
print(f"Desplazamiento a la izquierda: 10<<2 = {10<<2}") #101000 que es 40

'''
Estructuras de control
'''

#Condicionales
is_empty = True
if is_empty == True:
    print("Está vacío")
#elif
else:
    print("No está vacío")

#Iterativas
for i in range(11):
    print(i)
    
i = 0

while i <= 10:
    print(i)
    i += 1
    
#Manejo de excepciones
try:
	print(10/0)
except: 
    print("Error en el programa")
finally:
    print("Ha finalizado el manejo de excepciones")

'''
Extra
'''

for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
    	print(i)