'''
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Inserta un elemento al final.
 * - Inserta un elemento al principio.
 * - Inserta varios elementos en bloque al final.
 * - Inserta varios elementos en bloque en una posicion concreta.
 * - Elimina un elemento en una posicion concreta.
 * - Actualiza el valor de un elemento en una posicion concreta.
 * - Comprueba si un elemento esta en un conjunto.
 * - Elimina todo el contenido del conjunto.
'''

print("\n\n=======================================EJERCICIO=======================================\n\n")


group = ['Miguel', 'Ana', 'Juan', 'Rantamplan', 'Helena', 'Brais']

print(f"Los elementos que conforman ahora mismo el conjunto son: {group}")

print("\n=====================\n")

group.append('Raul')
print(f"Inserto un elemento al final del conjunto: {group}")

print("\n=====================\n")

group.insert(0, 'Luis')
print(f"Inserto un elemento al principio del conjunto: {group}")

print("\n=====================\n")

group.extend(['Jaime', 'Isabel', 'Rosa'])
print(f"Inserto varios elementos en bloque al final del conjunto: {group}")

print("\n=====================\n")

group[2:2] = ['Fernando', 'Cristina', 'Jon']    
print(f"Inserto en bloque 3 elementos en la posicion 2 del conjunto: {group}")

print("\n=====================\n")

del group[4]
print(f"Elimino el elemento elegido (4 - Jon) del conjunto: {group}")

print("\n=====================\n")

group[6] = 'Rantamhack'
print(f"Actualizo el elemento elegido (6 - Rantamplan) del conjunto: {group}")

print("\n=====================\n")

print(f"Comprobar si esta es elemento 'Jon' en el conjunto 'group': {'Jon' in group}")

print(f"\nComprobar si esta es elemento 'Juan' en el conjunto 'group': {'Juan' in group}")

print("\n=====================\n")

group.clear()
print(f"El contenido del conjunto 'group' {group} ha sido borrado")


'''
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Union.
 * - Interseccion.
 * - Diferencia.
 * - Diferencia simetrica.
'''

print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

alumnos_ciencias = {'Luis', 'Miguel', 'Fernando', 'Cristina', 'Ana', 'Juan'}

alumnos_letras = {'Helena', 'Brais','Ana', 'Juan', 'Raul', 'Jaime', 'Luis', 'Isabel', 'Miguel', 'Rosa'}

total_alumnos = alumnos_ciencias.union(alumnos_letras)

print(f"El total de alumnos matriculados es: {sorted(total_alumnos)}")

print("\n=====================\n")

alumnos_mixtos = alumnos_ciencias.intersection(alumnos_letras)

print(f"El total de alumnos matriculados en las dos ramas: {sorted(alumnos_mixtos)}")

print("\n=====================\n")

alumnos_solo_ciencias = alumnos_ciencias.difference(alumnos_letras)

print(f"Alumnos matriculados solo en ciencias: {sorted(alumnos_solo_ciencias)}")

alumnos_solo_letras = alumnos_letras.difference(alumnos_ciencias)

print(f"\nAlumnos matriculados solo en letras: {sorted(alumnos_solo_letras)}")

print("\n=====================\n")

alumnos_una_matricula = alumnos_ciencias.symmetric_difference(alumnos_letras)

print(f"Alumnos matriculados solo en una rama sin importar cual: {sorted(alumnos_una_matricula)}")


