"""
Vamos a crear operadores aritméticos en python
"""

suma=2+3
resta=6-3
division=10/2
modulo=10%3
div_entera=10//3
exponencial=2**3


print(suma)
print(resta)
print(division)
print(modulo)
print(div_entera)
print(exponencial)

"""
operadores de asignación
"""
print(" ")
suma += 1
print(f"le sumo 1 = {suma}")
resta -=1
print(f"le resto 2 = {resta}")
division /= 2
print(f"divido por 2 = {division}")
modulo %= 2
print(f"divido por 2 y le asigno el resto = {modulo}")
div_entera //= 2
print(f"realizo división entera por 2 y la asigno = {div_entera}")
exponencial **= 2
print(f"realizo exponencial por 2 y la asigna = {exponencial}")

"""
operadores de comparación
"""
print(" ")
igual = 1 == 2
print(f"1 es igual a 2? Eso es {igual}")
desigual = 1!=2
print("1 es desigual a 2? eso es {desigual}")
superior = 2>1
print(f"2 es superior a 1? eso es {superior}")
inferior = 1<2
print(f"1 es inferior a 2? eso es {inferior}")
sup_igual= 2 >= 3
print(f"2 es superior o igual a 3? Eso es {sup_igual}")
inf_igual=2<3
print(f"2 es inferior o igual a 3? Eso es {inf_igual}")

"""
operadores lógicos que se usan habitualmente en las estructuras de control
"""
print(" ")
primero = True
segundo = True
if (primero and segundo): # operador AND. Se usa para concatenar dos valores iguales para operar
    print("cierto")

if (primero or segundo):
    print("cierto también") # operador OR. Se usa para operar si uno u otro es cierto.

contrario = False
if not contrario:
    print("es cierto si es falsa la variable") # operador NOT. Se usa para generar el valor contrario de la variable booleana

"""
Estructuras de control
if
elif
else
"""
print(" ")
control = True  # usamos solo if
if (control):
    print("control es cierto")

print(" ")
control = False # usamos elif si la funcion if no concuerda su condición
if (control):
    print("control es cierto")
elif control == False:
    print("control es falso")

print(" ")
control = False # usamos else cuando ni if ni elif actuan
a = 0
if (control):
    print("control es cierto")
elif control == False and a == 1:
    print("control es falso")
else:
    print("nada es correcto")

"""
funciones de iteración 
while
for
"""
print(" ")
while a<=5: # while realiza la iteración mientras se da la condición
    print(f"bucle while {a}")
    a+=1

print(" ")
for a in range(5): # for realiza una iteración que estableces en la función range() o en los valores de una tupla, lista, cadena
    print(f"bucle for {a}")

"""
EJERCICIO
"""
print(" ")
for i in range(10,56,2):
    if (i==16) or i%3 == 0:
        continue
    
    print(f"iteración {i} no es 16 ni múltiplo de 3")

