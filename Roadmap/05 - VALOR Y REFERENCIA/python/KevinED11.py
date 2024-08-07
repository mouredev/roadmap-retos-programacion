asignacion_por_valor = 1
asignacion_por_referencia = asignacion_por_valor
asigmación_por_referencia = 2
print(asignacion_por_valor)


lista_por_valor = [1, 2, 3]
lista_por_referencia = lista_por_valor
lista_por_referencia.append(4)

print(lista_por_valor)


listilla = [1, 2, 3]


def funcion_por_valor(numero: int) -> None:
    numero += 1
    print(numero)


def funcion_por_referencia(lista: list) -> None:
    lista[0] = 100


def funcion_por_valor2(lista: list) -> None:
    lista[1] = 200


value1 = 100
value2 = 200


def intercambio_por_valor(a, b) -> tuple[int, int]:
    a, b = b, a

    return a, b


def intercambio_por_referencia(lista: list) -> list:
    lista[0], lista[1] = lista[1], lista[0]

    return lista


def intercambio_por_referencia2(lista1: list, lista2: list) -> None:
    lista1[:], lista2[:] = lista2[:], lista1[:]


def main() -> None:
    funcion_por_valor(1)
    funcion_por_referencia(listilla)
    print(listilla)

    funcion_por_valor2(listilla[:])
    print(listilla)

    print("valores originales")
    print(value1, value2)

    print("valores intercambiados")
    print(intercambio_por_valor(value1, value2))

    lista_original = [10, 20]
    nueva_lista = lista_original[:]
    print("lista original")
    intercambio_por_referencia(nueva_lista)
    print(lista_original)

    print("valores intercambiados")
    intercambio_por_referencia(lista_original)
    print(lista_original)

    lista1 = [10, 20]
    lista2 = [30, 40]
    intercambio_por_referencia2(lista1, lista2)
    print(lista1, lista2)

if __name__ == "__main__":
    main()
