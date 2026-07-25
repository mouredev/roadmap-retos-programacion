'''
* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
*   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
*   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
'''

'''
* - Debes hacer print por consola del resultado de todos los ejemplos.
'''

# Operadores Aritméticos
print("OPERADORES ARITMÉTICOS: \n")
# Variables que usaremos para ilustrar los ejemplos
a = 5
b = 13
print(f"Valores a usar a:{a}, b:{b}")
# Suma
suma = a + b
print(f"Suma a + b: {suma} \n")
# Resta
resta = b - a
print(f"Resta b - a: {resta} \n")
# Multiplicación
multi = a * b
print(f"Multiplicación a * b: {multi} \n")
# División
divi = a / b
print(f"División a / b: {divi} \n")
# Módulo
modulo = b % a
print(f"Módulo b % a: {modulo} \n")
# Potencia
potencia = b ** a
print(f"Potencia b ** a: {potencia} \n")
# División entera
divient = b // a
print(f"División entera b // a: {divient} \n")

# Operadores de Asignación
print("OPERADORES DE ASIGNACIÓN: \n")
# Asignación de valor y variables que usaremos para ilustrar los ejemplos
a = 10
b = 100
c = 55
print(f"Variables a:{a}, b:{b}, c:{c} \n")
# Asig. Valor + 1
a += 6 # a = 16
print(f"a += 6: {a} \n")
# Asig. Valor - 1
a -= 6 # a = 10
print(f"a -= 6: {a} \n")
# Asig. Valor * 5
a *= 5 # a = 50
print(f"a *= 5: {a} \n")
# Asig. Valor / 2
a /= 5 # a = 10
print(f"a /= 5: {a} \n")
# Asig. Valor % 3
a %= 3 # a = 1
print(f"a %= 3: {a} \n")
# Asig. Valor % 3
a **= 5 # a = 1
print(f"a **= 5: {a} \n")
# Asig. Valor // 4
b //= 4 # b = 25
print(f"b //= 4: {b} \n")
# Asig. Valor & 3
b &= 3 # b = 1
print(f"b &= 3: {b} \n")
# Asig. Valor | 5
b |= 5 # b = 5
print(f"b |= 5: {b} \n")
# Asig. Valor ^=
c ^= 5 # c = 50
print(f"c ^= 5: {c} \n")
# Asig. Valor >>=
c >>= 5 # c = 1
print(f"c >>= 5: {c} \n")
# Asig. Valor <<=
c <<= 5 # c = 32
print(f"c <<= 5: {c} \n")

# Operadores de Identidad
print("OPERADORES DE IDENTIDAD: \n")
# Variables que usaremos para ilustrar los ejemplos
a = 5
b = 13
c = 5
print(f"Variables a:{a}, b:{b}, c:{c} \n")
# Comparación valores iguales => True
print(f"a is c: {a is c} \n")
# Comparación valores NO iguales => False
print(f"a is b: {a is b} \n")
# Comparación valores si no son iguales => False
print(f"a is not c: {a is not c} \n")
# Otras variables tipo String
txt1 = "RestosDeProgramacion"
txt2 = "RestosDeProgramacion"
# Comparación valores iguales => True
print(f"txt1 is txt2: {txt1 is txt2} \n")
# Comparación valores si no son iguales => False
print(f"txt1 is not txt2: {txt1 is not txt2} \n")
# Otras variables tipo list
list1 = [10,20,30]
list2 = [10,20,30]
# Comparación valores iguales => False (Las listas son objetos mutables)
print(f"list1 is list2: {list1 is list2} \n")

# Operadores Relacionales
print("OPERADORES RELACIONALES: \n")
# Variables que usaremos para ilustrar los ejemplos
a = 10
b = 20
c = 10
print(f"Variables a:{a}, b:{b}, c:{c} \n")
# Mayor que
print(f"Mayor que: a>b: {a>b} \b")
# Menor que
print(f"Menor que: a<b: {a<b} \n")
# Valor igual
print(f"Valor igual: a==c: {a==c} \n")	
# Mayor que o igual
print(f"Mayor que o igual: b>=c: {b>=c} \n")	
# Menor que o igual
print(f"Menor que o igual: c<=b: {c<=b} \n")	
# Valor diferente
print(f"Valor diferente: a!=c: {a!=c} \n")

