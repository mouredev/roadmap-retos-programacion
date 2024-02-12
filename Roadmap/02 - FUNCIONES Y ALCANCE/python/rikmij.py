import colorama

color_green = colorama.Fore.GREEN
color_blue = colorama.Fore.BLUE
color_grey = colorama.Fore.BLACK
color_red = colorama.Fore.RED
end_color = colorama.Fore.RESET

print(color_grey,'\n--> Función sin parámetros ni retorno:', end_color)
def funcion_1():
    print("Hola, soy una función sin parametros ni retorno")

funcion_1()


print(color_grey, '\n--> Función con 1 parámetro:', end_color)
def funcion_2(text):
    print(text)

funcion_2("Hola, soy una función con 1 parámetro")


print(color_grey, '\n--> Función con varios parámetros:', end_color)
def funcion_3(*args):
    print(f"Hola, soy {args[0]} y tengo {args[1]} años. Quiero decir:\n{args[2]}")

funcion_3("Rick", 26, "Graaande MoureDev!!")


print(color_grey, '\n--> Función con retorno:', end_color)
def funcion_4(a, b):
    return a+b

funcion_4(3,3)  #no imprime
print(funcion_4(2,3))   #sí imprime


print(color_grey, '\n--> Función anónima / Función lambda:', end_color)
saludo = (lambda a: f"Soy una función lambda, {a}")
print(saludo("el argumento"))


print(color_grey, '\n--> Función recursiva:', end_color)
def funcion_5(num):
    if num == 0:
        return 1
    else:
        return num * funcion_5(num-1)

print(funcion_5(5))


print(color_grey, '\n--> Función generadora:', end_color)
def funcion_6(num):
    while num < 9:
        num = num+1
        yield num

'''n = funcion_6(3)
print(next(n))
print(next(n))'''   #con esto elijo imprimir 2 valores

for n in funcion_6(3):
    print(n)


print(color_grey, '\n--> Función decoradora:', end_color)
def decor(funcion):
    def decora_funct(a,b):
        print("El resultado es:")
        funcion(a,b)
        print("Ya está")
    return decora_funct

@decor
def suma(a,b):
    print(a+b)

suma(2,3)


print(color_blue, '\n--> Sí se puedes crear funciones dentro de funciones, se llaman "funciones anidadas":', end_color)
def numeros(num):
    
    def suma():
        return num + 3
    
    def resta():
        return num - 2
    
    def multip():
        return num * 3
    
    #podríamos hacer un return de cualquiera y funcionaría, pero encadenemos 2

    def div():
        return multip()/2
    
    return div()

print(numeros(4))


print(color_green, '\n--> Uso de Variables Globales y Locales:', end_color)
name = "Brais"

def presentation():
    name = "Rick"
    age = 26

    return(f"Hola, soy {name} y tengo {age} años")

print(name) #funciona, es una variable GLOBAL (está fuera de la función y se puede usar donde se quiera)
#print(age) da error, es una variable LOCAL (dentro de la función)

print(presentation())


print(color_blue, '\n--> Función del sistema:', end_color)
nums = [21, 33, 9]

print(max(nums))    #tanto print() como max() son funciones del sistema


print(color_red,'\n','*'*13, "EXTRA", '*'*13, end_color)
def extra():
    t1 = "Py"
    t2 = "Thon"
    contador_nums = 0
    contador_t1 = 0
    contador_t2 = 0
    contador_t12 = 0

    for n in range(1,101):
        if n%3 == 0 and n%5 == 0:
            print(t1,"+",t2)
            contador_t12 +=1
    
        elif n%3 == 0:
            print(t1)
            contador_t1 +=1
    
        elif n%5 == 0:
            print(t2)
            contador_t2 +=1
        
        else:
            print(n)
            contador_nums +=1
    
    return(f"--> Hay en total '{contador_nums} números', '{contador_t1} Py', '{contador_t2} Thon' y '{contador_t12} PyThon'")

print(extra())
