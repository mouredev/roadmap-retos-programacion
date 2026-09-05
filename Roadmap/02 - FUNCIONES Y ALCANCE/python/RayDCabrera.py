def saludar():
    print("Hola")

def saludar_alguien(nombre):
    print("Hola ", nombre)

def potencia(num,pot):
    resultado = num ** pot
    print("La potencia de: ",num," elevado a: ",pot," es: ", resultado)

def suma(n1,n2):
    resultado = n1 + n2
    return resultado

saludar()
saludar_alguien("mouredev")
potencia(2,2)
print(suma(1,1))

def papa():
    def hijo(saluda):
        return ('Hola '+ saluda)
    return hijo('Raymond')

print(papa())


def calculolista(lista):
    sumar = sum(lista)
    cantidad_elementos = len(lista)
    return sumar, cantidad_elementos

lista = [1,2,2]
print(calculolista(lista))


def cantidad_repeticiones():
    #si la lista dentro de la funcion esta comentado va a utilizar la lista que se encuentra definida afuera de la funcion
    #lista = [2,2,2]
    global lista
    lista = lista + [2] # intentar modificar una lista que esta definida fuera de la funcion va a dar error, ya que al momento de la asignacion = este toma como que la variable es local, para evitar eso necesitamos decirle que queremos usar la de afuera (global lista)
    #lista.append(2)

    cantidad = lista.count(2)
    return cantidad

print(cantidad_repeticiones())

def extra(t1:str, t2:str):
    c = 0
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            print(t1+t2)
        elif i % 5 == 0:
            print(t2)
        elif i % 3 == 0:
            print(t1)
        else:
            print(i)
            c = c + 1
    return c
print(extra("multiplo de 3","multiplo de 5"))
