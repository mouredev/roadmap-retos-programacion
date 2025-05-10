'''EJERCICIO:
 - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
   su tipo de dato.
 - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)'''

#Asignación de variables "por valor". Cuando la nueva variable recibe una copia de la original
a = 5
b = a
b = 10 #cambiar b no ha supuesto cambiar a
print(a)
print(b)

#Asignación de variables "por referencia"
list1 = [1,2,3,4]
list2 = list1
list2.append(3)
print(list1)

dict1 = {"Luke": "Jedi",
         "Anakin": "Jedi",
         "Conde Doku": "Sith"}

dict2 = dict1

dict2["Anakin"] = "Sith"

print(dict1)

'''DIFICULTAD EXTRA (opcional):
 Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
   Comprueba también que se ha conservado el valor original en las primeras.'''
#Por Valor
x = 3
y = 9

def intercambio_variables(a,b):
    return b,a

nuevo_x, nuevo_y = intercambio_variables(x,y)
print(nuevo_x)
print(nuevo_y)

list1 = [1,3,5]
list2 = [2,4,6]
nueva_list1, nueva_list2 = intercambio_variables(list1, list2)
print(nueva_list1)
print(nueva_list2)


