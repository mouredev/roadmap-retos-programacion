# 1- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

# operadores aritméticos #
a = 3
b = 2

print ("la suma de a y b: ",  (a + b))# operador de suma
print ("la resta de a y b: ",  (a - b))# operador de resta .
print ("la multiplicación de a y b: ",  (a * b))# operador de multiplicación
print ("la división de a y b: ",  (a / b))# operador de división
print ("la división entera de a y b: ",  (a // b))# operador de división entera
print ("la división de resto o módulo de a y b: ",  (a % b))# operador de división de resto o módulo
print ("la potencia de a y b: ",  (a ** b))# operador de potencia o exponencial

## operadores de comparación ##

print (a == b)# operador es igual a: (output False)
print (a != b)# operador es diferente a: (output True)
print (a > b)# operador es mayor que: (output True)
print (a < b)# operador es menor que: (output False)
print (a >= b)# operadro es mayor o igual que: (output True)
print (a >= b)# operadro es menor o igual que: (output False)

### operadores de pertenencia ###

colores_primarios = ["rojo", "amarillo", "azul"]
color_test = input("ingresa un color: ")
if color_test in colores_primarios:
    print(color_test, "es un color primario!")
else:
    print(color_test, "no es un color primario")

### operadores lógicos ###

c = 1

print (a > b and a > c)# operador de conjunción: (output True)
print (a > b or a > c)# operador de diyunción: (output True)
print (not (a > b))# operador not: (output False)


## operadores de asignación ##

my_assignment_variable = "este es mi operador de asignación"
print( my_assignment_variable)

my_number = 10 #asignación de valor a una variable
print(my_number)
my_number += 1 #asignación y suma
print(my_number)
my_number -= 1 #asignación y resta
print(my_number)
my_number *= 1 #asignación y multimplicación
print(my_number)
my_number /= 2 #asignación y divición
print(my_number)
my_number //= 2 #asignación y divición entera
print(my_number)
my_number %= 1 #asignación y resto o módulo
print(my_number)
my_number **= 1 #asignación y exponencial o potencia



### operadores de bits ###

print (a & b)# operación AND (output 2)
print (a | b )# operación or (output 3)
print (a ^ b)# operación Xor (output 1)
print (~ b) #operador Not  (b=2 en binario: b=10 por lo tanto ~b= 01)
print (a >> b) # operador de desplazamiento a la derecha (output 0)
print (a << b)# operador de desplazamiento a la izquierda (output 12)

## estructuras de control##

#condicional if, elif, else. #
if a > b:
    print(a, "es mayor que ", b)
elif a == b:
    print(a, "es igual que ", b)
else:
    print(a, "es menor que ", b)

### iterativas##
#bucle while#

while c < a:
    c+=1
print(" ahora ", c ,"es igual a  ", a)

# bucle for#

for i in range (11):
    print(i)

#excepciones ##

try:
    print("en esta linea, tal vez haya un error")
except: 
    print(" ha ocurrido un error")
finally: 
     print("la ejecución continua")

##DIFICULTAD EXTRA (opcional):##

for number in range (10, 56, 2):
    #if number % 2== 0 and number != 16 and number %3 !=0: (version compacta)
    if number == 16:
        continue
    elif number % 3 == 0:
        continue
    print(number)
