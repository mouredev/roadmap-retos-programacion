# EJERCICIO:
# - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#   su tipo de dato.

print("===============================")
print("=== ASIGNACIÓN DE VARIABLES ===")
print("===============================")
print("Integers:")
a = 1
b = 2
c = a
print(f"a = {a}, b = {b}, c = a")
print("IDs:")
print(f"¿'a' es 'c'? {a is c}")
print(f"¿'c' es 'a'? {c is a}")
print(f"¿'b' es 'a'? {b is a}")

a += 1
b += 1
print("\nSumar 1 a 'a' y 'b':")
print(f"a = {a}, b = {b}, c = {c}")
print("IDs:")
print(f"¿'a' es 'c'? {a is c}")
print(f"¿'c' es 'a'? {c is a}")
print(f"¿'b' es 'a'? {b is a}")


print("\n\nFloats:")
a = 1.2
b = a
c = a + 2.3
print(f"a = {a}, b = a, c = a + 2.3")
print("IDs:")
print(f"¿'a' es 'b'? {a is b}")
print(f"¿'b' es 'a'? {b is a}")
print(f"¿'c' es 'a' + 2.3? {c is (a + 2.3)}")

a *= 2
c *= 2
print("\nMultiplicar 2 a 'a' y 'c':")
print(f"a = {a}, b = {b}, c = {c}")
print("IDs:")
print(f"¿'a' es 'b'? {a is b}")
print(f"¿'b' es 'a'? {b is a}")
print(f"¿'c' es 'a'? {c is a}")


print("\n\nStrings:")
a = "Hola"
b = "Python"
c = a
d = ", "
print(f"a = '{a}', b = '{b}', c = a, d = '{d}'")
print("IDs:")
print(f"¿'a' es 'c'? {a is c}")
print(f"¿'c' es 'a'? {c is a}")

c += d
c += b
print(f"\nConcatenar 'd' y 'b' a 'c':")
print(f"a = '{a}', b = '{b}', c = '{c}', d = '{d}'")
print("IDs:")
print(f"¿'a' es 'c'? {a is c}")
print(f"¿'c' es 'a'? {c is a}")
print(f"¿'c' es 'a' + 'd' + 'b'? {c is (a + d + b)}")


print("\n\nBooleans:")
a = True
b = a
c = not a
print(f"a = {a}, b = a, c = not a")
print(f"¿'a' es 'b'? {a is b}")
print(f"¿'b' es 'a'? {b is a}")
print(f"¿'c' es not 'a'? {c is not a}")

a = not a
print("\nConvertir 'a' a False:")
print(f"a = {a}, b = {b}, c = {c}")
print(f"'a' es 'b'? {a is b}")
print(f"'b' es 'a'? {b is a}")
print(f"'c' es 'a'? {c is a}")


print("\n\nLists:")
frutas = ["Manzana", "Pera", "Uva"]
verduras = ["Zanahoria", "Lechuga", "Tomate"]
mixto = frutas
print(f"Frutas: {frutas}")
print(f"Verduras: {verduras}")
print(f"Mixto: {mixto}")

print("\nAgregando verduras a lista mixta:")
mixto.extend(verduras)
print(f"Frutas: {frutas}")
print(f"Verduras: {verduras}")
print(f"Mixto: {mixto}")

print("\nEliminando el último ítem de lista verduras:")
verduras.pop()
print(f"Frutas: {frutas}")
print(f"Verduras: {verduras}")
print(f"Mixto: {mixto}")

print("\nEliminado verduras de lista frutas sin afectar a lista mixta:")
frutas = mixto.copy()
frutas.remove("Zanahoria")
frutas.remove("Lechuga")
frutas.remove("Tomate")
print(f"Frutas: {frutas}")
print(f"Verduras: {verduras}")
print(f"Mixto: {mixto}")


