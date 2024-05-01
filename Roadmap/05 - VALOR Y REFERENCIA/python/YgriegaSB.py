 # Variables dada por valor
def variables_por_valor(a, b):
    temp = a
    a = b
    b = temp
    return [a, b]

num1 = 10
num2 = 20

[aNuevo, bNuevo] = variables_por_valor(num1, num2)

print(f"Valores originales => v1:{num1} v2:{num2}")
print(f"Valores nuevos => v1:{aNuevo} v2:{bNuevo}")




def variables_por_referencia(objeto):
    keys = list(objeto.keys())
    if len(keys) >= 2:
        temp = objeto[keys[0]]
        objeto[keys[0]] = objeto[keys[1]]
        objeto[keys[1]] = temp 
    return objeto

objeto = {'a': 10, 'b': 20}

objeto_nuevo = variables_por_referencia(objeto)

print(f"Valores originales v1:{objeto['a']} v2:{objeto['b']}")
print(f"Valores nuevos v1:{objeto_nuevo['a']} v2:{objeto_nuevo['b']}")
