#Asignacion por valor 
a=8
b = a
b = 2

print("Asignacion valor: ",a,b)

#Asignacion por referencia
list1 = [3,9,6]
list2 = list1 
list2.append(2)

print("Asignacion por referencia ")
print(list1)
print(list2)

# Funciones paso por valor
def double_num(num):
    return num **2

number = 2

print("Paso por valor", double_num(number))

#Funciones paso por referencia
def double_nums(numbers):
    
    for index,number  in enumerate(numbers):
        numbers[index] = number ** 2
    

list_numbers = [6,9,17]
double_nums(list_numbers)
print("Paso por referencia",list_numbers) 

def string_referencia(cadena):
    
    cadena += " + concatenate"       

string_cadena = "New string"    
string_referencia(string_cadena)
print("Paso por referencia string: ", string_cadena)

#Extra exercise 

def intercambia_valor(a,b):
    aux = a
    a = b
    b = aux
    return a,b
     
value1 = 4
value2 = 8 

value3,value4 = intercambia_valor(value1,value2)  

print("Valores originales: ",value1,value2)
print("Valores retorno: ",value3,value4)


def intercambia_referencia(a,b):
    
    aux = a
    a = b
    b = aux
    return a,b

list3 = [9,8,7]
list4 = [2,1,4]  

list5,list6 = intercambia_referencia(list3,list4)
list4.append(16)
print("Valores originales", list3,list4)
print("Valores retorno: ",list5,list6)
  