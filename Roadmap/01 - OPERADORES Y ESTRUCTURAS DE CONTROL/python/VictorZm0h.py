"""EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)"""

#Operadores:

# Aritméticos
suma = 5 + 3
resta = 10 - 4
multiplicacion = 2 * 6
division = 8 / 2
modulo = 10 % 3
exponente = 2 ** 3
#Ejemplos:
primernumero=float(input("Introduce el primer numero: "))
segundonumero=float(input("Introduce el segundo numero: "))
tipoDeOperacion=input("Introduce el tipo de operacion: ")
if tipoDeOperacion=="suma":
    print("El resultado de la suma es: ", primernumero+segundonumero)
elif tipoDeOperacion=="resta":
    print("El resultado de la resta es: ", primernumero-segundonumero)
elif tipoDeOperacion=="multiplicacion":
    print("El resultado de la multiplicacion es: ", primernumero*segundonumero)
elif tipoDeOperacion=="division":
    print("El resultado de la division es: ", primernumero//segundonumero)
else:
    print("Operacion no valida")
# Lógicos
and_logico = True and False # Deben cumplirse ambas condiciones
or_logico = True or False # Se cumple si al menos una condición es verdadera
xor_logico = True ^ False  # Se cumple si solo una condición es verdadera
not_logico = not True # Negación de una condición
#Ejemplos: 
#Si la edad es mayor o igual a 18 Y menor o igual a 100, mostrar "Puedes votar". En caso contrario, mostrar "No puedes votar".
"""edad=(int(input("Introduce tu edad: ")))
if edad>=18 and edad<=100:
    print("Puedes votar")
else:
    print("No puedes votar")"""
"""edad=(int(input("Introduce tu edad: ")))
pais=input("Introduce tu país: ")
if edad>=18 and pais.lower()=="venezuela":
    print("Puedes ingresar al ejercito")
else:
    print("No puedes ingresar al ejercito")"""
#Si el cliente es estudiante O tiene más de 65 años, mostrar "Tienes descuento". En caso contrario, mostrar "No tienes descuento".
"""estudiante=(int(input("¿Eres estudiante? (1-Si/0-No): ")))
edad=int(input("Introduce tu edad: "))
if estudiante==1 or edad>65:
    print("Tienes descuento")
else:
    print("No tienes descuento")"""
"""edad=int(input("Introduce tu edad: "))
pais=input("Introduce tu país: ")
if (edad>=18 and pais.lower()=="venezuela") or (edad>=20 and pais.lower()=="colombia"):
    print("Puedes ingresar al ejercito")
else:
    print("No puedes ingresar al ejercito")"""
#Si NO tiene membresía, mostrar "Debes pagar la tarifa completa".Si tiene membresía, mostrar "Tienes acceso gratuito".
"""membresia=(int(input("¿Tienes membresía? (1-Si/0-No): ")))
if not membresia==1:
    print("Debes pagar la tarifa completa")
else:
    print("Tienes acceso gratuito")"""

# Comparación
igual = (5 == 5)
diferente = (5 != 3)
mayor_que = (5 > 3)
menor_que = (3 < 5)
mayor_igual = (5 >= 5)
menor_igual = (3 <= 5)
# Asignación
asignacion = 10
asignacion += 5  # equivalente a asignacion = asignacion + 5
asignacion -= 3  # equivalente a asignacion = asignacion - 3    
asignacion *= 2  # equivalente a asignacion = asignacion * 2
asignacion /= 4  # equivalente a asignacion = asignacion / 4
asignacion %= 3  # equivalente a asignacion = asignacion % 3
asignacion **= 2  # equivalente a asignacion = asignacion ** 2
# Identidad
is_identity = (asignacion is not None)  # Verifica si asignacion no es None
# Pertenencia
lista = [1, 2, 3, 4, 5]
pertenencia = 3 in lista  # Verifica si 3 está en la lista
# Bits
bit_and = 5 & 3  # AND bit a bit
bit_or = 5 | 3   # OR bit a bit
bit_xor = 5 ^ 3  # XOR bit a bit
bit_not = ~5  # NOT bit a bit
# Desplazamiento de bits
desplazamiento_izquierda = 5 << 1  # Desplaza los bits de 5 a la izquierda (multiplica por 2)
desplazamiento_derecha = 5 >> 1  # Desplaza los bits de 5 a la derecha (divide por 2)
