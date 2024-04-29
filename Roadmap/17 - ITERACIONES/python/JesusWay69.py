import os, random
os.system('cls')
os.system('clear')

"""* EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?"""

'''FOR CON RANGO CONDICIONAL DE INICIO Y PARADA'''
def iterator_1():
    for i in range (1,11):
        print(i, end=" ")
    print("\b --> Método 1")
iterator_1()

'''FOR CON RANGO SOLO DE PARADA Y CONDICIONAL PARA SALTARSE EL 0 CON EL QUE EMPIEZA POR DEFECTO'''
def iterator_2():
    for i in range (11):
        if i == 0:
            continue
        print(i, end=" ")
    print("\b --> Método 2")
iterator_2()

'''FOR ANIDADOS CON CONDICIÓN DE INICIO,PARADA Y PASO, EL PRIMERO IMPRIME LOS IMPARES Y EL SEGUNDO LOS PARES'''
def iterator_3(i:int):
    for i in range (1,11,2):
        print(i, end=" ")
        for j in range(1):
            if i<10:
                print (i+1, end=" ")
    print("\b --> Método 3")
iterator_3(0)

'''BUCLE FOR-ELSE CON CONDICIÓN DE INICIO Y PARADA'''
def iterator_4(i:int):
    for i in range (i,1):
        if i == 1:
            break 
    else:
        for i in range(i+1,11):
            print(i,end=" ")
    print("\b --> Método 4")
iterator_4(0)


   
'''WHILE CON CONDICIÓN DE PARADA Y OPERADOR DE INCREMENTO'''
def iterator_5(i:int):
    while i<10:
        i+=1
        print(i, end=" ")
    print("\b --> Método 5")
iterator_5(0)


'''WHILE CON OPERADOR DE INCREMENTO Y CONDICIÓN DE SALIDA (DO-WHILE)'''
def iterator_6(i:int):
    while True:
        i+=1
        print (i,end=" ")
        if i == 10:
            break
    print("\b --> Método 6")
iterator_6(0)


'''WHILE ANIDADOS CON CONDICIÓN DE PARADA Y OPERADOR DE INCREMENTO'''
def iterator_7(i:int):
    while i<10:
        i+=1
        print(i, end=" ")
        while i<10:
            i+=1
            print(i, end=" ")
    print("\b --> Método 7")
iterator_7(0)


'''FUNCIÓN CON INCREMENTO, CONDICIÓN DE PARADA Y RECURSIVIDAD'''
def iterator_8(i:int):
    i+=1
    print(i, end=" ")
    if i<=9:
        iterator_8(i)
iterator_8(0)
print("\b --> Método 8")

'''FUNCIÓN CON GENERACIÓN DE NÚMEROS ALEATORIOS QUE SE AÑADEN A UN SET HASTA QUE ESTE CUMPLA LA CONDICIÓN DE LONGITUD 10'''
def iterator_9(i:int):
    my_list = set()
    while len(my_list)<i:
       num = random.randint(1,10)
       my_list.add(num)
    [print(num, end=" ") for num in my_list]
    print("\b --> Método 9")
iterator_9(10)

'''FUNCIÓN CON MÉTODO DE LENGUAJE ITER'''
def iterator_10():
    my_list = []
    [my_list.append(i) for i in range(1,11)]
    my_iterator = (iter(my_list))
    [print(next(my_iterator), end=" ") for i in range (len(my_list))]
    print("\b --> Método 10")
iterator_10()

'''FUNCIÓN QUE TRANSFORMA CARACTERES A SU CÓDIGO ASCII CON EL MÉTODO ORD'''
def iterator_11(symbols:str):
    for char in symbols:
        print(ord(char)-40,end=" ")
    print("\b --> Método 11")
iterator_11(")*+,-./012")

'''FUNCIÓN QUE CREA 2 SETS CON FOR Y WHILE E IMPRIME LOS ELEMENTOS COMUNES DE AMBOS '''
def iterator_12():
    set1 = set()
    set2 = set()
    for i in range (10,-15,-1):
       set1.add(i)
    i=1
    while i>0 and i<25:
        set2.add(i)
        i+=1
    [print(i, end = ' ') for i in set2.intersection(set1)]  
    print("\b --> Método 12")     
iterator_12()

'''FUNCIÓN QUE CREA UN SET DE NÚMEROS PARES DEL 0 AL 20 Y LUEGO UN DICCIONARIO A PARTIR DE ESE SET
   CON SUS ELEMENTOS COMO CLAVES Y LA DIVISIÓN DE ESTOS ENTRE 2 COMO VALORES '''
def iterator_13():
    my_list = set() 
    [my_list.add(i) for i in range(0,21,2)]
    my_dict = {j:j/2 for j in my_list}
    del(my_dict[0])
    [print(int(v),end=" ") for v in my_dict.values()]
    print("\b --> Método 13") 
iterator_13()

'''FUNCIÓN QUE CREA UNA LISTA CON NÚMEROS DE 10 A 1 CON FOR REGRESIVO Y LUEGO CON OTRO FOR
   SE DESAPILA Y SE IMPRIME'''
def iterator_14():
    my_list = []
    [my_list.append(i) for i in range(10,0,-1)]
    [print(my_list.pop(), end=" ") for j in range(len(my_list))]   
    print("\b --> Método 14")    
iterator_14()
'''FUNCIÓN QUE CREA UNA LISTA CON NÚMEROS DE 10 A 1 CON FOR REGRESIVO, SE CONVIERTE
   A UN STRING, SE VOLTEA EL ORDEN DE LOS CARACTERES Y SE IMPRIMEN LOS CARACTERES CON
   OTRO FOR'''
def iterator_15():
    my_list = []
    my_str = ""
    [my_list.append(i) for i in range(10,0,-1)]
    for j in my_list:
        j = str(j)
        my_str=my_str+j
    my_str=my_str.replace("10","01")
    my_str= (my_str[::-1])
    for n in my_str:
        if n=="0":
            print("\b",end="0")
        else:
            print(int(n), end=" ")
    print(" \b --> Método 15")
iterator_15()





 



