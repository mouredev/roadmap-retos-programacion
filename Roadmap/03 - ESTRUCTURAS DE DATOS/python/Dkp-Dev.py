"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 """

# Listas

lista: list = ["Perro","Gato","Conejo","Tortuga"]     # Es una lista definida por []
print(type(lista))
print(lista)

lista.append("Cuervo")  # Insercion
print(lista)

lista.remove("Gato")    # Eliminacion
print(lista)

print(lista[2])         # Acceso

lista[2] = "Serpiente"  # Modificacion en posicion
print(lista)

lista.sort()            # Orden alfabetico por defecto
print(lista)

# Tuplas son listas inmutables

tupla = ("Numeros","Letras","Simbolos")         # Es una tupla definida por () a diferencia de la lista []
print(type(tupla))
print(tupla)

print(tupla[2])         # Acceso unicamente
print(tupla[0])

tupla = tuple(sorted(tupla))    # Ordenar una tupla consiste en crear una lista a partir de la tupla, ordenarla y transformarla a tupla nuevamente
print(type(tupla))
print(tupla)

# Sets son basicamente listas desordenadas con el proposito de ser "eficientes" y no permite datos duplicados

sett: set = {"Cuadrado","Circulo","Rectangulo","Triangulo"}
print(type(sett))
print(sett)

sett.add("Ovalo")            # Insercion
sett.add("Cuadrado")         # Aunque se inserte nuevamente un dato, el sistema no lo tomara en cuenta
print(sett)

sett.remove("Rectangulo")    # Eliminacion
print(sett)                  # La unica forma de "modificar" es mediante la insercion y eliminacion de dato

sett = set(sorted(sett))     # No se puede ordenar, se puede convertir a lista y entonces ordenar
print(type(sett))
print(sett)

# Diccionario se crea con {} pero aqui se asignan claves:valores

mi_dict: dict = {
    "Canino": "Perro",      
    "Canino": "Lobo",           # Lobo termina borrando a Perro
    "Felino": "Gato",
    "Roedor": "Conejo"
}
print(type(mi_dict))
print(mi_dict)

mi_dict["Ave"] = "Cotorro"      # Insercion
print(mi_dict)

print(mi_dict["Felino"])        # Acceso mediante claves

mi_dict["Roedor"] = "Liebre"    # Modificacion mediante insercion
print(mi_dict)

del mi_dict["Felino"]           # Eliminacion
print(mi_dict)

mi_dict = dict(sorted(mi_dict.items()))     # Ordenar mediante items, cambia a lista y termina en dict, pero ordena las claves
print(type(mi_dict))
print(mi_dict)

