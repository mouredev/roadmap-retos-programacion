# 02 Funciones y Alcance

#Funciones sin parametros ni retorno
def noParFun():
    print("Saludos mi gente")

noParFun()

#Funciones uno o varios parametros y retorno
def potNum(num1,num2):
    return pow(num1,num2)  #Aqui utilizamos una funcion predimentada, la cual genera una potencia acorde dos numeros dados.

#Dentro de funciones podemos invocar otras funciones
def listpow(lista,pot):
    listpot = []
    for x in lista:
        listpot.append(potNum(x,pot))
    return listpot

print(listpow([1,2,3,4,5],5))

'''En Python existe un tipo de funciones nombradas "High Functions" en las cuales podemos manejar otras funciones de 'baja'
    jerarquia
'''

# En una alta funcion, podemos ingresar otra funcion como parametro, y a su vez que nos regrese una funcion como retorno.
def altaFunc(f,param):
    ret = []
    return f(param)  # Nota, al invocarlas es importante tener conocimiento sobre los parametros con los que trabaja la funcion

def funSencilla(nombre):
    return "Hola {}!".format(nombre)

print(altaFunc(funSencilla,"Python"))

# Dentro de una funcion no solo podemos invocar otra funcion, si no tambien podemos crear nuevas funciones

def sumMulti(n,m):
    x = 0
    def multipl(n):  # Definimos una funcion dentro de la alta funcion
        return n*m
    for i in range(n):
        x = x + multipl(i) 
    return x

print(sumMulti(5,7))

def funcReto(par1,par2):
    for i in range(100):
        if i%3 == 0 and i%5 == 0:
            print("{} {}".format(par1, par2))
        elif i%3 == 0:
            print(par1)
        elif i%5 == 0:
            print(par2)
        else: print(i)

print(funcReto("Hola","Python"))