"#18 - Python"
# 
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
# 
# DIFICULTAD EXTRA (opcional):
# Muestra ejemplos de las siguientes operaciones con conjuntos:
# - Unión.
# - Intersección.
# - Diferencia.
# - Diferencia simétrica.
# 
def serparacion(cadena) -> str:
    print('{}'.format(cadena * 20))

def listasset(lista: list) -> set:
    my_set = lista
    print(my_set)
    serparacion('-:-')
    # Añade un elemento al final.
    my_set.append('Aguila')
    print(my_set)
    serparacion('-:-')
    # Añade un elemento al principio.
    my_set.insert(0, 'Elefante')
    print(my_set)
    serparacion('-:-')
    # Añade varios elementos en bloque al final.
    my_set.extend(['Tigre', 'Yak'])
    print(my_set)
    serparacion('-:-')
    # Añade varios elementos en bloque en una posición concreta.
    for animal in ['Pato', 'Orca', 'Delfín']:
        my_set.insert(3, animal)
    print(my_set)
    serparacion('-:-')
    # Elimina un elemento en una posición concreta.
    my_set.pop(4)
    print(my_set)
    serparacion('-:-')
    # Actualiza el valor de un elemento en una posición concreta.
    my_set.pop(1)
    my_set.insert(1, 'Iguana')
    print(my_set)
    serparacion('-:-')
    # Comprueba si un elemento está en un conjunto.
    tocheck = 'Iguana'
    print(f'Existe "{tocheck}" en "{my_set}": {bool(my_set.count(tocheck))}')
    serparacion('-:-')
    tocheck = 'Perro'
    print(f'Existe "{tocheck}" en "{my_set}": {bool(my_set.count(tocheck))}')
    serparacion('-:-')
    my_set_copy = my_set.copy()
    # Elimina todo el contenido del conjunto.
    my_set.clear()
    print(my_set)
    serparacion('-:-')
    return set(my_set_copy)

def setasset(my_set: set) -> None:
    check_set = {'Tigre', 'Yak', 'Perro', 'Minotauro', 'Hydra'}
    # Unión.
    new_set = check_set.union(my_set)
    print(new_set)
    serparacion('-\-')
    # Intersección.
    print(my_set.intersection(check_set))
    serparacion('-\-')
    # Diferencia.
    print(my_set.difference(check_set))
    print(check_set.difference(my_set))
    serparacion('-\-')
    # Diferencia simétrica.
    print(my_set.symmetric_difference(check_set))
    serparacion('-\-')
    
def main():
    new_list = ['Perro', 'Gato', 'Leon', 'Cebra']
    setasset(listasset(new_list))

if __name__ == '__main__':
    main()
