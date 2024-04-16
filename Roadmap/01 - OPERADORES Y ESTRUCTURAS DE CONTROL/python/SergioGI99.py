"""
-----------------------------------
OPERADORES Y ESTRUCTURAS DE CONTROL
-----------------------------------
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje:
  Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
(Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.)
"""
#Ejercicio

# Operadores aritméticos
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)

# Operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(2 < 3 != 4)

# Operadores lógicos
print(3 > 4 and "Hola" > "Python") # False and False = False
print(3 > 4 or "Hola" > "Python") # False or False = False
print(3 < 4 and "Hola" < "Python") # True and True = True
print(3 < 4 or "Hola" <  "Python") # True or True = True
print(3 < 4 and "Hola" > "Python") # True and Fasle = False
print(3 < 4 or "Hola" >  "Python") # True or False = True
print(not(3 > 4)) # Not(False) = True (Not niega)

# Operadores bit a bit
print(bin(0b100001 & 0b101101)) # AND
print(bin(0b100001 | 0b101101)) # OR
print(bin(~0b101101)) # NOT (-x -1) (cambia a negativo y añade -1)
print(bin(0b100001 ^ 0b101101)) #XOR
print(bin(0b000100 >> 1)) # Desplaza todos los bits a la derecha un numero determinado de veces
print(bin(0b000100 << 1)) # Analogo de >>

# Operadores de asignación
a = 20; print(a) #20
a += 2; print(a) #22
a -= 2; print(a) #20
a *= 2; print(a) #40
a /= 2; a = int(a); print(a) #20
a %= 3; print(a) #2
a **= 3; print(a) #8
a //= 3; print(a) #2
b = 0b101010
b &= 0b111111; print(bin(b)) #0b101010
b |= 0b111111; print(bin(b)) #0b111111
b = 0b101010
b ^= 0b111111; print(bin(b)) #0b010101 = 0b10101
b <<= 1; print(bin(b))
b >>= 1; print(bin(b))

# Operadores de identidad
  
  # is
a = 10
b = 10
print(a is b) # True
b = 15
print(a is b) # False
  
  # is not
a = 10
b = 10
print(a is not b) # False
b = 15
print(a is not b) # True

# Operadores de pertenencia
my_str = "Hola Python"
print("Hola" in my_str) # True
print("hola" in my_str) # False
my_set = set([1, 2, 3, 4, 5])
print(3 in my_set) # True
print(8 in my_set) # False
print(8 not in my_set) # True

# Estructuras de control
number = 25
  
  # condicionales
if number >= 10  and number <= 20:
  print(number, "es igual o mayor que 10 y menor o igual que 20")
elif number < 10:
  print(number, "es menor que 10")
else:
  print(number, "es mayor que 20")
  
  # iterativas
while number > 0:
  print(number)
  number -= 1
  
  # for
for n in range(0, 6):
  print(n)

# EXTRA
for n in range(10, 56):
  if n % 2 == 0 and n % 3 != 0 and n != 16:
    print(n)