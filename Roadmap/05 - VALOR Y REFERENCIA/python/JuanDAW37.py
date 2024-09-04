"""
* EJERCICIO:
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
"""
# Variable con asignación por valor:
var1 = 15
var2 = var1
print(var1)
print(var2)
var1 = 50
print(var1)
print(var2)

# Variable con asignación por referencia, todos los tipos de datos que no son primitivos
lista1 = [10, 30,50, 60]
lista2 = lista1
print(lista1)
print(lista2)
lista1.append(100)
print(lista1)
print(lista2)

# Función con asignación por valor:
var3 = 20

def varVal(var4:int):
    print(f'Valor de var4 antes de modificarla: {var4}')
    var4 = 30
    print(f'Valor de var4 después de modificarla: {var4}')
    print(f'Valor de var3: {var3}')
    
varVal(var3)
print(f'Valor de var3 fuera de la función: {var3}')

# Función con asignación por referencia:
lista3 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
print(f'ANTES de modificar lista3: {lista3}')

def funcVal(lista:list):
    lista.append('Domingo')
    print(f'DESPUÉS de modificar lista3: {lista3}')
    
funcVal(lista3)
print(f'DESPUÉS de llamar a funcVal: {lista3}')

# DIFICULTAD EXTRA

def valor(valor1:int, valor2:int)->tuple:
    temporal = valor1
    valor1 = valor2
    valor2 = temporal
    return valor1, valor2

v1 = 10
v2 = 20
v1_nuevo, v2_nuevo = valor(v1, v2)
print(f'Valor de v1 {v1}, valor de v2 {v2}')
print(f'Valor de v1_nuevo {v1_nuevo}, valor de v2_nuevo {v2_nuevo}')

def referencia(lista1:list, lista2:list)->tuple:
    temporal = lista1
    lista1 = lista2
    temporal.append(1000)
    lista2 = temporal
    return lista1, lista2

lista4 = [10,20,30]
lista5=[30,20,10]
lista4_nueva, lista5_nueva = referencia(lista4, lista5)
print(f'Valores de lista4 {lista4}, Valores de lista5 {lista5}')
print(f'Valores de lista4_nueva {lista4_nueva}, Valores de lista5_nueva {lista5_nueva}')