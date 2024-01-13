# #02 FUNCIONES Y ALCANCE

# sin parámeros
def fun() -> None:
    print("¿quien eres?")

fun()

#con un parámetro
def fun(nom) -> None:
    print(f"Hola {nom}")

fun("Pepe")

#con un parámetro por defecto
def fun(nom="Brais") -> None:
    print(f"Hola {nom}")

fun()

#con mas parámetros
def fun(n,nom) -> None:
    print(f"Hola {nom}\n"*n)

fun(5,"Pepe")

#con n parámetros
def fun(*nombres) -> None:
    for nom in nombres:
        print(f"Hola {nom}")

fun("Carlos","Pepe")

#devuelve un parámetro
def fun() -> str:
    return "¿quien eres?"

print(fun())

#entran n parámetros y devuelve n parámetros
def reversa(*cosas) -> tuple:
    cosas=list(cosas)
    rev=[]
    for i in range(len(cosas)):
        rev.append(cosas.pop())
    return rev

a,b,c=reversa(1,2,3)
print(a,b,c)


# funciones dentro de funciones y entorno de variables
nombre="Ataulfo"
def imprimehola() -> None:
    def nombre()-> None:
        if nombre =="Ataulfo":
            print("¿Que haces aqui, Ataulfo? ¡no perteneces a este entorno¡")
        else :
            print("Brais!")
    print("¡Hola ", end="")
    nombre()

imprimehola()

nombre="Ataulfo"
def imprimehola()-> None:
    def nombre()-> None:
        global nombre
        if nombre =="Ataulfo":
            print("¿Que haces aqui, Ataulfo? ¡no perteneces a este entorno!?")
        else :
            print("Brais!")
    print("¡Hola ", end="")
    nombre()

imprimehola()




            







