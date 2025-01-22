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
Función con un parametro y retorno
'''
def return_greet(saludo)
    return "hola, Dani!"

print (return_greet())
