# Creación
numeros = [5, 10, 15, 20]  
nombres = ["Ana", "Juan", "María"]

# Inserción
numeros.append(25)       # Agrega al final
numeros.insert(1, 8)     # Inserta 8 en la posición 1
nombres.extend(["Carlos", "Laura"])  # Agrega varios elementos al final

# Borrado
del numeros[0]          # Elimina el elemento en la posición 0
numeros.remove(15)       # Elimina la primera aparición de 15
eliminado = numeros.pop()  # Elimina y retorna el último elemento

# Actualización
numeros[2] = 12         # Cambia el valor en la posición 2
nombres[1:3] = ["Pedro", "Sofía"]  # Reemplaza elementos desde la posición 1 hasta la 2 (sin incluir la 3)

# Ordenación
numeros.sort()          # Ordena la lista en orden ascendente
nombres.sort(reverse=True)  # Ordena la lista en orden descendente

# Creación
coordenadas = (3, 5)
colores = ("rojo", "verde", "azul")

# Acceso a elementos (igual que listas)
print(coordenadas[0])  # 3

# No se pueden modificar (son inmutables)
# coordenadas[1] = 8  # Esto generaría un error

# Creación
numeros_unicos = {1, 3, 5, 3, 1}  # Solo se almacenan valores únicos: {1, 3, 5}
frutas = set(["manzana", "pera", "uva"])

# Inserción
frutas.add("plátano")

# Borrado
frutas.remove("pera")  # Error si el elemento no existe
frutas.discard("kiwi")  # No hay error si el elemento no existe

# Operaciones de conjuntos
otros_numeros = {4, 5, 6}
union = numeros_unicos | otros_numeros  # {1, 3, 4, 5, 6}
interseccion = numeros_unicos & otros_numeros  # {5}
diferencia = numeros_unicos - otros_numeros  # {1, 3}

# Creación
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
puntajes = dict(matemáticas=95, física=88, química=92)

# Inserción/Actualización
persona["profesión"] = "Ingeniera"
puntajes["física"] = 90

# Borrado
del persona["ciudad"]
eliminado = puntajes.pop("química")  # Elimina y retorna el valor

# Acceso y recorrido
print(persona["nombre"])  # "Ana"
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
