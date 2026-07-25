"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico. 
 *
"""

# Definimos el decorador, va a redecorar la función que le pasemos
# como argumento
def decorador(funcion):
    def envoltura(nombre:str, edad:int):
        print(f"Yo soy {nombre} y tengo {edad}")            
        return funcion       
    return envoltura

# Decoramos las funciones
@decorador
def imprimeLuis():
    pass   

# Decoramos las funciones
@decorador
def imprimePepe():
    pass

# Decoramos las funciones
@decorador
def imprimeJuan():
    pass

# Llamamos a las funciones
imprimeLuis("Luis", 34)
imprimePepe("Pepe", 40)
imprimeJuan("Juan", 30)

"""
DIFICULTAD EXTRA (opcional):
Crea un decorador que sea capaz de contabilizar cuántas veces
se ha llamado a una función y aplícalo a una función de tu elección.
"""

# Definimos el decorador, va a redecorar la función que le pasemos
# como argumento
def decoradorContador2(funcion):
    contador = 0  
    def envoltura(nombre:str, edad:int):
        nonlocal contador
        contador += 1        
        print(f"Yo soy {nombre}, tengo {edad} y he llamado a la función {funcion.__name__} {contador} veces")            
        return funcion
    return envoltura

# Decoramos las funciones, cada función va a tener su propia instancia
@decoradorContador2
def imprimeLuis2():
    pass

# Decoramos las funciones
@decoradorContador2
def imprimePepe2():
    pass

# Decoramos las funciones
@decoradorContador2
def imprimeJuan2():
    pass

# Llamamos a las funciones
imprimeLuis2("Luis", 34)
imprimeLuis2("Luis", 34)
imprimePepe2("Pepe", 40)
imprimeJuan2("Juan", 30)