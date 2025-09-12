#Funcion sin parametros ni retorno
def funcion1 ():
    var="Una variable en la funcion"
    var2=3

funcion1()

#Funcion con parametros y retorno
def funcion2 (num1,num2):
    return num1+num2

print(funcion2(6,3))

#Funciones integradas en el lenguaje:
print("El print es una funcion de Python")

a="El len() también lo es"
print(len(a))

#Existen tambien las funciones lambda, que son funciones anónimas pequeñas
multiplicacion=lambda a,b,c : a*b*c
print(multiplicacion(10,3,5))
#Tambien se pueden declarar y llamar en la misma linea
print((lambda var1,var2 : var1**var2)(2,3))

#EXTRA
def ej_extra(a,b):
    for i in range(1,101):
        if not i%3 and not i%5:
            print(a,b)
        elif not i%3:
            print(a)
        elif not i%5:
            print(b)
        else:
            print(i)

ej_extra("pen","pineapple")