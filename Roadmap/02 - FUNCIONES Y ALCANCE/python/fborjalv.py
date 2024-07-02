# FUNCIONES EN PYTHON 

# Funcionaes sin parámetros y sin retorno

def func_no_param_no_return():
    print("Soy una función sin parámetros ni retorno")

# Funciones con un parametro

func_no_param_no_return()

def func_param_no_return(param1, param2):
    print(f"Soy una función con estos parametros: {param1, param2}")

func_param_no_return(354, "string")

def func_param_no_return_tipado(param1: str, param2: int): 
    print(f"Soy una función con estos parametros tipados: {param1, param2}")

func_param_no_return_tipado(354, "string") # Python no impore restricciones  

def func_param_predefinidos(name="Borja", l_name="Laja"):
    print(f"Soy {name} {l_name}")

func_param_predefinidos()
func_param_predefinidos("Brais", "Moure")

# Funciones con varios parámetros

def func_param_varias_variables(*nombres):
    print(nombres)

func_param_varias_variables("Montaña", "Playa", "Campo")

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language="Python",
    name="Borja",
    alias="fborjalv",
    age=32)

# Funciones con retorno

def func_con_retorno(numero, numero_2):
    return numero + numero_2

print(func_con_retorno(2, 3))

# Funciones con varios retornos 

def func_con_varios_retornos(numero, numero_2):
    return numero, numero_2
print(func_con_varios_retornos(4, 6))

# Funciones dentro de funciones 

def func_padre():
    print("soy la función padre")
    def func_hijo():
        print("soy la función hijo")
    func_hijo()

func_padre()

# Variables locales y globales

my_var_global = "Soy una variable global"

def manejo_de_variables():
    my_var_local = "Soy una variable local"
    print(my_var_global)
    print(my_var_local)
    

    def manejo_de_variables_hija(): 
        my_var_local_hija = "Soy variable local hija"
        print(my_var_global)
        print(my_var_local)
        print(my_var_local_hija)

print(my_var_global)
print(manejo_de_variables())

# EJERCICIO EXTRA

def multiplos (text: str, text_2: str):

    contador = 0

    for index in range(1, 101):

        if index % 3 == 0 and index % 5 == 0:
            print(index, text + " " + text_2)
            
        elif index % 3 == 0:
            print(index, text)
            
        elif index % 5 == 0:
            print(index, text_2)
            
        else: 
            print(index)
            contador += 1

    return contador

contador = multiplos("primer", "segundo")
print(f"Números que no son múltiplos ni de 3 ni de 5: {contador}")