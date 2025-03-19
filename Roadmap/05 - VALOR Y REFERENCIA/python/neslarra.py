"""
 EJERCICIO:
 - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
   su tipo de dato.
 - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

 DIFICULTAD EXTRA (opcional):
 Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
   Comprueba también que se ha conservado el valor original en las primeras.
"""
a = 'hola'
b = a
l = [1, 2, 3]
m = l
print(f"""
Una variable es un 'alias' a una dirección de memoria.
Cuando una o más variables tienen el mismo valor, entonces apuntan al mismo objeto. Por ejmeplo:
  a = 'hola' /  b = a  /  c = 'hola' <= tanto a como b apuntan al mismo objeto =>
  a paunta a {id(a)}  /  b apunta a {id(b)}  /  id(a) == id(b) = {id(a) == id(b)}
Otro ejemplo:
  l = [1, 2, 3]  /  m = l  /  n = [1, 2, 3] <= tanto l como m apuntan al mismo objeto =>
  l paunta a {id(l)}  /  m apunta a {id(m)}  /  id(l) == id(m) = {id(l) == id(m)}
""")
b += " mundo"
print(f"""
Cuando un tipo primitivo se modifica, se destruye esa relación y se crea una nueva apuntando a un nueva dirección:
  b += " mundo"      => id(b) = {id(b)} <= id(a) == id(b) = {id(a) == id(b)}
""", end="")
b += " mundo mio"
print(f"""  b += " mundo mio"  => id(b) = {id(b)} <= id(a) == id(b) = {id(a) == id(b)} (notar que incluso b cambió respecto de su anterior valor)""")
m.append(77)
print(f"""
En cambio cuando un tipo compuesto se modifica, mantiene la referencia a la posición de memoria original => todas las variables que la apuntaban verán la modificación:
  m.append(77) => m es {m}  /  l es {l} (y no la tocamos) => id(l) = {id(l)}  /  id(m) = {id(m)}  /  id(l) == id(m) = {id(l) == id(m)} (notar que el id NO CAMBIÓ)

La misma característica se cumple cuando se llama a una función pasándole argumentos prmitivos o compuestos:

def paso_args(a: str, l: list):
    print("Modifico a y l:")
    a += " MODIFCADA DENTRO DE LA FUNCIÓN"
    l.append("MODIFCADA DENTRO DE LA FUNCIÓN")
    print(f"Nuevos valores dentro de la función: a es """ + """{a}'  (id: {id(a)}) /  l es {l} (id: {id(l)})")
""")


def paso_args(a: str, l: list):
    print("Modifico a y l:")
    a += " MODIFICADA DENTRO DE LA FUNCIÓN"
    l.append("MODIFICADA DENTRO DE LA FUNCIÓN")
    print(f"Nuevos valores DENTRO de la función: a es '{a}'  (id: {id(a)}) /  l es {l} (id: {id(l)})")


print(f"Valores ANTES de la llamada a la función: a es '{a}'  (id: {id(a)}) /  l es {l} (id: {id(l)})")
paso_args(a, l)
print(f"Valores DESPUÉS de la llamada a la función: a es '{a}'  (id: {id(a)}) /  l es {l} (id: {id(l)})")
print(f"""
La variable primitiva 'a' se pasa por valor y su contenido solo existe dentro del ámbito en donde es utilizada (fuera O dentro de la función).
La variable compuesta 'l' se pasa por referencias y su contenido se mantiente no importa desde que ámbito se modifique.
Notar como el id de la variable 'a' cambia dentro de la función pero fuera mantiene el valor, en cambio l mantiene el mismo id siempre.

Aún así se puede modificar una variable primitiva en un ámbito distinto si se la referencia como global:

def paso_args_2():
    global a
    print("Modifico a:")
    a += " MODIFCADA DENTRO DE LA FUNCIÓN"
    print(f"Nuevos valores dentro de la función: a es """ + """{a}'  (id: {id(a)}))
""")


def paso_args_2():
    global a
    print("Modifico a:")
    a += " MODIFICADA DENTRO DE LA FUNCIÓN PERO GLOBAL"
    print(f"Nuevos valores DENTRO de la función: a es '{a}'  (id: {id(a)})")


print(f"Valores ANTES de la llamada a la función: a es '{a}'  (id: {id(a)})")
paso_args_2()
print(f"Valores DESPUÉS de la llamada a la función: a es '{a}'  (id: {id(a)})")

print(f"""
También podemos evitar modificar una variable compuesta original haciento un "copy" de la misma, lo cual genera un nuevo objto:

def paso_args_3(l: list) -> list:
    print("Copio y modifico l:")
    ll = l.copy()
    _ = ll.pop()
    ll.append("ESTO NO DEBE VERSE REFLEJADO EN l")
    print(f"Nuevos valores dentro de la función: l es """ + """{l}'  (id: {id(l)})  /  ll es {ll} (id: {id(ll)}))
    return ll
""")


def paso_args_3(l: list) -> list:
    print("Copio y modifico l:")
    ll = l.copy()
    _ = ll.pop()
    ll.append("ESTO NO DEBE VERSE REFLEJADO EN l")
    print(f"Nuevos valores dentro de la función: l es {l}'  (id: {id(l)})  /  ll es {ll} (id: {id(ll)})")
    return ll


print(f"Valores ANTES de la llamada a la función: l es '{l}'  (id: {id(l)})")
ll = paso_args_3(l)
print(f"Valores DESPUÉS de la llamada a la función: l es '{l}'  (id: {id(l)})  /  l es '{ll}'  (id: {id(ll)})", end="\n\n")

# Complejidad extra
print("Compejidad extra caso 1:\n")

cadena1 = "Hola"
cadena2 = "Mundo"


def prog_por_valor(cadena1: str, cadena2: str):
    cadena = cadena1
    cadena1 = cadena2
    cadena2 = cadena
    return cadena1, cadena2


print(f"Valores originales => cadena1: {cadena1}  /  cadena2: {cadena2}")
cadena1_, cadena2_ = prog_por_valor(cadena1, cadena2)
print(f"Valores después de la llamada => cadena1: {cadena1}  /  cadena2: {cadena2}  /  cadena1_: {cadena1_}  /  cadena2_: {cadena2_}")

print("\n\nCompejidad extra caso 2:\n")

lista1 = [1, 2, 3]
lista2 = ["a", "b"]


def prog_por_referencia(lista1: list, lista2: list):
    lista = lista1.copy()
    lista1 = lista2.copy()
    lista2 = lista.copy()
    return lista1, lista2


print(f"Valores originales => lista1: {lista1}  /  lista2: {lista2}")
lista1_, lista2_ = prog_por_referencia(lista1, lista2)
print(f"Valores después de la llamada => lista1: {lista1}  /  lista2: {lista2}  /  lista1_: {lista1_}  /  lista2_: {lista2_}")
