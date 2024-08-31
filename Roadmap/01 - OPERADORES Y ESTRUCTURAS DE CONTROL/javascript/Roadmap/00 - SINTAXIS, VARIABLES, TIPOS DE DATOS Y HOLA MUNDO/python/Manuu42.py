
# https://www.python.org

#varias lineas
#de comentarios
"""
comentario
de varias
lineas
"""

'''
1. Operadores Aritméticos:
    + Suma
    - Resta
    * Multiplicación
    / División
    // División entera
    % Módulo (resto de la división)
    ** Potenciación
'''
numero1 = 20
numero2 = 30

print("Suma", numero1 + numero2)        # 50
print("Resta", numero1 - numero2)       # -10
print("Multiplicación", numero1 * numero2)  # 600
print("División", numero1 / numero2)    # 0.6666666666666666
print("División entera", numero1 // numero2)  # 0
print("Módulo", numero1 % numero2)     # 20
print("Potenciación", numero1 ** numero2)  # 107374182400

# Operadores de comparación ( >, <, ==, >=, <=, !=, ) -> devuelve un valor booleano
# Estructuras de control (if, elif, else), condicionales
'''

2. Operadores de Comparación:
    == Igual a
    != Diferente de
    < Menor que
    > Mayor que
    <= Menor o igual que
    >= Mayor o igual que
'''
if numero1 == numero2:
    print("Los números son iguales")
elif numero1 != numero2:
    print("Los números son diferentes")
    if numero1 < numero2:
        print(f"El numero {numero1} es menor que {numero2}")
    elif numero1 > numero2:
        print(f"El numero {numero1} es mayor que {numero2}")    
if numero1 <= numero2 or numero1 >= numero2:
    if numero1 <= numero2:
        print(f"El numero {numero1} es menor o igual que {numero2}")
    elif numero1 >= numero2:
        print(f"El numero {numero1} es mayor o igual que {numero2}")

# Operadores lógicos (para trabajar con valores de tipo bool) -> AND, OR, NOT
'''

3. Operadores Lógicos:
    and = Y
    or  = O
    not = Negación
'''
print(True and True)        # devuelve True
print(True and False)       # devuelve False
print(True or False)        # devuelve True
print(False or True)        # devuelve True
print(not True)             # devuelve False
print(not False)            # devuelve True

'''
4. Operadores de Asignación:
    = Asignación
    += Suma y asignación
    -= Resta y asignación
    *= Multiplicación y asignación
    /= División y asignación
    //= División entera y asignación
    %= Módulo y asignación
    **= Potenciación y asignación
'''
numero_uno = 10
numero_dos = 20

numero_uno -= numero_dos
print(numero_uno)
numero_uno *= numero_dos
print(numero_uno)
numero_uno /= numero_dos
print(numero_uno)
numero_uno //= numero_dos
print(numero_uno)
numero_uno %= numero_dos
print(numero_uno)
numero_uno **= numero_dos
print (numero_uno)


'''
5. Operadores de Identidad:
    is     - Es el mismo objeto
    is not - No es el mismo objeto
'''
a = 1
b = 2
c = 2

a is b # False
b is c # True
b is not c # False
a is not c # True


'''
6. Operadores de Pertenencia:
    in      = (...Está en)
    not in  = (...No está en)
'''
lista = [1, 2, 3, 4, 5, 12]
print(9 in lista) # False
print(9 not in lista) # True
print(12 in lista) # True
print(12 not in lista) # False


# For para la iteración en listas y tuplas

tupla = ("Colombia", "Perú", "México", "Argentina", "Chile")
for i in tupla:
    print(i)


''' DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''

for i in range (10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0: #Si el residuo de la division entre 2 es 0 y entre 3 es diferente 0 
        print(i)
