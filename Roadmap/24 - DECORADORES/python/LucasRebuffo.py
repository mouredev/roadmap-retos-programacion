def imprimir_funcion(func):

    def imprimir():
        print(f"La funcion {func.__name__} se llamo")
        return func

    return imprimir


@imprimir_funcion
def funcion_de_ejemplo():
    pass


@imprimir_funcion
def funcion_de_ejemplo_2():
    pass


@imprimir_funcion
def funcion_de_ejemplo_3():
    pass


funcion_de_ejemplo()
funcion_de_ejemplo_2()
funcion_de_ejemplo_2()

""" Extra """


def contador_de_llamadas(func):
    def counter():
        counter.llamadas_counter += 1
        print(f"La funcion {func.__name__} se llamo {counter.llamadas_counter} veces")
        return func

    counter.llamadas_counter = 0
    return counter

@contador_de_llamadas
def funcion_de_ejemplo_4():
    pass

@contador_de_llamadas
def funcion_de_ejemplo_5():
    pass

funcion_de_ejemplo_4()
funcion_de_ejemplo_4()
funcion_de_ejemplo_4()
funcion_de_ejemplo_4()

funcion_de_ejemplo_5()
funcion_de_ejemplo_5()
funcion_de_ejemplo_5()

funcion_de_ejemplo_4()
funcion_de_ejemplo_4()
funcion_de_ejemplo_4()
