"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
"""
# paso por valor: se crea una copia local de la variable dentro de la funcion (int, float, string, boolean)
# paso por referencia: los cambios realizados dentro de la funcion le afectara tambien afuera (listas, diccionarios, tuplas, set)

#paso por valor un int
my_variable_valor = 10
def doblar_valor(entrada):
    entrada * 2
doblar_valor(my_variable_valor)
print(my_variable_valor) #imprime 10

#paso por referencia
my_variable_referencia = [10, 20, 30]
def doblar_valores(entrada, valor):
    entrada.append(valor)
doblar_valores(my_variable_referencia, 40)
print(my_variable_referencia) #imprimr [10, 20, 30, 40]

"""
EXTRA
"""
# por valor
variable_valor1 = 15
variable_valor2 = 20
def funcion_paso_valor(variable_valor1, variable_valor2):
    variable_valor1 = 38
    variable_valor2 = 40
    return(variable_valor1, variable_valor2)

variable_valor3, variable_valor4 = funcion_paso_valor(variable_valor1, variable_valor2)
print(f"Valores originales: valor1 = {variable_valor1}, valor2 = {variable_valor2}")
print(f"Nuevos valores: valor3 = {variable_valor3}, valor4 = {variable_valor4}")


#por referencia
variable_referencia1 = [10, 20, 30]
variable_referencia2 = [5, 6, 7]
def funcion_paso_referencia(variable_referencia1, variable_referencia2):
    variable_aux = variable_referencia1
    variable_referencia1 = variable_referencia2
    variable_referencia2 = variable_aux
    #variable_referencia1.append(40)
    #variable_referencia2.append(8)
    return variable_referencia1, variable_referencia2

variable_referencia3, variable_referencia4 = funcion_paso_referencia(variable_referencia1, variable_referencia2)
print(f"Valores originales: referencia1 = {variable_referencia1}, referencia2 = {variable_referencia2}")
print(f"Nuevos valores: referencia3 = {variable_referencia3}, referencia4 = {variable_referencia4}")
