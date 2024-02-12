
print(" Operadores de Python")
print("")

# Operadores aritméticos 
print(f"Operadores aritméticos")
print("")
print(f"Definiremos: 'x' = 4 e 'y' = 3")
print("")
x = 4
y = 3

# Suma
suma = x + y  # Suma de 'x' mas 'y'
print("Suma:")
print(f"x + y = {suma}")
print("")

# Resta
resta = x - y # Resta de 'x' menos 'y'
print("Resta:")
print(f"x - y = {resta}")
print("")

# Multiplicación
multiplicacion = x * y  # Multiplicación de  'x' por 'y'
print("Multiplicacion:")
print(f"x * y = {multiplicacion}")
print("")

# Potenciación
potenciacion = x ** y  # Potenciación de 'x' elevado a 'y'
print("Potenciación:")
print(f"x ** y = {potenciacion}")
print("")

# División
division = x / y  # División de 'x' sobre 'y'
print("División:")
print(f"x / y = {division}")
print("")

# División entera (resulta solo la parte entera de la división)
division_entera = x // y  # División entera de 'x' sobre 'y'
print("División entera:")
print(f"x // y = {division_entera}")
print("")

# Resto de una división o Módulo
resto_division = x % y  # Resto o modulo de la división de 'x' sobre 'y'
print("Resto de una división o Módulo:")
print(f"x % y = {resto_division}")
print("")


print("""
Operadores Relacionales

>  Devuelve True si el operador de la izquierda es mayor que el operador de la derecha
<  Devuelve True si el operador de la derecha es mayor que el operador de la izquierda
== Devuelve True si ambos operandos son iguales
>= Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
<= Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda
!= Devuelve True si ambos operandos no son iguales

Fuente: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
""")

print("")

resultado_mayor_que = x > y  # Retorna True
print("Ejemplo con > :")
print(f"x > y  = {resultado_mayor_que}")
print("")


resultado_menor_que = x < y  # Retorna False
print("Ejemplo con < :")
print(f"x < y  = {resultado_menor_que}")
print("")

resultado_igualdad = x == y  # Retorna False
print("Ejemplo con == :")
print(f"x == y  = {resultado_igualdad}")
print("")

resultado_mayor_igual = x >= y  # Retorna True
print("Ejemplo con >= :")
print(f"x >= y  = {resultado_mayor_igual}")
print("")

resultado_menor_igual = x <= y  # Retorna False
print("Ejemplo con <= :")
print(f"x <= y  = {resultado_menor_igual}")
print("")

resultado_distinto_a = x != y  # Retorna True
print("Ejemplo con != :")
print(f"x != y  = {resultado_distinto_a}")
print("")

print("""
Operadores Bit a bit

&	Realiza bit a bit la operación AND en los operandos.
|	Realiza bit a bit la operación OR en los operandos.
^	Realiza bit a bit la operación XOR en los operandos.
~	Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando.
>>	Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador 
    de la izquierda a la derecha tantos bits como indica el operador de la derecha.
<<	Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando
    de la izquierda a la izquierda tantos bits como especifique el operador de la derecha.

Fuente: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
""")

print("")
print("Como ejemplo usaremos a = 2 (bit = 10) y b = 3 (bit = 11)")
a = 2
b = 3

# AND
resultado_and = a & b  # El resultado es 2 (Bit: 10 & 11 = 10 )
print("Ejemplo con AND:")
print(f"a & b = {resultado_and} (Bit: 10 & 11 = 10 )")
print("")

# OR
resultado_or = a | b  # El resultado es 3 (Bit: 10 | 11 = 11 )
print("Ejemplo con OR:")
print(f"a | b = {resultado_or} (Bit: 10 | 11 = 11 )")
print("")

# XOR
resultado_xor = a ^ b  # El resultado es 1 (Bit: 10 ^ 11 = 01)
print("Ejemplo con XOR :")
print(f"a ^ b = {resultado_xor} (Bit: 10 ^ 11 = 01)")
print("")

# NOT
resultado_not = ~a  # El resultado es -3 (Bit: ~(00000010) = (11111101))
print("Ejemplo con NOT:")
print(f"~a  = {resultado_not} (Bit: ~(00000010) = (11111101))")
print("")

# Desplazamiento a la derecha bit a bit.
resultado_der = a >> b  # El resultado es 0 (Binario: 00000010 >> 00000011 = 0)
print("Ejemplo con Desplazamiento a la derecha bit a bit:")
print(f"a >> b  = {resultado_der} (Binario: 00000010 >> 00000011 = 0)")
print("")

# Desplazamiento a la izquierda bit a bit.
resultado_izq = a << b  # El resultado es 16 (Binario: 00000010 >> 00000011 = 00001000)
print("Ejemplo con Desplazamiento a la izquierda bit a bit:")
print(f"a << b  = {resultado_izq} (Binario: 00000010 >> 00000011 = 00001000)")
print("")

