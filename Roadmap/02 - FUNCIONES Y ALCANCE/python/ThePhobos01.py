# Funciones en Python

def funcion():
    print('Hola, funcion!')

funcion() #dfuncion sin parametro

def funcion_parametro(a):
    print(a**2)

funcion_parametro(3)

def funcion_parametros(num1, num2):
    print(num1 + num2)

funcion_parametros(2, 3) #Funcion con varios parametros

def funcion_retorno(b, c):
    return b + c

resultado = funcion_retorno(5, 5)
print(resultado) # Funcion con return

def funcion_anidada(n):
    def division(num):
        if num % 2 == 0:
            return True
        else:
            return False


    if division(n):  
        return n ** 2  
    else:
        return None  

resultado2 = funcion_anidada(10)
print(resultado2)

#Funciones ya creadas en Python (Built-in function)

string = 'Hola mundo!'
print(len(string)) # Dice la longitud de una cadena de texto

print(string) #imprime en consola

'''name = input('Como te llamas') #Pide al usuario insertar un valor
print(f'Tu nombre es {name}')'''

print(type(string)) #Devuelve el tipo de valor de una variable

#Variable global

var_global = "Mi variable global"

print(f'La variable {var_global} puede ser accedida desde cualquier parte del programa')

def mi_funcion():
    var_local = "Mi variable local"
    print(f'Mi variable local puede ser accedida solamente aqui: {var_local}')

mi_funcion()

def imprimir_numeros(texto1, texto2):
    contador_numeros = 0  

    for i in range(1, 101): 
        if i % 3 == 0 and i % 5 == 0:  
            print(texto1 + texto2)  
        elif i % 3 == 0: 
            print(texto1)  
        elif i % 5 == 0:  
            print(texto2)  
        else:  
            print(i)  
            contador_numeros += 1  

    return contador_numeros  

veces_numeros = imprimir_numeros("Fizz", "Buzz")

print(f"Se imprimieron números {veces_numeros} veces.")