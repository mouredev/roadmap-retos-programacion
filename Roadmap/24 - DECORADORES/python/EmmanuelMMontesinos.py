"""
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 */
"""

# Decoradores
def decorador(funcion):
    nombre_funcion = funcion.__name__.title()
    def parametros(*args,**kwargs):
        if not kwargs:
            print(f"Decorando la función {nombre_funcion}")
        else:
            print(f"Decorando la función Doble {nombre_funcion}")
            print(f"Argumentos nominales: {kwargs}")
        print(f"Argumentos posicionales: {args}")
        resultado = funcion(*args,**kwargs)
        print(f"Fin del Decorado, resultado de {nombre_funcion}: {resultado}\n")
        return resultado
    return parametros

@decorador
def suma(a,b,doble=None):
    resultado = a + b
    if doble:
        resultado *= 2
    print(resultado)
    return resultado

# Pruebas
suma(2,3)
suma(16.5,500)
suma(10,6,doble="Es doble suma")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""
contador = {}
def nueva_llamada(funcion):
    def parametros(*args,**kwargs):
        if args and kwargs:
            resultado = funcion(*args,**kwargs)
        elif args:
            resultado = funcion(*args)
        elif kwargs:
            resultado = funcion(**kwargs)
        else:
            resultado = funcion()

        nombre = funcion.__name__
        if nombre in contador:
            contador[nombre] += 1
        else:
            contador[nombre] = 1
        print(contador)
        return resultado
    return parametros

@nueva_llamada
def primera():
    resultado = "Primera Función: sin ningun tipo de argumento"
    print(resultado)
    return resultado

@nueva_llamada
def segunda(posicional):
    resultado = f"Segunda Función: con argumento posicional -> {posicional}"
    print(resultado)
    return resultado

@nueva_llamada
def tercera(nominal=True):
    resultado = f"Terccera Función: con argumento nominal -> {nominal}"
    print(resultado)
    return resultado

@nueva_llamada
def cuarta(posicional,nominal=False):
    resultado = f"Cuarta Función: ambos tipos de argumentos\nposinional -> {posicional}\nnominal -> {nominal}"
    print(resultado)
    return resultado

# Pruebas
primera()

segunda("Posicional")
segunda("Posicional")

tercera(nominal=True)
tercera(nominal=True)
tercera(nominal=True)

cuarta("Posicional",nominal=True)
cuarta("Posicional",nominal=True)
cuarta("Posicional",nominal=True)
cuarta("Posicional",nominal=True)