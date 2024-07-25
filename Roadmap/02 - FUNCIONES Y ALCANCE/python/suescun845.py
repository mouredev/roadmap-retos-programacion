### Ejercicio ###

def hola(): #Sin parámetros ni retornos#
    print("Hola")

def suma(a,b): # Con parámetros sin retorno
    print(a+b) 

def resta(a,b): # Con parámetros y con retorno
    return a-b

def perro(): # Sin parámetros y con retorno
    return "guau"

def superfuncion(): #Función dentro de otra función
    def division(a,b):
        return a/b

    def multiplicacion(a,b):
        return a*b
    
    return division(5,6),multiplicacion(3,5)

hola()
suma(12,45)
print(resta(12,789))
print(perro())
print(superfuncion())

list =[2, 6, 4, 23, 67, 0]
string = "programación con python"
print(len("Hola Moure")) #Cuenta los caracteres
print(sorted(list)) #Ordena los caracteres
print(string.upper())# Coloca todos los caracteres en Mayúsculas
print(string.title())# Coloca todos los primeros caracteres de cada palabra en Mayusculas

### Variable Local y Global ###

global_Variable = "Soy Global" # Se puede usar en cualquier parte del código

def variables():
    local_Variable = "Soy Local"
    print(local_Variable)
    print(local_Variable, global_Variable)

variables()
try:
    print(global_Variable) 
    print(local_variable)
except:
    print("No se puede imprimir una variable local de una función")

### Extra ###
cadena1 = str(input("Digite una cadena de texto que se digite cuando el valor sea múltiplo de 3: "))
cadena2 = str(input("Digite una cadena de texto que se digite cuando el valor sea múltiplo de 5: "))

def extra(parametro1, parametro2):
    cuenta = 0
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0 :
            print(parametro1 + parametro2)
        elif i % 3 == 0:
            print(parametro1)
        elif i % 5 == 0:
            print(parametro2)
        else:
            print(i)
            cuenta += 1
    return cuenta

print(f"La cantidad de veces que apareció un numero en vez de texto fueron: {extra(cadena1,cadena2)}")
