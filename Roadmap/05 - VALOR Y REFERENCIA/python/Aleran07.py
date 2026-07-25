# 05
# Variables por valor int, float, str, bool, tuple

# int
a = 10
b = a      # b recibe una copia del valor de a

a = 20     # Cambiamos 'a'

print(a)  # 20
print(b)  # 10 → b NO se vio afectada

# str
x = "Hola"
y = x
x = "Chao"

print(x)  # Chao
print(y)  # Hola → no cambia, porque string es INMUTABLE


# Variables por referencia list, dict, set, objetos personalizados

#list
lista1 = [1, 2, 3]
lista2 = lista1   # lista2 apunta a la MISMA lista en memoria

lista1.append(4)

print(lista1)  # [1, 2, 3, 4]
print(lista2)  # [1, 2, 3, 4] → también cambió

"""se puede evitar la referecia con . copy()"""

lista1 = [1, 2, 3]
lista2 = lista1.copy()  # o lista2 = lista1[:] o list(lista1)
lista3 = lista1[:]
lista4 = list(lista1)

lista1.append(4)

print(lista1)  # [1, 2, 3, 4]
print(lista2)  # [1, 2, 3]
print(lista3)  # [1, 2, 3]
print(lista4)  # [1, 2, 3]

# Ejemplo de referencia en memoria
a = [1, 2, 3]
b = a

print(id(a))  # 140192940769920 (ejemplo)
print(id(b))  # 140192940769920 → mismo id = MISMO objeto

b = a.copy()  # Con copia
print(id(a))  # 140192940769920
print(id(b))  # 140192940770288 → distinto id = OBJETO DIFERENTE

# Funciones por valor
# int
def modificar_numero(x): # Se crea una copia del valor, no afecta a 'a'
    x = x + 10
    print("Dentro de la función:", x)

a = 5
modificar_numero(a)
print("Fuera de la función:", a)

# str
def cambiar_texto(texto):
    texto = texto.upper()
    print("Dentro de la función:", texto)

msg = "hola"
cambiar_texto(msg)
print("Fuera de la función:", msg)

# funciones por valor
def modificar_lista(lista):
    lista.append(100) # La modificación AFECTA al original porque apuntan al mismo objeto en memoria
    print("Dentro de la función:", lista)

nums = [1, 2, 3]
modificar_lista(nums)
print("Fuera de la función:", nums)

# Evitar que se modifique el original
def modificar_sin_afectar(lista):
    copia = lista.copy()  # o lista[:] o list(lista)
    copia.append(999)
    print("Dentro de la función:", copia)

nums = [1, 2, 3]
modificar_sin_afectar(nums)
print("Fuera de la función:", nums)

# Ejemplo visual de objeto en memoria
def revisar(obj):
    print("ID dentro:", id(obj))

a = [1,2,3]
print("ID fuera:", id(a)) # Los IDs coinciden → es el mismo objeto en memoria
revisar(a)

"""
----------------------------------------------------------------------------------------
Tipo de dato                 - Se modifica fuera de la funcion? - Naturaleza
----------------------------------------------------------------------------------------
int, float, str, bool, tuple - No cambia                        - Inmutable por valor

list, dict, set, objetos     - Puede cambiar                    - Mutable por referencia

Para evitarlo                - Usar .copy()                     - se protege el original
----------------------------------------------------------------------------------------
"""

"""Ejecicio Extra
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
"""

# Funcion de intercambio por Valor

valor1 = 10
valor2 = "Hola"

# nota si no le añado nada para crear un nuevo objeto, el id no cambia.
def  intercam_valor (valor1, valor2):
    ax = valor1
    valor1 = valor2 + " bro" # <-- aquí se crea una NUEVA cadena
    valor2 = ax + 10
    return (valor1, valor2)  # <-- aquí se crea un NUEVO entero (20)

valor3, valor4 = intercam_valor(valor1, valor2)

print(valor1, f"Id variable 1: {id(valor1)}", valor2, f"Id variable 2: {id(valor2)}")
print(valor3,f"Id variable 3: {id(valor3)}", valor4, f"Id variable 4: {id(valor4)}")



# Funcion de intercambio por Referencia
valor1 = [1, 2 , 3]
valor2 = [4, 5, 6]
print(valor1, f"Id variable 1: {id(valor1)}", valor2, f"Id variable 2: {id(valor2)}")

def  intercam_valor (x, y):
    y.append(10)
    x.append(100)
    return (x, y)

valor3, valor4 = intercam_valor(valor1, valor2)

print(valor1, f"Id variable 1: {id(valor1)}", valor2, f"Id variable 2: {id(valor2)}")
print(valor3,f"Id variable 3: {id(valor3)}", valor4, f"Id variable 4: {id(valor4)}")