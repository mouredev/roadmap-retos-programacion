#funciones basicas

#sin parametros ni retorno
def saludo():
    print("hola, que tal tu dia?")

saludo()

#con parametros
def resta(num1, num2):
    print(num1-num2)
resta(10,9)

def fruts(*args):
    for arg in args:
        print(arg)
fruts("manzana", "pera", "banana")

def datos(**kargs):
    for i, item in kargs.items():
        print(f"{i}: {item}")    
datos(name="Jhon", lastname="Wick", favorite_color="Black")

#con retorno
def producto(num1,num2):
    return num1 * num2
resultado_producto=producto(10,5)
print(f" resultado producto: {resultado_producto}")


#funciones anonimas
calculator = lambda a,b: a * b
resultado1 = calculator(7,8) # 56
resutlado2 = calculator(5,2) # 10
print(resultado1, resutlado2)

#Extra

def mostrar_numeros(param1, param2) -> int:
    count = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(param1 + param2)
        elif i % 3 == 0:
            print(param1)
        elif i % 5 == 0:
            print(param2)
        else:
            print(i)
            count+=1
    return count

print(mostrar_numeros("ping", "pong"))