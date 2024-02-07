'''
Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
'''
# asignacion por valor 

from ast import Return


my_variable = "hola"
my_new_variable = my_variable
my_new_variable = "mundo"

print(my_variable)
print(my_new_variable)

#asignacion por referencia

my_list = [3,4,67,10]
my_new_list = my_list
my_new_list [3] = "hello"

print(my_list)         #salida: my_list =[3,4,67"hello"]
print(my_new_list)     #salida: my_new_list =[3,4,67"hello"]

'''
Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas
'''
# funcion con variable por valor

def my_function (my_variable):
    print(my_variable)   # variable original no se ve afectada 

# funcion con variable por referencia 
    
def variable_referencia(my_list):
    my_list.append(5)
    print(my_list)       # variable original si ve afectada 

'''
DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''

def intercambio_valor(value1,value2):
    
    value_temp = value1
    value1 = value2 
    value2 = value_temp

    return value1, value2

# variables originales 
valor1 = 34
valor2 = 15

# llamado de la funcion y asignacion a los nuevas variables los valores
valor_new1, valor_new2 = intercambio_valor(valor1,valor2)

print('valores orginales: ',valor1,valor2)
print('\nvalores intercambiados: ',valor_new1,valor_new2)


