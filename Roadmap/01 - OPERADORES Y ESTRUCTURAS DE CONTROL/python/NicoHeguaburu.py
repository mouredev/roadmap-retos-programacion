


#aritmeticos
x = 3
y = 6

suma = x + y
print (suma)

resta = x - y
print (resta)

dividir = x / y 
print (dividir)

multiplicar = x * y
print (resta)

dividir_enteros = x // y
print(dividir_enteros)

exponente = x ** y
print(exponente)

resto = x % y
print(resto)


#logicos
#and
print (True and True) 
print (False and False)
print (True and False)
print (False and True)


#or 
print (True or True)
print (False or False)
print (True or False)
print (False or True)


#not
print (not True)
print (not False)


#comparacion
igual = 5 == 5
print(igual)

diferente = 5 != 5
print(diferente)

mayor = 5 > 3
print(mayor)

menor = 5 < 9
print(menor)

mayor_igual = 5 >= 5
print(mayor_igual)

menor_igual = 5<= 1
print(menor_igual)


#asignacion

#simple
z = 3
print(z)

#suma
z += 4
print(z)

#resta
z -= 8
print(z)

z *= 2
print(z)

z /= 2
print(z)

#identidad
a = 25
b = 2

print(a is b)
print(a is not b)


#pertenecia
print("n" in "nicolás")
print("x" in "nicolás")

print("n" not in "nicolás")
print("x" not in "nicolás")

#bits
x = 5               # 5 = 101 en bit
y = 3               # 3 = 011 en bit

print(x & y)      #AND bit a bit
print(x | y)      #OR  bit a bit
print(x ^ y)      #XOR bit a bit
print(~ x)        #NOT bit a bit
print(x << 1)     #dezplazar a la izq en bit 
print(x >> 1)     #dezplazar a la der en bit





#ESTRUCTURAS DE CONTROL

#condicionales
x = 10
y = 20
if x > y:
    print("X ES MAYOR A Y")
elif x == y: 
    print("X ES IGUAL A Y")
else:
    print("X ES MENOR A Y")


#iteraciones
for i in range(11):
    print(i)

y = 8
while y <= 10:
    print(y)
    y += 1


#excepciones
try:
    print(10 / 10)
except:
    print("hay un error")
finally:
    print("se a completado la operacion")


#DIFICULTAD EXTRA
i = 10
while i <= 55:
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print (i)
        i += 1
    else:
        i += 1 