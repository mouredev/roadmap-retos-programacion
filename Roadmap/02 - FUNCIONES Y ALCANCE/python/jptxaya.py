#Funciones

def funcion_basica():
    print("funcion basica")
funcion_basica()

def funcion_con_parametros(param1):
    print(f"funcion con parametros {param1}")
    
funcion_con_parametros("Parametro 1")

def funcion_return(param1, param2):
    return(param1 + param2)

print(f"funcion return {funcion_return(4, 5)}")

#Funcion anidada
def funcion1(param1):
    def funcion1_1(param2):
        print(f"funcion1_1 {param2 * 2}")
    def funcion1_2():
        print("funcion1_2")
    funcion1_1(param1 - 2) #LLamada a la funcion anidada
        
funcion1(5)

#Utilizacion de funcion
print(f"Utilizacion de funcion sum {sum([1,2,3])}")


variable_global = 2

def funcion_var():
    variable_local = 3
    print("variable local:" + str(variable_local))
    print("variable global dentro de funcion:" + str(variable_global))
    
funcion_var()

#Dificultad Extra
print("Dificultad extra")

def funcion_extra(param_str1, param_str2):
    count = 0
    for elem in range(1,101):
        if elem % 3 == 0 and elem % 5 == 0:
            print(param_str1 + " " + param_str2)
        elif elem % 3 == 0:
            print(param_str1)
        elif elem % 5 == 0:
            print(param_str2)
        else:
            print(elem)
            count += 1
    return count

num_veces = funcion_extra("texto1","texto2")
print(f"Numero de veces solo Numero Funcion Extra: {num_veces}")
    