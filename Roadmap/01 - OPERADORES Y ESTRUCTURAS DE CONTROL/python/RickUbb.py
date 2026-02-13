# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# Aritmeticos
from operator import truediv

mi_suma = 4 + 4
mi_resta = 4 - 2
mi_multip = 3 * 3
mi_div = 10/3
# 2 elevado a la 4
mi_expoenciacion = 2**4
# modulo es lo que sobra de la division
mi_modulo = 10 % 5
# Se redondea hacia abajo
mi_diventera = 10//3
mi_diventera2 = -10//3
print(mi_suma)
print(mi_resta)
print(mi_multip)
print(mi_div)
print(mi_expoenciacion)
print(mi_modulo)
print(mi_diventera)
print(mi_diventera2)

# Logicos
# and
edad = 18
tiene_licencia = True

if (edad >= 18 and tiene_licencia == True):
    print("Podeis pasar!")

# or
edad = 18
tiene_licencia = True

if (edad <= 18 or tiene_licencia == False):
    print("No podeis pasar!")

# not
edad = 18
tiene_licencia = True

if not(edad <= 18 or tiene_licencia == False):
    print("No podeis pasar!")

# De comparación
# igual a
if 7 == 7:
    print("Siuu!")

# diferente de
if mi_suma != mi_resta:
    print("Not Siuu!")

# menor
if mi_suma < mi_resta:
    print("Suma menor")
else:
    print("Resta menor")

# menor o igual
if mi_suma <= mi_resta:
    print("Suma menor o igual")
else:
    print("Resta menor y no igual")

# mayor
if mi_suma > mi_resta:
    print("Suma mayor")
else:
    print("Resta mayor")

# mayor o igual
if mi_suma >= mi_resta:
    print("Suma mayor o igual")
else:
    print("Resta mayor y no igual")

# is
a = 9
b = 9
print(a is b)
a = [1,2,3]
b = [1,2,3]
print(a is b)

x = None

if x is None:
    print("No tiene valor")

# in
# OJO: en diccionarios, in busca en las claves, no en los valores.
print(7 in [7, 8, 9])

texto = "hola mundo"

print("hola" in texto)   # True
print("z" in texto)      # False

# De asignacion
# basico
# normal =
mi_variable = 20
print(mi_variable)

# suma =
mi_variable += 2
print(mi_variable)

# resta =
mi_variable -= 2
print(mi_variable)

# multp =
mi_variable *= 2
print(mi_variable)

# div =
mi_variable /= 2
print(mi_variable)

# divent =
mi_variable //= 2
print(mi_variable)

# potencia =
mi_variable **= 2
print(mi_variable)

# modulo =
mi_variable %= 2
print(mi_variable)

# Asignacion con bits
# &= AND bit a bit
x = 6   # 110
x &= 3  # 011
print(x)  # 2

# |= OR bit a bit
x = 6   # 110
x |= 3  # 011
print(x)  # 7

# ^= XOR bit a bit
x = 6   # 110
x ^= 3  # 011
print(x)  # 5

# <<= Shift izquierda (desplazar bits a la izquierda)
# Es como multiplicar por 2 cada vez que te mueves 1 lugar.
x = 3      # 011
x <<= 2    # mueve 1 a la izquierda
print(x)   # 12

# >>= Shift derecha (desplazar bits a la derecha)
# Es como dividir por 2 (entero) cada vez que te mueves 1 lugar.
x = 24      # 011
x >>= 2    # mueve 1 a la izquierda
print(x)   # 6

# Operador especial := (Walrus operator)
# Permite asignar valor a variables dentro de if, while, etc

saludo = "Hola"
if (n := len(saludo) == 4) :
    print(saludo)

#while (linea := input("Escribe algo: ")) != "":
#    print("Dijiste:", linea)


# Estructuras de control
# Condicionales
#If elif else
if (2 > 10):
    print("Hola")
elif (3 > 10):
    print("Holas")
else:
    print("Hola mundo")

#Iterativas
#For
for i in range(5):
    print(i)


#While

while (i < 10):
    print(i)
    i += 1

#break
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
for i in range(5):
    if i == 2:
        continue
    print(i)

if True:
    pass


# Manejo de exepciones
try:
    x = int(input("Ingresa un número: "))
    print(10 / x)
except ValueError:
    print("Eso no es un número")
except ZeroDivisionError:
    print("No se puede dividir para 0")
else:
    print("Todo salió bien ✅")
finally:
    print("Esto siempre se ejecuta")


# Selección múltiple:
opcion = 2

match opcion:
    case 1:
        print("Crear")
    case 2:
        print("Editar")
    case 3:
        print("Eliminar")
    case _:
        print("Opción inválida")


# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
print("")
for i in range(10 , 55):
    if (i % 2 == 0 and i >= 10 and i % 3 != 0 and i != 16):
        print(i)
