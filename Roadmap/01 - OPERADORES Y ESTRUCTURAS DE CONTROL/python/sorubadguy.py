num1 = 2
num2 = 10
num3 = 100
#Operadores Aritmeticos

print(f"suma: {num1} + {num2} = {num1 + num2}")
print(f"resta: {num2} - {num1} = {num2 - num1}")
print(f"multiplicacion: {num1} * {num2} = {num1 * num2}")
print(f"divicion: {num2} / {num1} = {num2 / num1}")
print(f"suma: {num1} + {num2} = {num1 + num2}")
print(f"modulo: {num2} % {num1} = {num2 % num1}")
print(f"exponente: {num1} ** {num2} = {num1 ** num2}")
print(f"division entera: {num3} // {num2} = {num3 // num2}")

#Operadores de comparacion

print(f"igual que: {num1} == {num2} = {num1 == num2}")
print(f"distinto que: {num1} != {num2} = {num1 != num2}")
print(f"mayor que: {num1} > {num2} = {num1 > num2}")
print(f"menor que: {num1} < {num2} = {num1 < num2}")
print(f"mayor o igual que: {num1} >= {num2} = {num1 >= num2}")
print(f"menor o igual que: {num1} <= {num2} = {num1 <= num2}")

#Operadores Logicos

print(f"AND: {num1} + {num2} = {num3} and {num2} ** {num1} == {num3} = {(num1 + num2 == num3) and (num2 ** num1 == num3)}")
print(f"OR: {num1} + {num2} = {num3} or {num2} ** {num1} == {num3} = {(num1 + num2 == num3) or (num2 ** num1 == num3)}")
print(f"NOT: not {num2} ** {num1} == {num3} = {not(num2 ** num1 == num3)}")

#Operadores de Asignacion

num3 = num1 + num2
print(f"num3 = num1 + num2: {num3}")
num3 += num1
print(f"num3 += num1: {num3}")
num3 -= num1
print(f"num3 -= num1: {num3}")
num3 *= num1
print(f"num3 *= num1: {num3}")
num3 /= num1
print(f"num3 /= num1: {num3}")
num3 **= num1
print(f"num3 **= num1: {num3}")
num3 //= num1
print(f"num3 //= num1: {num3}")
num3 %= num1
print(f"num3 %= num1: {num3}")

#Operadores de Identidad

print(f"num1 is num3: {num1 is num3}")
print(f"num1 is not num3: {num1 is not num3}")

#Operadores de pertenencia

print(f"'b' in 'sorubadguy': {'b' in 'sorubadguy'}")
print(f"'b' not in 'sorubadguy': {'b' not in 'sorubadguy'}")

#Operadores de bit

num1 = 5  #0101
num2 = 10 #1010
print(f"AND: num1 & num2: {num1 & num2}") #0000
print(f"OR: num1 | num2: {num1 | num2}") #1111
print(f"XOR: num1 ^ num2: {num1 ^ num2}") #1111
print(f"NOT: ~num1: {~num1}") #1010
print(f"Desplazamiento hacia la izquierda: num1 << num2: {num1 << num2}")
print(f"Desplazamiento hacia la derecha: num1 >> num2: {num1 >> num2}")

#Estructuras de Datos

#Condicionales

if(num1 == num2):
    print(f"{num1} y {num2} son iguales")
elif(num1 == num2):
    print(f"{num1} y {num3} son iguales")
else:
    print("ningun numero es igual")

#Iteraciones

for i in range(10):
    print(i)

i=0

while i <= 10:
    print(i)
    i += 1

#manejo de exepciones

try:
    print(25/0)
except:
    print("se ha producido un error")
finally:
    print("fin del manejo de exepciones")

#Extra
i=0

for i in range(10,56):
    if(i % 2 == 0 and i % 3 != 0 and i != 16):
        print(i)