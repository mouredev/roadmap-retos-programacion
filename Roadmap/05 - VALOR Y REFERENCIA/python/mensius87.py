"""
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
  su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
  "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""

# ------------------------------------------------------------------------------------------------------

"""
Paso por Valor (números, cadenas y tuplas):
En este enfoque, al llamar a una función, se pasa una copia del valor de la variable como argumento.
Cualquier modificación realizada dentro de la función no afectará a la variable original fuera de ella.

Paso por Referencia (listas, diccionarios y sets):
En este enfoque, al llamar a una función, se pasa la referencia a la variable original como argumento.
Esto significa que cualquier modificación realizada dentro de la función afectará directamente a la variable original
fuera de la función. Es común en tipos de datos mutables como listas, diccionarios y conjuntos.
"""

# Asignación de variables por valor
numero_1 = 23
numero_2 = 3.14
color = "rojo"
agenda = (1, "hola", numero_2)


# Asignación de variables por referencia
colores = ["rojo", "verde", "azul"]
ingles_espanol = {
    "hello": "hola",
    "red": "rojo",
    "green": "verde",
    "blue": "azul"
    }

mi_set = {1, 2, 3, 4, 5}

print()


# Ejemplos de funciones con variables de paso por valor
def suma(num_1, num_2):
    numero_1 = num_1 + num_2
    print(f"El valor de 'numero_1' es {num_1}+{num_2} es {num_1 + num_2}")


def datos_agenda(datos):
    print(agenda)


# Ejemplos de funciones con variables de paso por referencia
def imprimir_vocabulario(vocabulario):
    for clave, valor in ingles_espanol.items():
        print(f"{clave}: {valor}")





suma(numero_1, numero_2)
print()
datos_agenda(agenda)
print()
imprimir_vocabulario(ingles_espanol)


print()
print("::::::::::::::::::::::::::::::::::::: EXTRA :::::::::::::::::::::::::::::::::::::")
print()


