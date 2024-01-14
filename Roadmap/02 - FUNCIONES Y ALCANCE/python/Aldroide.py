# Función sin parametros ni retorno
def funcion():
    print(3+4)


funcion()

# Función con parametro sin retorno


def funcion(A):
    print(A)


funcion("Esta es una función con parametro")

# Función con parametros y con retorno


def funcion(A):
    return (A+1)


B = funcion(3)
print(f"Esta función regreso un {B}")

# Funciones dentro de Funciones


def Funcion(A):
    print("Primera función")

    def función(B):
        print(f"Este es el parametro de la primer función {B}")
    función(A)


Funcion("45")

# Funciones lambda


def x(a, b): return a + b  # Función lambda que multiplica dos números


print(x(9, 6))

# funciones propias del lenguaje
A = sum([4, 6, 7, 8, 0, 5, 16, 9])
print(f"Suma de un arreglo usando la función sum() {A}")
A = pow(4, 2)
print(f"Elevar un numero a una potencia pow(a,b) {A}")
A = min([4, 6, 7, 8, 0, 5, 16, 9])
print(f"Minimo numero de un arreglo usando función min() {A}")
A = max([4, 6, 7, 8, 0, 5, 16, 9])
print(f"Maximo número de un arreglo usando la función max() {A}")

# Variables locales y globales
G = "yo soy una variable global"


def funcion():
    L = "soy una variable local"
    print(L)
    print(G)


funcion()

# Ejercicio de dificultad extra
def funcion_final(a, b):
    cont = 0
    for i in range(1, 101):
        if i%3==0 and i%5==0:
            print(a+b)
        elif i%3 ==0:
            print(a)
        elif i%5==0:
            print(b)
        
        else:
            cont +=1
    return cont


resultado = funcion_final("Hello", " word")
print(f"Número que se ha impreso el número : {resultado}")
