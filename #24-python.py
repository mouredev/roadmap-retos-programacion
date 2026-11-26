'''
* EJERCICIO:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
'''
def decorador(funcion): 
    def funcion_decorada_0(*args, **kwargs):
        print(f"Antes de llamar a {funcion.__name__}")
        return funcion(*args, **kwargs)
    return funcion_decorada_0

@decorador
def mi_funcion():
    print("Hola, soy una función decorada")

@decorador
def otra_funcion(x, y):
    print(f"El resultado de la suma es: {x + y}")

@decorador
def funcion_con_parametros(a, b, c):
    print(f"Hola, resultado = {a * b * c}. Esta función tiene 3 parámetros.")    
 
def funcion_contador(funcion):
    contador = 0
    def funcion_decorada_1(*args, **kwargs):
        nonlocal contador
        contador += 1
        print(f"La función {funcion.__name__} ha sido llamada {contador} veces.")
        return funcion(*args, **kwargs)
    return funcion_decorada_1   


@funcion_contador
def funcion_a_contar():
    print("Esta función fue contada.")



mi_funcion()
otra_funcion(3, 5)
otra_funcion(10, 20)
funcion_con_parametros(2, 3, 4)        
funcion_a_contar()
funcion_a_contar()

'''
* DIFICULTAD EXTRA (opcional):
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
'''