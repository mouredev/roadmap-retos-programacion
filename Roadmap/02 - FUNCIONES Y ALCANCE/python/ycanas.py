# --------- Funciones

# --- I. Tipos

# 1. Sin parametros y sin retorno

def sin_parametros_sin_retornos():
    print("No recivo valores ni retorno valores.")


# 2. Con parametros y sin retorno
    
def con_parametros_sin_retornos(parametro):
    print(f"Este es mi parametro: {parametro}, pero no retorno nada")


# 3. Sin parametros y con retorno
    
def sin_parametros_con_retorno():
    return "No recivo parametros pero si retorno valores."


# 4. Con parametros y con retorno

def con_parametros_con_retorno(parametro):
    return f"Estoy retornando mi parametro: {parametro}"


# 5. Con varios parametros y retornos

def varios_parametros_varios_retornos(parametro1, parametro2):
    return f"Parametro 1: {parametro1}", f"Parametro 1: {parametro2}"


sin_parametros_sin_retornos()
con_parametros_sin_retornos("Soy un parametro")
sin_parametros_con_retorno()
con_parametros_con_retorno("Soy un parametro")
varios_parametros_varios_retornos("Soy un parametro", "Y yo otro")


# --- II. Función dentro de función

def funcion():
    def funcion2():
        print("Y yo estoy dentro de ti 😈")


    print("Soy una función...")
    funcion2()


# --- III. Funciones creadas dentro del lenguaje
    
a = [x for x in range(100)]
b = len(a)
print(f"Soy la funcion len() y retorno la longitud de un objeto: {b}")


# --------- Variables

# --- I. Globales

variable_global = 5


def vg():
    global variable_global
    variable_global = 0


vg()
print(f"Global: {variable_global}")

# --- II. Locales

variable_local = 5


def vl():
    variable_local = 0
    print(f"Varible local: {variable_local}", end=", ")


vl()
print(f"Variable local: {variable_local}")


# --------- Extra

def extra(str1: str, str2: str) -> int:
    cont = 0

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(str1 + str2)
        
        elif i % 3 == 0:
            print(str1)

        elif i % 5 == 0:
            print(str2)

        else:
            cont = cont + 1
            print(i)

    return cont


extra("uno", "dos")
