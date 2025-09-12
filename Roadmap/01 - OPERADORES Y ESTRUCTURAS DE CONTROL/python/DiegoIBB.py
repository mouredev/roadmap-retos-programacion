#01 ESTRUCTURAS DE CONTROL_Retos_Semanales

""" OPERADORES
	Asignación: =, +=, -=, *=, /=, %=, **=, etc..
	Aritméticos: +, -, *, /, %, **, etc..
	Comparasión: <, >, <=, >=, ==, !=
	Lógicos: &&(and),||(or), !(not)
"""
#OPERADORES ARITMETICOS

x = 6
y = 2

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
modulo = x % y
exponente = x ** y

print("----OPERADORES ARITMETICOS----")
print(f"Suma {x} + {y}: {suma}")
print(f"Resta {x} - {y}: {resta}")
print(f"Multiplicación {x} * {y}: {multiplicacion}")
print(f"División {x} / {y}: {division}")
print(f"Modulo {x} % {y}: {modulo}")
print(f"Exponente {x} ** {y}: {exponente}")


#OPERADORES DE ASIGNACIÓN

a = 0 #Asignación 

b = 1 #Incremento
b += 1

c = 2 #Decremento
c -= 1

d = 3 #Multiplicacion 
d *= 2 

e = 2 #Division
e /= 2

f = 5 #Modulo
f %= 3

g = 2 #Exponenciación
g **= 3

print("----OPERADORES DE ASIGNACION----")
print(f"Asignación = {a}")
print(f"Incremento += {b}")
print(f"Decremento -= {c}")
print(f"Multiplicación *= {d}")
print(f"División /= {e}")
print(f"Modulo %= {f}")
print(f"Exponente **= {g}")


#OPERADORES DE COMPARACION

h = 45
i = 34

print("----OPERADORES DE COMPARACION----")
print(f"Operador menor que -> h(45) < i(34): {h < i}")
print(f"Operador mayor que -> h(45) > i(34): {h > i}")
print(f"Operador menor o igual que -> h(45) <= i(34): {h <= i}")
print(f"Operador mayor o igual que -> h(45) >= i(34): {h >= i}")
print(f"Operador igualdad -> h(45) == i(34): {h == i}")
print(f"Operador desigualdad -> h(45) != i(34): {h != i}")

#OPERADORES DE LOGICOS

j = True
k = False
n = True

print("----OPERADORES DE LOGICOS----")
print(j == k and n >= j)
print(j != k or n == j)
print(not k <= j)

#OPERADORES DE IDENTIDAD Y PERTENENCIA
"""
Los operadores de identidad permiten revisar si un objeto es identico a otro, por otro lado
los operadores de pertenencia permiten ver si un elemento es parte de un conjunto
"""
print("----OPERADORES DE IDENTIDAD----")
elementos = ["casa", 3234, 'D', 4.6, True]
e1 = "casa"
e2 = 89

print(e1 is elementos[1])
print(e2 is not elementos[3])

print("----OPERADORES DE PERTENENCIA----")
frutas = ("Pera", "Manzana", "Piña", "Platano", "Mango")
f1 = "Mango"
f2 = "Piña"

print(f1 in frutas[4])
print(f2 not in frutas[3])


#OPERADORES DE BITS

num_1 = 5 #0000000000000101
num_2 = 7 #0000000000000111

print (num_1 & num_2) #Nos entrega la cantidad de 1(unos) que tienen los números en su descripción binaria
print (num_1 | num_2) #Nos entrega un número que comparte todos los 1(unos) que tienen los números en común
print (num_1 ^ num_2) #Cambia todos los números por 1(unos) inclusive si solo uno lo es
print (~ num_2) #Invierte los valores de 1s a 0s y viceversa
print (num_1 << num_2)
print (num_1 >> num_2)


#ESTRUCTURAS DE SELECCION O TOMA DE DESICION

#Estructuras if-elif-else

print("----ESTRUCTURAS IF_ELIF_ELSE----")
año = int(input("Year: "))

if (año % 4) == 0:
    if (año % 100) == 0:
        if (año % 400) == 0:
            print("Es año bisiesto")
        else:
            print("No es año bisiesto")
    else:
        print("Es año bisiesto")
else:
   print("No es año bisiesto")

bebidas = ["Te", "Mocca", "Capuccino", "Mocaccino", "Americano", "Espresso"]

eleccion = int(input("Elija una bebida: "))

if eleccion == 1:
    print(f"Ha elegido {bebidas[0]}")
elif eleccion == 2:
    print(f"Ha elegido {bebidas[1]}")
elif eleccion == 3:
    print(f"Ha elegido {bebidas[2]}")
elif eleccion == 4:
    print(f"Ha elegido {bebidas[3]}")
elif eleccion == 5:
    print(f"Ha elegido {bebidas[4]}")
elif eleccion == 6:
    print(f"Ha elegido {bebidas[5]}")
else:
    print("Opción no registrada")

print("----ESTRUCTURAS FOR----")

#ESTRUCTURAS DE REPETICION

print("----ESTRUCTURAS WHILE----")

num_ciclos = 6

while num_ciclos >= 0:
    print(f"N° de Ciclo: {num_ciclos}")
    num_ciclos -= 1

print("----ESTRUCTURAS WHILE_EXCEPCIONES----")

while True:
    try:
        name = int(input("Ponga su edad: "))
    except ValueError:
        print("Su edad no es un valor númerico valido")
    else:
        print(f"Edad ingresada: {name}")
        break


print("----ESTRUCTURAS FOR----")

x = 0
palabra = "Hola"

for letra in palabra:
    x += 1
    print(palabra[0:x])
x = 0


frase = input("Inserte una frase: ")
contador_a = 0

for i in frase:
     if i == "a":
          contador_a = contador_a + 1
          continue
     elif i == "A":
          contador_a = contador_a + 1
          continue     

print(f"Letras a en la {frase}: {contador_a} letras a")

