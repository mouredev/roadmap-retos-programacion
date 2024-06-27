""" 1. Lists """

# Creación de listas
numeros = [5, 10, 15, 20]
nombres = ["Ana", "Juan", "María"]

# Inserción de elementos
numeros.append(25) # Agrega el elemento "25" al final de la lista "numeros"
numeros.insert(1, 8) # Inserta el elemento "8" en la posicion 1 (segundo lugar) de la lista "numeros"
nombres.extend(["Pedro", "Luisa"]) # Agrega los elementos "Pedro" y "Luisa" al final de la lista "nombres"

# Borrado de elementos
del numeros[0] # Elimina el elemento en la posicion 0 (el primer elemento) de la lista "numeros"
numeros.remove(15) # Elimina la primera ocurrencia del valor "15" de la lista "numeros"
eliminado = numeros.pop() # Elimina y retorna el ultimo elemento de la lista "numeros"
numeros.clear() # Elimina todos los elementos de la lista "numeros"

# Actualización de elementos
numeros[1] = 12 # Cambia el elemento en la posición 1 (segundo lugar) de la lista 'numeros' por el valor '12'
nombres[0:2] = ["Carlos", "Sofia"] # Reemplaza los elementos en las posiciones 0 y 1 con "Carlos" y "Sofía"

# Ordenación de elementos
numeros.sort() # Ordena los elementos de la lista 'numeros' en orden ascendente (de menor a mayor)
nombres.sort(reverse=True) # Ordena los elementos de la lista 'nombres' en orden descendente (Z-A)

""" 2. Tuples """

# Creación de tuplas
coordenadas = (3, 5) # Tupla que almacena coordenadas (x, y)
colores = ("rojo", "verde", "azul") # Tupla que almacena colores

# Acceso a elementos
print(coordenadas[0]) # Accede al primer elemento de la tupla 'coordenadas' (3)
print(colores[1]) # Accede al segundo elemento de la tupla 'colores' ("verde")

# Desempaquetado de tuplas
x, y = coordenadas # Asigna los valores de la tupla "coordenadas" a las variables x e y
print(x, y) # Imprime los valores de x e y (3, 5)

# Inmutabilidad (no se pueden modificar)
# coordenadas[0] = 10 # Esto generaría un error porque las tuplas son inmutables

""" 3. Conjutos (Sets)  """

# Creación de conjuntos
numeros_unicos = {1, 3, 5, 3, 1} # Crea un conjunto con valores únicos (elimina duplicados): {1, 3, 5}
frutas = set(["manzana", "pera", "uva"]) # Crea un conjunto a partir de una lista

# Inserción de elementos
frutas.add("platano") # Agrega el elemeno "platano" al conjunti "frutas"

# Borrado de elementos
frutas.remove("pera") # Elimina el elemento "pera" del conjunto de "frutas"
frutas.discard("kiwi") # Intenta eliminar "kiwi", pero no genera erro si no existe

# Operaciones de conjuntos
otros_numeros = {4, 5, 6}
union = numeros_unicos | otros_numeros # Unión de conjuntos: {1, 3, 4, 5, 6}
interseccion = numeros_unicos & otros_numeros # Intersección de conjuntos: {5}
diferencia = numeros_unicos - otros_numeros # Diferencia de conjuntos: {1, 3}

""" 4. Diccionarios (Dictionaries): """

# Creación de diccionarios
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"} # Diccionario con claves "nombres", "edad" y "ciudad"

# Inserción/Actualización de elementos
persona["profesión"] = "Ingeniera" # Agrega una nueva clave "profesión" con el valor "Ingeniera"
persona["edad"] = 31               # Actualiza el valor de la clave "edad" a 31

# Borrado de elementos
del persona["ciudad"] # Elimina la clave "ciudad" y su valor
edad_eliminada = persona.pop("edad") # Elimina la clave "edad" y retorna su valor (31)

# Acceso y recorrido de elementos
print(persona["nombre"]) # Accede al valor de la clave "nombre" ("Ana")
for clave, valor in persona.items(): # Itera sobre los pares clave-valor del diccionario
    print(f"{clave}: {valor}")
