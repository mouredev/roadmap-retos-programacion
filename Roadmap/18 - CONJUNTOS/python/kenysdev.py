# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * CONJUNTOS
# -----------------------------------
# Son una colección desordenada de elementos únicos.
my_set: set = {1, 2, 3, 0}

"""
 * EJERCICIO #1:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
"""
# Algunas operaciones del ejercicio no pueden realizarse utilizando 'set'.
my_list: list = ["a", "b", "c"]

# Añade un elemento al final.
my_list.append("d")

# Añade un elemento al principio.
my_list.insert(0, "-")

# Añade varios elementos en bloque al final.
my_list.extend(["e", "f"])

# Añade varios elementos en bloque en una posición concreta.
my_list[4:4] = "-", ">"

# Elimina un elemento en una posición concreta.
del my_list[5]

# Actualiza el valor de un elemento en una posición concreta.
my_list[2] = "-b"

print(my_list)
print(my_set)

# Comprueba si un elemento está en un conjunto.
print(f"4 en conjunto: {4 in my_set}")
print(f"c en lista: {'c' in my_list}")

# Elimina todo el contenido del conjunto.
my_set.clear()
my_list.clear()

"""
* EJERCICIO #2:
* Muestra ejemplos de las siguientes operaciones con conjuntos:
* - Unión.
* - Intersección.
* - Diferencia.
* - Diferencia simétrica.
"""

set_1: set = {1, 2, 3, 4}
set_2: set = {3, 4, 5, 6}

print(f"""
* set_1: {set_1} - set_2: {set_2}

- Unión: {set_1 | set_2}
  Elementos que están en al menos uno de los conjuntos.

- Intersección: {set_1 & set_2}
  Elementos que están en ambos conjuntos.

- Diferencia: {set_1 - set_2}
  Elementos que están en set_1 pero no en set_2

- Diferencia simétrica: {set_1 ^ set_2}
  Elementos que están en uno de los conjuntos pero no en ambos.
""")

"""
Nota: También pueden usarse los métodos::
      - union()
      - intersection()
      - difference()
      - symmetric_difference()
"""

