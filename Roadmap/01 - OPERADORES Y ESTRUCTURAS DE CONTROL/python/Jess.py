#Operadores
    #Aritmeticos
suma=10+2
resta=suma-4
multiplicacion=suma*resta
division_float=multiplicacion/suma 
division_entero=multiplicacion//suma
modulo= multiplicacion%suma
exponente=suma**2

print(suma)
print(resta)
print(multiplicacion)
print(division_float)
print(division_entero)
print(modulo)
print(exponente)

    #Asignacion Compuesto
num=10
print(num)
num+=4
print(num)
num-=4
print(num)
num*=3
print(num)
num/=3
print(num)
    #Condicionales
a = 3
b = 5

igual = a == b
print(igual)
diferente = a != b
print(diferente)
menor = a < b
print(menor)
mayor = a > b
print(mayor)
menor_igual = a <= b
print(menor_igual)
mayor_igual = a >= b
print(mayor_igual)
    #Logicos
x=True
y=False
operador_and= x and y
print(operador_and)
operador_or= x or y
print(operador_or)
operador_not= not x
print(operador_not)

#Estructuras de control
#If
edad=20
if edad==30:
    print("Tienes 30")

#Sentencia elif
elif edad==20:
    print("Tienes 20")
#If else
else:
    print("No tienes 30")

#Operador Tenario
numero=18
es_adulto="si" if numero>=18 else "No"
print(es_adulto)

#Ciclo While 
contador=1
while contador<=3:
    print(contador)
    contador +=1

#Ciclo for
cadena="Hola Mundo"
for letra in cadena:
    print(letra, end='')

#Funcion range 
for i in range (5):
    print(i)

#Break
for i in range (10):
    if i==5:
        break
    print (i)

#Continue
for i in range (6):
    if i ==3:
        continue
    print(i)

#Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
finally:
    print("Fin del bloque try")

'''
Crea un programa que imprima por consola
todos los números comprendidos
entre 10 y 55 (incluidos), pares, y 
que no son ni el 16 ni múltiplos de 3.
'''
for i in range (10, 56, 2): 
    if(i==16 or i%3==0): #Omitimos el 16 y los multiplos de 3
        continue
    else:
        print(i)

    