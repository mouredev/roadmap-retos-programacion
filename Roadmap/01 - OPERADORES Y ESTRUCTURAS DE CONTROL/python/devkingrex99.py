""""""
#operadores

""""""
# Operadores aritmeticos
print(f"Suma: 10 + 5 = {10 + 5}")
print(f"Resta: 10 - 5 = {10 - 5}")
print(f"Multiplicacion: 10 * 5 = {10*5}")
print(f"Division: 10 / 5 = {10/5}")
print(f"Modulo: 10 % 5 = {10%5}")
print(f"Exponente: 10 ** 5 = {10**5}")
print(f"division entera: 10 // 5 = {10//5}")
      
#operadores de comparacion
print(f"Igualdad: 10 == 5 = (10 == 5)")
print(f"desigualdad: 10 != 5 = {10 != 5}")
print(f"mayor que: 10 > 5 = (10 > 5)")
print(f"menor que: 10 < 5 = {10 < 5}")
print(f"mayor o igual que: 10 >= 5 = {10 >= 5}")
print(f"menor o igual que: 10 <= 5 = {10 <= 5}")

#operadores logicos
print(f"and 66:10 + 8 > 5 and 10 - 2 < 5 = {(10 + 8 > 5) and (10 - 2 < 5)}")
print(f"or 66: ll + 8 > 5 or 10 - 2< 5 = {(10 + 8 > 5) or (10 - 2 < 5)}")
print(f"not 66: !(10 + 8 > 5) + not(10 - 2 < 5) = (not(10 + 8 > 5) + not(10 - 2 < 5)")

#operadores de asignacion
my_number = 10
print(my_number)
my_number += 1 #suma y asignacion
print(my_number)
my_number -= 1 #resta y asignacion
print(my_number)
my_number *= 1 #multiplicacion y asignacion
print(my_number)
my_number /= 1 #division y asignacion
print(my_number)
my_number %= 1 #modulo y asignacion
print(my_number)
my_number **= 1 #exponente y asignacion
print(my_number)
my_number //= 1 #division entera y asignacion

#operadores de identidad
my_new_number = 1.0
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#operadora de pertenencia
print(f"'u' in 'moure' = {'u' in 'mouredev'}")
print(f"'u'not in'moure'= {'u'not in 'mouredev'}")

#operadores de bit
a= 10 #1010
b= 3 # 00 01 10 
print("and: = 10 & 3 = {10 & 3}") #0010
print("or:= 10 & 3 {10 & 3}") #1011
print("xor:= 10 & 3 {10 & 3}") #1101
print(f"desplazamiento a la derecha: 10 >> 3 = {10 >> 3}") #0001
print(f"desplazamiento a la izquierda: 10 << 3 = {10 << 3}") #1010000


""""""
#estructuras de control
""""""
#condicionales

my_string = "Mouredev"

if my_string == "Mouredev":
    print("my_string es 'Mouredev'")
elif my_string == "Python":
    print("my_string es 'Python'")
else:
    print("my_string no es 'Mouredev' ni 'Python'")

#iteraciones
for i in range(11):
    print(i)
i = 1
while i <= 10:
    print(i)
    i += 1

    #manejo de excepciones
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("ha finalizado el manejo de excepciones")

for number in range(18, 56):
    print(number)
    if number % 2 == 0 and number != 16 and number % 3 != 0 :
        print(number)