# FUNCIONES 
'''Sin parametros ni retorno'''
# No se esta retornando ni pidiendo nada solo ejecuta el bloque de codigo dentro la funcion.
def greet():
    print('Hola, como estas?')
    
greet() #-> Hola, como estas?


'''Con un parametro'''
# No se esta retornando solo pide un parametro.
def greet(name):
    print(f'Hola, como estas {name}?')
    
greet('juanRCoder') #-> Hola, como estas juanRCoder?


'''Con varios parametros'''
#Tiene un parametro name y luego un parametro variable que suma cantidad indefinida de numeros
def sumar(name, *args):
    print(f'Buenos dias {name}')
    print(sum(*args))

sumar('Mario', [1,2,3,4,5]) # Buenos dias Mario | 15


'''Con retorno'''
# funcion con retorno si se cumple la condicion retorna y sale de la funcion, caso contrario retorna el ultimo return
# el return, solamente retorna mas no imprime por eso se le coloca un print para ver el resultado retornado.
def isPar(n):
    if n % 2 == 0: return 'Es par'
    return 'No es par'

print(isPar(13)) # No es par
print(isPar(16)) # Es par


'''Funciones dentro de otras funciones'''
# Esta funcion retorna una lista de numeros primos menores a n.
def numPrimos(n):
    # Funcion para saber si el numero es primo
    def isPrimo(primo):
        if primo <= 1: return True
        for i in range(2, (primo//2)+1):
            if primo % i == 0: return False
        return True
    
    # Logica para almacenar numeros primos menores a n
    primos = []
    for j in range(2, n + 1):
        if (isPrimo(j)): primos.append(j)
    
    return primos

print(numPrimos(10)) # [2, 3, 5, 7]
    

'''Algunas funciones integradas mas utilizadas'''
print(len(['a', 'b', 'c', 'd', 'e']))   # 5, cantidad de elementos.
print(max([20, 40]))                    # 40, numeros maximo de una lista.
print(type('string'))                   # <class 'str'>, tipo de dato.
print(dir(list))                        # muestra todos los metodos de una lista.
print(range(10))                        # rango de numeros entre 0, 10 inmutable.


# VARIABLE GLOBAL Y LOCAL
"""
variable local, es una variable que solo esta disponible dentro de un rango como una funcion o una condicional.
variable global, es una variable que esta en el codigo y puede ser utilizada en cualquier bloque de codigo mediante
la palabra reservada 'global'.
"""
# EJEMPLO 
# Aqui podemos distingui una variable local y global
x = 10      #-> variable global
def show():
    x = 6   #-> variable local
    return(x)

print(show()) # 6
print(x)      # 10

# Usar la variable global dentro de la funcion
x = 10       #-> variable global
def show():
    global x # palabra reservada para usar la variable global dentro de la funcion
    x = 6    #-> variable local
    return(x)

print(show()) # 6
print(x)      # 6


#  * DIFICULTAD EXTRA (opcional):

def cadena(str, str2):
    lista = []
    
    # Agregar a la lista los numeros y los textos segun las condiciones
    for i in range(0, 100 + 1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append(f"{str}{str2}")
        elif i % 3 == 0:
            lista.append(str)
        elif i % 5 == 0:
            lista.append(str2)
        else:
            lista.append(i)  
            
    # Quitar los textos de la lista
    lista = [letter for letter in lista if letter != str and letter != str2 and letter != f"{str}{str2}"]
    return len(lista)

print(cadena('hola', 'mundo')) # 53
