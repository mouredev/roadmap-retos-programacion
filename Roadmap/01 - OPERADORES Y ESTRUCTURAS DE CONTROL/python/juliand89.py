#operadores aritmeticos

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3:2f}")
print(f"Modulos: 10 % 3 = {10 % 3:2f}")
print(f"Exponenciacion: 10 ** 3 = {10**3}")
print(f"Division entera : 10 // 3 = {10 // 3}")

#Operadores de comparacion 
print(f"Igualdad: 2 == 3 = {2==3}")
print(f"Desigualdad 2 != 3 = {2!=3}")
print(f"Mayor que: 2 > 3 = {2>3}")
print(f"Menor que: 2 < 3 = {2<3}")
print(f"Moyor o igual que: 2 >= 3 = {2>=3}")
print(f"Menor o igual que: 2 <= 3 = {2<=3}")

# operadores Logicos
print(f"AND: 10 + 3 == 13 and 5 - 1 == 4 es {10+3 == 13 and 5-1 == 4}")
print(f"OR: 10 + 3 == 13 or 5 - 1 == 5 es {10+3 == 13 or 5-1 == 5}")
print(f"NOT: not 10 + 3 == 13 es {not(10+3 == 13)}")

#operadores de asignacion 
number = 89
print(number)
number += 1
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number %= 2
print(number)
number //= 1
print(number)
number **= 1
print(number)

#operadores de identidad
new_number = number
print(f"IS: new_number is number es {new_number is number}")
print(f"IS NOT: new_number is not number es {new_number is not number}")

#operadores de menbresia 
print(f"IN: 'j' in 'julian' =  {'j' in 'julian'}")
print(f"NOT IN: 'y' not in 'julian' =  {'y' not in 'julian'}")

#Operadores de Bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # Establece cada bit en 1 si ambos bits son 1 0010 = 2
print(f"OR: 10 | 3 = {10 | 3}") # Establece cada bit en 1 si uno de los dos bits es 1  1011 = 11
print(f"XOR: 10 ^  3 = {10 ^  3}") # Establece cada bit en 1 si solo uno de los dos bits es 1 1001 = 9

#Estructuras de control 

# if, elif y else
edad = 15
if edad >= 30:
    print("Puede ver la pelicula con descuento")
elif edad >= 18:
    print("Puede ver la pelicula")    
else:
    print("No puede ingresar")

# For 
buscar = 4
for numero in range(5):
    print(numero)
    if numero == buscar: 
        print (f"Encontre el numero {buscar}")
        break
else:
    print(f"No encontre el numero {buscar}")

#while    
numero = 1
while numero < 10:
    print(numero)
    numero +=1  
# ejercicio
c = 10
while c < 56:
    if (c % 2 == 0 and c != 16 and c % 3 != 0):
        print(c)
    c +=1