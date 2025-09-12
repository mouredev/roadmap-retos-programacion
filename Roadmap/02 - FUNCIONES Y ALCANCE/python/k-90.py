### Función Simple
def my_function():
    print("Hola Mundo!")

my_function()

### Función con Retorno

def function_return():
    return "Hola Mundo!"

print(function_return())

### Función con un argumento

def arg_function(code):
    print(f"Mi codigo es {code}")

arg_function("Python")

### Función con dos argumentos

def arg_function_2(name, surname):
    print(f"Mi nombre es {name} y mi apellido es {surname}.")

arg_function_2("Enrique", "Castro")
arg_function_2(name="Kike",surname="90")

### Función con argumento predeterminado

def fun_prede (name="Kike"):
    print(f"Hola, {name}")

fun_prede("Avelino")
fun_prede()

### Función con argumentos y return

def other_function(number1:int, number2:int):
    number3 = number1 + number2
    return number3
print(other_function(4,5))

### Función con retorno de varios valores

def fun_var_val():
    return "Hola", "Mundo"

my_function, name= fun_var_val()
print(my_function)
print(name)

### Función con numero variable de argumentos

def variable_arg(*languages):
    for language in languages:
        print(f"Mi codigo es {language}")

variable_arg("Python", "Java", "JavaScript","Kotlin")

### Función con numero variable de argumentos con palabra clave

def variable_arg_keys(**languages):
    for key, language in languages.items():
        print(f"Mi codigo es {language} ({key}).")

variable_arg_keys(
    dificil = "Cobol",
    medio = "Python",
    facil = "JavaScript"
)

### Funciones dentro de funciones

def outside():
    def inside():
        print("Hola Mundo")
    inside()
    
outside()

### Funciones del Lenguaje

print(len("Enrique"))
print(type(33))
print("kike".upper())

### Variables Locales y globales

var_global = "Enrique"

def saludo():
    var_local = "Hola"
    print(f"{var_local} {var_global}!")
          
saludo()

### Extra

def ejercicio_extra(text1:str, text2:str) ->int:
    contador = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            contador += 1
    return contador

ejercicio_extra("Fizz","Buzz")
