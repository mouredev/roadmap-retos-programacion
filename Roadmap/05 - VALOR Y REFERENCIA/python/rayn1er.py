# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

#datos por valor

value_a = 100
print(value_a) # mostramos lo que vale a 
value_b = value_a # le asignamos a b el valor de a 
print(value_b) # imprimimos el valor de b
value_a = 200 #cambiamos el valor de a
print(value_a,value_b) # imprimimos y notamos que b sigue valiendo lo mismo que valia a, puesto que le hemos asignado el valor que tenia previamente a 
