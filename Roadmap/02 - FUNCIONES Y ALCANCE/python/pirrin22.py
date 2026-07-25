# Funcion sin parametros y sin retorno.
def area_cuadrado():
    lado = 6
    print(f'El area de un cuadrado de un lado {lado} metros es {lado*lado}')

area_cuadrado()

# Funcion con un parametro y retorno.
def myname(name):
    name = input('Ingresa tu nombre: ')
    return f'Tu nombre es: {name}'

print(myname(input))

# Funcion con 2 parametros
def area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f'El area del triangulo es: {area}')

area_triangulo(4, 3)

# Funcion con 2 parametros y retorno.
def area_poligono(apotema, perimetro):
    ar_pol = (apotema * perimetro) / 2
    return f'El area del poligono es: {int(ar_pol)}'

print(area_poligono(4, 35))

# Funcion dentro de Funcion.

def user():
    def username(alias):
        alias = input('Ingresa tu alias: ')
        print(f'Este es tu alias {alias}')
    username(input)

user()

# Funciones ya creadas en el lenguaje.-

print(max(5, 7, 18))

print(len('Esto es una cadena de texto'))

x = (5, 7, 9, 16)
print(sum(x))


# Variuable Global dentro de una funcion.

def loc():
    global y
    y = ('Esto es una variable Global!')
    print(y)

loc()
print(y)

# Variable local.

age = 32

def myage(age):
    age = input('Ingresa tu edad: ')
    print(f'Tu edad segun la variable local {age}')

myage(input)

print(f'Tu edad segun la variable global {age}')


# Ejercicio de dificultad extra.

def numeros(texto1, texto2):
    num = 0
    for numero in range(1, 101):
       if numero % 3 == 0 and numero % 5 == 0:
           print(texto1 + texto2)
       elif numero % 3 == 0:
           print(texto1) 
       elif numero % 5 == 0:
           print(texto2) 
       else:
           print(numero) 
           num += 1
    return f'El numero se ha impreso {num} veces.'

print(numeros('fizz', 'buzz'))