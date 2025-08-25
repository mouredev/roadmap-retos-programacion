#VALOR Y REFERENCIA EN PYTHON


#Tipos de datos por valor

a = 1
print(a)
b = a 
a = 2 
print(a)
print(b)
print("--------------------")

#Tipos de datos por referencia

mi_lista = [1,2,3]
print(mi_lista)
mi_lista_modificada = mi_lista 
mi_lista_modificada.append(4)

print(mi_lista)
print(mi_lista_modificada)

print("--------------------")
#Funciones con datos por valor

mi_entero = 20

def fun_entero(mi_entero_modificado : int):
    mi_entero_modificado = 40
    print(mi_entero_modificado)
    
fun_entero(mi_entero)
print(mi_entero)

print("------------------")
#Funciones con datos por referencia

mi_lista_a = [1,2,3]

def añadir_a_lista(mi_lista : list):
    mi_lista.append(4)
    print(mi_lista)
    
print(mi_lista_a)
añadir_a_lista(mi_lista_a)
print(mi_lista_a)

print("------------------")

#EJERCICIO EXTRA

#FUNCION POR VALOR

valor_1 = 10
valor_2 = 20

def modificador_por_valor(mi_valor_1 : int, mi_valor_2 : int):
    mi_valor_3 = mi_valor_1
    mi_valor_4 = mi_valor_2
    
    mi_valor_1 = mi_valor_4
    mi_valor_2 = mi_valor_3
    
    print(mi_valor_1)
    print(mi_valor_2)

modificador_por_valor(valor_1,valor_2)
print(valor_1)
print(valor_2)

#FUNCION POR REFERENCIA

lista_1 = [1,2,3]
lista_2 = [4,5,6]

def modificar_por_referencia(mi_lista_1 : list, mi_lista_2 : list):  
    mi_lista_3 = mi_lista_2
    mi_lista_4 = mi_lista_1
    
    print(mi_lista_3)
    print(mi_lista_4)

modificar_por_referencia(lista_1, lista_2)
print(lista_1)  
print(lista_2)  
