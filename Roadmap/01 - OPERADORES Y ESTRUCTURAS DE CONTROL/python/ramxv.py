### Tipos de Operadores ###

# Aritméticos
'''
  Operador    Nombre
  +           Suma
  -           Resta
  *           Multiplicación
  /           División
  %           Modulo
  **          Exponente
  //          Cociente
''' 
adicion = 12 + 15
subtraccion = 12 - 15
multiplicacion = 12 * 15
division = 12 / 4
modulo = 12 % 3
potencia = 12 ** 2
division_entero = 12 // 5
print("### Operadores Aritméticos ###")
print(adicion)
print(subtraccion)
print(multiplicacion)
print(division)
print(modulo)
print(potencia)
print(division_entero,"\n")

# Lógicos
'''
  Operador              Descripción
  and         Devuelve True si ambos son True
  or          Devuelve True si alguno de los operandos es True
  not         Devuelve True si alguno de los operandos es False
'''
print("### Operadores Lógicos ###")
print(True and False)
print(True or False)
print(not True,"\n")

# Comparación
'''
  Operador    Nombre
  ==          Igual
  !=          Distinto
  >           Mayor
  <           Menor
  >=          Mayor o igual
  <=          Menor o igual
''' 
x=2; y=3
print("### Operadores de Comparación ###")
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y,"\n")

# Bit a Bit
'''
Los operadores a nivel bit o bitwise operators son operadores actúan sobre números enteros pero usando su representación binaria.

  Operador      Nombre
  |             And bit a bit
  &             Or bit a bit
  ~             Not bit a bit 
  ^             Xor bit a bit
  >>            Desplazamiento a la derecha 
  <<            Desplazamiento a la izquierda
'''
print("### Operadores Bit a Bit ###")
a = 0b1101
b = 0b1011
print(bin(a | b)) # 0b1111
print(bin(a & b)) # 0b1001
print(bin(~a)) # -0b1110
print(bin(a ^ b)) # 0b110
print(bin(a>>2)) # 0b11
print(bin(a<<2),"\n") # 0b110100

# Asignación
'''
  Operadores
  =  
  += 
  -= 
  *= 
  /= 
  %= 
  **=
  //=         
  &=
  |=
  ^=
  >>=
  <<=
''' 
print("### Operadores de Asignación ###")
# Le asignamos el valor de 7 a la variable a
a = 7
print("a = 7 ->",a) # 7

# a += 2 es equivalente a: a = a + 2 
a = 7
a += 2 
print("a += 2 ->",a) # 14

# a -= 2 es equivalente a: a = a - 2 
a = 7
a -= 2
print("a -= 2 ->",a) # 2

# a *= 2 es equivalente a: a = a * 2 
a = 7
a *= 2
print("a *= 2 ->",a) # 49

# a /= 2 es equivalente a: a = a / 2
a = 7
a /= 2
print("a /= 2 ->",a) # 3.5

# a %= 2 es equivalente a: a = a % 2
a = 7
a %= 2
print("a %= 2 ->",a) # 1

# a **= 2 es equivalente a: a = a ** 2
a = 7
a **= 2
print("a **= 2 ->",a) # 49

# a //= 2 es equivalente a: a = a  2
a = 7
a //= 2
print("a //= 2 ->",a) # 3

# a &= 2 es equivalente a: a = a  2
a = 7
a &= 2 
print("a &= 2 ->",a) # 2

# a |= 2 es equivalente a: a = a  2
a = 7
a |= 2
print("a |= 2 ->",a) # 7

# a ^= 2 es equivalente a: a = a  2
a = 7
a ^= 2
print("a ^= 2 ->",a) # 5

# a >>= 2 es equivalente a: a = a  2
a = 7
a >>= 2
print("a >>= 2 ->",a) # 1

# a <<= 2 es equivalente a: a = a  2
a = 7
a <<= 2
print("a <<= 2 ->",a,"\n") # 28

# Pertenencia
'''
Un operador de pertencia se emplea para identificar pertenencia en algunas secuencia(listas,strings,tuplas).

- 'in' y 'not in' son operadores de pertencia.

- 'in' devuelve True si el valor especificado se encuentra en la    secuencia. En caso contrarios devulve False.

- 'not in' devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.
'''
l = [1,2,3,4,5,6]
print("### Operadores de Pertenencia ###")
print(6 in l) # True
print(7 not in l) # True
print(0 in l) # False
print(2 not in l) # False
string = "Hola Python"
print("Hola" in string) # True
# Nota: distingue entre mayúsculas y minúsculas.
print("python" in string,"\n") # False

# Identidad
'''
Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.

- 'is' y 'is not' son operadores de identidad.

- 'is' devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.

- 'not in' devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.

Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.
'''
z = 3 
k = 3
i = 2
print("### Operadores de Identidad ###")
print(z is k)
print(z is not k)
print(z is not i, "\n")

### Estructuras de Control ###

# Estructura de control if: 
print("### Estructura de control if ###")

# Utilizando else
a = 10
if a > 5 and a < 15:
  print("Mayor que 5 y menos que 15")
else:
  print("No esta en el rango")

# Utilizando elif
b = 16
if b > 5 and b < 15:
  print("Mayor que 5 y menos que 15")
elif b <= 5:
  print("Menor o igual que 5")
elif b >= 15:
  print("Mayor o igual que 15")

# Operador Ternario 
x = 5
print("Es 5" if x == 5 else "No es 5")
print("\n")

# Estructura de control for
print("### Estructura de control for ###")
for i in range(0,10):
  print(i)
print("\n")

# Estructura de control while
print("### Estructura de control for ###")
x = 5
while(x > 0):
  x -= 1
  print(x)
print("\n")

# Punto opcional
print("### Punto Opcional ###")
for i in range(10,56):
  if i % 2 == 0 and i != 16 and i % 3 != 0:
    print(i)
