"""
ejercicio de recursividad
"""

def hola ():
    print("nico")
    hola()

#es una funcion recursiva ya que se vuelve a llamar dentro de la funcion

"""
Funcion recursiva que imprima los valores del 100 al 1
"""

def fun_recursiva(num : int):
    if num >= 0:
        print(num)
        fun_recursiva(num - 1)


# fun_recursiva(100)




#DIFICULTAD EXTRA

#Calcular un factorial

def calc_factorial(num):   
    if num == 0 or num == 1:
        return 1
    elif num < 0: 
        print("no se puede calcular el factorial de un numero negativo")
    else:
        return num * calc_factorial(num - 1)
        
    

print(calc_factorial(10))



#calcular fibonacci

def calc_fibonacci(num):
    if num == 0:
        return(0)
    elif num == 1:
        return(1)
    elif num < 0:
        print("fibonacci no tiene posiciones negativas")
    else:
        return(calc_fibonacci(num - 1) + calc_fibonacci(num - 2))


print(calc_fibonacci(7))