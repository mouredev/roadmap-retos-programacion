"""
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
 
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

#### EJEMPLOS DE TODOS LOS TIPOS DE OPERADORES ###
#De comparación:
print(3<4)
print(3<=4)
print(3>4)
print(3>=4)
print(3==4)
print(3!=4)

my_list = []
my_tuple = ()
print(my_list is my_tuple)
print(my_list is not my_tuple)


#Matemáticos
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(3//4)
print(3%4)
print(-4) #(valor negativo)
print(+4) #(valor positivo)
print(abs(-4))
print(int(4.459))
print(float(4))
c = complex(4)
print(c)
print(c.conjugate()) #parte real igual, opuesta de la imagiaria original
print(divmod(3, 4)) #(x // y, x % y)

print(pow(3, 4)) #x^y
print(3 ** 4) #x^y


#BITS
print(3<4 | 3>4) #or
print(3<4 ^ 3>4) #exclusive or

print(3<4 & 3>4) #and

print(3 << 10) #3 desplazado a la izquierda 10 bits
print(3 >> 1) #3 desplazado a la derecha 10 bits

print(~0) #invertir los bits de 4





### ESTRUCTURAS DE CONTROL ###

#if
if 3==4:
    print("TRUE")
elif 3>4:
    print("TRUE")
else:
    print("FALSE")

#while 
while 4!=4:
    print("Hola Python")
else:
    print("Adiós Python")

#for
for i in range(0, 5):
    print(i)
else:
    print("Hola mundo")    
    
#try
try:
    res = 4/0
    print(res)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print(res)
finally:
    print("Gracias")


    
### EXTRA ###
print("\nPROGRAMA EXTRA:")
for i in range(10, 56, 2):
    if i%3 != 0 and i != 16:
        print(i)  