print("\n\nDictionaries:")
info = {
    "username": "HaloGabriel",
    "nombre": "Gabriel",
    "edad": 25,
    "conocimientos": ["Python", "Java", "C#"]
}
info_plus = {
    "pais": "Perú",
    "fecNac": "2000-09-19",
    "conocimientos": ["JavaScript", "SQL Server", "MongoDB", "MySQL"]
}
info_backup = info
info_other_backup = info.copy()
info_other_backup["conocimientos"] = info["conocimientos"].copy()
print(f"Información: {info}")
print(f"Adicional: {info_plus}")
print(f"Backup: {info_backup}")
print(f"Otro Backup: {info_other_backup}")

print("\nAgregando 'Adicional' a 'Información':")
for k, v in info_plus.items():
    if k in info and type(v) == list:
        info[k].extend(v)
    else:
        info[k] = v
print(f"Información: {info}")
print(f"Adicional: {info_plus}")
print(f"Backup: {info_backup}")
print(f"Otro Backup: {info_other_backup}")

print("\nLimpiando Backup, Adicional e Info:")
info = {}
info_backup = {}
info_plus = {}
print(f"Información: {info}")
print(f"Adicional: {info_plus}")
print(f"Backup: {info_backup}")
print(f"Otro Backup: {info_other_backup}")

print(f"\nRestaurando inicial Info:")
info = info_other_backup.copy()
print(f"Información: {info}")
print(f"Adicional: {info_plus}")
print(f"Backup: {info_backup}")
print(f"Otro Backup: {info_other_backup}")


print("\n\nSets:")
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
numeros_pares = {2, 4, 6, 8, 10}
numeros_impares = set()
numeros_pares_e_impares = numeros_pares

