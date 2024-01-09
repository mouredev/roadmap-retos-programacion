#Python tolera funciones de tipo void (sin return) y con return, no hace falta especificar a diferencia de otros lenguajes
#Además las funciones admiten un número ilimitado de parámetros o ninguno
def sin_retorno(a, b):
    print(a+b)

def con_retorno(c, d):
    return c + d

def sin_parametros():
    print("Esta es una función sin parametros")

def con_parametros(e):
    print("Este es el parametro a imprimir: ", e)

#Se pueden crear funciones dentro de funciones
def funcion_interna():
    def funcion_segunda():
        print("hola")

    funcion_segunda()

#También se pueden crear funciones que se llaman a si mismas, dentro de funciones
def recursiva(g):
    if g != 10:
        g += 1
        print(g)
        recursiva(g)
    else:
        print("final")

#Definición de variable local
def local(w):
    local = 10
    print(w+local)

#Extra
def extra(texto1, texto2):
    for item in range(1, 101):
        if item%3 == 0 and item%5 == 0:
            print(item, texto1, texto2)
        elif item%5 == 0:
            print(item, texto2)
        elif item%3 == 0:
            print(item, texto1)
        else:
            print(item)




if __name__ == "__main__":
    sin_retorno(2,2)
    print(con_retorno(2,2))

    sin_parametros()
    con_parametros("hola")

    funcion_interna()
    recursiva(1)

    #Función propia del lenguaje
    print(len([1,2,3]))

    print(local)
    local(2)

    #Función lambda, sin cabecera
    suma = lambda x, y: x + y

    resultado = suma(3, 5)
    print(resultado)

    extra("uno", "dos")
