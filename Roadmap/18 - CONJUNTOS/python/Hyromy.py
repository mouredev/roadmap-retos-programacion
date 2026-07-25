conjunto = [1, 2, 3, 4, 5] # ya se que es una lista y no un conjunto
print(conjunto)

conjunto.append("A")
print(conjunto)

conjunto.insert(0, "b")
print(conjunto)

conjunto.extend([-1, -2, -3])
print(conjunto)

block = ["x", "y", "z"]
for i, item in enumerate(block):
    conjunto.insert(i + 3, item)
print(conjunto)

conjunto.pop(5)
print(conjunto)

conjunto[7] = "C"
print(conjunto)

print(-1 in conjunto)
print(5 in conjunto)

conjunto.clear()

# ---- DIFUCULTAD EXTRA ----
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print(conjunto_a.union(conjunto_b)) # unir ambos conjuntos
print(conjunto_a.intersection(conjunto_b)) # elementos comunes
print(conjunto_a.difference(conjunto_b)) # elementos en A que no estan en B
print(conjunto_b.difference(conjunto_a)) # elementos en B que no estan en A
print(conjunto_a.symmetric_difference(conjunto_b)) # insertesecion inversa