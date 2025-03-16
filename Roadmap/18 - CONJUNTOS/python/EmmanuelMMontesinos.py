"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * x Añade un elemento al final.
 * x Añade un elemento al principio.
 * x Añade varios elementos en bloque al final.
 * x Añade varios elementos en bloque en una posición concreta.
 * x Elimina un elemento en una posición concreta.
 * x Actualiza el valor de un elemento en una posición concreta.
 * x Comprueba si un elemento está en un conjunto.
 * x Elimina todo el contenido del conjunto.
 */
"""

'''Base'''
# Conjuntos
# Pensaba que se referia a sets {}, pero al ver los requerimientos he visto que se refiere a conjunto de datos simplemente

mi_conjunto = ["Hola",1,False]
print(mi_conjunto)

# Añadir Elementos
'''Inicio'''
mi_conjunto.insert(0, "Nuevo Elemento Principio")
print(mi_conjunto)
'''Final'''
mi_conjunto.append("Nuevo Elemento Final")
print(mi_conjunto)
'''Varios al Final'''
mi_conjunto.extend(["Varios1","Varios2"])
print(mi_conjunto)

'''Varios en Posición Concreta'''
mi_conjunto[1:1] = ["Varios3","Varios4"]
print(mi_conjunto)

# Eliminar Elementos
mi_conjunto.remove(mi_conjunto[4])
print(mi_conjunto)

# Actualizar Elemento
mi_conjunto[4] = True
print(mi_conjunto)

# Comprobación de Elemento
elemento_comprobar = "Varios3"
print(f"¿{elemento_comprobar} esta en el conjunto?: {elemento_comprobar in mi_conjunto}")

# Borrar todo el conjunto
mi_conjunto.clear()
print(mi_conjunto)

'''
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * x Unión.
 * x Intersección.
 * x Diferencia.
 * x Diferencia simétrica.
'''

conjunto_1 = [1,"2",False,"3",4]
conjunto_2 = [1,"2",False,3,"4"]

# Union
union = list(set(conjunto_1).union(conjunto_2))
print(union)

# Intersección
interset = list(set(conjunto_1).intersection(conjunto_2))
print(interset)

# Diferencia
deffe_1 = list(set(conjunto_1).difference(conjunto_2))
deffe_2 = list(set(conjunto_2).difference(conjunto_1))
print(deffe_1)
print(deffe_2)

# Diferencia simetrica
simetrica = list(set(conjunto_1).symmetric_difference(conjunto_2))
print(simetrica)
