'''
* EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
   operaciones (debes utilizar una estructura que las soporte):
   - Añade un elemento al final.
   - Añade un elemento al principio.
   - Añade varios elementos en bloque al final.
   - Añade varios elementos en bloque en una posición concreta.
   - Elimina un elemento en una posición concreta.
   - Actualiza el valor de un elemento en una posición concreta.
   - Comprueba si un elemento está en un conjunto.
   - Elimina todo el contenido del conjunto.
  
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
   - Unión.
   - Intersección.
   - Diferencia.
   - Diferencia simétrica.
'''

# 📦 Conjunto de datos inicial
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("📂 Conjunto inicial:", data)

# 1️⃣ Añadir un elemento al final de la lista
data.append(110)
print("1️⃣ ➕ Añadir al final:", data)

# 2️⃣ Añadir un elemento al principio de la lista
data.insert(0, 0)
print("2️⃣ 🔝 Añadir al inicio:", data)

# 3️⃣ Añadir múltiples elementos al final en bloque
data.extend([120, 130, 140, 150])
print("3️⃣ 📦 Añadir varios al final:", data)

# 4️⃣ Insertar múltiples elementos en una posición específica (desplaza los demás)
data[4:4] = [31, 32, 33, 34, 35]
print("4️⃣ 📌 Añadir varios en índice 4:", data)

# 5️⃣ Eliminar un elemento en una posición específica (índice 0)
del data[9]
print("5️⃣ ❌ Elimina un elemento en una posicion concreta:", data)

# 6️⃣ Actualizar el valor de un elemento en una posición específica (índice 8)
data[8] = 45
print("6️⃣ 🔄 Actualizar valor en índice 8:", data)

# 7️⃣ Verificar si un valor existe en la lista
exists = 20 in data
print("7️⃣ 🔍 ¿Existe el número 20 en la lista?", "✅ Sí" if exists else "❌ No")

# 8️⃣ Vaciar completamente la lista
data.clear()
print("8️⃣ 🧹 Lista vaciada:", data)

'''
Extra
'''

# Operaciones con conjuntos
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

# Union
print(f"Union: {set_1.union(set_2)}")

# Interseccion
print(f"Interseccion: {set_1.intersection(set_2)}")

# Diferencia
print(f"Diferencia: {set_1.difference(set_2)}")
print(f"Diferencia: {set_2.difference(set_1)}")

# Diferencia Simetrica
print(f"Diferencia Simetrica: {set_1.symmetric_difference(set_2)}")