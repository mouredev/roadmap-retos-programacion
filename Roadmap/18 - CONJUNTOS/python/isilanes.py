def main():
    collection = [1, 2, 3]
    print(f"El conjunto inicial (una lista): {collection}")

    print("\nAñadimos el elemento '4' al final:")
    print('collection.append(4)')
    collection.append(4)
    print(f"El conjunto actualizado: {collection}")

    print("\nAñadimos el elemento '-1' al inicio (posición 0):")
    print('collection.insert(0, -1)')
    collection.insert(0, -1)
    print(f"El conjunto actualizado: {collection}")

    print("\nAñadimos los elementos '[5, 6, 7]' en bloque al final:")
    print('collection.extend([5, 6, 7])')
    collection.extend([5, 6, 7])
    print(f"El conjunto actualizado: {collection}")

    print('\nAñadimos los elementos \'["a", "b",  "c"]\' en bloque en la posición 2 (entre el 1 y el 2):')
    print('collection[2:2] = ["a", "b", "c"]')
    collection[2:2] = ["a", "b", "c"]
    print(f"El conjunto actualizado: {collection}")

    print('\nEliminamos el elemento en la posición 5 (el 2):')
    print('collection.pop(5)')
    collection.pop(5)
    print(f"El conjunto actualizado: {collection}")

    print('\nActualizamos el elemento en la posición 3 (la "b") al valor \'True\':')
    print('collection[3] = True')
    collection[3] = True
    print(f"El conjunto actualizado: {collection}")

    print("\nComprobamos el conjunto contiene el valor '4':")
    print(f"El conjunto contiene un 4?: 4 in collection = {4 in collection}")

    print('\nVaciamos el conjunto (sin sustituir el objeto por otro vacío):')
    print(f"id(collection) = {id(collection)}")
    collection[:] = []
    print(f"El conjunto actualizado: {collection}")
    print(f"id(collection) = {id(collection)}")


if __name__ == "__main__":
    main()
