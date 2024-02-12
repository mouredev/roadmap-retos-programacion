# - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
# Primero hay que aclarar que significan las asignaciones de variables pasadas "por valor" y "referencia".
## * Si usamos un parametro pasado por valor, se creara una copia local de la variable, lo que implica que cualquier modificacion sobre la
##      la misma no tendra efecto sobre la original.
## * Con una variable pasada como referencia, se actuara directamente sobre la variable pasada, por lo que las modificaciones afectaran
##      a la variable original.

### Tradicionalmente:
### * Los tipos de datos inmutables se pasan por valor: Numericos, Textos, Booleanos, Tuplas
### * Los tipos de datos mutables se pasan por referencia: Listas, Diccionarios, Conjuntos

# Variables por valor:
# Ya que los numericos son inmutables entonces no se cambiaran sus valores al asignarlo a otra variable, se creara una copia de ellas.
a = 400
b = a
b += 5
print(a)
print(b)
# Variables por referencia:
# Ya que las lista son tipos de datos asignados por referencia podran ser modificados luego de haber sido asignados a otra variable (tipo de dato mutable)
lista_a = [30, 400, 100]
lista_b = lista_a # Se comparte la referencia
lista_b.append(60)
print(lista_a, lista_b)
## > Para verificar que la lista_a y lista_b comparten la misma referencia del objeto podemos usar la funcion id()
print(f"Las listas a y b comparten la misma referencia al objeto, id(lista_a): {id(lista_a)} ,id(lista_b): {id(lista_b)} (tienen el mismo id)")

# - Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en 
#   el momento de ser modificadas.

## Tipos de datos pasados por valor
# Entero: (int)
# Como puedes ver esta funcion dobla la variable pasada pero como es un tipo de dato entero y es un tipo de dato que se pasa por valor.
# Entonces la variable no es modificada.
variable_numerica = 30
def doblar_valor(variable):
    variable *= 2

doblar_valor(variable_numerica)
print(variable_numerica)
# Textos (str):
# Como ves como str es un tipo de dato por valor entonces no sera modificada por la funcion
variable_cadena = "abc"
doblar_valor(variable_cadena)
print(variable_cadena)
# Booleanos
# En el caso de los booleanos al multiplicarlos por numeros, True seria 1 y False seria 0.
# Como los booleanos son tipos de datos pasados por valor no seran modificados por la funcion
variable_booleana = True
doblar_valor(variable_booleana)
print(variable_booleana)
# Tuplas
# Como puedes ver la tupla es un tipo de dato inmutable, entonces debido a las reglas y caracteristicas que contiene este tipo de dato, no se va
# a poder modificar luego de haber sido declarada. Entonces al intentar duplicar los elementos de la tupla no se van a poder reasignar.
variable_tupla = ("Hola", True, 59, "Mundo")
doblar_valor(variable_tupla)
print(variable_tupla)

## Tipos de datos pasados por referencia
# Listas
# Como puedes ver la lista si sera modificada por la funcion, ya que es un tipo de dato pasado por referencia.
variable_lista = [2, 300, 400, 50, 19]
doblar_valor(variable_lista)
print(variable_lista)
# Diccionarios
# Como puedes ver la funcion anadira una clave al diccionario, ya que el diccionario es un tipo de dato por referencia se modificara.
variable_diccionario = {
    "nombre": "Alvaro",
    "apellido": "Neyra",
    "edad": 19
}
def anadir_clave(dict: dict):
    dict.update({"mascota": True})
anadir_clave(variable_diccionario)
print(variable_diccionario)
# Conjuntos (sets)
variable_conjunto = {True, "Moure", "❤️"}
# Una de las caracteristicas de los conjuntos es que no puede tener elementos duplicados, entonces anadiremos un elemento nuevo con otra funcion
# Ya que el conjunto es un tipo de dato pasado por referencia entonces si se podra modificar.
def anadir_elemento(conjunto: set):
    conjunto.add("Gracias por todo!")
anadir_elemento(variable_conjunto)
print(variable_conjunto)

"""DIFICULTAD EXTRA:"""
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
variable_valor1 = 400
variable_valor2 = "'Hola, Mundo!'"
variable_referencia1 = [30, 600, 81, 20]
variable_referencia2 = {True, "'Soy Un conjunto'", 20}

def modificar_variables_valor(valor1, valor2):
    valor1, valor2 = valor2, valor1
    print(f"Valor1: {valor1}")
    print(f"Valor2: {valor2}")
    return valor1, valor2
def modificar_variables_referencia(referencia1, referencia2):
    referencia1, referencia2 = referencia2, referencia1
    return referencia1, referencia2

resultado_por_valor1, resultado_por_valor2 = modificar_variables_valor(variable_valor1, variable_valor2)
resultado_por_referencia1, resultado_por_referencia2 = modificar_variables_referencia(variable_referencia1, variable_referencia2)

# Imprimir resultados:
print(f"Variables originales:")
print(f"- Variables por valor:")
print(f"Originales: {variable_valor1}, {variable_valor2}, Luego de pasarlas a la funcion: {resultado_por_valor1}, {resultado_por_valor2}")
print(f"- Variables por referencia:")
print(f"Originales: {variable_referencia1}, {variable_referencia2}, Luego de pasarlas a la funcion: {resultado_por_referencia1}, {resultado_por_referencia2}")