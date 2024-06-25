def m1():
    print("== (m1) for loop simple ==")
    for i in range(1, 11):
        print(i)


def m2():
    print("== (m2) print dentro de loop comprehension ==")
    [print(i) for i in range(1, 11)]


def m3():
    print("== (m3) imprimir lista completa formada desde generador ==")
    print(list(range(1, 11)))


def e1():
    print("== (e1) for loop sobre generador ==")
    for i in range(3):
        print(f"Valor {i} OK")


def e2():
    print("== (e2) for loop sobre lista ==")
    for c in ["a", "b", "c"]:
        print(f"Valor {c} OK")


def e3():
    print("== (e3) for loop sobre tupla ==")
    for v in (True, False, None, Ellipsis):
        print(f"Valor {v} OK")


def e4():
    print("== (e4) for loop sobre cadena ==")
    for c in "hola":
        print(f"Valor {c} OK")


def e5():
    print("== (e5) for loop sobre clave/valor de diccionario ==")
    d = {f"k{i}": f"v{i}" for i in range(3)}
    for k, v in d.items():
        print(f"Clave {k} -> Valor {v} OK")


def e6():
    print("== (e6) dict comprehension para construir diccionarios (usado también en e5) ==")
    print({f"k{i}": f"v{i}" for i in range(3)})


def e7():
    print("== (e7) list comprehension para construir lista ==")
    print([i**2 for i in range(5)])


def e8():
    print("== (e8) comprehension para construir generador ==")
    g = (i**2 for i in range(5))
    print("Generador:", g)
    print("Lista desde generador:", list(g))


def e9():
    print("== (e9) comprehension para construir set ==")
    print({abs(i) for i in range(-5, 3)})


def e10():
    print("== (e10) map para procesar enumerable ==")
    print(list(map(int, [1.1, 2.2, 3.3, 4.5])))


def main():
    print("==== MAIN ====")
    for fun in (m1, m2, m3):
        fun()


def extra():
    print("==== EXTRA ====")
    for fun in (e1, e2, e3, e4, e5, e6, e7, e8, e9, e10):
        fun()


if __name__ == "__main__":
    main()
    extra()
