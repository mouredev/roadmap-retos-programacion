
def main ():
    #Página Oficial del Lenguaje Python: https://www.python.org/

    #Esta es la primera sintaxi para escribir un comentario en Python (comentario de una sola línea)

    """
    Esta es la segunda sintaxis para escribir un comentario
    en Python (comentario de varias lineas o comentario en bloque)
    """

    saludo = str("¡Hola, ")

    """
    En Python, las constantes no son una característica nativa como en otros lenguajes de programación. Sin embargo, puedes simular una constante declarando una variable con un nombre característico y asignándole un valor que no debería modificarse durante la ejecución del programa.
    """

    MI_CONSTANTE = "Valor de mi constante"

    numero_entero = int(25)
    numero_decimal = float(3.1416) 
    cadena_texto = str("Python!") 
    booleano = bool(True) 

    print(saludo + cadena_texto)

if __name__ == "__main__":
    main()
