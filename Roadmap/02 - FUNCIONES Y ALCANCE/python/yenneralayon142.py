"""
Funciiones definidas por el usuario
"""

# Simple

def simple():
    print("Hola mundo")


# Con retorno
    
def retorno():
    return "Hola,Python"


# Con parametro

def parametro(futbol):
    print(f"Hola,{futbol}")

parametro("Cristiano")


# Con parametros
def parametros(champions,messi):
    print(f"{champions} tiene {messi}")

parametros(0,"messi")
parametros(champions="messi",messi=0)


# Con parametros predeterminados

def predeterminados(adverbio="no"):
    print(f"{adverbio}, usar python")


# Con argumentos y return 
    
def argumento(casa,cosa):
    return f"{casa},{cosa}"
print(argumento("Hola" , "Yenner"))


# Con un número varible de argumentos

def variable(*names):
    for name in names:
        print(f"hola, {name}")

variable("Gonzalo", "David", "Antonio")


# Con un número variable de argumentos con palabra clave

def palabrasclave(**names):
        for key, value in names.items():
            print(f"{value} ({key})!")


palabrasclave(
    language="Español",
    name="Millos",
    alias="El más grande",
    age=20
)


"""
Funciones dentro de Funciones

"""

def funcionExterna():
    def funcionInterna():
        print("Hola a todos soy una función interna")
    funcionInterna
funcionExterna()


"""

Variables locales y globales

"""

global_var = "Xolo"

def outside():
    local_var = "Milloz"
    print(f"{global_var},{local_var}")

# No se puede acceder a local var desde fuera de la función
    
def fizzbuzz(text1,text2) -> int:

    count = 0

    for i in range(1,101):
        if i % 3 == 0 and  i % 5 == 0:
            print(text1 + text2)
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            count += 1
    return count

print(fizzbuzz("fizz","Buzz"))
