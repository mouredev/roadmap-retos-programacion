# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23


# EJERCICIO:
# Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
# operaciones (debes utilizar una estructura que las soporte):
# - Añade un elemento al final.
# - Añade un elemento al principio.
# - Añade varios elementos en bloque al final.
# - Añade varios elementos en bloque en una posición concreta.
# - Elimina un elemento en una posición concreta.
# - Actualiza el valor de un elemento en una posición concreta.
# - Comprueba si un elemento está en un conjunto.
# - Elimina todo el contenido del conjunto.

# DIFICULTAD EXTRA (opcional):
# Muestra ejemplos de las siguientes operaciones con conjuntos:
# - Unión.
# - Intersección.
# - Diferencia.
# - Diferencia simétrica.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"*Lista antes de ser modificada: \n{ lista }")

# Añadiend un elemento al final de la lista 
lista.append("Ultimo elemento")
print(f"\n*Lista al agregarle un elemento al final: \n{ lista }")

# Añadiend un elemento al inicio de la lista 
lista.insert(0, "Primer elemento")
print(f"\n*Lista al agregarle un elemento al inicio: \n{ lista }")

# Añadiend varios elementos al final de la lista
lista.append([word for word in "Hola Mundo"])
print(f"\n*Lista al agregarle varios elemento al inicio: \n{ lista }")

# Añadiend varios elementos al inicio de la lista
lista.insert(0, [word for word in "Refugio"])
print(f"\n*Lista al agregarle varios elemento al inicio: \n{ lista }")

# Eliminar un elemento de una posicion concreta
lista.remove(lista.index(4))
print(f"\n*Lista despues de eliminar el elemento en la posicion4: \n{ lista }")

# Actualizar un elemento en una posicion concreta
lista[2] = "Elemento actualizado"
print(f"\n*Lista despues de actualizar el elemento No.2: \n{ lista }")

# Comprobar si un elemento esta e un conjunto
response = 4 in lista
print(f"\n*¿Está el número 4 en la lista?: \n{ response }")

# Eliminar todos llos valores contenidos en la lista
lista.clear()
print(f"\n*Lista despues de haber eliminado todos sus valores: \n{ lista }")

A = { 1, 2 , 4, 5, 6, 7, 8, 9 }
B = { 10, 35 , 575, 5, 6, 57, 8, 90 }

print(f"****** Conjuntos A { A } y B { B } ******\n")

# - Unión.
print(f"Union A | B: { A | B }")
# - Intersección. 
print(f"Union A & B: { A & B }")
# - Diferencia.
print(f"Union A - B: { A - B }")
# - Diferencia simétrica.
print(f"Union A ^ B: { A ^ B }")