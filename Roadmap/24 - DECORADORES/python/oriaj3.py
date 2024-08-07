"""
24 - DECORADORES
Autor de la solución: Oriaj3

Teoría: 
Los decoradores son funciones que envuelven a otras funciones o métodos para extender
o modificar su comportamiento. Los decoradores son una característica poderosa de Python
que permite añadir funcionalidades a una función sin modificar su código.

En la vida real, un decorador se puede comparar con un envoltorio de regalo. El regalo  
es la función original y el envoltorio es el decorador que añade funcionalidades al regalo.

Por ejemplo, se puede utilizar un decorador para medir el tiempo de ejecución de una función,
para comprobar si el usuario tiene permisos para ejecutar una función o para registrar la
entrada y salida de una función.

Ejemplo: 
def decorador(funcion):
    def envoltura():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return envoltura
    
@decorador
def saludo():
    print("Hola, mundo!")
    
saludo()

En este ejemplo, el decorador "decorador" envuelve la función "saludo" y añade un mensaje
antes y después de ejecutar la función. Al llamar a la función "saludo", se ejecuta la
función envuelta por el decorador.
"""

"""
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

##Ejemplo propio
def mi_decorador(funcion):
    def decorar():
        print('Antes de la ejecución de la función a decorar')
        funcion()
        print('Después de la ejecución de la función a decorar')

    return decorar

@mi_decorador
def saludar():
    print('Hola mundo!!')

saludar()

#Ejemplo Mouredev
def mostrar_llamada(funcion):
    def mostrar_funcion():
        print(f"[{funcion.__name__}]")
        return funcion
    return mostrar_funcion

@mostrar_llamada    
def ejemplo_funcion1():
    pass

@mostrar_llamada
def ejemplo_funcion2():
    pass

ejemplo_funcion1()
ejemplo_funcion2()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */
"""
import time 

def mostrar_llamadas(funcion):
    def contador_funciones():
        contador_funciones.contador += 1
        print(f"[{funcion.__name__}]- {contador_funciones.contador}")
    contador_funciones.contador=0
    return contador_funciones

@mostrar_llamadas
def ejemplo_1():
    pass

@mostrar_llamadas
def ejemplo_2():
    pass

ejemplo_1()
ejemplo_1()
ejemplo_2()
ejemplo_1()
ejemplo_2()

#Ejemplo de decorador que cuenta el tiempo

def contador_tiempo(funcion):
    def contador():
        start_time = time.time()
        funcion ()
        final_time = time.time()
        total = final_time - start_time
        print(f"[{funcion.__name__}]- ha tardado {total} segundos")

    return contador

@contador_tiempo
def ejemplo_tiempo():
    for i in range (0, 20):
        time.sleep(0.1)
        pass

ejemplo_tiempo()

#DEcorador con argumentos que cuenta el tiempo

def contador_tiempo_args(funcion):
    def contador(*args, **kwargs):
        start_time = time.time()
        funcion(*args, **kwargs)
        final_time = time.time()
        total = final_time - start_time
        print(f"[{funcion.__name__}]- ha tardado {total} segundos")

    return contador

@contador_tiempo_args
def ejemplo_tiempo_args(n):
    for i in range (0, n):
        time.sleep(0.1)
        pass
    
ejemplo_tiempo_args(10)

#Decorador que comprueba si el usuario tiene permisos
def comprobar_permisos(permisos_requeridos):
    """Decorador que comprueba si el usuario tiene los permisos necesarios.

    Args:
        permisos_requeridos: Una lista de permisos necesarios para ejecutar la función.
    """
    def decorador(funcion):
        def comprobar(*args, **kwargs):
            if all(permiso in permisos_usuario for permiso in permisos_requeridos):
                return funcion(*args, **kwargs)  # Ejecutar la función original
            else:
                print("No tienes permisos para ejecutar esta función.")
        return comprobar
    return decorador

# Ejemplo de uso:

permisos_usuario = ["leer"]  # Permisos del usuario actual

@comprobar_permisos(["leer"])
def funcion_lectura():
    print("Función de lectura ejecutada con éxito.")

@comprobar_permisos(["escribir"])
def funcion_escritura():
    print("Función de escritura ejecutada con éxito.")

@comprobar_permisos(["leer", "escribir"])
def funcion_lectura_escritura():
    print("Función de lectura y escritura ejecutada con éxito.")

funcion_lectura()      # Se ejecuta
funcion_escritura()   # Se ejecuta
funcion_lectura_escritura() # Se ejecuta