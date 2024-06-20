"""
Recurcividad
"""

def imp_del_1_al_100(num:int=0):
    if num<100:
        imp_del_1_al_100(num+1)
    print(num)

imp_del_1_al_100()


"""
Extra
"""

#Calcula el factorial de un numero

def factorial(num:int) -> int:
    aux=num
    if num>1:
        aux=aux*factorial(num-1)
        
    else: 
        aux=1
    return aux


numero= 4

print(f"El de {numero} es:{factorial(numero)}")

#El valor de una posición en la suseción de fibonachi

def pos_en_fibonachi (pos: int)-> int:
    if pos==1:
        return 0
    elif pos==2:
        return 1
    else:
        return pos_en_fibonachi(pos-1)+ pos_en_fibonachi(pos-2)


print(pos_en_fibonachi(8))