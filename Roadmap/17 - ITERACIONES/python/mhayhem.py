# @Author: Mhayhem

# EJERCICIO:
# Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
# números del 1 al 10 mediante iteración.

# iteración For.

def for_iteration():
    for n in range(1, 11):
        print(n, end=", ")
    print("\n")
# iteración while.

def while_iteration():
    n = 1
    while n < 11:
        print(n, end=", ")
        n += 1
    print("\n")

# iteración por compresión de lista.

def comprehesion_iteration():
    print([x + 1 for x in range(10)])
    print("\n")
    


# DIFICULTAD EXTRA (opcional):
# Escribe el mayor número de mecanismos que posea tu lenguaje
# para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?


# iteración compresión de conjunto.

def set_iteration():
    print({x +1 for x in range(10)})
    print("\n")

# iteración comprensión de diccionario.    

def dict_iteration():
    print({n: n + 2 for n in range(1,11)})
    print("\n")

# iteración usando map().
    
def map_iteration():
    print(list(map(lambda x: x, range(1,11))))
    print("\n")

# iteración usando filter.

def filter_iteration():
    print(list(filter(lambda x: True, range(1, 11))))
    print("\n")

# iteración usando iter.

def iter_iteration():
    it = iter(range(1, 11))
    
    while True:
        try:
            print(next(it), end=", ")
        except StopIteration:
            break
    print("\n")

# iteración usando zip.

def zip_iteration():
    values = "0123456789"
    for n, v in zip(range(1, 11), values):
        print(f"{n}:{v}", end=", ")
    print("\n")
    
def main():
    print("Iteración For")
    for_iteration()
    print("Iteración While")
    while_iteration()
    print("Iteración Comprensión de lista")
    comprehesion_iteration()
    print("Iteración compresión de conjunto")
    set_iteration()
    print("Iteración compresión de diccionario")
    dict_iteration()
    print("Iteración usando map()")
    map_iteration()
    print("Iteración usando filter()")
    filter_iteration()
    print("Iteración manual con iter()")
    iter_iteration()
    print("Iteración usando zip()")
    zip_iteration()

if __name__=="__main__":
    main()