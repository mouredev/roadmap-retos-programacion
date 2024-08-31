#EJEMPLOS DE OPERADORES

#Aritméticos
num1 = 2
num2 = 3
num3 = 6
num4 = 15
print(f"{num1} + {num2} = {num1+num2}") #suma
print(f"{num3} - {num2} = {num3-num2}") #resta
print(f"{num3} / {num2} = {num3/num2}") #división
print(f"{num1} * {num2} = {num1*num2}") #multiplicación
print(f"{num1} ^ {num2} = {num1**num2}") #potencia
print(f" {num4} mod {num3} = {num4%num3}") #módulo
print(f"El cociente de {num4}/{num3} es {num4//num3}") #cociente entero

#Lógicos
a = True
b = False
    #El operador and solo devuelve true si los dos valores son true
print(f"{a} and {b} es {a and b}")
print(f"{a} and {a} es {a and a}")
print(f"{b} and {b} es {b and b}")
    #El operador or devuelve true si al menos uno de los dos valores es true
print(f"{a} or {b} es {a or b}")
print(f"{a} or {a} es {a or a}")
print(f"{b} or {b} es {b or b}")
    #El operador not devuelve true si el valor es false y false si el valor es true
print(f"not {a} es {not a}")
print(f"not {b} es {not b}")

#Comparativos
x = 2
y = 3
z = 2
    #El operador == devuelve true si ambos valores son iguales
print(f"{x} == {y} es {x==y}")
print(f"{x} == {z} es {x==z}")
    #El operador != devuelve true si ambos valores no son iguales
print(f"{x} != {y} es {x!=y}")
print(f"{x} != {z} es {x!=z}")
    #El operador < devuelve true si el primer valor es menor que el segundo
print(f"{x} < {y} es {x<y}")
print(f"{y} < {x} es {y<x}")
    #El operador > devuelve true si el primer valor es mayor que el segundo
print(f"{x} > {y} es {x>y}")
print(f"{y} > {x} es {y>x}")
    #El operador <= devuelve true si el primero es menor o igual que el segundo
print(f"{x} <= {y} es {x<=y}")
print(f"{y} <= {x} es {y<=x}")
print(f"{z} <= {x} es {z<=x}")
    #El operador >= devuelve true si el primero es mayor o igual que el segundo
print(f"{x} >= {y} es {x>=y}")
print(f"{y} >= {x} es {y>=x}")
print(f"{z} >= {x} es {z>=x}")
#Asignación
    #El operador = asigna un valor a una variable
var1=36
print(f"La variable var1 tiene el valor de {var1}")
    #Los operadores +=, -=, *=, /=, %=, //=, **/ son equivalentes a:
x = 2
y = 12
print(f"El valor inicial de x es {x}")
x += 1
print(f"x += 1 es igual a x = x + 1 = {x}")
x -= 2
print(f"x -= 1 es igual a x = x - 2 = {x}")
x *= 9
print(f"x*= 9 es igual a x = x * 9 = {x}")
x /= 3
print(f"x /= 3 es igual a x = x / 3 = {x}")
x %= 2
print(f"x %= 2 es igual a x = x % 2 = {x}")
print(f"El valor inicial de y es {y}")
y //= 5
print(f"y //= 5 es igual a y = y // 5 = {y}")
y **= 3
print(f"y **= 3 es igual a y = y ** 3 = {y}")

#Identidad
    #El operador is devuelve true si dos variables hacen referencia al mismo objeto
    #no se debe confundir con el operador ==
a = 10
b = 10
print(f" a is b es {a is b}")
a = [1,2,3]
b = [1,2,3]
print(f" a is b es {a is b}")
    #El operador is not hace lo contrario que is
a = 10
b = 10
print(f" a is not b es {a is not b}")
a = [1,2,3]
b = [1,2,3]
print(f" a is not b es {a is not b}")

#Pertenencia
    #El operador in nos devuelve true si el elemento se encuentra dentro de una secuencia iterable
num = 3
lista1 = [1,2,3]
lista2 = [1,2,4]
print(f"3 in lista 1 es {num in lista1}")
print(f"3 in lista 2 es {num in lista2}")
    #El operador is not hace lo contrario
print(f"3 not in lista 1 es {num not in lista1}")
print(f"3 not in lista 2 es {num not in lista2}")
#EJEMPLOS DE ESTRUCTURAS DE CONTROL

#Condicionales
    #if/else es utilizado para controlar diferentes situaciones, si la condición que precede al if
    #es verdadera el codigo siguiente se ejecuta, sino se ejecutará el codigo de dentro del else
a = 5
b = 6
if a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es menor que {b}")
    #también se puede hacer uso de los elif para contar con más de dos escenarios
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual que {b}")

#Iterativas
    #bucle for: el codigo se ejecutará el numero de veces definido en el for
for i in range(1,11): #contar hasta diez
    print(i)
    #bucle while: el codigo se ejecutará mientras la condición se cumpla
a = 0
while a < 5:
    a += 1
    print(a)

#Excepciones
    #try/except: utililzado para controlar posibles errores en el codigo sinque el programa se detenga
try:
    c = 3/0
except Exception:
    print("Error")

'''Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''

for i in range(10,57,2):
    if (i != 16) and ((i%3) != 0):
        print(i)