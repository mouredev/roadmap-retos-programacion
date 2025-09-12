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

# Función fizz-buzz, por ejemplo, con diccionarios

def fizbuzz(fizz="fizz",buzz="buzz",nf=3,nb=5,max=100) -> int:
    '''
    introduce las cadenas fizz y buzz en las posiciones de una lista de 
    enteros hasta max, donde sean multiplos nf o nb respectivamente
    donde sean multiplos de ambos, concatena fizz+buzz
    devuelve la cantidad de no-cambios
    '''
    max+=1
    d0=dict(zip(range(1,max),[str(i) for i in range(1, max)]))
    d1=dict(zip(range(nf,max,nf),[fizz]*int((max/nf))))
    d2=dict(zip(range(nb,max,nb),[buzz]*int((max/nb))))
    d1.update(d2)
    d2=dict(zip(range(nf*nb,max,nf*nb),[fizz+buzz]*int((max/(nf*nb)))))
    d1.update(d2)
    d0.update(d1)
    for ele in d0:
        print(d0[ele])
    return max-len(d1)-1 # quiza resultase mas interesante devolver el diccionario d0

print(fizbuzz())




            







