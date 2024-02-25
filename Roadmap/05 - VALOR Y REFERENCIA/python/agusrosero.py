# 05 VALOR Y REFERENCIA

# Asignacion de variables por valor
valor1 = 23
valor2 = valor1
valor2 = 10

print(valor1)
print(valor2)

# Asignacion de variables por referencia


def ejemplo1(num):
    for i, n in enumerate(num):
        num[i] *= 2
    return num


mi_lista = [1, 2, 3, 4, 5]
print(ejemplo1(mi_lista))


def ejemplo2(num):
    return num * 2


num = 10
print(ejemplo2(num))

# DIFICULTAD EXTRA


def cambio_por_valor(valor1, valor2):
    temp = valor1
    valor1 = valor2
    valor2 = temp
    return valor1, valor2


a = 10
b = 20
print(cambio_por_valor(a, b))


def cambio_por_referencia(valor1, valor2):
    nuevo_valor = valor1
    nuevo_valor2 = valor2
    return nuevo_valor, nuevo_valor2


x = 30
z = 40
print(cambio_por_referencia(x, z))
