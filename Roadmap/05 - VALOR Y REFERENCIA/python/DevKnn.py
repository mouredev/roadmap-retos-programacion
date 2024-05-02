"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 """
palabra = "hola"
palabra = palabra.split()
n1 = 9
def index(n1):
    
 return print(n1+4)
def index2(palabra):
    
    palabra.append("esperando un elemento")
    return print(palabra)
"""
print(n1)
index2(palabra)
print(palabra)
"""
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */"""
palabra1 = "caiman"
palabra2 = "gorilla"

def valor(valor1,valor2):
    valor1,valor2 = valor2,valor1
    return valor1,valor2
nuevaPalabra1,nuevaPalabra2 = valor(palabra1, palabra2)

print("Por valor:")
print("Original:", palabra1, palabra2)
print("Nuevas:", nuevaPalabra1, nuevaPalabra2)

lista1 = ["cocodrilo"]
lista2 =["pescado"]
def referencia(referencia1,referencia2):
    referencia1[0],referencia2[0] = referencia2[0],referencia1[0]
    return referencia1,referencia2

nuevaLista1,nuevaLista2 = referencia(lista1,lista2)
print("\nPor referencia:")
print("Original:", lista1, lista2)
print("Nuevas:", nuevaLista1, nuevaLista2)