
lista = ["Sergio", "Damian", "Laura"]
print(lista)

lista.append("María")
print(lista)

lista.insert(0, "Ana")
print(lista)

lista.extend(["Viky", "Mica"])
print(lista)

lista[2:2] = ("Sofia", "Sol")
print(lista)

del lista[0]
print(lista)

lista[2] = "Damián"
print(lista)

if "Sofia" in lista:
    print("Sofia esta en el conjunto")

lista.clear()
print(lista)


#DIFICULTAD EXTRA:

set1 = {"Sergio", "Laura", "Vicky", "Mica"}
set2 = {"Vicky", "Sofia", "Mica", "Sol"}

print(f"Unión: {set1.union(set2)}")

print(f"Intersección: {set1.intersection(set2)}")

print(f"Diferencia: {set1.difference(set2)}")

print(f"Diferencia Simetrica: {set1.symmetric_difference(set2)}")