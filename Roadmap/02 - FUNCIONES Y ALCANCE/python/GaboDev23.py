''' 
- Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
'''
# Funciones sin parámetros, ni retorno
def sinParametrosSinRetorno():
    print('Esto es una función sin parámetros, ni retorno')
    
sinParametrosSinRetorno()

# Funciones con parámetros y sin retorno
def conParametrosSinRetorno(text):
    print(text)
    
conParametrosSinRetorno('Esto es una función con parámetros y sin retorno')

# Funciones sin parámetros y con retorno
def sinParametrosConRetrno():
    return 'Esto es una función sin parámetros y con retorno'

print(sinParametrosConRetrno())

# Funciones con parámetros y con retorno
def conParametrosConRetorno(text = 'Esto es un texto por defecto'):
    return text

# Función con parámetro por defecto
print(conParametrosConRetorno('Esto es una función con parámetros y con retorno'))
print(conParametrosConRetorno())

# Función con más de un parámetro
def saludo (nombre = 'Joe', saludo = 'hi'):
    return f'{saludo} {nombre}'

print(saludo('Gabriel', 'Hola'))
print(saludo())

# Función con número indefinido de parámetros
def numeros (*numeros):
    return numeros

print(numeros(2, 4, 6, 8, 10))

''' 
- Comprueba si puedes crear funciones dentro de funciones. 
'''

def funcion ():
    def funcion_dentro_otra ():
        return 'Si se puede jaja'
    
    return funcion_dentro_otra();
    
print(funcion())

''' - Utiliza algún ejemplo de funciones ya creadas en el lenguaje. '''

# print() es una función de python
print('Imprimo algo')

# Valor absoluto de un número
print(f'El valor absoluto de -1 es {abs(-1)}')

texto = 'Hola que tal me llamo Gabriel'

# Tamaño de un texto
print(f'El tamaño del texto: "{texto}" es de {len(texto)} carácteres')

# Tipo de una variable
print(f'El tipo de la variable con el valor: "{texto}" es {type(texto)}')

# Texto en mayúscula
print(f'Ahora si imprimimos ese texto en mayúsculas quedaría: "{texto.upper()}"')

'''
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
'''
var_global = 29 # Variable global, se puede acceder en cualquier parte del programa

def funcion ():
    var_local = 31 # Variable local, se puede acceder solo en esta función
    print(var_local) # Se imprime correctamente
    
print(var_global) # Se imprime correctamente
funcion()
# print(var_local) # Ocurre un error

'''
DIFICULTAD EXTRA
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''

def print_numbers (texto1, texto2):
    cont = 0
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i}. {texto1}, {texto2}')
        elif i % 3 == 0:
            print(f'{i}. {texto1}')
        elif i % 5 == 0:
            print(f'{i}. {texto2}')
        else:
            print(i)
            cont += 1
        
    return f'Fueron {cont} veces que se imprimió sólo un número'
    
print(print_numbers('Estoy comiendo', 'En un restaurante'))