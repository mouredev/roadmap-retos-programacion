#Operadores Aritmeticos

valor1 = 20
valor2 = 22
resultado = valor1 + valor2

print(f"La suma de {valor1} + {valor2} = {resultado}")


print(f"La Suma de 8 + 7 =  {8+7}")
print(f"La Resta de 10 - 2 = {10-2}")
print(f"La Multiplicacion de 8 x 7 =  {8*7}")
print(f"La Division de 10 / 2 = {int(10/2)}")
print(f"El residuo de 16 % 3 es {16 % 3}")
print(f"Exponente de  10 ^ 2 = {10**2}")
print(f"La Division entere de 16 // 3 =  {16 // 3}")


#operadores de comparacion
print (f"Igualdad: 4 == 2 es {4 == 2}") #compara si 4 es igual 2, si es igual pone true, sino false
print (f"Desigualdad: 4 != 2 es {4 != 2}")
print (f" 4 > 2 = {4 > 2}") #mayor que
print (f" 4 < 2 = {4 < 2}") #menor que 
print (f" 4 >= 2 = {4 >= 2}") #mayor o igual que
print (f" 4 <= 2 = {4 <= 2}") #menor o igual que


#operadores logicos
print(f"AND &: 20 == 10 AND 7 - 2 == 5  = {20 == 10 and 7 - 2 == 5} ")
print(f"or ||: 20 == 10 or 7 - 2 == 5  = {20 == 10 or 7 - 2 == 5} ")
print(f"NOT !: 20 + 20 == 50 {not 20 + 20 == 50} ")


#operadores de asignacion
cantidad = 12
print(cantidad)
cantidad +=1 #suma y asignacion 
print(cantidad)
cantidad -= 1 #restq y asignacion
print(cantidad)
cantidad *=2 #multipliclacion y asignacion
print(cantidad)
cantidad /=3 #division y asignacion
print(int(cantidad))
cantidad %=3 #modulo y asignacion
print(int(cantidad))
cantidad **=3 #exponente y asignacion
print(int(cantidad))
cantidad //=3 #division entera y asignacion



"""operadores de identidad: Son operadores que comparan si dos variables apuntan al mismo objeto en memoria, 
no si su contenido es igual, sino si son el mismo objeto"""

nueva_cantidad  = 8
print(f"cantidad es mi nueva_cantidad: {cantidad is nueva_cantidad}") #false 


nueva_cantidad  = cantidad
print(f"cantidad es mi nueva_cantidad: {cantidad is nueva_cantidad}") #true
print(f"cantidad no es mi nueva_cantidad: {cantidad is not nueva_cantidad}") #False



#Operadores de pertenencias

print(f"p in Complex:{'p' in 'Complex'}") #la letra p esta en la palabras "Complex"? en este casi si, por lo que devuelve true
print(f"p in Complex:{'p' not in 'Complex'}") #false


#operadores de bit
a = 10 #1010
b = 3 #0011
print(f"AND: 10 & 3 = {10 & 3}") #LOS DOS TIENE QUE SER 1. #EL RESULTADO SERIA: 0010 (2) EN BIT
print(f"OR: 10 | 3 = {10 | 3}") #AL MENOS UNO TIENE QUE SER 1. #EL RESULTADO SERIA: 1011 (11) EN BIT
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #SI LOS BIT SON DIFERENTE ES 1, SI SON IGUALES ES 0. #EL RESULTADO SERIA: 1001 (9) EN BIT
print(f"NOT: ~10 = {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #10 (1010) si lo desplamazamos 2 veces a la dercha seria = 2 (0010)
print(f"Desplazamiento a la izquiera: 10 << 2 = {10 << 2}") #10 (1010) si lo desplamazamos 2 veces a la dercha seria 101000 (40)


#Estructura de control

#condicionales

year = 2024

if year == 2025:
    print("El año es 2025")
elif year < 2025:
    print("El año ya paso")
else:
    print("El año no es 2025")


#iterativas

for i in range(11):
    print(i)


i = 0

while i <= 10:
    print(i)
    i +=1


#manejo de excepciones
try:
    print(10/0)
except:
    print("No se puede dividir entre 0")
finally:
    print("Ha finalizado el manejo de excepciones")


'''
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. '''




for num in range(10, 56):
    if num % 2 ==0 and num != 16 and num % 3 != 0:
        print(num)