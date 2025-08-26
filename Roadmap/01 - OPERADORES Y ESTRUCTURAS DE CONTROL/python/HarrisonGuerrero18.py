# Operadores

print("Bienvenido al pequeño menú de para realizar operaciones aritméticas en Python")

print('''
Estas son las operaciones disponibles: 
1) Suma
2) Resta
3) Multiplicación
4) División
5) Exponenciación
6) Módulo/Residuo
''')

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return int(valor) if valor % 1 == 0  else valor
        except ValueError:
            print("Error: debes ingresar un número válido.")

def dividir(num1, num2):
    if num2 == 0:
        return "Error. No se puede dividir entre 0"
    if num1 % 1 == 0 and num2 % 1 == 0:
        if num1 % 2 == 0 or num2 % 2 == 0:
            return num1 // num2
        else:
            return num1 // num2
    else:
        return num1 / num2
    

def exponenciar(num1, num2):
    return num1**num2

def modular(num1, num2):
    return num1 % num2

try:
    opcion = int(input("Ingresa el numero correspondiente a tu elección: "))
except ValueError:
    print("Debes ingresar un número válido")

match opcion:
    case 1:
        x = int(input("Digita un número: "))
        y = int(input("Digita otro número: "))
        print(f'El resultado de la suma entre {x} y {y} es: {sumar(x,y)}')
    case 2: 
        x = int(input("Digita un número: "))
        y = int(input("Digita otro número: "))
        print(f'El resultado de la resta entre {x} y {y} es: {restar(x,y)}')
    case 3:
        x = int(input("Digita un número: "))
        y = int(input("Digita otro número: "))
        print(f'El resultado de multiplicar {x} x {y} es: {multiplicar(x,y)}')
    case 4:
        x = pedir_numero("Digita un número: ")
        y = pedir_numero("Digita otro número: ")
        resultado = dividir(x,y)
        print(f"El resultado de la división entre {x} y {y} es: {resultado if resultado % 1 != 0 else int(resultado)}")
    case 5:
        x = int(input("Digita un número: "))
        y = int(input("Digita otro número: "))
        print(f'El resultado de exponer {x} sobre {y} es: {exponenciar(x,y)}')
    case 6:
        x = int(input("Digita un número: "))
        y = int(input("Digita otro número: "))
        print(f'El residuo que queda al dividir {x} entre {y} es: {modular(x,y)}')  
    case _:
        print("Digitaste un valor incorrecto. Rango:1-6")
        
# Operadores de comparación

print("Operadores de comparación: tendrás que ingresar 2 números para compararlos")

def pedir_numeros(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError as e:
            print(f"Error: Debes ingresar un número válido. Por favor, inténtalo de nuevo. Detalle: {e}")
        
def comparar_numeros (num1, num2):
    if num1>num2:
        return f"{num1} es mayor que {num2}"
    elif num1 < num2:
        return f"{num1} es menor que {num2}"
    elif x == y:
        return f"{num1} y {num2} son el mismo número"

x = pedir_numeros("Ingresa un número: ")
y = pedir_numeros("Ingresa otro número: ")

print(comparar_numeros(x,y))

# Operadores lógicos

print("Operadores lógicos. Aquí tendrás que escribir verdadero o falso segun la comparación")

def obtener_operaciones():
    caso_uno = 5 > 2 and not 10 > 5
    caso_dos = 3 == 2 or 6 > 3
    caso_tres = 10 % 2 == 0 and not 10 % 2 == 5 / 5
    caso_cuatro = 4**4 >= 125 or 56 / 8 <= 7 and 12 / 6 + 5 * 3 >= 18 or not 5 * 12 / 2 + 8 == 6 ** 3 - 526 / 2
    caso_cinco = not 25 / 5 ** 3 + 6 == 16 * 4 / 2 - 100 or 32 * 2 / 8 ** 2 + 140 == 50 * 6 + 15 / 5 ** 4 and not 268 / 14 + 22 * 7 ** 2 - 19 == 1998 / 6 + 3 * 12 - 4 ** 3
    
    return [caso_uno, caso_dos, caso_tres, caso_cuatro, caso_cinco]

def evaluar_operaciones(operaciones):
    resultados = []
    for i, resultado in enumerate(operaciones, start=1):
        respuesta = input(f"¿Es verdadero o falso el caso {i}: {resultado}? ")
        resultados.append((i, respuesta.lower() == "verdadero"))
    return resultados
