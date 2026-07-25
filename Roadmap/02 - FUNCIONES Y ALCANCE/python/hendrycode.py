def hola_Mundo():
    print("Hola mundo!")
    
hola_Mundo()
    
def suma_mas_uno(a,b):
    return a + b + 1

print(suma_mas_uno(10, 20))

def contar(numero):
    for i in range(numero + 1):
        print(i)
contar(10)

def primera_funcion():
    def segunda_funcion():
        print("soy la segunda funcion")

global_variable = "soy una variable global"
def obtener_numeros(a: str, b: str) -> int:
    counter = 0 #soy una varible local
    global_variable
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(a, b)
        elif i % 3 == 0:
            print(a)
        elif i % 5 == 0:
            print(b)
        else:
            counter += 1
    return counter
print(obtener_numeros("fizz", "buzz"))
        

