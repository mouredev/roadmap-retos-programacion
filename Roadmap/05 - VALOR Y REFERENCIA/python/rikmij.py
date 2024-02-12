#asignación por valor. Son tipos simples: strings, ints, bool...
value = "Asignado por valor"

#asignación por referencia. Son colecciones: listas, tuples, sets...
refer = ["Referencia", 33]


def fun_valor(valor):
    valor = "he sido modificado"

val = "mondongo"
fun_valor(val)
print(val)


def fun_reference(ref):
    ref[0] = "Ahora el primero soy yo"

refe = [1, 2, 3]
fun_reference(refe)
print(refe)


def fun_valor_mod(val):
    valor = "He sido modificado"
    return valor

val1 = "mondongo1"
val1 = fun_valor_mod(val1)
print(val1)


print('\n', '~'*7, "EJERCICIO EXTRA", '~'*7)

def funcion_valor(v1, v2):
    aux = v1
    v1 = v2
    v2 = aux

    return v1, v2

v1 = 1
v2 = 2
new_v1, new_v2 = funcion_valor(v1, v2)

print(f"v1 = {v1}, v2 = {v2}")
print(f"new_v1 = {new_v1}, new_v2 = {new_v2}")


def funcion_referencia(ref1, ref2):
    aux = ref1
    ref1 = ref2
    ref2 = aux
    return ref1, ref2

ref1 = ["Uno", "Dos", "Tres"]
ref2 = (1, 2, 3)
n_ref1, n_ref2 = funcion_referencia(ref1, ref2)

print(f"ref1 = {ref1}, ref2 = {ref2}")
print(f"n_ref1 = {n_ref1}, n_ref2 = {n_ref2}")
