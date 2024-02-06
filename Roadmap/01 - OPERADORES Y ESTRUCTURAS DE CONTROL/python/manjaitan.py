'''

OPERATORS:

+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=

'''

# ARITMETICOS:

print ("########################")

# Operador suma:
resultado = 1 + 1
print (resultado)

# Operador resta:
resultado = 1 - 1
print (resultado)

# Operador multiplica:
resultado = 2 * 2
print (resultado)

# Operador dividir:
resultado = 2 / 2
print (resultado)

# Operador division del piso, descarta el resto:
resultado = 2 // 2
print (resultado)

# Operador resto:
resultado = 2 % 2
print (resultado)

# LOGICOS:

# and => True and True => Devuelve True.
# or => True or false => Devuleve True.
# not => not True => Devuelve False.

print ("########################")

a = True
b = False

resultado = a and a
print (resultado)

resultado = a or b
print (resultado)

resultado = b or b
print (resultado)

resultado = (not a)
print (resultado)

resultado = (not b)
print (resultado)

# OPERADORES DE ASIGNACION:

# = += -= *= /= %= **= //=

print ("########################")

valor = 1
valor += 1
print(valor)

valor = 1
valor -= 1
print(valor)

valor = 2
valor *= 2
print(valor)

valor = 20
valor /= 5
print(valor)

# OPERADORES DE INDENTIDAD:

# is , is not.

print ("########################")

a = 1
b = 2
c = 3

print (a is b)
print (a is not b)
print (a is not c)

# OPERADORES DE PERTENCIAS, devuelve valor True o Falso.
# in, not in.
print ("########################")

lista = [1,2,3,4,5,6,8,9,10]
resultado = 4 in lista
print (resultado)
resultado = 5 in lista
print (resultado)
resultado = 5 not in lista
print (resultado)
resultado = 4 not in lista
print (resultado)


# OPERADORES DE BIT.
# x | y, x ^ y, x & y, x << n, x >> n, ~x

print ("########################")

a = 4
b = 2
resultado = a | b
print(resultado)

# ESTRUCTURAS CONDICIONALES, ITERATIVAS, EXCEPCIONES.
# if, if-else
# for
print ("########################")

a = 1 ; b = 2; c = 3

resultado = a + b + c

if ( resultado >= 3 ):
    print ("Resultado es mayor a 3")
else:
    print ("Resultado es menor a 3")

print ("########################")
    
# ITERATIVAS.

for x in range (1, 10, 1):
    print (x)
    

print ("########################")

# EXCEPCION.

while True:
    try:
        x = int(input("Introduzca un número: "))
        break
    except ValueError:
        print ("Número introducido no es del tipo correcto, vuelva a intentarlo.")
        
# OPCIONAL:
print ("########################")


for x in range (10, 56, 1 ):
    if x == 16:
        exit
    elif x % 2 == 0:
        print (x)
    elif x % 3 == 0:
        exit