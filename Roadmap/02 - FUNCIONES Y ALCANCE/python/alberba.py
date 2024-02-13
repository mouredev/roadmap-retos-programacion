
# Función básica sin retorno
def funcion_basica():
    pass

# Función básica con retorno
def funcion_basica_con_retorno():
    return 5

# Función con parámetros 
def funcion_con_parametros(string: str, string2:str) -> str:
    return string + string2

def funcion_dentro_de_funcion():
    def inside_function():
        pass

    inside_function()

# Dificultad extra
def extra(string: str, string2: str) -> int:
    count = 0
    for i in range (1, 101):
        salida = ""
        if (i % 3 == 0):
            salida += string
        if (i % 5 == 0):
            salida += string
        if salida == "":
            print(i)
            count += 1
        else:
            print(salida)
    
    return count

print(extra("Hola", "Mundo"))

