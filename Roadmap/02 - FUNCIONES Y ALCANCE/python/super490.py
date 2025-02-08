#  Funciones

#  Sin parámetros ni retorno

def saludo():
    print('Hola mundo')
    
saludo()

# Con un parámetros

def dato(nombre):
    print(f'Mi nombre es {nombre}')
    
dato('Manuel')

# Con varios parámetros

def datos(nombre,apellido,edad):
    print(f'Mi nombre y apellido es {nombre} {apellido} y tengo {edad} de edad')
    
datos('Manuel','Morales','28')

# Con retorno

def suma(num1,num2):
    return num1 + num2

resultado = suma(30,20)

print(f'El resultado de la suma es: {resultado}')


def dividir(num1,num2):
    if num2 == 0:
        return 'Error: División por cero'
    return num1 / num2

resultado = dividir(30,2)

print(f'El resultado de la division es: {resultado}')

# funciones dentro de funciones

def resultado_resta(num5,num6):
    
    def resta(num3,num4):
        return num3 - num4

    return resta(num5,num6)

resultado = resultado_resta(30,10)
    
print(resultado)

# funciones ya creadas en el lenguaje

# 1. print()
print("Hola, Python!")

# 2. len()
cadena = "Python"
longitud = len(cadena) 
print(longitud)

# 3. type() 
numero = 10
print(type(numero))

# 4. input()

nombre = input("Ingrese su nombre: ")  
print("Hola,", nombre)

# 5. int()

numero = "10"
numero_entero = int(numero) 
print(numero_entero)

# 6. float()

precio = "99.99"
precio_float = float(precio)
print(precio_float)

# 7. float()

edad = 25
edad_str = str(edad)
print(edad_str)

# 8. abs()

numero = -10
valor_absoluto = abs(numero)
print(valor_absoluto)

# 9. round()

numero = 3.14159
numero_redondeado = round(numero, 2) 

# 10. max(), min()

numeros = [1, 5, 2, 8, 3]
maximo = max(numeros)  
minimo = min(numeros)
print(maximo)
print(minimo)

# 11. sum()

numeros = [1, 2, 3, 4, 5]
suma = sum(numeros)
print(suma)

# Funcion con una variable local

def mi_funcion():
    x = 12
    print(x)

mi_funcion()

# Funcion con una variable global

variable = 'Hola mundo'

def mi_codigo():
    print(variable)

mi_codigo()

print(variable)

# DIFICULTAD EXTRA

def numbers(number_1,number_2):
    count = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print (number_1 + ' '+ number_2)
        elif numero % 3 == 0:
            print(number_1 )
        elif numero % 5 == 0:
            print(number_2)
        else:
            print(numero)
            count += 1
    return count

print(numbers('Number_1', 'Number_2'))