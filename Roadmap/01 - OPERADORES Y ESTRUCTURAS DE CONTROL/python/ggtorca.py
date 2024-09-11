# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
#### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

"""""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap]

# Operadores aritmeticos

print("")
print("Operadores aritemticos")

mi_suma = 20+5
mi_resta = 20-5
mi_multiplicacion = 25*4
mi_division = 300/2
mi_division_entera = 10//3
mi_residuo = 15%4
mi_exponenciacion = 2**3

print(f"resultado suma = {mi_suma}, resultado resta = {mi_resta}, resultado multiplicacion = {mi_multiplicacion}, resultado division = {mi_division}, resultado mi division entera = {mi_division_entera}, resultado de mi residuo = {mi_residuo}, resultado de mi exponienciacion = {mi_exponenciacion}")
# Operadores lógicos

print("")
print("Operadores logicos")
print("")

#and
a = True
b = False

resultado_and = a and b

print(f"Reslutado and {resultado_and}")

#or
a = True
b = False

resultado_or = a or b

print(f"Reslutado or {resultado_or}")

#not
a = True

resultado_not = not a

print(f"Reslutado not {resultado_not}")
# Operadores de comparación

print("")
print("Operadores de comparacion")
print("")

x = 20
y = 30
print(x==y)#Igual a
print(x!=y)#No igual a
print(x>y)#Mayor que
print(x<y)#Menor que
print(x>=y)#Mayor o igual que
print(x<=y)#Menor o igual que
# Operadores de asignación

print("")
print("Operadores de asignacion")
print("")

c = 50

c+= 10 #Asignacion de suma
c-= 10 #Asignacion de resta
c*= 10 #Asignacion de multiplicacion
c/= 10 #Asignacion de division
c//= 10 #Asignacion de division entera
c%= 10 #Asignacion de resto
c**= 10 #Asignacion de exponienciacion

# Operadores de identidad

print("")
print("Operadores de identidad")
print("")

g = "xabi"
t = "julen"

print(g is t)
print(g is not t)

# Operadores de pertenencia

print("")
print("Operadores de pertenencia")
print("")

lista_compra = ["huevos", "haria", "chocolate para fundir"]
print("chocolate para fundir" in lista_compra)
print("levadura" not in lista_compra)

# Operadores de bits

print("")
print("Operadores de bits")
print("")

h = 4
i = 5
#AND
print (h & i)
#OR
print (h | i)
#XOR
print (h ^ i)
#NOT
print (~h)
#<<
print(h << 1)
#>>
print(h >> 1)
'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 '''
def ImprimerNum():
    print("")
    print("Ejercicio extra: ")
    print("")
    
    for i in range (10, 56):
        if i != 16 and i %2 == 0 and i %3 != 0:
            print(i)
ImprimerNum()