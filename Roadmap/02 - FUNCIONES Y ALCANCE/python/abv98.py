## CREACION DE FUNCIONES BÁSICAS

# Sin argumentos ni retorno
def mi_funcion_sin_args_ni_retorno() -> None: # Como el tipado de python es bajo el None es opcional
    print("Esta función no tiene argumentos de entrada ni retorno")

print("Se ejecuta función mi_funcion_sin_args_ni_retorno():")
mi_funcion_sin_args_ni_retorno()
print()

# Sin argumentos pero con retorno
def mi_funcion_sin_args_con_retorno():
    return "Esta función no tiene argumentos de entrada pero sí retorno"

print("Se ejecuta función mi_funcion_sin_args_con_retorno():")
print(mi_funcion_sin_args_con_retorno())
print()

# Con argumentos y sin retorno
def mi_funcion_con_args_sin_retorno(cadena):
    print(cadena)

print("Se ejecuta función mi_funcion_con_args_sin_retorno(cadena):")
mi_funcion_con_args_sin_retorno("Esta función tiene argumentos de entrada pero no retorno")
print()

# Con argumentos y con retorno
def mi_funcion_con_args_con_retorno(cadena:str,edad:int): # Se puede indicar el tipo de dato que se debe pasar como argumento
    return cadena, edad

print("Se ejecuta función mi_funcion_con_args_con_retorno(cadena, edad):")
print(mi_funcion_con_args_con_retorno("Esta función tiene dos argumentos de entrada y retono",28))
print()

# Con argumentos con valor por defecto y con retorno
def mi_funcion_args_defecto_retorno(cadena = "Hola mundo",edad = 28):
    return cadena, edad

print('Se ejecuta función mi_funcion_args_defecto_retorno(cadena = "Hola mundo",edad = 28) sin pasarle argumentos:')
print(mi_funcion_args_defecto_retorno())
print('Se vuelve a ejecutar la funcion pasandole solo la edad y un valor diferente al defecto')
print(mi_funcion_args_defecto_retorno(edad = 58))
print()

# Con número variable de argumentos
def mi_funcion_argumentos_variables(*lo_que_sea):
    return lo_que_sea

print('Se ejecuta función mi_funcion_argumentos_variables(*lo_que_sea):')
print(mi_funcion_argumentos_variables("hola",True,5/10,0b1111,0xDD,["a", 78, "45"]))

print("El tipo de cada dato guardado en la tupla es:")
tupla = mi_funcion_argumentos_variables("hola",True,5/10,0b1111,0xDD,["a", 78, "45"])
for elemento in tupla:
    print(f'{elemento} -> {type(elemento)}')
print()

# Con número variable de argumentos con clave
def mi_funcion_argumentos_variables_clave (**lo_que_sea):
    for clave,valor in lo_que_sea.items():
        print(f"{clave} -> {valor}")
        print(type(clave),type(valor))

print("Se ejecuta función mi_funcion_argumentos_variables_clave (**lo_que_sea)")
mi_funcion_argumentos_variables_clave(coche = "Seat", ruedas = 4,color = "rojo")
print()

# Función dentro de función
def mi_funcion_externa(cadena = "Hola"):
    def mi_funcion_interna(cadena):
        print(cadena)
    mi_funcion_interna(cadena)

print('Se ejecuta la función mi_funcion_externa(cadena = "Hola"):')
mi_funcion_externa("Adiós")
print()

# Algunas funciones del sistema (Notar que ya se han empleado varias funciones y métodos sobre la marcha)
print("Se emplean algunas funciones del sistema")
print(len("Abcd"))
print(type({2,4,5.6}))
print("abcd".capitalize(),"\n") # Esto es un método definido en el sistema 


# Por último se practica el concepto de variable global y local
print("Variables globales y locales")
mi_variable = 25 
def mi_funcion_variable(mi_variable) -> int:
    return mi_variable

print(mi_funcion_variable(40),type(mi_funcion_variable(40)))
print(mi_variable)
