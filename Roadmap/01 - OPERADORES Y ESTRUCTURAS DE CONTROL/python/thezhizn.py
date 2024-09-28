'''
lista de operadores en python 
'''

# 1= operadores aritmeticos, calculo matematico:
print(f"sumas 2+2={2 + 2}")
print(f"restas 3-1={3 - 1}")
print(f"multiplicacion 2*4={2 * 4}")
print(f"divición 8/3={8 / 3}") 
print(f"modulo 100%5={100 % 5}")
print(f"exponencial / potencia 4**2={4 ** 2}")
print(f"divicion con resultado entero 17//3={17 // 3}")

# operadores racionales: comparan y establecen relaciones
print(f"6 mayor que 3={3 < 6}")
print(f"3 menor que 6={3 > 6}")
print(f"4 igual que 4={4 == 4}")
print(f"8 mayor o igual que 8={8 <= 8}")
print(f"3 menor o igual que 6={3 >= 6}")
print(f"8 desigual que 5={8 != 5}") 
    
# operadores de asignacion: asignan a la variable
a = 10
print(a)
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a //= 2
print(a)
a %= 3
print(a)

# operadores logicos 
print(f"NOT niega y en caso de que lo que niega sea falso, entonces seria cierto que es falso= {not 5==6}")
print(f"OR tiene que cumplirse almenos una: 4 + 1 == 5 or 10 > 15={4 + 1 == 5 or 10 > 15}")
print(f"AND tienen que cumplirse ambas condiciones: 8 < 9 and 16/8 <= 8={8 < 9 and 16/8 <= 8}")

# operadores de pertenencia
print(f"'IN se puede usar para decir que la letra 'h' esta en 'thezhizn'={"h" in "thezhizn"}")
print(f"IN NO se puede usar para decir que la 's' no esta en hola ={"s" not in "hola"}")

# operadores de identidad
my_variable = 2.0 
print(f"IS sirve para ver si lo que se compara comparte memoria a is my_variable = {a is my_variable}")
print(f"IS NOT sirve para saber si no comparten la memoria a is not my_variable = {a is not my_variable}")

# operadores de bit a bit: trata de binario 
x = 5 # 0101
y = 3 # 0011
print(f"AND se representa con '&' = {x & y}")
#compara los binarios y escribe 1 si comparten un 1 si no escribe un 0
print(f"OR se representa con '|' = {x | y}") 
#compara los binarios y si almenos uno de los dos es 1 escribe 1 
print(f"XOR se representa con '^' = {x ^ y} ")
#compara los binarios, si los numeros son diferentes escribe uno y si no es 0
print(f"NOT se representa con '~' = {~ x}")
# invierte los numeros del binario 
print(f"desplazamiento a la derecha '>>' = {x >> y}")
#desplaza los numeros de X la candidad de Y posiciones a la derecha
print(f"desplazamiento a la izquierda '<<' = {x << y}")
# desplaza las numero de X la cantidad de Y posiciones a la izquierda
 
# estructuras de control condicionales 
my_number = 14

if my_number * 3 == 32: 
    print("Es 32")
elif my_number * 3 == 42:
    print("El resultado es 42")
else:
    print("no es 32 ni es 42")

# estructuras de control interactivas
for t in range(7):
    print(t)
t = 0 

while t <= 7:
    print(t)
    t += 1

# estructuras de control excepciones 
try:
    print("t"/2)
except:
    print("oh parece que fallamos")
finally:
    print("ya lo hemos resuelto")

# ejercicio extra 
for m in range(10 , 56):
    if m % 2 == 0 and m != 16 and m % 3 != 0:
      print(m)
