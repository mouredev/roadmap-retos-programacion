# ------------------- Asignacion por valor ---------------
# Al ser por valor son datos inmutables, Una vez guardado objeto en memoria no puede ser cambiado, al crear otra variable asignadno el valor de esta, se crea es una copia
# Int
a = 10
b = a  # b es una copia del valor de a
print(f"Original: a = {a}, b = {b}")
a = 20
print(f"Despues del cambio: a = {a}, b = {b}")

# Float
a = 10.5
b = a
print(f"Original: a = {a}, b = {b}")
a = 20.5
print(f"Despues del cambio: a = {a}, b = {b}")

# bool
a = True
b = a
print(f"Original: a = {a}, b = {b}")
a = False
print(f"Despues del cambio: a = {a}, b = {b}")

# Cadena de texto
texto = "Hola"
texto2 = texto
print(f"Original: texto = {texto}, texto2 = {texto2}")
texto = "Chao"
print(f"Despues del cambio: texto = {texto}, texto2 = {texto2}")

# Tupla
t = (1, 2, 3)
t2 = t  # Copia de t
print(f"Original: t = {t}, t2 = {t2}")

# Al intentar modificar una tupla da error
# t[0] = 5  # Error

# ---------------- Asignacion por referencia --------------------
# Al ser por referencia son datos mutables, estos se pueden mutar despues de la creacion, por eso siempre apuntan al mismo objeto en memoria
# Listas
lista = [1, 2, 3]
lista2 = lista
print(f"Original: lista = {lista}, lista2 = {lista2}")
lista[0] = 55  # Se modifica el elemento
print(f"Despues del cambio: lista = {lista}, lista2 = {lista2}")

# Diccionario
dic = {"Nombre": "Ana", "edad": 40}
dic2 = dic
print(f"Original: dic = {dic}, dic2 = {dic2}")
dic["edad"] = 80
print(f"Despues del cambio: dic = {dic}, dic2 = {dic2}")

# Conjunto
conjunto = {1, 2, 3}
conjunto2 = conjunto
print(f"Original: conjunto = {conjunto}, conjunto2 = {conjunto2}")
conjunto.add(4)
print(f"Despues del cambio: conjunto = {conjunto}, conjunto2 = {conjunto2}")


# ------------------ Funciones ----------------------------------------
# ejemplos de funciones con variables que se les pasan "por valor" y "por referencia"
# Valor pasado por parametro es el original dentro de la funcion se crea una copia que es el que se modifica


# ------------------- Asignacion por valor ---------------
# ---------------- inmutables -------------------
# Int
def modificar_numero(numero):
    print(f"Valor original = {numero}")
    numero = 10
    print(f"Despues de modificar numero: = {numero}")


mi_numero = 20
modificar_numero(mi_numero)
print(f"Numero fuera de la funcion = {mi_numero}")


# Float
def modificar_float(numero):
    print(f"Valor original: {numero}")
    numero = 40.5
    print(f"Despues de modificar: {numero}")


mi_float = 20.5
modificar_float(mi_float)
print(f"Float fuera de la fucnion = {mi_float}")


# bool
def modificar_bool(bool):
    print(f"Valor original: {bool}")
    bool = False
    print(f"Despues de modificar: {bool}")


mi_bool = True
modificar_bool(mi_bool)
print(f"Bool fuera de la funcion = {mi_bool}")


# Cadena de texto
def modificar_cadena_texto(texto):
    print(f"Valor original: {texto}")
    texto = "Nuevo valor"
    print(f"Despues de modificar: {texto}")


mi_cadena = "Hola"
modificar_cadena_texto(mi_cadena)
print(f"Cadena fuera de la funcion = {mi_cadena}")


# Tupla
def modificar_tupla(tupla):
    print(f"Valor original: {tupla}")
    tupla = (4, 5, 6)
    print(f"Despues de modificar: {tupla}")


mi_tupla = (1, 1, 2, 6)
modificar_tupla(mi_tupla)
print(f"Tupla fuera de la funcion = {mi_tupla}")

# ---------------- Asignacion por referencia --------------------
# -------------- Mutables ----------------------


# Listas
def modificar_lista(lista):
    print(f"Valor original = {lista}")
    lista[0] = 99
    print(f"Despues de modificar = {lista}")


mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(f"Lista fuera de la funcion = {mi_lista}")


# Diccionario
def modificar_diccionario(dic):
    print(f"valor original = {dic}")
    dic["nombre"] = "ivan"
    print(f"Despues de modificar en la funcion: {dic}")


mi_dic = {"nombre": "Alejandro"}
modificar_diccionario(mi_dic)
print(f"Diccionario fuera de la funcion = {mi_dic}")


# Conjunto
def modificar_conjunto(conjunto):
    print(f"Valor original = {conjunto}")
    conjunto.remove(4)
    print(f"Despues de modificar en la funcion = {conjunto}")


mi_conjunto = {5, 4, 6}
modificar_conjunto(mi_conjunto)
print(f"Conjunto fuera de la funcion = {mi_conjunto}")


#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.


# ------------ Por valor ----------------
def intercambio_parametros1(parametro1, parametro2):
    print(f"Valor original = {parametro1}, {parametro2}")
    aux = parametro2
    parametro2 = parametro1
    parametro1 = aux
    print(
        f"Al intercambiar los parametros tenemos: parametro1 = {parametro1}, parametro2 = {parametro2}"
    )
    return parametro1, parametro2


parametro1 = "Hola"
parametro2 = "Soy ivan"
str1, str2 = intercambio_parametros1(parametro1, parametro2)
print(f"Parametros modificados por la funcion: str1 = {str1}, str2 = {str2}")
print(
    f"Fuera de la funcion mantienen du valor original: parametro1 = {parametro1}, parametro2 = {parametro2}"
)


# ------- Por referencia --------------
def intercambio_parametro2(parametro1, parametro2):
    print(f"Valor original = {parametro1}, {parametro2}")
    aux = parametro2
    parametro2 = parametro1
    parametro1 = aux
    return parametro1, parametro2


dic1 = {"nombre": "ivan"}
dic2 = {"pais": "Colombia"}
rta1, rta2 = intercambio_parametro2(dic1, dic2)
print(f"Parametros modificados por la funcion: rta1 = {rta1}, rta2 = {rta2}")
print(f"Fuera de la funcion mantienen su valor original: dic1 = {dic1}, dic2 = {dic2}")
