"""
Ejercicio
"""

conjunto=[1,2,3,4]
print(f"Comienzo del conjunto")

#Agregar elemento al final
conjunto.append(5)
print(f"Aregando al final {conjunto}")
#Agregando al principio
conjunto.insert(0,0)
print(f"Aregando al principio {conjunto}")
#Agrega unbloque de elementos al final
conjunto.extend([6,7,8,])
print(f"Aregando un bloque final {conjunto}")
#Agrega unbloque de elementos en la pcisión 3
conjunto[3:3]=[9,10,11]
print(f"Aregando un bloque en pocisión concreta {conjunto}")
#Elimina un ellemnto de una pocisión concreta
#conjunto.pop(3)
del conjunto[3]
print(f"Elimina un elemnto pocisión concreta {conjunto}")
#Actualiza valor de un elemneto en una pocosión concreta
conjunto[3]=9
print(f"Actualiza el valor de pocision concreta {conjunto}")
#Corrobora si un elemnto está en el conjunto
valor=3
print(f"Comprobar si {valor} está en {conjunto}  {valor in conjunto}")
#Elimina todos los elementos
conjunto.clear()
print(conjunto)

"""
Extra
"""

conj_1={1,2,3,4,5}
conj_2={1,2,3,4,6,7}

print(conj_1)
print(conj_2)

print(f"Union de conjuntos {conj_1.union(conj_2)}")
print(f"Intersección de conjuntos {conj_1.intersection(conj_2)}")
print(f"Diferencia de conjuntos {conj_1.difference(conj_2)}")
print(f"Diferencia simetrica de conjuntos {conj_1.symmetric_difference(conj_2)}")
