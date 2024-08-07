### VALOR Y REFERENCIA ###

num_1 = 20 
num_2 = num_1 #Parametro por valor

nombres = ["Ana", "Julio" , "David"] #Parametros por referencia

print(num_2) 
print(num_1) 
print(nombres)

num_1 = 1.5
nombres[0] = "Luis"



print(num_2) #mantiene su valor inicial
print(num_1) 
print(nombres) #se modifica

def saludo(mensaje, nombres) :
    mensaje = mensaje.upper() #Modificando la variable
    nombres[0] = nombres[0].upper() #Modificando la lista
    res = ""
    for nombre in nombres :
        res += f'{mensaje} {nombre} \n'
    return print(res)

usuarios = ["Ana", "Julio" , "David", "Leonor"]
mensaje = "Hola que hace"
print (mensaje)
print (usuarios)

saludo(mensaje, usuarios) 

print (mensaje) #Dado que es una variable por valor no se modifica, mantiene su valor original
print (usuarios) #Al igual que la anterior, se modifica en la funcion y al ser una variable por referencia se modifica

def var_valor(v_1:int,v_2:int):
    temp = v_1
    v_1 = v_2  #Bloque de intercambio de variables por valor
    v_2 = temp
    print(v_1)
    print(v_2)
    return v_1 ,  v_2
def var_referencia(lista:list):
    print (lista[0])
    print (lista[1])
    lista[0], lista[1] = lista[1], lista [0]  # Intercambio variables por referencia
    return lista [0] , lista[1] 

v_3, v_4 = var_valor(2,4)
print (v_3)
print (v_4)
print("------------------------------")
l_1, l_2 = var_referencia([2,4])

print(l_1)
print(l_2)