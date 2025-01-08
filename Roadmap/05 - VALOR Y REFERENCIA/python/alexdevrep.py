'''
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
'''

#Asignación por valor
valor1 = 10
valor2 = valor1
valor1 =20
print(f'El valor2 es {valor2}')
print(f'Sin embargo el valor1 es {valor1}')
'''
Como podemos comprobar el valor de la variable valor2 no se modifica cuando
variamos el valor de la variable valor 1
'''

#Asignación por referencia
mi_list = [1,2,3,4,5]
mi_listNew = mi_list
mi_list.pop(4)
print(mi_listNew)
'''
Como podemos comprobar tanto como mi_list como mi_listNew apuntan hacia la misma dirección de memoria
asi que cuando modificamos una de las dos variables la otra también se ve afectada
'''

#Dificultad EXTRA
valor3 = 3
valor4 = 5
def programa1(valor3,valor4):
    valor3 = 5
    valor4 = 3
    return [valor3 , valor4]

[resultado3,resultado4] = programa1(valor3,valor4)
print(f'El valor de la variable valor3 originalmente es: {valor3}')
print(f'El valor de la variable valor3 se ha modificado ahora es: {resultado3}')
print(f'El valor de la variable valor4 originalmente es: {valor4}')
print(f'El valor de la variable valor4 se ha modificado ahora es: {resultado4}')


print("---------------------------")
lista = ["Hola","Alexdevrep","Python"]
def programa2(lista):
    listaNueva = lista
    listaNueva.append("Mundo")
    return listaNueva

resultado = programa2(lista)

print (f'La lista resultante es :{resultado}')
print (f'Y sin embargo nuestra lista original tambien se ha visto modificada{lista}')


