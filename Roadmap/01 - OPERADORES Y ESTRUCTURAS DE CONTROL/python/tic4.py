#Operadores
#Artirmeticos
x= 10; y=5
print("x+y = ", x+y) #15
print("x-y =", x-y) #5
print ("x*y = ", x*y) #50
print("x/y =", x/y) # 2
"Operadores de Asignacion"
a=7; b=2
x=a; x+=b;  print("x+=", x)  # 9
x=a; x-=b;  print("x-=", x)  # 5
x=a; x*=b;  print("x*=", x)  # 14
x=a; x/=b;  print("x/=", x)  # 3.5

#Operadores Relacionales#
x=2; y=3
print("x==y =", x==y) # False
print("x!=y =", x!=y) # True
print("x>y  =", x>y)  # False
print("x<y  =", x<y)  # True

#Operadores logicoa#
print(True and True)   # True
print(True and False)  # False

print(True or True)   # True
print(True or False)  # True

print(not True)  # False
print(not False) # True

#Condiciomales#
a = 10
b = 30

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")

a es menor que b
#Repeticion#
numeros = [18,50,90,-20,100,80,37]
for n in numeros:
    print(n)
18
50
90
-20
100
80
37

x = 1
while x < 5:
    print(x)
    x += 1
1
2
3
4

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

try:
    c = a / b 
except ZeroDivisionError:
    print("Estás intentando dividir por cero")
Ingrese un número entero: 50
Ingrese otro número entero: 0
Estás intentando dividir por cero




