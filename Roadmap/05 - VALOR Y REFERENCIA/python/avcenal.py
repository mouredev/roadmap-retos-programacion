"""VALOR Y REFERENCIA

 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""
#ASIGNACIÓN DE VARIABLES POR VALOR Y POR REFERENCIA
#Por valor, Python realiza una asignación por valor en datos "simples"
print("Asignación por valor")
a = 10
print(id(a))
b = a
print(id(b)) #aqui se puede observar que b apunta a la misma referencia en memoria que a
a += 5
print(id(a)) #pero al modificar a sumándole 5 su referncia en memoria cambia
print(a)
print(b)

#Por referencia, en cambio Python realiza una asignación por referencia para datos complejos
print("\n")
print("Asignación por referencia")
print("Con Listas")
one_list = [1,2,3,4]
for element in one_list: #usando este loop los valores originales de la lista no cambian
    element *= 2
print(one_list)

for index in range (0,len(one_list)): #pero si usamos este, al acceder al valor mediante la posición, el valor queda modificado
    one_list[index] *= 2
print(one_list)

print("\n")
print("Con diccionarios")

x = {
    "a":10,
    "b":15
}
print(id(x))
y = x
print(id(y))
x["a"] = x["a"]+5
x["b"] = x["b"]+10

print(x)
print(y)

#FUNCIONES CON VARIABLES POR VALOR Y POR REFERENCIA
#Por valor, igual que antes, datos simples se pasarán siempre por valor

def increase_value(value):
    return value+5

number = 3
print(increase_value(number)) #al ser un tipo de dato simple, aqui aparece modificado (+5)
print(number) #y aqui continúa con el mismo valor

#Por referencia, igual, solo datos complejos como las listas

def append_value(one_list):
    one_list.append(10) #se hace un append a la lista del número 10 sin retornarla
    print(one_list)

append_value(one_list.copy()) #si le paso como parámetro una copia de la lista original 
print(one_list) #dicha lista original no se modifica

append_value(one_list) #en cambio, si le paso directamente la lista original
print(one_list) #se modifica con el append del número 10

"""
* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""
def exchange_valor (value1, value2):
    temp = value1
    value1 = value2
    value2 = temp
    return value1,value2

var_1 = 5
var_2 = 7
new_var_1, new_var_2 = exchange_valor(var_1,var_2)
print(f"Los valores de las primeras variables son: {var_1} y {var_2}")
print(f"Los nuevos valores son: {new_var_1} y {new_var_2}")

def exchange_ref (list_1,list_2):
    temp = list()
    for index in range(0,len(list_1)):
        temp.append(list_1[index])
    list_1.clear()
    for index in range(0,len(list_2)):
        list_1.append(list_2[index])
    list_2.clear()
    for index in range(0,len(temp)):
        list_2.append(temp[index])
    return list_1,list_2

var_3 = [1,2,3]
var_4 = [4,5,6]
new_var_3, new_var_4 = exchange_ref(var_3.copy(),var_4.copy()) #si quitamos el copy() los valores de las variables originales se modificarán
print(f"Los valores de las primeras variables son: {var_3} y {var_4}")
print(f"Los nuevos valores son: {new_var_3} y {new_var_4}")