print("""
Operadores de Asignación

=   Asigna el valor ejemplo: x = 4 se le asigna el valor de 4 a 'x'
+=  Incrementa, es equivalente a la suma
-=  Decrementa, es equivalente a la resta
*=  Es equivalente a la multiplicación
**= Es equivalente a la potenciación
/=  Es equivalente a la división
//= Es equivalente a la división entera
%=  Es equivalente al resto o modulo
&=  Es equivalente a AND
|=  Es equivalente a OR
^=  Es equivalente a XOR
>>= Es equivalente a el desplazamiento a la derecha
<<= Es equivalente a el desplazamiento a la izquierda

Fuente: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/

""")
print("Definimos z = 5")
print("")

z = 5  # Se le asigna el valor de 5 a 'z'
print("Ejemplo = :")
print(f"z = 5  = {z}")
print("")

z += 5  # Se le suma el valor de 5 al valor anterior de z (resultado z = 10)
print("Ejemplo += :")
print(f"z += 5 = {z}")
print("")

z -= 5  # Se le resta el valor de 5 al valor anterior de z (resultado z = 5)
print("Ejemplo -= :")
print(f"z -= 5 = {z}")
print("")

z *= 5  # Se le multiplica el valor de 5 al valor anterior de z (resultado z = 25)
print("Ejemplo *= :")
print(f"z *= 5 = {z}")
print("")

z **= 5 # Se le eleva a 5 al valor anterior de z (resultado z = 9765625)
print("Ejemplo **= :")
print(f"z **= 5 = {z}")
print("")

z /= 100000  # Se le divide 'z' sobre 100000 (resultado z = 97.65625)
print("Ejemplo /= :")
print(f"z /= 5 = {z}")
print("")

z //= 30  # Se hace una division entera a 'z' sobre 30 (resultado z = 3)
print("Ejemplo //= :")
print(f"z //= 5 = {z}")
print("")

z %= 2  # Se obtiene el resto de 'z' divido por 2 (resultado z = 1)
print("Ejemplo %= :")
print(f"z %= 5 = {z}")
print("")


print("Utilizare los valores de a y b de la seccion de operadores bit a bit" )
print("")
a = 2
b = 3

a &= b  # El resultado es a = 2 (Bit: 10 & 11 = 10 )
print("Ejemplo con &= :")
print(f"a &= b el valor de a es: {a} (Bit: 10 & 11 = 10 )")
print("")

a = 2
b = 3
a |= b  # El resultado es a = 3 (Bit: 10 | 11 = 11 )
print("Ejemplo con |= :")
print(f"a |= b el valor de a es: {a} (Bit: 10 | 11 = 11 )")
print("")

a = 2
b = 3
a ^= b  # El resultado es a = 1 (Bit: 10 ^ 11 = 01)
print("Ejemplo con |= :")
print(f"a |= b el valor de a es: {a} (Bit: 10 ^ 11 = 01)")
print("")

a = 2
b = 3
a >>= b  # El resultado es a = 0 (Binario: 00000010 >> 00000011 = 0)
print("Ejemplo con >>= :")
print(f"a >>= b el valor de a es: {a} (Binario: 00000010 >> 00000011 = 0)")
print("")

a = 2
b = 3
a <<= b  # El resultado es a = 16 (Binario: 00000010 >> 00000011 = 00001000)
print("Ejemplo con <<= :")
print(f"a <<= b el valor de a es: {a} (Binario: 00000010 >> 00000011 = 00001000)")
print("")


print("""
Operadores Lógicos

and Devuelve True si ambos operandos son True
or  Devuelve True si alguno de los operandos es True
not Devuelve True si alguno de los operandos False

Fuente: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/

""")

resultado_log_and = x > y and x < y
print("Ejemplo 'and' :")
print(f"x > y and x < y = {resultado_log_and}, con 'x' = 4 e 'y' = 3")
print("")

resultado_log_or = x > y or x < y
print("Ejemplo 'or' :")
print(f"x > y or x < y = {resultado_log_or}, con 'x' = 4 e 'y' = 3")
print("")

resultado_log_not = not x > y
print("Ejemplo 'or' :")
print(f"not x > y = {resultado_log_not}, con 'x' = 4 e 'y' = 3")
print("")


print("""
Operadores de Pertenencia

in  Devuelve True si el valor especificado se encuentra en la secuencia.
    En caso contrario devuelve False.

not in  devuelve True si el valor especificado no se encuentra en la secuencia.
        En caso contrario devuelve False.

Fuente: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/

""")

mi_cadena = "Hola Mundo"

resultado_in = "H" in mi_cadena
print("Ejemplo 'in' :")
print(f"'H' in mi_cadena = {resultado_in}, con 'mi_cadena' = 'Hola Mundo'")
print("")

resultado_not_in = "x" not in mi_cadena
print("Ejemplo 'not in' :")
print(f"'x' not in mi_cadena = {resultado_not_in}, con 'mi_cadena' = 'Hola Mundo'")
print("")

