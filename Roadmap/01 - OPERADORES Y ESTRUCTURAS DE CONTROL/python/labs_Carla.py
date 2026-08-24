'''
Operadores
'''

#Operadores aritméticos

print(f"Suma: 5 + 5 = {5+5}")
print(f"Resta: 5 - 5 = {5-5}")
print(f"Multiplicación: 5 * 5 = {5*5}")
print(f"División: 5 / 5 = {5%5}")
print(f"Módulo 5 % 5 = {5%5}")
print(f"Exponente: 5**5 = {5**5}")
print (f"División entera 5//5 = {5//5}")

#Operadores de comparación

print(f"Igualdad: 10==3 es {10==3}")
print(f"Desigualdad: 10 != 3 {10!=3}") #es diferente de
print(f"Mayor qué: 10>3 {10>3}") #es mayor qué
print(f"Es menor qué: 10<3 {10<3}") 
print(f"Es mayor o igual que 10>4= {10>=3}") #True
print (f"Es menor o igual que 10<=3 {10<=3}") #False

#Operadores lógicos

print (f"AND &&: 10 > 5 and 5-2 {10 > 5 and 5-2}")
print (f"OR ||: 10 > 3  or 5-1 {10 > 3 or 5-1}")
print (f"NOT !: 10 == 14 {not 10==14}")

#Operadores de asignación 

my_number = 11 #asigno valor a una variable
print(my_number)
my_number += 1 #suma y asignación
print(my_number)
my_number -= 1 #resta y asignación
print(my_number)
my_number *= 3 #multiplicación y asignación
print(my_number)
my_number /= 1 #división y asignación
print(my_number)
my_number %= 2 #módulo y asignación
print(my_number)
my_number **= 2 #exponente y asginación
print(my_number)
my_number //= 2 #divisón entera
print(my_number)

#Operadores de identidad 

my_new_number = my_number
print(f"my_number is  my_number es {my_number is  my_new_number }")#compara posiciones en memoria true 
print (f"my_number is not my_new_number {my_number is not my_new_number}") #false   

#Operaciones de pertenencia

print(f"'C' in Carla {'C' in "Carla"}")
print(f"'x' not in Carla {'x' not in "Carla"}") 

#Operadores de bits

"""
Se usan mayormente para:
criptografía
compresión
protocolos HTTP/TCP
parsers binarios
procesamiento de imágenes
drivers
sistemas operativos
videojuegos
IoT
hardware
"""

a = 10 # 0010
b = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3 }")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"N0T: ~ ={~10} ")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10>>2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {10<<2}")

#Estructuras de control

#Condicionales

my_star_sign =  "Virgo"

if(my_star_sign == "Virgo"):
    print("El regente de Virgo es Mercurio")
elif my_star_sign == "Géminis":
    print("El regente de Géminis también es Mercurio")
else:
    print("Si no sabes tu signo, saca tu carta astral en astrea.charts.site")

#Iterativas

for i in range(13): #12 signos zodiacales
    print(i)

i = 0 

while i <= 12: #12 signos zodiacales si i=0
    print(i)
    i+=1

#Manejo de excepciones

try:
    print (10/0)
except:
    print ("No existe la división por 0, checa tus matemáticas.")
finally:
    print ("Se finaliza el manejo de errores")


# Extra 

for i in range(10,56):
    if (i%2==0 and i%3==0 and i!=16):
        print(i)
    


