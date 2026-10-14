# operadores y estructura de control
""" 
operadores de lenguaje Python
Aritméticos: funcionan para cuentas matemáticas:
    (+) suma, (-) resta, (*) multiplicación, (/) división, (//) división entera, (**) potencia y (%) módulo
"""
# constantes:
n1= 3
n2= 7
n3= 4
n4= 20
n5= 12

print("La suma de 3+3 es igual a:",n1+n1) # resultado 6
print("La resta de 7-3 es igual a:",n2-n1) #resultado 4
print("La multiplicación de 4x7 es igual a:",n3*n2) #resultado 28
print("La división de 20/4 es igual a:" ,n4/n3) #resultado 5
print("La División de 20/4 sin decimales es igual a:" ,n4//n3)
print("La potencia de 12 al cubo es",n5**3) #resultado 1728
print("modulo: 7 y 3 es:" ,n1%n2)



"""
De comparación: permiten comparar dos valores y dan como resultado:
    (True) verdadero o (False) falso, (==) como igual a, (<) menor que, (>) mayor que
"""
print("12 es menor que 20?:" ,n5<n4)
print("20 es menor que 3?:" ,n1>n4)
print("3 oes igual a 03?:" ,n3==n3)

"""
Lógicos: combinan condiciones
    (y) and, (or) o y (not) no
"""
print("condición and: n1=3? y n2=7?" ,n1==3 and n2==7)
print("condicion or: n1=1 o n2=7" ,n1==1 or n2==7)
print("condición not: n1=1?" ,not n1==1)


"""
De asignación: guardan valores en una variable
    (=) igual, (+=) suma y asigna, (-=)
"""
m= 15 # = es una asignacion
print (m) 
m += 1 #suma y asignación
print (m)
m -= 1 #resta y asignación
print (m)
m *= 2 #multiplicación y asignación
print (m)
m /= 2 #división y asignación
print (m)
m %= 2 #modulo y asignación
print (m)
m **= 1 #potencia y asignación
print (m)
m //= 1 #división entera y asignación
print (m)

"""    
De identidad: comprueba si dos varibles apuntan al mismo lugar
    is e is not
"""
nn= m #esta variable toma el valor de m que es 1.0
print (f"Es {nn} el valor del nuevo número?", m is nn)
print (f"No es {nn} el valor del nuevo número?", m is not nn)


"""""
De pertenencia: Verifica si un valor se encuentra dentro de una secuencia
    in y not in
"""
print (f"La letra 'a' esta en este apellido Mendoza?", 'a' in 'mendoza')
print (f"La letra 'x' no esta en este apellido Mendoza?", 'x' not in 'mendoza')

"""""
A nivel de bits (Bitwise): manipulan números a nivel de sus bits binarios
    &, |, ^
"""
a = 10 # 1010
b = 3 # 0011
print(f"El resultado AND de 10 & 3 es: {a & b}") #0010
print(f"El resultado OR de 10 | 3 es: {a | b}") #1011
print(f"El resultado XOR de 10 ^ 3 es: {a ^ b}") #1001
print(f"El resultado NOT de 10 es: {~10}")
print(f"desplazamiento a la derecha: 10 >> 2 es: {10 >> 2}") #0010
print(f"desplazamiento a la izquierda: 10 << 2 es: {10 << 2}") #101000

#Estructuras de control 

#condicionales 
my_string = "Tony"

if my_string == "Antonio":
    print ("Hola Antonio")
elif my_string == "Tony":
    print("Hola Tony")
else:
    print ("Hola quien eres?")

#iterativas

for i in range(9):
    print (i)

i=0
while i <=10:
    print (i)
    i += 1

# manejo de exepciones
try:
    print(10/1)
except:
    print("Error: No se puede dividir entre cero")
finally:
    print("ha finalizado el manejo de exepciones")


#extra

for numero in range (10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)

