#Funciones con retorno y sin retorno
def hola():
    print('hola')

def hola_con_retorno():
    return 'hola'

print(hola_con_retorno())

#Funcion con varios parametros
n1 = 3
n2 = 6
def sumar_dos(n1,n2):
    return n1 + n2

print(sumar_dos(n1,n2))

#Funciones dentro de funciones
def sumar_funciones():
    x = 0
    def sumar1(x):
        return x + 1
    def sumar2(x):
        return x + 2
    return (sumar1(x) + sumar2(x))

print(sumar_funciones())

#Global y Local
x = 35
z = 25

def global_local():
    global x
    x = 0
    z = 0


print('x:',x ,'z:', z)
global_local()
print('x:',x ,'z:', z)

#Funcion de Python
lista = [i for i in range(1, 51)]
mapa = filter(lambda x: x% 2 == 0, lista)
print(list(mapa))


def extra(str1,str2):
    count = 0
    for i in range(1,101):
        print(i)
        if i % 15 == 0:
            count +=1
            print(str1,str2)
        elif i % 3 == 0:
            count +=1
            print(str1)
        elif i % 5 == 0:
            count +=1
            print(str2)
    return count

times = extra('xd','uwu')
print('veces' , times)