#24 PATRONES DE DISEÑO: DECORADORES
"""
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */
"""

# Definición de un decorador llamado 'decorador'
def decorador(funcion):
    # Definición de una función interna que envuelve la función original
    def pintar_terminal(a, b):
        for i in range(3):
            print(f"=================={i}==================")

        # Llama a la función original con los argumentos proporcionados
        func = funcion(a, b)
        return func

    # Devuelve la función interna, que ahora es una versión decorada de la función original
    return pintar_terminal

# Aplicación del decorador 'decorador' a la función 'multiplicar'
@decorador
def multiplicar(a, b):
    return a * b

print(multiplicar(5, 5))

#extra

# Definición de un decorador llamado 'contador'
def contador(funcion):
    cantidad: int = 1

    def contar():
        nonlocal cantidad  # Utiliza la variable 'cantidad' definida en el ámbito del decorador
        print("Se ha llamado esta función un total de", cantidad, "veces")
        cantidad += 1

        func = funcion()
        return func

    return contar

@contador
def saludar():
    print("Hola mundo")

saludar()
saludar()
saludar()
