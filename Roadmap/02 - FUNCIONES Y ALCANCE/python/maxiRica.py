"""
FUNCIONES BÁSICAS. Se declaran con el termino "def"

Son las funciones creadas por el usuario. Hay del tipo:
1. Sin parámetros ni retorno
2. Con parámetros sin retorno
3. Sin parámetros con retorno
4. Con parámetros y con retorno
5. Recursiva
6. 
"""

# 1. Funciones sin parámetros ni retorno
def Hola():
    print("hola, estoy programando con Python")

print(" ")

# 2. Funciones con parámetros sin retorno
def saludo(name):
    print(name)

# 3. Funciones sin parámetros con retorno
def retorno():
    return print("devolvemos un valor")

# 4. Funciones con parámetros y retorno
def ret_param(valor,porcentaje):
    calculo=valor*porcentaje/100
    return calculo

# 5. Función recursiva
def recursiva(valor):
    if valor == 1:
        return 1
    else:
        return valor * recursiva(valor - 1)


        

# ejercicios aplicando el código escrito

print("# 1. Funciones sin parámetros ni retorno") #1
print("def Hola():\nprint(\"hola, estoy programando con Python\")\n")
Hola()
print("")

maxi ="maxi" #2
print("# 2. Funciones con parámetros sin retorno")
print("def saludo(name):\nprint(name)\n")

saludo(maxi)
print(" ")

print("# 3. Funciones sin parámetros con retorno") #3
print("def retorno():\nreturn print(\"devolvemos un valor\")\n")
retorno() 
print(" ")

print("# 4. Funciones con parámetros y retorno") #4
print("def ret_param(valor,porcentaje):\ncalculo=valor*porcentaje/100\nreturn calculo\n")
print(ret_param(1000,25)) 
print(" ")

print("# 5. Función recursiva\n")
print("def recursiva(valor):\n  if valor == 1:\n      return 1\n  else:\n      return valor * recursiva(valor - 1)\n")
print(recursiva(5))
print(" ")

"""
Vamos a trabajar con variables LOCALES y GLOBALES

Las variables GLOBALES se ejecutaran en todo el código, mientras que las LOCALES
solo se ejecutan dentro de las funciones.

En la gestión de recursos, las variables locales es mucho más efectivo, dado que solo
ocupan con caráter temporal recursos del sistema. Las variables globales al perdurar
mantienen el uso de los recursos.

En un programa bien realizado, se ha de usar el mínimo de variables globales posible.
"""

saludo="Hola a tod@s!!" #variable global

def saludin(valor): #función donde generamos una variable local tipo string
    cortes=valor
    hola="holita a tod@s! " + cortes
    return hola


print(saludin(saludo))


"""
Dificultad extra:

* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
* Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
* Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
* Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
* La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def funcion(string1,string2):
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(f"i({i}): {string1} {string2}")
        elif i%3==0:
            print(f"i({i}): {string1}")
        elif i%5==0:
            print(f"i({i}): {string2}")
    return
        
    
funcion("uno", "dos")