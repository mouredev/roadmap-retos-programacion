
'''
Tipos de operadores en Python
'''
# OPERADORES ARTMÉTICOS (Realizan operaciones matemáticas básicas)

a = 10; b = 3

suma = a + b 
print(suma)

resta = a - b
print(resta)

multiplicación = a * b
print(multiplicación)

división = a / b # flotante
print(división)

división_entera = a // b
print(división_entera)

Módulo = a % b # Residuo de la división
print(Módulo)

Exponenciación = a ** b
print(Exponenciación)

# OPERADORES DE COMPARACIÓN (Comparan dos valores y devuelven un Booleano)
'''
Un Booleano sólo puede tener dos valores posibles: True o False
'''

Igualdad = a == b
print(Igualdad)

Desigualdad = a != b
print(Desigualdad)

Mayor_que = a > b
print(Mayor_que)

Menor_que = a < b
print(Menor_que)

Mayor_o_igual_que = a >= b
print(Mayor_o_igual_que)

Menor_o_igual_que = a <= b
print(Menor_o_igual_que)

# OPERADORES LÓGICOS (Permiten combinar valores Booleanos y devuelen un Booleano)

x = True; y = False

AND = x and y # Devuelve True si ambos valores son True
print(AND)

OR = x or y # Devuelve True si al menos uno de los valores es True 
print(OR)

NOT = not x # Devuelve True si el valor es Falsa y viceversa
print(NOT)

# OPERADORES DE ASIGNACIÓN (Asignan un valor a una variable)

a = 7; b = 2 # Asignación simple
print(a, b)

x=a; x+=b; print("x+=", x) # Suma en asignación
x=a; x-=b; print("x-=", x) # Resta en asignación
x=a; x*=b; print("x*=", x) # Multiplicación en asignación
x=a; x/=b; print("x/=", x) #División en asignación
x=a; x%=b; print("x%=", x) # Módulo en asignación
x=a; x//=b; print("x//=", x) # División entera en asignación
x=a; x**=b; print("x**=", x) # Exponenciación en asignación
x=a; x&=b; print("x&=", x) # AND en asignación
x=a; x|=b; print("x|=", x) # OR en asignación
x=a; x^=b; print("x^=", x) # XOR en asignación
x=a; x>>=b; print("x>>=", x) # Desplazamiento a la derecha en asignación 
x=a; x<<=b; print("x<<=", x) # Desplazamiento a la izquierda en asignación

# OPERADORES BIT A BIT (Realizan operaciones bit a bit)

a = 10; b = 3

AND = a & b # AND bit a bit
print(AND)

OR = a | b # OR bit a bit
print(OR)

XOR = a ^ b # XOR bit a bit
print(XOR)

NOT = ~a # NOT bit a bit
print(NOT)

Desp_a_izq = a << b # Desplazamiento a la izquierda
print(Desp_a_izq)

Desp_a_der = a >> b # Desplazamiento a la derecha
print(Desp_a_der)

#OPERADORES DE IDENTIDAS (Comparan la memoria de dos objetos y devuelven un Booleano)

a = 10; b = 10; c = 5

is_1 = a is b # Devuelve True si ambos objetos son iguales
print(is_1)

is_2 = a is c # Devuelve True si ambos objetos son iguales
print(is_2)

is_not_1 = a is not b # Devuelve Trues si ambos objetos no son iguales
print(is_not_1)

is_not_2 = a is not c # Devuelve True si ambos objetos no son iguales
print(is_not_2)

# OPERADORES DE PERTENENCIA (Comprueban si un objeto se encuentra en otro objetos y devuelven un Booleano)

lista = [1, 2, 3, 4, 5]

in_1 = 1 in lista # Devuelve True si el objeto se encuentra en la lista
print(in_1)

in_2 = 6 in lista # Devuelve True si el objeto se encuentra en la lista
print(in_2)

not_in_1 = 1 not in lista # Devuelve True si el objeto no se encuentra en la lista
print(not_in_1)

not_in_2 = 6 not in lista # Devuelve True si el objeto no se encuentra en la lista
print(not_in_2)

