#Operadores aritmeticos

print (f"Suma: 2 + 5 = {2 + 5}")
print (f"Resta: 2 - 5 = {2 - 5}")
print (f"Division: 2 / 5 = {2 / 5}")
print (f"Multiplicacion: 2 * 5 = {2 * 5}")
print (f"Modulo: 2 % 5 = {2 % 5}")
print (f"Exponente: 2 ** 5 = {2 ** 5}")
print (f"Division entera: 2 // 5 = {2 // 5}")

#Operadores de comparacion

print (f"Igualdad: 10 == 3 = {10 == 3}")
print (f"Igualdad: 10 != 3 = {10 != 3}")
print (f"Mayor que: 10 > 3 = {10 > 3}")
print (f"Menor que: 10 < 3 = {10 < 3}")
print (f"Mayor o igual que: 10 >= 3 = {10 >= 10}")
print (f"Menos o igual que: 10 <= 3 = {10 <= 3}")

#Operadores logicos

print (f"AND : 10 + 3 == 13 and 5 - 1 == 4 = {10 + 3 == 13 and 5 - 1 == 4}")
print (f"OR : 10 + 3 == 15 and 5 - 1 == 4 = {10 + 3 == 15 or 5 - 1 == 4}")
print (f"NOT : not 10 + 3 == 14 = {not 10 + 3 == 14}")

#Operadores de asignacion

numero= 11  #asignacion
print (numero)
numero += 3 #asignacion con suma
print (numero)
numero -= 3 #asignacion con resta
print (numero)
numero *= 3 #asignacion con multiplicacion
print (numero)
numero /=3 #asignacion con division
print (numero)
numero %=3 #asignacion con modulo
print (numero)
numero //=3 #asignacion con division entera
print (numero)
numero **=3 #asignacion con exponente
print (numero)


#Operadores de identidad

nuevo_numero = 10

print(f"numero is nuevo_numero es: {numero is nuevo_numero}")
print(f"numero is not nuevo_numero es: {numero is not nuevo_numero}")

#Operadores de pertenencia

print (f"'r' in 'Andres'= {'r' in 'Andres'}")
print (f"'b' not in 'Andres'= {'r' in 'Andres'}")

#Operadores de bit

a = 10 #1010
b = 3 # 0011

print (f"AND: 10 & 3 = {10 & 3}") #0010
print (f"OR: 10 | 3 = {10 | 3}") #1011
print (f"XOR: 10 ^ 3 = {10 ^ 3}") #1001
print (f"NOT: ~10 = {~10}") 
print (f"Desplazar a la derecha 10 >>2 = {10 >> 2}") 
print (f"Desplazar a la izquierda 10 <<2 = {10 << 2}") 

#Estructuras de control

my_string = "Andres"

if my_string == "Andres":
    print("my_string es Andres")
elif my_string == "Felipe":
     print ("my_string es Felipe")
else:
     print ("my_string no es Andres")


for i in range (0,5):
     print (i) 

for i in my_string:
     print (i)

it = iter(my_string)
print(next(it))
print(next(it))

lista_test= [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista_test:
     for j in i:
      print (j)

for i in my_string[::-1]:
    print (i)

for i in range (2,20,3):
 print(i)

for i in range (20,10,-1):
   print(i)

numero_while = 5 


while numero_while > 0:
    numero_while -=1
    print (numero_while)

my_list = ["Uno","Dos", "Tres"]
while my_list:
    my_list.pop(0)
    print (my_list)

while numero_while > 0:
    numero_while -=1
    print (numero_while)
else:
    print ("Bucle finalizado")   


for i in range (0,5):
    for j in range (6):
        print ("#",end="")
    print ()    

z = 7
x = 1

while z > 0:
    print('' * z + '*' * x + ''* z)
    x+=2
    z-=1

a = 0
b = 1

while b < 89:
    print (b)
    a, b = b, a+b


if(a == 1):
    print ("1")
elif ( a == 2):
    print("2")
elif (a == 3):
    print ("3")     

cadena = "python"

for letra in cadena:
    if letra == 'h':
        print ("se encontro la h")
        break 
    print (letra)


for letra in cadena:
    if letra == 't':
        print ("se encontro la t")
        continue
    print (letra)

lista1 = [1,2,3]
lista2 = ['a','b','c'] 
listazip = zip(lista1 , lista2)

for numerozip, textozip in zip (lista1 , lista2):
    print ("lista 1", numerozip, "lista 2", textozip)

c = [(1, 'One'), (2, 'Two'), (3, 'Three')]

a , b = zip(*c)
print (a)
print (b)

lista = ["A", "B", "C"]

for indice, l in enumerate (lista):
    print (indice, l)

en = list(enumerate(lista))
print (en)    


cuadrado = [i for i in range (5)]
print (cuadrado)

frase = "El perro de san roque no tiene rabo"

set = { i for i in frase if i == "o"}
print (set)

lista3 = ['nombre', 'edad', 'región']
lista4 = ['Pelayo', 30, 'Asturias']

dictionario = {i:j for i,j in zip(lista3, lista4)}
print (dictionario)


# Ejercicio Extra 

for i in range (10 , 55):
    if  i % 2 == 0 and i  != 16 and i % 3 > 0:
        print (i)                                                                                                                                                                
