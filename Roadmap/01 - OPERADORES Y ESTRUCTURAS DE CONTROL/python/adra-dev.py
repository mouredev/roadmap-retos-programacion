"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu 
lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad,
pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje: Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

- DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
by adra-dev.
"""

"""
Operadores: Los operadores son simbolos que indican la operacion que 
se va a llevar a cabo.
"""

"""
Operadores de asignacion: Son aquellos que permiten dar un valor a 
una variable o modificarlo.
"""

resultado = 6 # Asignacion simple
print(resultado)
resultado += 2 # Asignacion de suma
print(resultado)
resultado -= 4 # Asignacion de resta
print(resultado)
resultado *= 5 # Asignacion de multiplicacion
print(resultado)
resultado /= 2 # Asignacion de division
print(resultado)
resultado %= 4 # Asignacion de modulo
print(resultado)
resultado **= 3 # Asignacion exponencial
print(resultado)
resultado //= 5 # Aasignacion de division entera
print(resultado)

"""
Operadores aritmeticos: Son aquellos que permiten realizar operaciones 
aritmeticas.
"""

a = 10
b = 8

a + b # Suma
print(a+b)
a - b # Resta
print(a-b)
a * b # Multiplicacion
print(a*b)
a ** b # Potencia
print(a**b)
a / b # Cociente de la division
print(a/b)
a // b # Cociente de la division entera
print(a//b)
a % b # Resto de la division entera
print(a%b)

"""
Operadores relacionales o de comparacion: Son simbolos que se utilizan
para comparar dos valores o expresiones.
"""

a == b # Igual a 
print(a==b)
a != b # Distinto de 
print(a!=b)
a > b # Mayor que
print(a>b)
a < b # Menor que
print(a<b)
a >= b # Mayor o igual que
print(a>=b)
a <= b # Menor o igual que
print(a<=b)

"""
Operadores logicos o booleanos: Son aquellos que permiten conectar
dos expresiones de comparcion y evaluarlas de forma logica, excepto
el operador not que invierte el valor logico de la expresion sobre 
la que se aplica.
"""

a = (3 > 2)
b = (5 >= 6)
c = (3 != (2+1))
d = (4 == (2*3))

# and
print(a and b)
print(a and c)
print(c and a)
print(c and d)

# or
print(a or b)
print(a or c)
print(c or a)
print(c or d)

# not
print(not a)
print(not b)
print(not c)
print(not d)

"""
Operadores a nivel de bit: Se utilizan para comparar numeros enteros
en su representacion binaria, es decir operan sobre cada uno de los 
bits del entero sobre el que se aplican, y devuelven el numero entero
correspondiente al resultado binario.
"""

a = 5
b = 4

# & and binario
print(a & b)

# | or binario
print(a | b)

# ^ or exclusivo binario
print(a ^ b)

# ~ not binario
print(~a)
print(~b)

# << desplazamiento a la izquierda
print(a << 2)

# >> desplazamiento a la derecha
print(a >> 2)

# podmeos mostrar la representacion binaria de un entero con la funcion bin()

print(bin(5))

print(bin(3))

print(bin(5&3))
print(bin(5|3))
print(bin(5>>2))
print(bin(5<<2))

"""
Operadores de pertenencia: Se utilizan para comparar si un dato forma
parte o no de una coleccion.
"""

a = 4
b = [1, 2, 3, 4, 5, 6]
c = 2
d = ('caramelos', 2)
e = 'b'
f = 'casa'

print(a in b)

print(c in d)

print(e in f)

print(a not in b)

print(c not in d)

print(e not in f)

"""
Operadores de identidad: Evaluan si las referencias de dos variables
apuntan al mismo objeto.
"""

a = [1, 2, 3, 4, 5, 6]

b = [1, 2, 3, 4, 5, 6]

print(a is b)

a = [1, 2 , 3]

b = a

print(b is a)

"""
Estructuras de control: Permiten ejecutar mas de una vez una instruccion
o un bloque de instrucciones.
"""

"""
Condicones: permiten elegir entre distintos resultados segun el valor
de una expresion.
"""

# if
edad = 16

if edad >= 18:
    acceso = 'Puede entrar al pub'
else:
    acceso = 'No puede entrar al pub'
print(acceso)

# switch 
peso = 100
def colocar_huevo(caja):
    
    if peso < 53:
        caja = "S"
    elif peso < 63:
        caja = "M"
    elif peso < 73:
        caja = "L"
    else:
        caja = "XL"
    return caja

print(colocar_huevo(peso))



# match o switch (version de python 3.12 en adelante):

def http_error(status):
    """
    Una instrucción match toma una expresión y compara su valor con 
    patrones sucesivos dados como uno o más bloques de casos.
    """
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(http_error(418))


"""
Bucles for y while: permiten repetir un bloque de instrucciones hasta
que una condicion se cumpla.
"""

# while repite instrucciones mientras se cumpla la condicion.

# calculo de !4
a = 4
acc =1
while a > 1:
    acc *= a
    a -= 1
print(acc)

# for se utiliza cuando conocemos el numero de repeticiones.

for e in [1, 2, 3]:
    print(e**2)

"""
Excepciones: Una excepcion es un error logico que se produce en 
tiempo de ejecucion. 

Las excepciones van asociadas a distintos tipos,
y ese mismo tipo es el que se muestra en el mensaje de error.
"""

try:
    
    print(resultado =  15 * (3/0))   
except IOError:
    # Instrucciones si ocurre la excepcion IOError
    print("Error de entrada/salida.")
except ZeroDivisionError:
    # Instrucciones si ocurre la excepcion ZeroDivisionError
    print("Error de division por cero.")
else:
    # Instrucciones si no ocurre ninguna excepcion
    print("El resultado de la division es", resultado)
finally:
    # Instrucciones si ocurren o no ocurren excepciones
        print("Archivo resultado.txt cerrado.")


# Extra

for n in range(9, 56):
    if n == 16:
        pass
    elif not(n % 3 == 0) and (n % 2 == 0):
            print(n)
