"""
#05
VALOR Y REFERENCIA
/*
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
"""

# Variables por valor
x = 30  # Almacena directamente el valor
y = x

# Variables por asignación
lista_x = [1, 2, 3, 4, 5]  # Se guardan en memoria
lista_y = lista_x  # Se copia el contenido en otro lugar de memoria
lista_y.append(5)

# Verificación
if x == y:
    print("x es igual que y")
else:
    print("x no es igual a y")

if lista_x == lista_y:
    print("lista_x es igual a lista_y")
else:
    print("lista_x es diferente a lista_y porque no comparten el mismo contenido")

# Funciones
def modificacion_valor(valor):
    # Se crea una nueva variable local para evitar modificar la original fuera de la función
    nuevo_valor = valor + 10
    return nuevo_valor

def modificacion_asignacion(lista):
    # Se crea una nueva lista para evitar modificar la original fuera de la función
    nueva_lista = lista
    nueva_lista.append(6)
    return nueva_lista

x_modificada = modificacion_valor(x)
y_modificada = modificacion_asignacion(lista_y)


print(f"""
      #modificaciones_valor : {x_modificada}
      #original_valor : {x}

      #modificacion_asignacion : {y_modificada}
      #original_asignacion : {lista_y}

      """)

### EXTRA ###

#originales valor
x = 1
y = 2

#original asignacion
xy = [1,2]
xz = [2,1]


def intercambia_valor(x:int ,y:int):
    temporal = x
    x = y
    y = temporal

    return x , y

def intercambia_asignacion(x:list,y:list):
    temporal = x
    x = y
    y = temporal

    return x , y


x_modificada , y_modificada = intercambia_valor(x , y)
xy_modificada , xz_modificada = intercambia_valor(xy , xz)

print(f"""
      ### valor ###
      originales : {x} , {y}
      intercambiadas : {x_modificada , y_modificada}

      ### asignacion ###
      originales : {xy} , {xz}
      intercambiadas : {xy_modificada , xz_modificada}
      """)
