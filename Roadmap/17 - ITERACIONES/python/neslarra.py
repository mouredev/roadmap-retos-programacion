"""
 EJERCICIO:
 Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 números del 1 al 10 mediante iteración.
 DIFICULTAD EXTRA (opcional):
 Escribe el mayor número de mecanismos que posea tu lenguaje
 para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""
from collections.abc import Iterator

print(f"""##  Explicación  {'#' * 30}""")

print(f"""
Un "iterable" es una colección que puede recorrerse y referenciarse a través de un índice (implementan __iter__ y __getitem__,  que automáticamente
es llamada a través de [indice] o de [slice] => ES suscriptable).
Listas, tuplas, cadenas, diccionarios SON "iterables".
    a = [1, 2, 3]
    isinstance(a, Iterable) => True
    hasattr(a, "__iter__") => True
    hasattr(a, "__getitem__") => True
    isinstance(a, Iterator) => False
    hasattr(a, "__next__") => False
    
    a = 1
    isinstance(a, Iterable) => False
    isinstance(a, Iterator) => False
    
Un "iterador" es, en cambio, una colección que que genera un puntero a un elemento de manera secuencial y hacia adelante (implementa __iter__ y 
__next__, el cual es llamado cada vez para traer el próximo elemento => NO se puede referencia on un índice => NO es "suscriptable". Cuando ya no
hay elementos, lanza la excepción StopIteration).  
    
    class MiClase(Iterator):
        xxxxxxxx   <=  implementada en uno de los casos de "dificultad extra"
    a = MiClase()
    isinstance(a, Iterable) => True
    hasattr(a, "__iter__") => True
    hasattr(a, "__getitem__") => False
    isinstance(a, Iterator) => True
    hasattr(a, "__next__") => True
Dejo unos links donde se explica claramente Iterables e Iteradores:
    https://ellibrodepython.com/iterator-python
    http://cuartas.es/python/iterables/
    https://es.stackoverflow.com/questions/84591/diferencia-entre-objetos-iterable-iterator-y-secuencias-en-python-3
El ejercicio de implementar tres maneras de mostrar los números del 1 al 10 es parte de la "dificultad extra" <=> 10 maneras de iterar.
""")


def numerar_comprehension(inicio=0, fin=100):
    mapa = "".maketrans("", "", "[],")       # # mapa = {91: None, 93: None, 44: None}   <= cualquiera de las dos maneras es válida
    return f"{[x for x in range(inicio, fin + 1)].__str__().translate(mapa)}"


def numerar_for(inicio=0, fin=100):
    salida = ""
    for numero in range(inicio, fin + 1):
        salida += str(numero) + " "
    return salida


def numerar_loop(inicio=0, fin=100):
    salida = ""
    x = inicio
    while x <= fin:
        salida += str(x) + " "
        x += 1
    return salida


def numerar_recursivo(inicio=0, numeros="", fin=100):
    if inicio == fin:
        return numeros + str(fin)
    else:
        numeros += str(inicio) + " "
        return numerar_recursivo(inicio + 1, numeros, fin)


def generador(inicio, fin):
    valor = inicio
    while valor <= fin:
        yield valor
        valor += 1


def numerar_generador(inicio=0, fin=100):
    salida = ""
    numeros = generador(inicio, fin)
    while True:
        try:
            salida += str(next(numeros)) + " "
        except StopIteration:
            break
    return salida


class Numerar(Iterator):
    def __init__(self, inicio, fin):
        self.fin = fin
        self.inicio = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio > self.fin:
            raise StopIteration
        else:
            valor_actual = self.inicio
            self.inicio += 1
            return valor_actual


def numerar_zip(inicio=0, fin=100):
    salida = ""
    pares = [x for x in range(inicio, fin + 1) if (x % 2) == 0]
    impares = [x for x in range(inicio, fin + 1) if (x % 2) == 1]
    for x, y in zip(impares, pares):
        salida += str(x) + " " + str(y) + " "
    return salida


def numerar_cadena():
    salida = ""
    numeros = "0123456789"
    for d in numeros:
        salida += str(int(d) + 1) + " "
    return salida


def numerar_enumerate(lista_de_numeros, inicio=0, fin=100):
    salida = ""
    if fin > lista_de_numeros.__len__():
        return
    for ind, _ in enumerate(lista_de_numeros):
        if inicio <= ind <= fin:
            salida += str(ind) + " "
    return salida


def numerar_reversa(inicio=100, fin=-1):
    salida = ""
    for numero in reversed(range(inicio, fin - 1, -1)):
        salida += str(numero) + " "
    return salida


print(f"""\n \n##  Dificultad extra  {'#' * 30}\n""")

caso = Numerar(1, 10)
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 por comprehensión: {numerar_comprehension(1, 10)}")
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 con un for loop:   {numerar_for(1, 10)}")
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 con un while loop: {numerar_loop(1, 10)}")
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 con recursividad:  {numerar_recursivo(inicio=1, fin=10)}")
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 con un generador:  {numerar_generador(1, 10)}")
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 con zip:           {numerar_zip(1, 10)}")
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 desde cadena:      {numerar_cadena()}")
print(f"""Caso {caso.__next__()}: mostrar números del 1 al 10 con enumerate:     {numerar_enumerate(['cero', 'uno', 'dos', 'tres', 'cuatro',
                                                                                                 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 
                                                                                                 'once', 'doce'], 1, 10)}""")
print(f"Caso {caso.__next__()}: mostrar números del 10 al 1 en reversa:        {numerar_reversa(10, 1)}")
print(f"Caso {caso.__next__()}: mostrar números del 1 al 10 con un iterador:  la numeración de estos casos con la variable 'caso'")
