# Operadores Aritméticos
print("Operadores Aritméticos")

a = 1
b = 2
print(f"Suma:10+5={10+5}")#Suma
print(f"Resta:265-65={265-65}")#Resta
print(a*b)#Multiplicación
print(a/b)#División
print(a%b)#Módulo (resto de la división)
print(a**b)#Exponencial
print(b//a)#División con resultado entero

print("\n"*0)
#Operadores de Asignación
print("Operadores de Asignación")

c = 2
print(c)# =

c += 2
print(c)# +=

c -= 2
print(c)# -=

c *= 2
print(c)# *=

c /= 2
print(c)# /=

c %= 3
print(c)# %=

c //= 1
print(c)# //=

c **= 5
print(c)# **=

c = 1
c &= 2
print(c)# &=

c |= 2
print(c)# |=

c ^= 4
print(c)# ^=

c >>= 2
print(c)# >>=

c <<= 2
print(c)# <<=

c &= 2
print(c := 3)# :=

print("\n"*0)
# Operadores de Comparación
print("Operadores de Comparación")

d = 6
e = 15
print(d == e)# Igual

print(d != e)# No es igual

print(d < e)# Mayor que

print(d > e)#Menor que

print(d <= e)#Mayor o igual que

print(d >= e)# Menor o igual que

print("\n"*0)
#Operadores Lógicos
print("Operadores Lógicos")

f = 25
print (f > 15 and f < 2)

print (f > 15 or f < 2)

print (not(f > 15 and f < 2))

print("\n"*0)
#Operadores de Identidad
print("Operadores de Identidad")

g = 15
h = 32
print(g is h)
print(g is not h)

print("\n"*0)
#Operadores de Menbresía
print("Operadores de Membresía")

i = ["Melocotón", "Ciruela"]
print("Melocotón" in i)

i = ["Melocotón", "Ciruela"]
print("Melocotón" not in i)

print("\n"*0)
#Operadores de Bit a Bit
print("Operadores de Bit a Bit")

print(6 & 9)

print(6 | 9)

print(6 ^ 9)

print(6 << 9)

print(6 >> 9)

print(~ 9)

print("\n"*0)
#- crea ejemplos que representen todos los tipos de estructuras de control
print("Ejemplos de Estructuras de Control")

b = 14
c = 15

if c < b :
    print("c es menor que b")

elif b == c :
    print("b es igual que c")

else:
    print("c es mayot que b")


if c > b : print("c es mayor que b")

print ("B") if b > c else print ("C")
print("\n"*0)
#Bucles
x = 1
while x < 10:
    print (x)
    x += 3

print("\n"*0)

x = 1
while x < 100:
    x += 3
    if x == 4 :
        continue
    print(x)

print("\n"*0)

Objetos = ["Cuchara","Cuchillo","Tenedor"]
for a in Objetos:
    print (a)
print("\n"*0)

for b in "Plátano""Manzana":
    
    print(b)

print("\n"*0)
#Extra
print("extra")
print("\n"*0)



for x in range(10, 55):
   if  x % 3 != 0 and x % 2 == 0 and x != 16 :
      print(x)
