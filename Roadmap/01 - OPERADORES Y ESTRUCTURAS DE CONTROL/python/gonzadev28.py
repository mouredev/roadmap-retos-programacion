
#Operadores aritmeticos 
num1 = 11
num2 = 3 

#Suma
suma = num1 + num2
#Resta
resta = num1 - num2
#Multiplicacion 
multi = num1 * num2
#Division 
division = num1 / num2
#Modulo o resto
modulo = num1 % num2
#Potencia
potencia = num1 ** num2
#Division con numeros enteros
division_entera = num1 // num2

print("Los resultados son:", suma, resta, multi, division, modulo, potencia, division_entera)

#Operadores logicos 
estudiante = True 
programador = True 

print("Operador AND:", estudiante and programador) #Ambas condiciones se deben cumplir
print("Operador OR", estudiante, programador) #Al menos unas de las condiciones se debe cumplir
print("Operador NOT", not estudiante) # Invierte el valor (de true a false en este caso)

#Operadores de comparacion
print("Mayor que", num1 > num2)
print("Menor que", num1 < num2)
print("Mayor o igual que", num1 >= num2)
print("Menor o igual que", num1 <= num2)
print("Igual que", num1 == num2)
print("Distinto que", num1 != num2)

#Operadores de asignacion
mi_nuevo_numero = 7 # asigancion
print(mi_nuevo_numero)
mi_nuevo_numero += 1 #suma y asignacion
print(mi_nuevo_numero)
mi_nuevo_numero -=1 #resta y asignacion
print(mi_nuevo_numero)
mi_nuevo_numero *=2 #multiplicacion y asignacion
print(mi_nuevo_numero)
mi_nuevo_numero /= 2 #division y asignacion
print(mi_nuevo_numero)
mi_nuevo_numero %= 2 #modulo y asignacion
print(mi_nuevo_numero)
mi_nuevo_numero **= 2 #potencia y asignacion
print(mi_nuevo_numero)
mi_nuevo_numero //= 2 #division entera y asignacion
print(mi_nuevo_numero)

#Operadores de identidad

n1 = 93
n2 = 93 
print(n1 is n2) #True porque ambas variables hacen referencia al mismo objeto
print(n1 is not n2) #False 

#Operadores de pertencia 
mensaje = "Aprendiendo Python"
print(mensaje in "Aprendiendo Python")
print(mensaje not in "Aprendiendo Java")

#Operadores de bits
binario1 = 5 #0101 
binario2 = 7 #0111
print("AND: ", binario1 & binario2) #Compara si ambos bits contiene "1" en la misma posicion = 0101 --> 5
print("OR: ", binario1 | binario2) #Compara si al menos 1 de los bits es "1" en la misma posicion = 0111 --> 7
print("XOR: ", binario1 ^ binario2) #Si el bit es igual en la misma posicion es "0" sino es "1" = 0010 --> 2

#Condicionales

mi_entero = 19

if mi_entero == 20:
    print ("Se cumple la condicion del if")
elif mi_entero == 18:
    print("Se cumple la condicion del elif")
else:
    print("Ahora si se cumple la condicion")

# Imprime del 1 al 20 con un ciclo "while"
i = 1
while i <= 20:
    print(i)
    i += 1

# Imprime del 1 al 10 con un ciclo "for"
for i in range (1, 11):
    print(i)

"""DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)