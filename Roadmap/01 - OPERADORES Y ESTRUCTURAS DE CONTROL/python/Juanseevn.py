#OPERADORES MATEMÁTICOS
num1 = 6
num2 = 3

suma = num1 + num2
print(f"Suma: {suma}")

resta = num1 - num2
print(f"Resta: {resta}")

producto = num1 * num2
print(f"Producto: {producto}")

division = num1/num2
print(f"División: {division}")

residuo = num1%num2
print(f"Residuo: {residuo}")

#OPERADORES LÓGICOS
true=True
false=False

print(true and false)
print(true or false)
print(not false)

#OPERADORES DE COMPARACIÓN
num3 = 10
num4 = 5

print(f"true == false es {true==false}")
print(f"true != false es {true!=false}")
print(f"{num3} > {num4} es {num3>num4}")
print(f"{num3} < {num4} es {num3<num4}")

#OPERADORES DE ASIGNACIÓN
x=9
print(f"x=9, {x}")
x+=1
print(f"x+=1, {x}")
x-=2
print(f"x-=2, {x}")
x*=3
print(f"x*=3, {x}")
x/=2
print(f"x/=2, {x}")
x**=2
print(f"x**=2, {x}")

#OPERADORES DE IDENTIDAD

print(f"10 is 5 es {num3 is num4}")
print(f"10 is not 5 es {num3 is not num4}")

#OPERADORES DE MEMBRESÍA

lista = {1,2,3,4,5}

print(f"1 in lista es {1 in lista}")
print(f"6 not in lista es {6 not in lista}")

#ESTRUCTURAS CONDICIONALES

lista = {6,7,8,9,10}

if 10 in lista:
    print("10 se encuentra dentro de la lista")
elif 10 not in lista:
    print("10 no se encuentra dentro de la lista")
else:
    print("Demás eventos")
    
#ESTRUCTUA DE BUCLE

lista = {6,7,8,9,10}

for i in lista:
    print(i)

j=0
    
while j<5:
    print(j)
    j+=1

#ESTRUCTURA DE EXCEPCIONES
x=10
y=0

try:
    x/y
except ZeroDivisionError:
    print("No se puede dividir entre cero")
    
    
#CASO
limiteMin=10
limiteMax=56

print("\nCASO PROPUESTO")

for m in range(limiteMin, limiteMax):
    
    if(m%2==0 and m!=16 and m%3!=0):
    
        print(m)