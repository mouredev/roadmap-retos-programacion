# Operadores Aritmeticos:

# Suma
suma = 4 + 5
# Resta
resta = 9 - 3
# Multiplicacion
multiplicacion = 5 * 6
# Division
division = 20 % 5
# Modulo
modulo = 20 % 2
# Exponente
exponente = 4 ** 2
# Division Baja o Division Entera
division_baja = 5 // 2

# Operadores de comparacion: >, <, ==, >=, <=, !=

# > (Mayor que)
print(30 > 10) # True
# < (Menor que)
print(20 < 30) # False
# == (Igual que)
print("hola" == 'hola') # True
# >= (Mayor o Igual que)
print(20 >= 20) # True
# <= (Menor o Igual que)
print(20 <= 30) # True
# != (No Igual que)
print(20 != 200) # True


# Operadores Logicos: and, or, not

# and
print(40 > 10 and "hola" == "Hola".lower()) # Imprime True, ya que las dos condiciones son verdaderas

# or
print(30 - 20 == 10 or 30 - 20 == 100) # Imprime True, si una de las condiciones son verdaderas

# not
print(not 20 - 10 == 10) # Imprime False, ya que la condicion es True y el operador NOT invierte al valor contrario

# Operadores de asignacion: =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=

# = (Operador de asignacion)
variable_numerica = 40 - 20

# += (Operador de suma y asignacion)
numero= 20
numero += 10

print(numero) # 30

# -= (Operador de resta y asignacion)
numero1 = 50
numero1 -= 10
print(numero1) # 40

# *- (Operador de multiplicaion y asignacion)
numero2 = 30
numero2 *= 2
print(numero2) # 60

# /= (Operador de division y asignacion)
numero3 = 40
numero3 /= 2
print(numero3) # 20

# %= (Operador de modulo y asignacion)
numero4 = 30
numero4 %= 5
print(numero4) # 0 # 30 es divisible por 5

# **/ (Operador de potencia y asignacion)
numero5 = 2
numero5 **= 3
print(numero5) # 8

# //= (Operador de division entera y asignacion)
numero6 = 400
numero6 //= 3
print(numero6) # 133 (el operador de division entera, divide los dos operandos y devuelve el cociente entero descartando cualquier parte decimal)

# &= (Operador de AND bit a bit y asignacion) 
""" Este Operador de asignacion (&=), primero convierte cada operando a numeros binarios luego compara con AND cada bit
en la posicion correspondiente de cada numero binario. Si el resultado de True AND False es False, el resultado de 1 AND 0 es 0 y si
el resultado de True AND True es True entonces el resultado de 1 AND 1 es 1. (Asi se van a ir comparando cada bit de los numeros binarios)"""
x = 5 # en binario: 0b101
y = 3 # en binario: 0b011
x &= y # se comparan con AND 0b101 y 0b011, la respuesta seria 0b001. --> 1
"""Se compara cada bit de cada operando en sus posiciones correspondientes, si en el primer numero binario su ultimo
bit es 1 y en el segundo numero binario su ultimo bit es 1, la respuesta de la ultimo bit del resultado seria 1 ya que se esta usando AND.
Asi se compara cada bit restante de los operandos para hallar el numero binario resultante.
Recuerden los bits de los numeros binarios estan compuestos solo por 0 y 1. """
print(x) # 1

# |= (Operador de OR bit a bit y asignacion)
"""Este Operador de asignacion (|=), primero convierte cada operando a numeros binarios luego compara con OR cada bit
en la posicion correspondiente de cada numero binario. Si el resultado de True OR False es True, el resultado de 1 OR 0 es 1 y si
el resultado de True OR True es True entonces el resultado de 1 OR 1 es 1. (Asi se van a ir comparando cada bit de los numeros binarios)"""
z = 8 # en binario: 0b1000
g = 3 # en binario: 0b0011
z |= g # se comparan con OR 0b1000 y 0b0011, la respuesta es 0b1011. --> 11
"""Se compara cada bit de cada operando en sus posiciones correspondientes, si en primer numero binario su ultimo bit es 0
y el en segundo numero binario su ultimo bit es 1, la respuesta del ultimo bit del resultado es 1 ya que se esta usando OR"""
print(z)

# ^= (Operador de XOR bit a bit y asignacion)
"""Este Operador de asignacion (^=), primero convierte cada operando a numeros binarios luego compara con XOR cada bit
en la posicion correspondiente de cada numero binario. La operacion XOR bit a bit devuelve 1 en el bit resultante si los bits correspondientes
son diferentes y 0 si son iguales"""
m = 5 # en binario: 0b101
n = 3 # en binario: 0b011
m ^= n # se comparan con XOR 0b101 y 0b011, la respuesta es 0b110. --> 6
print(m)

# >>= (Operador de desplazamiento a la derecha con asignacion)
"""Este Operador de asignacion (>>=), primero convierte el operando principal (el mas a la izquierda) a binario y 
luego desplaza sus bits n(el otro operando) veces hacia la derecha, habran bits que se desplazaran fuera y se perderan. Los espacios
en donde estaban los bits desplazados seran reemplazandos por 0"""
binario1 = 8 # en binario: 0b1000
desplazar_n = 2
binario1 >>= desplazar_n # Se desplazan los bits de la izquierda hacia la derecha y las posiciones donde estaban los bits se reemplazan por 0 --> 0b0010
print(binario1) # 2

# <<= (Operador de desplazamiento a la izquierda con asignacion)
"""Este operador de asignacion (<<=), primero convierte el operando principal (el mas a la izquierda) a binario y
luego desplaza sus bits n(el otro operando) veces hacia la izquierda, habran bits que se desplazaran fuera y se perderan. Los espacios
en donde estaban los bits desplazados seran reemplazados por 0"""
binario2 = 2 # en binario: 0b0010
desplazar_m = 2
binario2 <<= desplazar_m # Se desplazan los bits de la derecha hacia la izquierda y las posiciones donde estaban los bits se reemplazan por 0 --> 0b1000
print(binario2) # 0b1000 --> 8

if 5 > 3 and 10 < 100:
    print("5 es mayor que 3 y 10 es menor que 100!")
else:
    print("5 no es menor que 3 y 10 no es menor que 100!")

if 10 + 12 == 22 or 30 + 1 == 31:
    print("La funcion print se ejecuta, ya que una de las dos condiciones es verdadera (10 + 12 == 22 --> True)")

lista = [20, 30, 40, 50]

if not 10 in lista:
    print("10 esta en la lista!")
else:
    print("10 no esta en la lista!")