print("""
Operadores de Identidad

is  Devuelve True si los operandos se refieren al mismo objeto.
    En caso contrario devuelve False.

is not  Devuelve True si los operandos no se refieren al mismo objeto.
        En caso contrario devuelve False.

Fuente: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/

""")

mi_cadena = "Hola Mundo"
mi_cadena_2 = "Hola Mundo"

resultado_is = mi_cadena is mi_cadena_2
print("Ejemplo 'not in' :")
print(f"mi_cadena is mi_cadena_2 = {resultado_is}, con 'mi_cadena' = 'Hola Mundo' y 'mi_cadena_2' = 'Hola Mundo'")
print("")

resultado_is_not = mi_cadena is not mi_cadena_2
print("Ejemplo 'not in' :")
print(f"mi_cadena is not mi_cadena_2 = {resultado_is_not}, con 'mi_cadena' = 'Hola Mundo'")
print("")


# Estructuras de control

print("""
Estruturas Condicionales

Estructura if, elif y else:

if 'condición':
    codigo a ejecutar si se cumple la condición
elfi 'condición_2':
    se ejecutara este bloque si la condicion no se cumple pero la condicion_2 si
else:
    Si no secumplen las condiciones anteriores se ejecutara este bloque

nota: la condición if puede utilizarse por si sola.

Fuente: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/

""")
print("")

print("""Usaremos el siguiente ejemplo

if suma == 7 and "H" in mi_cadena:
    print("Se cumple la primera condicion: 'suma == 7 and 'H' in mi_cadena:' ")
elif resta < division:
    print("Se cumple la segunda condicion: 'resta < division' ")
else:
    print('No se cumplio ninguna de las condiciones anteriores')

Como la suma si es igual a 7 y 'H' esta en micadena se ejecurara el codigo que esta en if.

""")

if suma == 7 and "H" in mi_cadena:
    print("Se cumple la primera condicion: 'suma == 7 and 'H' in mi_cadena:' ")
elif resta < division:
    print("Se cumple la segunda condicion: 'resta < division' ")
else:
    print('No se cumplio ninguna de las condiciones anteriores')

print("")
print("""
Estructuras Iterativas

Estructura while:

while 'condicion':
    se ejecutara el codigo iterativamente, hasta que la condicion no se cumpla

Estructura for:

for 'variable iteradora' in 'cantidad de iteraciones'
    se ejecutara el codigo

'cantidad de iteraciones': pueden ser listas, rangos, entre otros.

""")
print("")

print("""Usaremos el siguiente ejemplo:

while x < 7:
    x += 1
    print(x)

Entraremos al bucle, y se le sumara uno a la variabla 'x' que vale 4 y se imprimira en terminal
se saldra del bucle en el momento que no se cumpla la condicion x < 7

""")

print("Entrando en bucle while: ")

while x < 7:
    x += 1
    print(x)

print("Sali del bucle while ")

print("")
print("""Usaremos el siguiente ejemplo:

for i in range(3):
    print(i)

Entraremos al  for, que tiene como iterador la variable i y con range() daremos la cantidad de 
iteraciones que en este caso seran 3. y cada ves que se itere se imprimira la variable i

""")

print("Entrando en bucle for: ")

for i in range(3):
    print(i)

print("Sali del bucle for ")


print("""
Estructura de Excepciones

Estructura try, except, else y finally. usaremos el siguiente ejemplo:

try:
    # Intenta ejecutar este código
    resultado = 10 / 0
except ZeroDivisionError:
    # Se ejecuta si hay una excepción ZeroDivisionError
    print("¡Error! No se puede dividir por cero.")
else:
    # Se ejecuta si no hay ninguna excepción
    print("La división fue exitosa.")
finally:
    # Siempre se ejecuta, haya o no haya una excepción
    print("Este es el bloque finally, se ejecuta siempre al final.")

como 10/0 es un error del tipo 'ZeroDivisionError', el codifo aplicara la excepción y no se detendra,
pero como tenemos un finally se imprimira ese mensaje al final.
      
""")


try:
    # Intenta ejecutar este código
    resultado = 10 / 0
except ZeroDivisionError:
    # Se ejecuta si hay una excepción ZeroDivisionError
    print("¡Error! No se puede dividir por cero.")
else:
    # Se ejecuta si no hay ninguna excepción
    print("La división fue exitosa.")
finally:
    # Siempre se ejecuta, haya o no haya una excepción
    print("Este es el bloque finally, se ejecuta siempre al final.")


print("")

# Opcional
print(f"Se realiza el ejercicio de DIFICULTAD EXTRA")
print("""La estructura utilizada es:

lista_numeros = []

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        lista_numeros.append(i)
    elif i == 55:
        lista_numeros.append(i)

Lo que da como resultado la lista con los valores:
""")
lista_numeros = []

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        lista_numeros.append(i)
    elif i == 55:
        lista_numeros.append(i)

print(lista_numeros)
