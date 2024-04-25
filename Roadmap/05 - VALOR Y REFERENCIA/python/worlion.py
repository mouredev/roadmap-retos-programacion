"""

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
    se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
    variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
    Comprueba también que se ha conservado el valor original en las primeras.
"""

# Asignación de variables por valor y por referencia

# Variables por valor: Los enteros, por ejemplo, se asignan por valor
print("\n ---- Variables por valor ----\n")
a = 10
b = a
print(f"Variable a: {a}")   # 10
print(f"Variable b: {b}")   # 10
b = 20
print(f"Variable a: {a}")   # 10
print(f"Variable b: {b}")   # 20

# Variables por referencia: Los arrays, por ejemplo, se asignan por referencia
print("\n ---- Variables por referencia ----\n")
array1 = [10, 20, 30]
array2 = array1
print(f"Array 1: {array1}") # [10, 20, 30]
print(f"Array 2: {array2}") # [10, 20, 30]
array2[0] = 100
array1.append(40)
print(f"Array 1: {array1}") # [100, 20, 30, 40]
print(f"Array 2: {array2}") # [100, 20, 30, 40]


"""

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
    se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
    variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
    Comprueba también que se ha conservado el valor original en las primeras.
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")


# Intercambio por valor
def intercambio_valor(a: int, b: int) -> tuple:
    print(" - Intercambio por valor - ")
    temp = a
    a = b
    b = temp
    return a,b

x = 7
y = 99
print("Antes del intercambio:")
print(f"x = {x} ; y = {y}")
new_x, new_y = intercambio_valor(x, y)
print("Tras el intercambio:")
print(f"x = {x} ; y = {y}")
print(f"new_x = {new_x} ; new_y = {new_y}")

# Intercambio por referencioa
def intercambio_referencia(a: list, b: list) -> tuple:
    print(" - Intercambio por referencia - ")
    temp = a
    a = b
    b = temp
    return a,b

x = [7, 8]
y = [99, 0]
print("Antes del intercambio:")
print(f"x = {x} ; y = {y}")
new_x, new_y = intercambio_referencia(x, y)
print("Tras el intercambio:")
print(f"x = {x} ; y = {y}")
print(f"new_x = {new_x} ; new_y = {new_y}")