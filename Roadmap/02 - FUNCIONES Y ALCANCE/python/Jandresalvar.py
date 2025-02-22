# Funciones básicas:

# Sin parámetros ni retorno:
def saludar():
    print('Hola, mundo!')

# Con parámetros y retorno:
def saludar2(nombre):
    return f'Hola, {nombre}'

# Con múltiples parámetros:
def saludar3(nombre, idioma):
    if idioma == 'es':
        (print('Hola,', nombre))
    elif idioma == 'en':
        (print('Hello,', nombre))
    elif idioma == 'pt':
        (print('Olá', nombre))
    elif idioma == 'fr':
        (print('Bonjour', nombre))
    else:
         (print('Idioma no encontrado'))

# Con parámetro predeterminado:
def saludar_python(idioma, nombre = 'Python'):
    if idioma == 'es':
        (print('Hola,', nombre))
    elif idioma == 'en':
        (print('Hello,', nombre))
    elif idioma == 'pt':
        (print('Olá', nombre))
    elif idioma == 'fr':
        (print('Bonjour', nombre))
    else:
         (print('Idioma no encontrado'))

# Funciones dentro de funciones? 😎
    
def teorema_pitagoras(a, b):
    cuadrado = a**2 + b**2
    def raiz(cuadrado):
        return cuadrado ** (1/2)
    return raiz(cuadrado)

# Ejemplos de funciones ya creadas en python:

print(max('Retos de programacion'))
print('Retos de programacion'.count('o'))

# Variables locales y globales:
num1 = 8
def adicion():
    num2 = 16
    return num1 + num2

print(adicion())
print(num1)
# print(num2) # Error porque num2 solo se define en la instancia de la funcion y no se puede acceder a su valor por fuera de esta

# Ejercicio Opcional

def ejercicio_extra(string1, string2):
    
    cuenta = 0

    for num in range(1,101):
        
        if num % 3 == 0 and num % 5 == 0:
            print(f'{string1}{string2}')
        elif num % 3 == 0: 
            print(string1)
        elif num % 5 == 0:
            print(string2)
        else: 
            print(num)
            cuenta+= 1
    
    return cuenta