# OPERADORES DE MEMBRESÍA (Comprueban si un objeto se encuentra en otro objeto y devuelve un Booleano)

cadena = "Hola Mundo"

in_1 = "H" in cadena # Devuelve True si el objeto se encuentra en la cadena
print(in_1)

in_2 = "h" in cadena # Devuelve True si el objeto se encuentra en la cadena

not_in_1 = "H" not in cadena # Devuelve True si el objeto no se encuentra en la cadena
print(not_in_1)

not_in_2 = "h" not in cadena # Devuelve True si el objeto no se encuentra en la cadena

# OPERADORES TERNARIOS (Permiten realizar una operación condicional)

a = 10; b = 20

resultado = a if a > b else b 
print(resultado)

'''
Ejemplos prácticos Ternarios
'''
# Asignar Valores

edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)  # Salida: Mayor de edad

# Usar una función

def obtener_estado(puntaje): # def: es una palabra reservada que indica que se encuentra definida una función
    return "Aprobado" if puntaje >= 60 else "Reprobado"

print(obtener_estado(75))  # Salida: Aprobado
print(obtener_estado(50))  # Salida: Reprobado

# Anidar operadores ternarios

a = 5
b = 10
c = 15

resultado = "a es mayor" if a > b and a > c else "b es mayor" if b > c else "c es mayor"
print(resultado)  # Salida: c es mayor

# Usar en listas o generadores

numeros = [1, 2, 3, 4, 5]
pares_o_impares = ["Par" if num % 2 == 0 else "Impar" for num in numeros]
print(pares_o_impares)  # Salida: ['Impar', 'Par', 'Impar', 'Par', 'Impar']

# OPERADORES DE CONCATENACIÓN (Unen dos o mas cadenas)

cadena_1 = "Hola"
cadena_2 = "Mundo"

concatenacion = cadena_1 + " " + cadena_2
print(concatenacion)

# OPERADORES DE REPETICIÓN (Repite una cadena un número determinado de veces)

cadena = "Hola"

repetición = cadena * 3
print(repetición)

# OPERADORES DE SLICING (Extraen una parte de una cadena)

texto = "Hola Mundo"

slicing = texto[0:4] # Extrae las primeras 4 letras "Hola"
print(slicing)
slicing = texto[-5:] # Extrae las ultimas 5 letras "Mundo"
print(slicing)
slicing = texto[::-1] # Invierte el texto
print(slicing)

# OPERADORES DE FORMARO (Permiten formatear una cadena)

nombre = "Lio"
edad = 25

formateo = "Hola, mi nombre es {} y tengo {} años".format(nombre, edad)
print(formateo)

formateo = "Hola, mi nombre es {0} y tengo {1} años".format(nombre, edad)
print(formateo)

formateo = "Hola, mi nombre es {nombre} y tengo {edad} años".format(nombre="Lio", edad=25)
print(formateo)

# OPERADORES DE ENTRADA Y SALIDA (Permiten recibir y mostrar información)

nombre = input("ingresa tu nombre: ") # Input: Recibe información del usuario y la almacena en una variable
print("Hola", nombre)

edad = input("Ingresa tu edad: ")
print("Tu edad es", edad)

# OPERADORES DE SALIDA (Muestran información en la consola)

print("Hola Mundo") # Print: Muestra información en la consola 
print("Hola", "Mundo") 
print("Hola" + "Mundo")

# OPERADORES DE COMENTARIOS (Permiten añadir comentarios en el código fuente)

# Comentario de una sola línea

'''
Comentario
de
varias
líneas
'''

# OPERADORES DE BLOQUES DE CÓDIGO (Permiten agrupar instrucciones)

if True: # if: es una palabra reservada que indica que se encuentra una condiciónes verdadera
    print("Hola Mundo") # Bloque de código

edad = 18

if edad >= 18: 
    print("Eres mayor de edad")
else: # else: es una palabra reservada que indica que se encuentra un bloque de código alternativo
    print("Eres menor de edad")

for i in range(3): # for: es una palabra reservada que indica que se encuentra un bucle
    print(f"Iteración {i}") 

def saludar():
    print("¡Hola!")
    print("Bienvenido a Python")

saludar()



















