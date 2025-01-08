'''//////
 * Explora 
   el concepto de manejo de excepciones según tu lenguaje./////
'''

'''
###Definicion corta
 Se trata de una forma de controlar el comportamiento de
 un programa cuando se produce un error. Salvo que tratemos este error, 
 el programa se parará
 '''
a = 5
b = "0"
#print(a / b) error! 

#Usando try except se puede capturar el error en caso de que tire el error de div por 0
try:
    print(a / b)
except ZeroDivisionError:
    print('No se pueden dividir entre 0...')
except TypeError:
    print("Error de tipo!")

listado = [0, 1, 2, 3, 4]
#print(listado[5]) #IndexError error...

try:
    print(listado[5])
except IndexError:
    print("No se puede acceder a dicho indice, quizas porque no existe")


#La dificultad extra la hare despues :( entre el trabajo y la u no me da la cabeza, les he fallado TT_TT

