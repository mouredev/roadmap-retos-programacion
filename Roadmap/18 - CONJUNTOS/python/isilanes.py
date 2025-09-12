def main():
    print("\n==== Ejercicio ====")
    collection = [1, 2, 3]
    print(f"El conjunto inicial (una lista): {collection}")

    print("\nAñadimos el elemento '4' al final:")
    print('>>> collection.append(4)')
    collection.append(4)
    print(f"El conjunto actualizado: {collection}")

    print("\nAñadimos el elemento '-1' al inicio (posición 0):")
    print('>>> collection.insert(0, -1)')
    collection.insert(0, -1)
    print(f"El conjunto actualizado: {collection}")

    print("\nAñadimos los elementos '[5, 6, 7]' en bloque al final:")
    print('>>> collection.extend([5, 6, 7])')
    collection.extend([5, 6, 7])
    print(f"El conjunto actualizado: {collection}")

    print('\nAñadimos los elementos \'["a", "b",  "c"]\' en bloque en la posición 2 (entre el 1 y el 2):')
    print('>>> collection[2:2] = ["a", "b", "c"]')
    collection[2:2] = ["a", "b", "c"]
    print(f"El conjunto actualizado: {collection}")

    print('\nEliminamos el elemento en la posición 5 (el 2):')
    print('>>> collection.pop(5)')
    collection.pop(5)
    print(f"El conjunto actualizado: {collection}")

    print('\nActualizamos el elemento en la posición 3 (la "b") al valor \'True\':')
    print('>>> collection[3] = True')
    collection[3] = True
    print(f"El conjunto actualizado: {collection}")

    print("\nComprobamos el conjunto contiene el valor '4':")
    print(f"El conjunto contiene un 4?: 4 in collection = {4 in collection}")

    print('\nVaciamos el conjunto (sin sustituir el objeto por otro vacío):')
    print(f">>> id(collection) = {id(collection)}")
    print('>>> collection[:] = []')
    collection[:] = []
    print(f"El conjunto actualizado: {collection}")
    print(f">>> id(collection) = {id(collection)}")


def extra():
    print("\n==== Extra ====")
    print("Dado que no se indica que deba usarse el mismo tipo de conjunto que en el ejercicio anterior,")
    print("en este caso usaré objetos set(), o literalmente 'conjunto' en castellano.")
    print('>>> odd = {1, 3, 5, 7, 9, 11}')
    print('>>> prime = {1, 2, 3, 5, 7, 11}')
    odd = {1, 3, 5, 7, 9, 11}
    prime = {1, 2, 3, 5, 7, 11}

    print("\nUnión de primos e impares:")
    print('>>> res = odd | prime')
    res = odd | prime
    print(f"Resultado: {res}")

    print("\nIntersección de primos e impares:")
    print('>>> res = odd & prime')
    res = odd & prime
    print(f"Resultado: {res}")

    print("\nDiferencia entre primos e impares:")
    print('>>> res = prime - odd')
    res = prime - odd
    print(f"Resultado: {res}")
    print("Nótese que, a diferencia de las otras 3 operaciones, la diferencia no es conmutativa.")
    print("Hemos hecho la diferencia entre primos e impares, que son todos los primos que no son impares.")
    print("Si hubiéramos hecho la diferencia entre impares y primos, el resultado habría sido {9},")
    print("el número impar que no es primo.")

    print("\nDiferencia simétrica entre primos e impares:")
    print('>>> res = odd ^ prime')
    res = odd ^ prime
    print(f"Resultado: {res}")


if __name__ == "__main__":
    main()
    extra()