print(f"Números: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
print(f"Números pares e impares: {numeros_pares_e_impares}")

print("\nAñadiendo de 'Números':")
print("- pares a 'numeros_pares'")
print("- impares a 'numeros_impares'")
print("- pares e impares a 'numeros_pares_e_impares'")
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.add(numero)
    else:
        numeros_impares.add(numero)

    numeros_pares_e_impares.add(numero)
print("Resultado:")
print(f"Números: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
print(f"Números pares e impares: {numeros_pares_e_impares}")

print("\nEliminando impares de 'numeros_pares' sin afectar a 'numeros_pares_a_impares':")
numeros_pares = numeros_pares_e_impares.copy()
for numero in numeros:
    if numero % 2 != 0:
        numeros_pares.discard(numero)
print(f"Números: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
print(f"Números pares e impares: {numeros_pares_e_impares}")

print(f"\nLimpiando 'numeros_pares_e_impares':")
numeros_pares_e_impares.clear()
print(f"Números: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
print(f"Números pares e impares: {numeros_pares_e_impares}")


print(f"\n\nTuples:")
numeros = (2, 4, 6, 8, 10)
pares = numeros
print(f"Números: {numeros}")
print(f"Pares: {pares}")

print("\nLimpiando 'pares':")
pares = ()
print(f"Números: {numeros}")
print(f"Pares: {pares}")

print("\nAsignando 'numeros' a 'pares' de nuevo:")
numeros = (2, 4, 6, 8, 10)
pares = numeros
print(f"Números: {numeros}")
print(f"Pares: {pares}")

print("\nAgregando más valores a 'pares':")
pares = list(pares)
for number in range(11, 21):
    if number % 2 == 0:
        pares.append(number)
pares = tuple(pares)
print(f"Números: {numeros}")
print(f"Pares: {pares}")

# - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
#   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.

print("\n")
print("====================================")
print("=== PASAR ARGUMENTOS A FUNCIONES ===")
print("====================================")
print("Integers:")
a = 1
b = 2
print(f"a = {a}, b = {b}")

def sumar_uno_a_todos(*numbers):
    for item in numbers:
        if type(item) == int or type(item) == float:
            item += 1
            print(f"Nuevo valor (dentro de función): {item}")

print("Sumando 1 a todos (por valor):")
sumar_uno_a_todos(1, 2)
print(f"Valores fuera de función: a = {a}, b = {b}")

print("\nSumando 1 a todos (por referencia):")
sumar_uno_a_todos(a, b)
print(f"Valores fuera de función: a = {a}, b = {b}")


print("\n\nFloats:")
a = 1.2
b = a
print(f"a = {a}, b = a")

print("Sumando 1 a todos (por valor):")
sumar_uno_a_todos(a + 0, b + 0)
print(f"Valores fuera de función: a = {a}, b = {b}")

print("\nSumando 1 a todos (por referencia):")
sumar_uno_a_todos(a, b)
print(f"Valores fuera de función: a = {a}, b = {b}")


print("\n\nStrings:")
a = "Hola"
b = "HaloGabriel"
print(f"a = '{a}', b = '{b}'")

def concatenar_uno_y_empty_dos(cadena_uno, cadena_dos):
    cadena_uno += " "
    cadena_uno += cadena_dos
    cadena_dos = ""
    print("Nuevos valores (dentro de función):")
    print(f"Primer valor: '{cadena_uno}'")
    print(f"Segundo valor: '{cadena_dos}'")

print("Concatenando 'b' a 'a' y dejar vacío a 'b' (por valor):")
concatenar_uno_y_empty_dos("Hola", "HaloGabriel")
print(f"Valores fuera de función: a = '{a}', b = '{b}'")

print("\nContanenando 'b' a 'a' y dejar vacío a 'b' (por referencia):")
concatenar_uno_y_empty_dos(a, b)
print(f"Valores fuera de función: a = '{a}', b = '{b}'")


print("\n\nBooleans:")
a = True
b = False
print(f"a = {a}, b = {b}")

def invertir_booleans(*booleans):
    for item in booleans:
        if type(item) == bool:
            item = not item
            print(f"Nuevo valor (dentro de función): {item}")

print("Intercambiando booleans (por valor):")
invertir_booleans(True, False)
print(f"a = {a}, b = {b}")

print("\nIntercambiando booleans (por referencia):")
invertir_booleans(a, b)
print(f"a = {a}, b = {b}")


print("\n\nLists:")
frutas = ["Manzana", "Pera", "Fresa"]
verduras = ["Lechuga", "Papa", "Coliflor"]
print(f"Frutas (global): {frutas}")
print(f"Verduras (global): {verduras}")

def extender_y_luego_reasignar(list1: list, list2: list):
    list1.extend(list2)
    print(f"Extendiendo Lista 1 (dentro de función): {list1}")
    list1 = []
    print(f"Limpiando Lista 1 (dentro de función): {list1}")
    return list1

print("\nAñadir 'verduras' a 'frutas' y luego limpiar 'frutas' (por valor):")
list1 = extender_y_luego_reasignar(frutas.copy(), verduras.copy())
print(f"Frutas (global): {frutas}")
print(f"Verduras (global): {verduras}")
print(f"Lista 1 retornada de función (global): {list1}")

print("\nAñadir 'verduras' a 'frutas' y luego limpiar 'frutas' (por referencia):")
list1 = extender_y_luego_reasignar(frutas, verduras)
print(f"Frutas (global): {frutas}")
print(f"Verduras (global): {verduras}")
print(f"Lista 1 retornada de función (global): {list1}")


print("\n\nDictionaries:")
info = {
    "username": "HaloGabriel",
    "nombre": "Gabriel",
    "conocimientos": {
        "lenguajes_programacion": ["Python", "Java", "C#"],
        "bases_datos": ["SQL Server", "MySQL"]
    },
    "edad": 25
}
info_plus = {
    "fec_nac": "2000-09-19",
    "pais": "Perú",
    "conocimientos": {
        "lenguajes_programacion": ["C++", "JavaScript"]
    }
}
info_backup = info
print(f"Información (global): {info}")
print(f"Adicional (global): {info_plus}")
print(f"Backup (global): {info_backup}")
print("=" * 30)

def extender_diccionario_con_otro_diccionario(dict1: dict, dict2: dict): 
    for k, v in dict2.items():
        if k in dict1 and type(v) == dict and type(dict1[k]) == dict:
            extender_diccionario_con_otro_diccionario(dict1[k], dict2[k])
        elif k in dict1 and type(v) == list and type(dict1[k] == list):
            dict1[k].extend(dict2[k])
        else:
            dict1[k] = v
        print(f"Resultado (dentro de función): {dict1}")
        print()
    return dict1.copy()

info_copy = info.copy()
info["conocimientos"] = info["conocimientos"].copy()
info["conocimientos"]["lenguajes_programacion"] = info["conocimientos"]["lenguajes_programacion"].copy()
info["conocimientos"]["bases_datos"] = info["conocimientos"]["bases_datos"].copy()
print("\nExtendiendo 'Información' con 'Adicional' (por valor):")
dict1 = extender_diccionario_con_otro_diccionario(info_copy, info_plus.copy())
print(f"Información (global): {info}")
print(f"Adicional (global): {info_plus}")
print(f"Backup (global): {info_backup}")
print(f"Resultado (global): {dict1}")
print("=" * 30)

print("\nExtendiendo 'Información' con 'Adicional' (por referencia):")
dict1 = extender_diccionario_con_otro_diccionario(info, info_plus)
print(f"Información (global): {info}")
print(f"Adicional (global): {info_plus}")
print(f"Backup (global): {info_backup}")
print(f"Resultado (global): {dict1}")

print("\nLimpiando Información:")
info_copy = info.copy()
for k in info_copy.keys():
    if k in info:
        del info[k]
print(f"Información (global): {info}")
print(f"Adicional (global): {info_plus}")
print(f"Backup (global): {info_backup}")
print(f"Resultado anterior (global): {dict1}")

print("\nRestaurando Información y Backup con Resultado anterior (global):")
info = dict1.copy()
info_backup = info
print(f"Información (global): {info}")
print(f"Adicional (global): {info_plus}")
print(f"Backup (global): {info_backup}")
print(f"Resultado anterior (global): {dict1}")

print("\n\nSets:")
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
numeros_pares = set()
numeros_impares = set()
divisibles_por_2 = numeros_pares
print(f"Números: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
print(f"Divisibles por 2: {divisibles_por_2}")

def agregar_pares_o_impares(numeros_set: set, resultado_set: set, par: bool = True):
    for number in numeros_set:
        if type(number) == int:
            if par:
                if number % 2 == 0:
                    resultado_set.add(number)
            else:
                if number % 2 != 0:
                    resultado_set.add(number)
    print(f"Resultado (dentro de función): {resultado_set}")

print(f"\nAgregando 'numeros' a 'numeros_pares' y 'numeros_impares' (por valor):")
agregar_pares_o_impares(numeros, numeros_pares.copy())
agregar_pares_o_impares(numeros, numeros_impares.copy(), False)
print(f"Numeros (global): {numeros}")
print(f"Números pares (global): {numeros_pares}")
print(f"Números impares (global): {numeros_impares}")
print(f"Divisibles por 2 (global): {divisibles_por_2}")

print(f"\nAgregando 'numeros' a 'numeros_pares' y 'divisibles_por_2' (por referencia):")
agregar_pares_o_impares(numeros, divisibles_por_2)
agregar_pares_o_impares(numeros, numeros_impares, False)
print(f"Números (global): {numeros}")
print(f"Números pares (global): {numeros_pares}")
print(f"Números impares (global): {numeros_impares}")
print(f"Divisibles por 2 (global): {divisibles_por_2}")


print("\n\nTuples:")
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
pares = (2, 4, 6, 8, 10)
impares = (1, 3, 5, 7, 9)
divisibles_por_2 = pares
print(f"Números: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Divisibles por 2: {divisibles_por_2}")

def agregando_numeros_a_tuple(numeros: tuple, tuple_result: tuple, par: bool = True):
    tuple_result = list(tuple_result)
    for numero in numeros:
        if type(numero) == int:
            if par:
                if numero % 2 == 0 and numero not in tuple_result:
                    tuple_result.append(numero)
            else:
                if numero % 2 != 0 and numero not in tuple_result:
                    tuple_result.append(numero)
    tuple_result = tuple(tuple_result)
    print("Resultado pares" if par else "Resultado impares", end="")
    print(f" (dentro de función): {tuple_result}")
    return tuple_result

print(f"\nAgregando 'numeros' a 'pares' e 'impares' (por valor):")
resultado_pares = agregando_numeros_a_tuple(numeros, (2, 4, 6, 8, 10))
resultado_impares = agregando_numeros_a_tuple(numeros, (1, 3, 5, 7, 9), False)
print(f"Números (global): {numeros}")
print(f"Pares (global): {pares}")
print(f"Impares (global): {impares}")
print(f"Divisibles por 2 (global): {divisibles_por_2}")
print(f"Resultado pares (global): {resultado_pares}")
print(f"Resultado impares (global): {resultado_impares}")

print(f"\nAgregando 'numeros' a 'pares' e 'impares' (por referencia):")
resultado_pares = agregando_numeros_a_tuple(numeros, pares)
resultado_impares = agregando_numeros_a_tuple(numeros, impares, False)
print(f"Números (global): {numeros}")
print(f"Pares (global): {pares}")
print(f"Impares (global): {impares}")
print(f"Divisibles por 2 (global): {divisibles_por_2}")
print(f"Resultado pares (global): {resultado_pares}")
print(f"Resultado impares (global): {resultado_impares}")
print("\n")

# DIFICULTAD EXTRA (opcional):
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#   variables originales y las nuevas, comprobando que se han invertido su valor en las segundas.
#   Comprueba también que se ha conservado el valor original en las primeras.

print("=======================")
print("=== EJERCICIO EXTRA ===")
print("=======================")

lenguajes_programacion = ["Python", "C++", "C#", "Java", "Kotlin"]
bases_datos = ["SQL Server", "MongoDB", "MySQL"]
print(f"Lenguajes de programación: {lenguajes_programacion}")
print(f"Bases de datos: {bases_datos}")
print()

def intercambiando_valores(variable_uno, variable_dos):
    variable_uno, variable_dos = variable_dos, variable_uno
    return variable_uno, variable_dos

print("CASO 1 (por valor):")
resultado_uno, resultado_dos = intercambiando_valores(lenguajes_programacion.copy(), bases_datos.copy())
print(f"Lenguajes de programación: {lenguajes_programacion}")
print(f"Bases de datos: {bases_datos}")
print(f"Resultado 1: {resultado_uno}")
print(f"Resultado 2: {resultado_dos}")
print("\nAñadir un ítem a ambos resultados:")
resultado_uno.append('MariaDB')
resultado_dos.append('Swift')
print(f"Lenguajes de programación: {lenguajes_programacion}")
print(f"Bases de datos: {bases_datos}")
print(f"Resultado 1: {resultado_uno}")
print(f"Resultado 2: {resultado_dos}")
print()


print ("CASO 2 (por referencia):")
resultado_uno, resultado_dos = intercambiando_valores(lenguajes_programacion, bases_datos)
print(f"Lenguajes de programación: {lenguajes_programacion}")
print(f"Bases de datos: {bases_datos}")
print(f"Resultado 1: {resultado_uno}")
print(f"Resultado 2: {resultado_dos}")
print("\nAñadir un ítem a ambos resultados:")
resultado_uno.append('MariaDB')
resultado_dos.append('Swift')
print(f"Lenguajes de programación: {lenguajes_programacion}")
print(f"Bases de datos: {bases_datos}")
print(f"Resultado 1: {resultado_uno}")
print(f"Resultado 2: {resultado_dos}")