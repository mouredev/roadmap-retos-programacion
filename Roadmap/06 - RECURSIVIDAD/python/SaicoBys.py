def imprimir_descendente(n):
     """Imprime números de forma descendente desde n hasta 0."""

     if n < 0: # Caso base: detener la recursion cuando n es menor que 0
          return
     print(n) # Imprimir el número actual

     imprimir_descendente(n - 1)  # Llamada recursiva con n-1

# Llamada inicial a la función
imprimir_descendente(100)