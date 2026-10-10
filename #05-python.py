#por valor

my_variable_a = "Hola"
my_variable_b = "Mundo"
print(my_variable_a, my_variable_b)
my_variable_a = my_variable_b
print(my_variable_a, my_variable_b)

#por referencia
my_variable_a = list(["Hola", "Python"])
my_variable_b = list(["Mundo", "Cruel"])
print(my_variable_a, my_variable_b)
my_variable_c = my_variable_a.copy()
my_variable_b.append("Malo")
print(my_variable_c, my_variable_b)

#por referencia enteros
my_int_a = [10, 20]
my_int_b = [20, 30]
print(my_int_a, my_int_b)
my_int_b.append(40)
my_int_c = my_int_b
print(my_int_a, my_int_c)

#funciones por valor

def por_valor(my_variable):
    my_variable = "Hola Mundo"
    return my_variable

variable = "Hola"
print(variable)
variable = por_valor(variable)
print(variable)

#funciones por referencia

def por_referencia(my_variable):
    my_variable.append("Hola Mundo")
    return my_variable

variable = list(["Hola"])
print(variable)
variable = por_referencia(variable)
print(variable)

#intercambiar valores por valor

def intercambiar_por_valor(a, b):
    a, b = b, a
    return a, b

x = 5
y = 10
print(x, y)
x, y = intercambiar_por_valor(x, y)
print(x, y) 

#intercambiar valores por referencia

def intercambiar_por_referencia(a:list, b:list) ->tuple:
    a, b = b, a
    a.append(20)
    return a, b

x = [5, 10]
y = [10, 15]
print(x, y)
x.remove(x[0])
x, y = intercambiar_por_referencia(x, y)
x.append(40)
print(x, y) 