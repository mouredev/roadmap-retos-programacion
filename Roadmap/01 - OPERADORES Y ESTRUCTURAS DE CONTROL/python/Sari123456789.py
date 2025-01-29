
#operaciones aritmeticas

suma = 3+3
print (suma)

resta =3 -3
print(resta)

multiplicacion = 3*3
print(multiplicacion)

division = 10/2
print(division)

resto = 10 % 2
print(resto)

cuadrado = 3**2
print(cuadrado)

 #operaciones logicas

num1 = 1
num2 =2

print (num1 == num2)
print (num1 > num2)
print (num1 < num2)
print (num1 != num2)
print(num1 >= num2)
print (num1 <= num2)

 # operadores de asignacion

numero1 = 5
numero2= 9
print(numero1)
numero1 += numero1
print(numero1)
numero1 -= numero1
print(numero1)
numero1 *= numero2
print(numero1)

#if
entero= int(input("Introduce un numero: "))

if entero % 2 == 0:
	print(f"El numero {entero} es par")
else:
	print(f"El numero {entero} es impar")

#while 

entero_positivo= int(input("Introduce un numero positivo: "))
while entero_positivo <= 0:
    print("El numero tiene que ser positivo")
    entero_positivo= int(input("Introduce un numero positivo: "))

print(f"Los numeros del 0 hasta el {entero_positivo} son: ")  
for numero in range (entero_positivo):
		print (numero)
		
#for
for numeroo in range(11):
    if (numero %3 == 0 and numero%5 ==0 ):
        print("FizzBuzz")
    elif numeroo % 3 == 0:
        print("fizz")
    elif numeroo % 5 == 0:
        print("buzz")
    
		
#is, is not (identidad)

lista1 = [1, 2, 3]
lista2= lista1
print(lista1 is lista2)
print(lista1 is not lista2)
lista2= [4, 5, 6]
print(lista1 is lista2)

#in, in not (pertenencia)

lista_frutas = ["pera", "manzana", "melon"]
fruta_elegida = input("Elige entre pera, manzana y melon").lower()
if fruta_elegida in lista_frutas:
        print(f"La fruta : {fruta_elegida} esta en la lista" )
else:
        print(f"{fruta_elegida} no esta en la lista")
        
#bits

a = 5
b = 6
print(a & b)
print(a | b)
print(a ^ b)

#Manejo excepciones
try: 
    numero_si= int(input("introduce un numero: "))
    print ("El numero es: ", numero_si)
except ValueError:
    print("no es un numero")

#EXTRA (opcional):
#Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), 
#pares, y que no son ni el 16 ni múltiplos de 3

for numopcional in range(10, 56):
    if numopcional % 2 == 0 and numopcional != 16 and numopcional % 3 != 0 :
        print(numopcional)
