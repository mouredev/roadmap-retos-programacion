'''
ASIGNACION DE VARIABLES POR VALOR
'''
#ejemplo con numeros enteros
var1 = 5
var2 = var1

print(var1)
print(var2 + 10)  #No modifica el valor de la variable original
print(var1)

#ejemplo con cadenas de texto
var_str1 = "Hola"
var_str2 = var_str1

print(var_str1)
print(var_str2 + " mundo") #No modifica el valor de la variable original
print(var_str1)

'''
ASIGNACION POR REFERENCIA
'''
#ejemplo con listas
lista1 = [1, 2, 3]
lista2 = lista1

def ref_lista(mi_lista):
	mi_lista.append(4)
	print(mi_lista)

print(lista1)
ref_lista(lista2)	#aca actualiza la lista original
print(lista1)        

#ejemplo con diccionario

dict1 = {"jesus": 1, "pedro": 2}
dict2 = dict1

def ref_dict(my_dict):
	my_dict["carlos"] = 3
	print(my_dict)

print(dict1)
ref_dict(dict2)	 #aca actualiza el diccionario original 
print(dict1)

#ejemplo con una lista pero con la funcion copy para no modificar la original
list1 = [1, 2, 3]
list2 = list1

def ref_list(mi_list):
	mi_list.append(4)
	print(mi_list)

print(list1)
ref_lista(list2.copy())	#la funcion copy hace una copia de la lista
print(list1)            #la modifica con la funcion y la imprime
                        #sin modificar ni actualizar la lista original


#extra


#por valor
x = 10
y = 20

def hh(x, y):
	temp = x
	x = y
	y = temp
	print(x)
	print(y)

print(x)
print(y)
hh(x, y)	


#por referencia
n = [10, 20]
m = [30, 40]

def aa(x, y):
	temp = x
	x = y
	y = temp
	print(x)
	print(y)

print(n)
print(m)	
aa(n, m)






