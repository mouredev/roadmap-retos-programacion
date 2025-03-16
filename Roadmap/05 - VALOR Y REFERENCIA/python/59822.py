'''Asignación de variables por valor y por referencia'''
# Referencia significa que si se cambia una variable, la otra también se cambia
# Valor significa que si se cambia una variable, la otra no se cambiará

# Por valor -> primitivos
# int, float, boolean, string, tuple

variable = 19
variable1 = variable
variable1 = 20
print(variable)
print(variable1)

# Por referencia -> Listas
# listas, diccionarios, conjuntos

lista = [10, 20]
lista2 = lista
lista2.append(30) # Cambia la lista original porque es por referencia
print(lista)
print(lista2)


# Tipo de dato por valor

def valor(valor_a: int):
    valor_a = 20
    print(valor_a)

valor(10)

# Tipo de dato por referencia

def referenca(valor : list):
    valor.append(30)
    print(valor)
    
referenca([10, 20])

''' Difficultad extra '''
# 2 parametros por valor
def valores(x, y): 
    z = x
    x = y
    y = z
    return(x, y) # No puede ser print, porque no se puede asignar a una función

valor0 = 10
valor3 = 20
x1, y1 = valores(valor0, valor3)

print(valor0, valor3) # 10, 20
print(x1, y1) # 20, 10

# 2 parametros por referencia
def referencia(x: set, y: set):
    x = y
    y = x
    return x, y

valor1 = {10, 20}
valor2 = {20, 30}

valornew, valornew2 = referencia(valor1, valor2)

print(valor1, valor2) # {10, 20}, {20, 30}
print(valornew, valornew2) # {20, 30}, {20, 30}
    