 ### RETO #02 FUNCIONES Y ALCANCE

"""
 Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
 Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
"""
# Función vacía
def vacio():
    pass
vacio()

# Función sin parámetros
def sinpa():
    print("Esta función no tiene parámetros")
sinpa() 

# Función con un parámetro
def saludo(nombre):
    print(f"Hola {nombre}! Días buenos tenga usted")
saludo("Cris")

# Función con varios parámetros
def potencia(a,b):
    x = a**b
    print(x)
potencia(3,3)

# Función con parámetro por defecto
def area_circulo(r,pi=3.14):
    area = pi*(r**2)
    print(area)
area_circulo(1)

# Función con tuplas de argumentos variables
def producto(*args):
    x = 1
    for i in args:
        x *= i
    print(x)

producto(2,3,4,5)

# Función con diccionarios de argumentos variables 
def estadisticas_temperaturas(*temps, **kwargs):
    media = sum(temps)/len(temps)
    suma = sum((i - media)**2 for i in temps)
    devstd = (suma/(len(temps)-1))**0.5
    if kwargs.get('promedio'):
        print(f"El promedio de las temperaturas es {media} grados")
    if kwargs.get('desviacion'):
        print(f"El desviación estándar de las temperaturas es {round(devstd,3)} grados")

estadisticas_temperaturas(1,2,3,4,5,6,promedio=True,desviacion=True)

# Funcion que retorna un valor

def multiplicar(a,b):
    return a*b

print(multiplicar(2,3))

# Funcion que retorne varios valores
def ops_basicas(a,b):
    suma = a+b
    resta = a - b
    multiplicacion = a * b
    division = a/b
    return suma, resta, multiplicacion, division

print(ops_basicas(2,3))

# Funcion anónimas con un argumento
squared = lambda x : x**2
print(squared(2))

# Funcion anónimas con varios argumentos
divided = lambda x,y : x/y
print(divided(2,3))

# Funcion anidada
def conversor_temps(t,**kwargs):
    def celconv(c):
        cel2far = ((9/5)*c) + 32
        cel2kel = c + 273.15
        return cel2far,cel2kel
    def farconv(c):
        far2cel = (c-32)*(5/9)
        far2kel = ((c-32)*(5/9))+273.15
        return far2cel,far2kel
    def kelconv(c):
        kel2cel = c - 273.15
        kel2far = ((c - 273.15)*(9/5))+32
        return kel2cel,kel2far
    if kwargs.get('celcius'):
        far, kel = celconv(t)
        print(f"{t}°C son igual a {round(far,2)}°F y {round(kel,2)}K")
        return far, kel

    if kwargs.get('farenh'):
        cel, kel = farconv(t)
        print(f"{t}°F son igual a {round(cel,2)}°C y {round(kel,2)}K")
        return cel, kel

    if kwargs.get('kelvin'):
        cel, far = kelconv(t)
        print(f"{t}K son igual a {round(cel,2)}°C y {round(far,2)}°F")
        return cel, far

conversor_temps(4,celcius=True)
conversor_temps(4,farenh=True)
conversor_temps(4,kelvin=True)

## Funciones predefinidas

print(f"len() muestra el largo de los datos: Paralelepipedo = {len('paralelepipedo')}")
print(f"int() convierte a enteros por ejemplo 5.0 = {int(5.0)}, '10' = {int('10')} ")
print(f"min() y max() muestran los valores máximos y mínimos de una lista... [1,2,3,4,5,6,7,8,9] => min = {min([1,2,3,4,5,6,7,8,9])}; max = {max([1,2,3,4,5,6,7,8,9])}")
print(f"""
map() sirve para aplicar una función a cada ítem de un iterable (por ejemplo, una lista) y retorna un obejto map
por ejemplo, la conversión de la siguiente lista de °C a °F: [1,2,3,4,5,6,7,8,9,10] : """, list(map(lambda x : (x*9/5)+32,[1,2,3,4,5,6,7,8,9,10])))

## Alcance / scope

# Variable local

def localvar(c):
    x = c
    return print(x)

localvar("Este es un ejemplo de variable local")

# Variable global

k = "Variable global inicial"
print (k)

def modglobal(c):
    global k
    k = c
    return print(k)

modglobal("Este print ha modificado la variable global")

## EXTRA

"""
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
def charnums(str1,str2):
    counter = 0
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(str1+" "+str2)
        elif i%3==0:
            print(str1)
        elif i%5==0:
            print(str2)
        else:
            print(i)
            counter +=1
    return counter

resultado = charnums("texto de prueba 1", "texto 2")
print(f"Se imprimió {resultado} veces el número")