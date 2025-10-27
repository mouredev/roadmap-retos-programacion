'''
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''

# Asignación de variable por valor
print('Se asigna por valor cuando se llama a una variable que contiene un valor')
a = 2
b = 4
print(a)
print(b)
print('\n\n')

# Asignación de variable por referencia
print('Se asigna por referencia cuando se llama a una variable por una posición de memoria dentro de una lista')
x = [2, 4]
x[0] = 3
x[1] = 5
print(x[0])
print(x[1])
print('\n\n')

# Funciones con parámetros por valor y por referencia

def sumar(a, b):
    return a + b

def sumar2(a, b):
    a[0] = a[0] + b[0]
    a[1] = a[1] + b[1]
    return a

print('\n\n\n')
while True:
    print("1. Sumar por valor")
    print("2. Sumar por referencia")
    print("3. Salir")
    op = int(input("Elige una opció: "))
    if op == 1:
        a = int(input("Dame el primer valor: "))
        b = int(input("Dame el segundo valor: "))
        print(sumar(a, b))
    elif op == 2:
        a = [int(input("Dame el primer valor de la primera lista: ")), int(input("Dame el segundo valor de la primera lista: "))]
        b = [int(input("Dame el primer valor de la segunda lista: ")), int(input("Dame el segundo valor de la segunda lista: "))]
        print(sumar2(a, b))
    elif op == 3:
        print("Saliendo...")
        break