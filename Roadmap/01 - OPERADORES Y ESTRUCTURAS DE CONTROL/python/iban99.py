#Tipos de operadores
    #Comparación
print(f"10 es más grande que 3, es {10 > 3}")
""" 
2 == 3
98 <= 100
98 >= 100
76 < 0
76 > 0 
75 != 1 """

    #Lógicos
""" True AND && False
True OR || False
True NOT !: False """

    #Aritméticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Mult: 10 / 3 = {10 / 3}")
print(f"Div: 10 * 3 = {10 * 3}")
print(f"Mod: 10 % 3 = {10 % 3}")
print(f"Exp: 10 ** 3 = {10 ** 3}")
print(f"Suma: 10 // 3 = {10 // 3}")

    #Asignación
my_number = 11 #Asignación 
my_number += 1 #Asignación y suma
print(my_number) 
my_number -= 1 #Asignación y resta
print(my_number)
my_number *= 4 #Asignación y multiplicación
print(my_number) 
my_number /= 1 #Asignación y división
print(my_number) 
my_number %= 3 #Asignación y módulo
print(my_number) 
my_number **= 1 #Asignación y exponente
print(my_number) 
my_number //= 1 #Asignación y división entera
print(my_number)

    #Identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")
#Tener en cuenta la posición de memoria, aunque sea el mismo numero.

    #Pertenencia
print(f"'u' in moure = {'u' in 'moure'}") 
print(f"'b' not in moure = {'b' not in 'moure'}") 

    #Bit
a = 10 # 1010
b = 3 # 0011
#Los operadores binarios van a convertir el numero a bits para hacer operaciones
print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: 10 ~ 3 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplaxamiento a la izquierda: 10 << 2 = {10 << 2}")


#Estructuras de control
    #Condicionales
my_string = "MoureDev"

if my_string == "MoureDev":
    print("my_String es MoureDev")
elif my_string == "Brais":
    print(("my_String es Brais"))
else:
    print("my_String no es MoureDev")


    #Iterativas
for i in range(11):
    print(i)


i = 0
while i <= 10:
    print(i)
    i += 1
    

    #Manejo de Excepciones
try:
    print(10/1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
    

#Dificultad extra
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number  % 3 == 0:
        print(number)