# FUNCIONES Y ALCANCE

# Función simple sin retorno
def simpleFunc():
    print("Esto es una función simple")

simpleFunc()

# Función simple con retorno
def simpleReturn():
    return "Esto es una función simple con retorno"
print(simpleReturn())

# Función con un argumento
def funcArg(name):
    print(f"I'm {name}...!")

funcArg("Batman")

# Función con varios argumentos
def funcArguments(name, surname):
    print(f"{name}, {surname}")

funcArguments("Bruce", "Wayne")
funcArguments(name="Bruce", surname="Wayne")

# Función con argumento predeterminado
def defaultArgs(name="Bruce"):
    print(f"Hi, {name}!")

defaultArgs("Batman")
defaultArgs()

# Función con argumentos y return
def returnArgs(greet, name):
    return f"{greet}, {name}!"
print(returnArgs("Hi", "Bruce"))

# Función con retorno de varios valores
def multipleReturn():
    return "Hi", "Batman"
greet, name = multipleReturn()
print(greet)
print(name)

# Función con un número variable de argumentos
def varArgs(*names):
    for name in names:
        print(f"Hi, {name}!")
varArgs("Diana", "Barry", "Clark", "Arthur", "Victor")

# Función con un número de variable de argumentos con keyword
def varKeyArg(**names):
    for key, value in names.items():
        print(f"{value}({key})!")

varKeyArg(
    group="Justice League",
    name = "Barry",
    aka = "Flash",
    status = "Active"
)

# Funciones dentro de funciones
def firstFunc():
    def innerFunc():
        print("Inner function: I'm Batman!")
    innerFunc()
firstFunc()

# Funciones Built-in
print(len("Bruce Wayne"))
print(type(1972))
print("Bruce Wayne".upper())

# Variables locales y globales
globalVar = "Batman"

def im_Batman():
    localVar = "I'm"
    print(f"{localVar}, {globalVar}!")

print(globalVar)

im_Batman()

# EXTRA
def printNumbers(text1, text2) -> int:
    counter = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(text1 + text2)
        elif num % 3 == 0:
            print(text1)
        elif num % 5 == 0:
            print(text2)
        else:
            print(num)
            counter += 1
    return counter

print(printNumbers("Fizz", "Buzz"))
