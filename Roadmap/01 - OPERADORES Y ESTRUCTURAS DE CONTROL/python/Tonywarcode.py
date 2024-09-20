num_x = 7
num_y = 3



### Operadores de Asignación ###
print("---- Operadores Asignacion ----")

x=num_x; x+=num_y   #suma
print("x+=", x)

x=num_x; x-=num_y   #resta
print("x-=", x)

x=num_x; x*=num_y   #multiplicación
print("x*=", x)

x=num_x; x/=num_y   #división
print("x/=", x)

x=num_x; x%=num_y   #Módulo
print("x%=", x)

x=num_x; x**=num_y  #Exponente
print("x**=", x)

x=num_x; x//=num_y  #Cociente
print("x//=", x)

x=num_x; x&=num_y   #bit a bit con AND
print("x&=", x)

x=num_x; x|=num_y   #bit a bit con OR
print("x|=", x)

x=num_x; x^=num_y   #bit a bit con XOR
print("x^=", x)

x=num_x; x>>=num_y  #bit a bit desplazamiento a izquierda
print("x>>=", x)

x=num_x; x<<=num_y  #bit a bit desplazamiento a derecha
print("x<<=", x )
print('\n')

### Operadores Aritméticos ###
print("---- Operadores Aritméticos ----")

print("Suma x+y= ", num_x+num_y)
print( 10 + 5) # se puede operar directamente
print("Resta x-y= ", num_x-num_y)
print( 10 - 5)
print("Multiplicación x*y= ", num_x*num_y)
print( 10 * 5)
print("División x/y= ", num_x/num_y)
print( 10 / 5)
print("Módulo x%y= ", num_x%num_y)
print( 10 % 5)
print("Exponente x**y= ", num_x**num_y)
print( 10 ** 5)
print("Cociente x//y= ", num_x//num_y)
print( 10 // 5)
print('\n')

### Operadores Relacionales ###
print("---- Operadores Relacionales ----")

print("x==y", num_x==num_y) #false
print("x=!y", num_x!=num_y) #true
print("x>y", num_x>num_y) #true
print("x<y", num_x<num_y) #false
print("x>=y", num_x>=num_y) #true
print("x<=y", num_x<=num_y) #false
print('\n')

### Operadores lógicos ###

print("---- Operadores Lógicos ----")
print("**AND**")
print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false
print('\n')

print("**OR**")
print(True or True) #true
print(True or False) #true
print(False or True) #true
print(False or False) #false
print('\n')

print("**NOT**")
print(not True) #false
print(not False) #true
print(not not not not True) #true
print('\n')

### Operadores Identidad ###
print("---- Operadores Identidad ----")

a= 1
b= 1
print(num_x is num_y) #false
print(a==b) #true
print( a is b) # true
print(a is not b)  # false
print(num_x is not num_y)  # True
print('\n')

### Operadores Pertenencia ###
print("---- Operadores Pertenencia ----")
lista =[1, 2, 3]
print(3 in lista) #true
print(5 in lista) #false
print(3 not in lista) #false
print(5 not in lista) #true
print('\n')

# Operadores de bit
print("---- Operadores bit ----")

a=7 #111
print(bin(a))
b=10 #1010
print(bin(b))

print(a & b) 
print(a | b) 
print(~a)
print(a^b)
print(a>>b)
print(a<<b)


### Tipos Estructuras de Control ###
print("---- Condicional if-elif-else ----")

if num_x == num_y:
    print("Son Iguales")
else:
    print("No son iguales")


if num_y == 3:
    print("Es el número 3")
elif num_y == 6:
    print("Es el número 6")
elif num_y == 7:
    print("Es el número 7")
else:
    print("Es otro número")

print('\n')

print("---- Repetitivas - Bucles ----")

#Bucle FOR
print("** FOR **")
#número de iteraciones(repeticiones) ya esta definido

for i in range(0, 5):
    print(i)

print('\n')

text1 = "python"
for j in text1[::-1]:
    print(j)

print('\n')

for i in range(6, 60, 2):  #range(inicio, fin, salto)
    print(i, end=" ")

print('\n')

#Bucle While
print("** while **")
#iteraciones no definidas

x = 5
while x > 0:
    x -=1
    print(x)
print('\n')

### Excepciones ###
print("---- Excepciones ----")
try:
    print(num_x / 0)    # si hay error no la ejecuta salta al except
    print("No se ha producido un error")    
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")
finally:
    print("Se finaliza la excepción")

    
print('\n')

# *** extra ***
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

# Lista para almacenar los números que cumplen con las condiciones
numeros = []

# Recorrer los números del 10 al 55
for num in range(10, 56):  
    # Verificar si el número es par, no es 16 y no es múltiplo de 3
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        # Añadir el número a la lista si cumple con todas las condiciones
        numeros.append(num)

# Imprimir los números que cumplen las condiciones
print(numeros)

