## funciones definidas por el usuairo

def my_function ():
    print("esta funcion solo imprime por consola")
my_function ()

##función con retorno

def my_return_function ():
    return "no me sale el ejercicio"
    
#variable_con_retorno = my_return_function ()
#print(variable_con_retorno)
print(my_return_function())

### función con argumento 

def my_argument_function (name, surname):
    print(f"{name} {surname}")
my_argument_function("jorge", "adamowicz")

### función con argumento por defecto

def my_default_argument_function (name, surname, alias = "Chorch"): #argumento predefinido para "alias"
    print (f"{name} {surname} {alias}")
my_default_argument_function( "jorge", "adamowicz")
my_default_argument_function( "jorge", "adamowicz", "chorch")

### función con argumento posicional

def my_argument_function (name, surname):
    print(f"{name} {surname}")
my_argument_function(surname = "adamowicz", name="jorge")

#funciones dentro de funciones

def outer_function ():
    def inner_function():
        print("esto si no lo sabia!")
    inner_function()
outer_function()

###funciones dentro del lenguaje (bult- in)

print(len("jroge adamowicz"))
print(type("chorch"))

## variable global
my_global_var_name = "jorge"
my_global_var_surname = "adamowicz"

def imprimir_nombre_completo():
    # Acceder a las variables globales dentro de la función
    global my_global_var_name, my_global_var_surname
    print(my_global_var_name, my_global_var_surname)

imprimir_nombre_completo()

### variable local

def imprimir_nombre_completo():
   
    my_local_var_name = "jorge"
    my_local_var_surname = "adamowicz"
    print(f"{my_local_var_name}, {my_local_var_surname}")

imprimir_nombre_completo()

#print(my_local_var_name)# no tendrá acceso y dará NameError 'my_local_var_name' is not defined


### Extra ###
def my_extra_function (parameter_1, parameter_2):
    counter = 0
    multiplo_de_tres = 0
    multiplo_de_cinco = 0

    for number in range (1,101):
        if number % 3 == 0 and number % 5 == 0:
            counter += 1
            
        
        elif number % 3 == 0:
            multiplo_de_tres += 1
            
        
        elif number % 5 == 0:
            multiplo_de_cinco += 1
            
    return (f" {parameter_1}, y {parameter_2}, {counter}", f"{parameter_1}, {multiplo_de_tres}", f"{parameter_2}, {multiplo_de_cinco}")
 

print(my_extra_function ("multiplo de tres " , "multiplo de cinco "))
"""
#cuando vi el video, me di cuenta de que habia entendido mal la premisa. de todas maneras haber podido resolver
esto fue genial. soy muy principiante en la programación y ademas un poco entrado en años. a continuación voy a 
intentar resolverlo ya que el retp de "fizz, buzz" ya lo he resulto en otro momento.
"""

def my_extra_function (parameter_1, parameter_2):
    counter = 0
    
    for number in range (1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(parameter_1 + parameter_2)
            
        
        elif number % 3 == 0:
            print(parameter_1)
            
        
        elif number % 5 == 0:
            print(parameter_2)
        else:
            print(number)
            counter += 1
            
    return f"se ha impreso {counter} veces"
 

print (my_extra_function ("multiplo de tres " , "multiplo de cinco "))

  