# Operadores Bit a Bit
print("OPERADORES BIT A BIT: \n")
# Variables que usaremos para ilustrar los ejemplos
a = 2 # en binario = 10
b = 3 # en binario = 11
print(f"Variables a:{a}, b:{b} \n")
# Operación AND => a & b = 2 (Binario: 10 & 11 = 10)
print(f"Operación AND: a & b: {a & b} \n")
# Operación OR => a | b = 3 (Binario: 10 | 11 = 11)
print(f"Operación OR: a | b: {a | b} \n")
# Operación XOR => a ^ b = 1 (Binario: 10 ^ 11 = 01)
print(f"Operación XOR: a ^ b: {a ^ b} \n")
# Operación NOT => ~a = -3 (Binario: ~(00000010) = (11111101))
print(f"Operación NOT: ~a: {~a} \n")
# Desplaza los bits del operando de izquierda a la derecha => a >> b = 0 (Binario: 00000010 >> 00000011 = 0)
print(f"Desplazar Bits de Izquierda a Derecha: a >> b: {a >> b} \n")
# Desplazalos bits del operando de la izquierda a la izquierda => a << b = 16 (Binario: 00000010 << 00000011 = 00001000)
print(f"Desplazar Bits de Izquierda a Izquierda: a << b: {a << b} \n")

# Operadores Lógicos
print("OPERADORES LÓGICOS: \n")
# Variables que usaremos para ilustrar los ejemplos
a = True
b = False
print(f"Variables a:{a}, b:{b} \n")
# AND
print(f"AND: a and b: {a and b} \n")
# OR
print(f"OR: a or b: {a or b} \n")
# NOT
print(f"NOT: not a: {not a} \n")

# Operadores de Pertenencia
print("OPERADORES DE PERTENENCIA: \n")
# Variables que usaremos para ilustrar los ejemplos
lista = [1,2,3,4,5]
texto = "Hola Mundo"
print(f"Variables \n - Lista:{a} \n - Texto:{b} \n")
  
print("¿Esta el número/palabra en la lista/texto?: \n")
# Muestra True
print(f"4 in lista: {4 in lista} \n")
print(f"'Mundo' in texto: {"Mundo" in texto} \n")

print("¿No está el número/palabra en la lista/texto?: \n")
# Muestra True 
print(f"25 not in lista: {12 not in lista} \n")
print(f"'Visual' not in texto: {"Visual" not in texto} \n")

'''
* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
*   que representen todos los tipos de estructuras de control que existan
*   en tu lenguaje:
*   Condicionales, iterativas, excepciones...
'''

# Condicionales
print("OPERADORES CONDICIONALES: \n")

nombreMascota = "Caramelo"

if nombreMascota == "Calcetines":
    print("El nombre de la mascota es 'Calcetines' \n")
elif nombreMascota == "Manchitas":
    print("El nombre de la mascota es 'Manchitas' \n")
else:
    print(f"El nombre de la mascota no es 'Calcetines' ni 'Manchitas', es {nombreMascota} \n")

# Iterativas
print("OPERADORES ITERATIVOS: \n")
# Variables que usaremos para ilustrar los ejemplos
a = 3
b = 33
# Bucle For
print(f"Bucle For de {a} hasta {b} \n")
for i in range(a,b+1):
    print(f"- {i}")

# Bucle While
print(f"\n Bucle While de {a} hasta {b} \n")
i = a
while i <= b:
    print(f"- {i}")
    i += 1

# Excepciones
print("\n MANEJO DE EXCEPCIONES: \n")
try:
    print(f"Comparamos b <= a: {b <= a} \n")
except:
    print("Se ha producido un error en la operación. \n")
finally:
    print("Ha finalizado el manejo de excepciones pase lo que pase \n")

'''
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

# Hacemos uso de la estructura for para recorrer un rango e ir comprobando números
print ("EJERCICIO \n")
for i in range(10, 56):
    # Comprobamos que el número a imprimir cumple con las tres condiciones
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(f"- {i}")
