'''
Función sin parametros
'''
def greet():
    print ("Hello")
greet()

'''
Función con un parametro
'''
def greet_with_name(name):
    print ("Hello", name)
greet_with_name("Dani")

'''
Función con varios parametros
'''
def greet_with_surname(name, surname):
    print (f"Hello, {name} {surname}")

greet_with_surname("Dani", "Rojas")
greet_with_surname(name="Brais", surname="Moure")

'''
Función con un parametro por defecto
'''
# Si le damos un nuevo argumento lo coge, sino muestra el de por defecto
def default_greet_with_name(name="Paco"):
    print ("Hello", name)

default_greet_with_name("Manolo")
default_greet_with_name()

'''
Función con retorno
'''
def return_greet(): # Cuando se llama a esta función nos retorna lo que le indiquemos con el return, eso lo podemos utilizar para lo que queramos por ejemplo un print
    return "hola, Dani!"

print (return_greet())

'''
Función con retorno y argumentos
'''
def return_greet(name, surname): # Igual que la anterior pero dándole nosotros los argumentos
    return f"{name}, {surname}!"

print (return_greet("Hola", "Brais"))

'''
Función con argumentos de longitud variable
'''
def variable_greet (*numbers): # Con el * hacemos que se cree una tupla
    for n in numbers:
        print (f"Numbers is, {n}")

variable_greet (1, 2, 3, 4, 5, 6)

'''
Función con argumentos de longitud variable y palabra clave
'''
def variable_greet_key (**numbers): # con ** conseguimos tener como entrada a parte del valor una lista de elementos clave
    for key, n in numbers.items(): # key par la palbra clave, .items() para iterar los valores
        print (f"{key}, ({n})")

variable_greet_key (one=1, two=2, three=3, four=4, five=5, six=6)

'''
Función dentro de función
'''
def exterior_function ():
    print ("Llamo a la función exterior")
    def interior_function ():
        print ("Esto es la función interior")
    interior_function()

exterior_function()

'''
Funciones del lenguaje
'''
str="print: Imprime por consola"
print(str) # Imprime por consola
print(type(str)) # Nos indica el tipo de variable que le hayamos metido
print(len(str)) # Cuenta el número de caracteres de un string
new_str=str.replace("consola","terminal") # Reemplaza la palabra de la izquierda por la de la derecha
print(f"Se cambia 'consola' por 'terminal', {new_str}")

'''
Variables locales y globales
'''
global_varible="esto es una variable global" # Se puede acceder desde todo el código

def show_local_variable():
    local_variable="esto es una variable local"
    print(local_variable)


print(global_varible)
#print(local_variable) no se puede hacer porque estamos fuera de la función
show_local_variable() #Llamamos a la función para imprimir por consola local_variable

'''
Extra
'''
def print_numbers(str_1, str_2):
    c=0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(str_1,str_2)
        elif num % 3 == 0:
            print(str_1)
        elif num % 5 == 0:
            print(str_2)
        else:
            print(num)
            c+=1
    return c
        
print(print_numbers("Múltiplo de 3", "Múltiplo de 5"))

