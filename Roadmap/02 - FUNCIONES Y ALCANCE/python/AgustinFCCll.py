## RETO 02  DIFICULTAD EXTRA

def fuction(value_one, value_two):
    contador = 0
    for i in range(1, 101):            
        if i % 3 == 0 and i % 5 == 0:
            print(value_one + value_two)
        elif i % 3 == 0:         
            print(value_one)
        elif i % 5 == 0:          
            print(value_two)
        else:
            print(i)
            contador += 1
    return contador               

resultado = fuction( " Multiplo de 3 ", " multiplo de 5 ")
print("El numero se a impreso: ",resultado)
