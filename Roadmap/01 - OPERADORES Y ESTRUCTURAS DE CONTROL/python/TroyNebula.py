#!/usr/bin/env python

''' 
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
'''
 # Debes hacer print por consola del resultado de todos los ejemplos.

print("***Operadores Aritméticos***")
print ("suma 1+2=",(1+2),"\n""resta 2-1=",(2-1),"\n""multiplicación 2*2=",(2*2),"\n""división 10/3=" ,(10/3),"\n""devuelve resto de división 10/3=" ,(10%3),"\n""división sin decimales 10/3=",(10//3),"\n""exponenciación 3 elevado a 3=",(3**3))
print(f"Suma: 10 + 3 = {10 + 3}")  # una sola línea por operador y más limpio
print()
# 
print("***Operadores de Comparación***")  # Devuelven booleano    
print("¿Es 1 igual a 1?:",(1==1),"\n""¿2 es diferente de 3?=",(2!=3),"\n""¿Es 10 mayor que 1?:",(10>1),"\n""¿Es 10 menor que 1?:",(10<1),"\n""¿Es 1 mayor o igual que 1?:",(1>=1),"\n""¿Es 2 menor o igual que 1?:",(2<=1),"\n")

print("***Operadores Lógicos***")
Uno=1
print(f"1=1 y 2+2=4: {(1==1) and (2+2==4)},\n1=1 o 2+3=4: {(1==1) or (2+3==4)},\nUno no es 3: {not Uno == 3}")
print()

print("***Operadores de asignación***")
variable=10
print ("Mi variable es:",variable)
print ("Mi variable es al sumarle 1:",variable+1) # suma y asignación
variable -=1 # resta y asignación
print ("Mi variable es al restarle 1:",variable)
print("... También podemos combinar con los demás operadores aritméticos como **= etc.")
print()

print ("vOperadores de Identidad***")  # comparan valores de la posición de memoria no de la variable
nueva_variable= variable
print ("Mi nueva variable es igual a variable:",(nueva_variable is variable))
print ("Mi nueva variable no es igual a variable:",(nueva_variable is not variable))
print()

print ("***Operadores de pertenencia***")  # si algo existe en otro conjunto
print(f"'u' está en Nebula: {"u" in "Nebula"}")
print(f"'h' no está en Nebula: {"h" not in "Nebula"}")
print()

print ("***Operadores de Bit***")
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 1010
print()

''' 
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
 '''
 # Debes hacer print por consola del resultado de todos los ejemplos.

print("***Estructuras de control***")
print("***Condicionales***")

mi_string = "Nebula"
if mi_string == "Nebula":
    print("mi_string es 'Nebula'")
elif my_string == "Troy":
    print("mi_string es 'Troy'")
else:
    print("mi_string no es ni 'Nebula' ni 'Troy'")
print()

print("***Iterativas***")
print("Deben salir del 0 al 5:")
for i in range(6):
    print(i)
i = 0
while i <= 5:
    print(i)
    i += 1
print()

print("***Manejo de excepciones***")
try:
    print(10 / 0)  #intenta
except:
    print("¡¡Se ha producido un error!!")  #si no funciona
finally:
    print("Ha finalizado el intento/manejo de excepciones")  #sí o sí cuando acabe la excepción
print()

'''DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''

print ("***Números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3:***")
def numeros_pares():
    for num in range (10,56):
        if num % 2 ==0 and num !=16 and num %3!=0:
            print (num)

numeros_pares()
            
