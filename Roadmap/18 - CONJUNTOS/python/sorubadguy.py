# Conjuntos

animales = ["conejo", "perro", "gato"]
print(animales)
animales.append("serpiente")
print(animales)
animales.insert(0,"gallina")
print(animales)
animales.extend(["hamster", "panda", "iguana"])
print(animales)
animales[5:3] = ["cocodrilo", "avestrus", "mono"]
print(animales)
animales.pop(3)
print(animales)
animales[5] = "tigre"
print(animales)

animal = "cocodrilo"
if animal in animales:
    print(f"{animal} se encuentra en animales")
else:
    print(f"{animal} no se encuentra en animales")
    
animales.clear()
print(animales)

#!Extra

mult2 = {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30}
mult3 = {3,6,9,12,15,18,21,24,27,30}

print(f"union: {mult2.union(mult3)}")
print(f"union: {mult2 | mult3}")
print(f"interseccion: {mult2.intersection(mult3)}")
print(f"interseccion: {mult2 & mult3}")
print(f"diferencia: {mult2.difference(mult3)}")
print(f"diferencia: {mult2 - mult3}")
print(f"diferencia simetrica: {mult2.symmetric_difference(mult3)}")
print(f"diferencia simetrica: {mult2 ^ mult3}")