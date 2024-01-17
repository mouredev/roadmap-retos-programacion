''' * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:'''
#variables
a = 10
b = 20
c = 0
saludo = 'saludos estimado usuario!\n'

def funcionConTodo(): #Una funcion con varias funciones dentro
    #Funcion con parametros
    def saludoSuma(a, b):
        c = a + b
        print(saludo, a, '+', b, '=', c, '\n')

    saludoSuma(a, b)

    dialogo = 'me cuesta mucho trabajo hacer una carita feliz ->'
    #Funcion sin parametros
    def presentacion():
        print(dialogo)
        amsiedad = ':d', ':d', ':d', ':d', ':d', ':d', ':d', ':D' #variable local, no se puede utilizar fuera de la funcion
        print(amsiedad, '\n') 
    presentacion()

    #funciones con retorno
    def si_o_no():
        if any (caracter == '>' for caracter in dialogo):
            variable_extremadamente_larga_y_totalmente_inutil_en_el_programa_que_no_deberia_existir_pero_aun_asi_la_incluyo_porque_soy_tonto = True
        else:
            variable_extremadamente_larga_y_totalmente_inutil_en_el_programa_que_no_deberia_existir_pero_aun_asi_la_incluyo_porque_soy_tonto = False

        return variable_extremadamente_larga_y_totalmente_inutil_en_el_programa_que_no_deberia_existir_pero_aun_asi_la_incluyo_porque_soy_tonto
    print(si_o_no(), '\n') #Return = True en caso de existir ">", sin el Return, el valor seria NONE.

funcionConTodo()


a = 'hola'
b = 'mundo'
import random
def dificultadExtra(a , b):
    i2 = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0 :
            print(i, a, b)
        elif i % 3 == 0:
            print(i, a)
        elif i % 5 == 0:
            print(i, b)
        else:
            i2 = i2 + 1
            print(i)
    print('\n', 'Numero de veces que no se imprimio ningun parametro:')
    return i2

print(dificultadExtra(a, b))