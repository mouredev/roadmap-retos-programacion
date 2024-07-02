def manejo_de_excepciones():
    try:
        resultado_division = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error capturado: {e}")

    try:
        lista = [1, 2, 3]
        elemento = lista[5]
    except IndexError as e:
        print(f"Error capturado: {e}")

    print("El programa continúa ejecutándose a pesar de los errores.")

manejo_de_excepciones()
