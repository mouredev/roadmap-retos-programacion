#Ejercicio

#Función decoradora sin parámetros
def my_decorate(function):
    def wrap_function():
        #Código que añade la función decoradora
        print("Realizando la operación....")
        function()
        print("Operación realizada.")
    return wrap_function

#Función decoradora con parámetros
def show_message(function):
    def add_message(*args):
        #Código que añade la función decoradora
        print("Realizando la operación")
        function(*args)
        print("Operación realizada")
    return add_message

@my_decorate #Añade la función decoradora a la función sum_values
def sum_values():
    print(f"3 + 2 = {3 + 2}")

@show_message #Este decorador tambien funcionaría en una función sin parámetros
def sum_two_values(value1, value2):
    print(f"{value1} + {value2} = {value1 + value2}")

sum_values()
sum_two_values(5, 6)

#Extra

def call_function(function):
    def counter():
        counter.count += 1 
        function()
        print(f"La función {function.__name__} ha sido llamada {counter.count} veces")
    counter.count = 0 #Variable de la función interna
    return counter

@call_function
def greeting():
    print("Hello Python!")

greeting()
greeting()