
#Operadores aritméticos

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Residuo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

#Operadores de comparacion

print(f"Igualdad: 10==5 {10==5}")
print(f"Diferencia: 10!=5 {10!=5}")
print(f"mayorque: 10>5 {10>5}")
print(f"menorque: 10<5 {10<5}")
print(f"mayoroigualque: 10>=5 {10>=5}")
print(f"menoroigualque: 10<=5 {10<=5}")

#operadores logicos

print(f"and &&: 10>5 and 5>3 {10>5 and 5>3}")
print(f"or ||: 10>5 and 5>3 {10<5 or 5>3}")
print(f"not !: 10+3=14 {not(10+3==14)}")

#operadores de asignación
num=15
print(num)
num+=2
print(num)
num-=2
print(num)
num*=2
print(num)
num/=2
print(num)
num%=12
print(num)
num**=2
print(num)
num//=2
print(num)

#operadores de identidad
num2=num
print(f"num is num2 es {num is num2}")
print(f"num is not num2 es {num is not num2}")

#operadores de pertenencia

print(f"v in victor {'v' in 'victor'}")
print(f"b in victor {'b' in 'victor'}")

#operadores de bits


a=10
b=3

print(f"and &: 10 and 3 es: {10&3}")#compara los numeros a nivel de bits y si ambos bits son 1 el bit resultante es 1 de lo contrario es 0
print(f"or |: 10 | 3 es: {10|3}")# con que haya 1 al comparar el bit será 1
print(f"xor ^: 10 ^ 3 es: {10 ^ 3}")# si los bits son iguales es 1, si son diferentes es 0
print(f" ~a es {~a}")
print(f"Desplazamiento a la derecha 10>>2 {10>>2}")
print(f"Desplazamiento a la izquierda 10<<2 {10<<2}")

#estructuras de control
#condicionales

nombre="Andres"
if nombre=="victor":
    print(f"Mi nombre es:{nombre}")
elif nombre=="Andres":
    print(f"Entonces mi nombre es: {nombre}")
else:
    print("Mi nombre no es Victor")

#iterativas

for i in range(11):
    print(i)

i=0
while i <= 10:
    print(i)
    i += 1

#manejo de exepciones

try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

#EJERCICIO DE DIFICULTAD EXTRA

for i in range(10,56):
    if i%2==0 and i%3!=0 and i!=16:
     print(f"[{i}]",end="")