#Valor y referencia



# tipos de dato por valor

mi_entero_a = 10
mi_entero_b = 20

mi_entero_a = mi_entero_b

print(mi_entero_a)
print(mi_entero_b)


#tipos de dato por referencia

mi_lista_a = [10, 20]
mi_lista_b = [30, 40]

mi_lista_a = mi_lista_b #cambio de direccion de memoria

mi_lista_a.append(50)

print(mi_lista_a)
print(mi_lista_b)


# Funciones con datos por valor

def mi_entero_funcion(mi_entero: int):
    mi_entero = 20
    print(mi_entero)


mi_entero_funcion(55)


#funciones de datos por referencia
#funciona como un puntero al igualar valores lo que hace es que tengan el mismo valor de memoria

def mi_lista_funcion(mi_lista: list):
    mi_lista.append(4)
    mi_lista_d = mi_lista
    mi_lista_d.append(5)
    print(mi_lista_d)
    print(mi_lista)

mi_lista_c = [1,2,3]
mi_lista_funcion(mi_lista_c)
print(mi_lista_c)



#DIFICULTAD EXTRA

#parametros por valor
valor_a = 30
valor_b = 50

#parametros por referencia
referencia_a = [1,2,3,4]
referencia_b = [5,6,7,8]

#programa de valor
def programa_valor():
    def cambiar_valores (param_a, param_b):
        guardar_valor = param_a
        param_a = param_b
        param_b = guardar_valor
        return(param_a , param_b)


    resultados = cambiar_valores(valor_a, valor_b)
    valor_1 = resultados[0]
    valor_2 = resultados[1]

    print(valor_a)
    print(valor_b)
    print(valor_1)
    print(valor_2)

programa_valor()

    
#programa de referencia
def programa_referencia():
    def cambiar_referencia (param_a, param_b):
        guardar_valor = param_a
        param_a = param_b
        param_b = guardar_valor
        return(param_a , param_b)


    resultados = cambiar_referencia(referencia_a, referencia_b)
    referencia_1 = resultados[0]
    referencia_2 = resultados[1]

    print(referencia_a)
    print(referencia_b)
    print(referencia_1)
    print(referencia_2)

programa_referencia()






