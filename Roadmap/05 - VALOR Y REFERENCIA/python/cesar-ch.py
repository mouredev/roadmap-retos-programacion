# Asignación de variables por valor
a = 10
b = a

a = 5

print(a)  # 5
print(b)  # 10

# Asignación de variables por referencia
x = {"a": 10, "b": 5}
y = x

x["a"] = 12
x["b"] = 24

print(x)  # {'a': 12, 'b': 24}
print(y)  # {'a': 12, 'b': 24}


# Función con parámetro por valor
def cambiar_valor(numero):
    numero = 100
    print(numero)  # 100


numero = 5
cambiar_valor(numero)

print(numero)  # 5


# Función con parámetro por referencia
def cambiar_referencia(objeto):
    objeto["a"] = 100
    print(objeto)  # {'a': 100}


objeto = {"a": 5}
cambiar_referencia(objeto)

print(objeto)  # {'a': 100}


# Ejemplo que intercambia los valores de dos variables por valor
def intercambiar_valores(c, d):
    temp = c
    c = d
    d = temp

    return c, d


# Ejemplo que intercambia los valores de dos variables por referencia
def intercambiar_referencias(obj1, obj2):
    temp = obj1.copy()
    temp2 = obj2.copy()
    temp3 = temp["value"]
    temp["value"] = temp2["value"]
    temp2["value"] = temp3
    return temp, temp2


c = 10
d = 5
objA = {"value": 10}
objB = {"value": 5}

newc, newd = intercambiar_valores(c, d)
print("Valores iniciales:", c, d)  # 10 5
print("Valores por valor:", newc, newd)  # 5 10

newObjA, newObjB = intercambiar_referencias(objA, objB)
print("Valores iniciales:", objA, objB)  # {'value': 10} {'value': 5}
print("Valores por referencia:", newObjA, newObjB)  # {'value': 5} {'value': 10}
