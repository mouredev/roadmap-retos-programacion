# Operadores Aritmeticos:

# Suma
suma = 4 + 5
print(suma)
# Resta
resta = 9 - 3
print(resta)
# Multiplicacion
multiplicacion = 5 * 6
print(multiplicacion)
# Division
division = 20 % 5
print(division)
# Modulo
modulo = 20 % 2
print(modulo)
# Exponente
exponente = 4 ** 2
print(exponente)
# Division Baja o Division Entera
division_baja = 5 // 2
print(division_baja)

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


# Operadores Bit a Bit: &, |, ^, ~, >>, <<

# & (AND bit a bit)
numero_binario1 = 8 # --> 0b1000
numero_binario2 = 4 # --> 0b0100
"""Este operador primero convierte sus operandos a numeros binarios para luego comparar cada bit con AND. Si 1 AND 1 es 1, 1 AND 0 es 0."""
resultado_binario = numero_binario1 & numero_binario2
print(resultado_binario) #0b0000 --> 0

# | (OR bit a bit)
numero_binario3 = 5 # --> 0b0101
numero_binario4 = 10 # --> 0b1010
"""Este operador primero convirte sus operandos a numeros binarios para luego comparar cada bit con OR. Si 1 OR 0 es 1, 0 OR 0 es 0, entonces
1 OR 1 es 1"""
resultado_binario2 = numero_binario3 | numero_binario4
print(resultado_binario2) # 0b1111 --> 15

# ^ (XOR bit a bit)
numero_binario5 = 7 # --> 0b0111
numero_binario6 = 2 # --> 0b0010
"""Este operador primero convirte sus operandos a numeros binarios para luego comparar cada bit con XOR. En XOR si los numeros que se estan
comparando son iguales es 0 y sin son diferentes es 1"""
resultado_binario3 = numero_binario5 ^ numero_binario6
print(resultado_binario3) # 0b0101 --> 5

# >> (desplazamiento a la derecha bit a bit)
numero_binario7 = 6 # --> 0b0110
desplazar_x = 1
"""Este operador primero convierte el primer operando a binario luego desplaza cada bit del extremo izquierdo x(el otro operando) veces
hacia la derecha"""
resultado_binario4 = numero_binario7 >> desplazar_x
print(resultado_binario4) # 0b0011 --> 3

# << (desplazamiento a la izquierda bit a bit)
numero_binario8 = 3 # --> 0b00000011
desplazar_y = 8
"""Este operador primero convierte el primer operando a binario luego desplaza cada bit del extremo derecho x(el otro operando) veces
hacia la izquierda"""
resultado_binario5 = numero_binario8 << desplazar_y
print(resultado_binario5) # 0b1100000000 --> 768

# Operadores de asignacion: =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=

# = (Operador de asignacion)
variable_numerica = 40 - 20
print(variable_numerica)

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

# Operadores de identidad: is , is not

# is devuelve True si los operandos se refieren al mismo objecto. De lo contrario devuelve False
# is not devuelve True si los operandos no se refieren al mismo objecto. De lo contrario devuelve False

a = 2
b = 10
c = 2
print(a is b) # --> False
print(a is not c) # --> False
print(a is c) # --True

# Operadores de pertenencia: in, not in

# in devuelve True si el valor especificado se encuentra en la secuencia (objeto). De lo contrario devuelve False
# not in devuelve True si el valor especificado no se encuentra en la secuencia (objeto). De lo contrario devuelve False

lista_de_numeros = [20, 50, 100, 70, 400]
print(30 in lista_de_numeros) # False
cadena_de_texto = "Hola, Mundo!"
print("H" in cadena_de_texto) # True

# Estructuras de control:
# Condicional if, elif y else

ganancia = int(input("Cuanto dinero ganas al mes aproximadamente?: "))
gasto = int(input("Cuanto gastas aproximadamente cada mes?: "))

if ganancia/3 >= gasto :
    print("Estas ahorrando correctamente!!")
elif ganancia/2 >= gasto:
    print("Estas ahorrando!!")
elif ganancia > gasto and gasto <= ganancia * 0.8:
    print("Estas ahorrando pero puedes ahorrar mucho mas!!")
else:
    print("No estas ahorrando correctamente!")

# Bucles for, while
lista_iterable = ["Hola", "mi", "nombre", "es", "Alvaro", "Neyra"]

#for

for palabra in lista_iterable:
    print(palabra)

# for, range
    
for i in range(10):
    print(f"{i + 1}")

# while and exceptions: Se ejecuta ilimitadamente hasta que la condicion sea falsa

while True:
    print("Dividir dos numeros....")
    dividir_numero1 = int(input("Primer operando: "))
    dividir_numero2 = int(input("Segundo operando: "))
    try:
       resultado_de_la_division = dividir_numero1 / dividir_numero2
    except ValueError as e:
        print("Tiene que ser un numero!!")
        print(f"Error: {e}")
    except Exception as Error:
        print(f"Error cometido: {Error}")
    else:
        break
    finally:
        print("Finally siempre se ejecuta siempre!")

print(resultado_de_la_division)

# for, zip()
numeros = [8, 100, 200]
se_llaman = ["Ocho", "Cien", "Doscientos"]

for e, i in zip(numeros, se_llaman):
    print(f"{e} se llama: {i}")

# for, enumerate():
lista_de_elementos = ["Palabra", True, 300]

for indice, elemento in enumerate(lista_de_elementos):
    print(f"Este es el elemento: {elemento} del indice: {indice}")

# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
def dificultad_extra():
    for i in range(10, 56):
        if i == 16:
            continue
        if i % 3 == 0:
            continue
        if i % 2 != 0:
            continue

        print(i)

dificultad_extra()