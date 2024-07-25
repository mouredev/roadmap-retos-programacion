def funcion_sinRetorno_sinParametros():
    print ("Esta funcion solo imprime en pantalla")

funcion_sinRetorno_sinParametros()

def funcion_conParametros(x, y):
    print(f"Esta funcion recibe dos parametros y = {y} y x = {x}")

funcion_conParametros(54, 62)

def funcion_parametros_retorno(x, y):
    suma = x + y
    print (f"Esta funcion recibe parametro  y = {y} y x = {x} y retorna el resultado multiplicado por 2 ")
    return (suma*2)

suma_x2 = funcion_parametros_retorno(32, 52)
print (suma_x2)


nombre_global = "Alejandro mazo" # variable global
def primera_funcion ():
    str_uno = "Hola" + " " #variable local

    def segunda_funcion():
        str_dos = "mundo, mi nombre es "
        return str_uno+str_dos+nombre_global
    print (segunda_funcion())

primera_funcion()


## Difucltad extra 

def dificultad_extra (buzz):
    count = 0
    for i in range(1,101):  
        if i % 3 == 0 and i % 5 == 0:
            print (fizz + buzz)

        elif i % 3 == 0:
            print (fizz)
        
        elif i % 5 == 0:
            print (buzz)
       
        else:
            print (i)
            count += 1

    return (count)
        
fizz = "fizz"
print("el número de veces que se ha impreso el número en lugar de los textos es: ", dificultad_extra("buzz"))

