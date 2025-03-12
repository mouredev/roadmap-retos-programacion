"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
 """

# Asignación de variables "por valor"
suma = 1 + 40
multiplicacion = 20 * 17

# Asignación de variables "por referencia".

def descuentoAplicado(precio):
    return precio - (precio * 10 / 100)

precio = 100

precio_total = descuentoAplicado(precio)

print(precio_total)

# Asignación de variables según tipo de dato.

cadena = "Esto es una cadena"
num = 20
flotante =  43.0
booleano = False

# Funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.

def porValor(num):
    num * 2

num = porValor(num)
print(num)

listado = ['Rojo', 'Verde', 'Amarillo', 'Blanco', 'Negro']

# Por referencia
def porReferencia(listado):
    listado.append('Naranja')

porReferencia(listado)
print(listado)

# /////////////////////////////////////  DIFICULTAD EXTRA (opcional)  /////////////////////////////////////

param1 = "Primer parametro"
param2 = "Segundo parametro"

param_ref1 = ['arroz', 'manzana', 'pollo']
param_ref2 = ['destornillador', 'taladro', 'martillo']

def programa1(valor1, valor2):
    valor_cambio = valor2
    valor2 = valor1
    valor1 = valor_cambio

    return valor1, valor2

def programa2(ref1, ref2):
    ref_cambio = ref2
    ref2 = ref1
    ref1 = ref_cambio

    return ref1, ref2


resultado1 = programa1(param1, param2)
resultado2 = programa2(param_ref1, param_ref2)

print(f"Sin cambio: \nParametro 1 = {param1} \nParametro 2 = {param2}")
print(f"Con cambio: \nParametro 1 = {resultado1[0]} \nParametro 2 = {resultado1[1]}\n")

print(f"Sin cambio: \nParametro 1 = {param_ref1} \nParametro 2 = {param_ref2}")
print(f"Con cambio: \nParametro 1 = {resultado2[0]} \nParametro 2 = {resultado2[1]}")