def imprimir_numeros(n):
    if n < 0:
        return
    else:
        print(n)
        imprimir_numeros(n - 1)

# Llamamos a la función con el valor inicial de 100
imprimir_numeros(100)
# Esto nos imprimirá de los numero de 100 a cero de manera descendiente. 
