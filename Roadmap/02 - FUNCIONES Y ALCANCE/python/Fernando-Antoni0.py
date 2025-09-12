'''
 Crea ejemplos de funciones básicas que representen las diferentes
 posibilidades del lenguaje:
 Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
'''

#Funcion basica
def suma():
    print(1 + 4)

suma()

#De retorno

def resta():
    return 5 - 2

resultado = resta()
print(resultado)

#Con un argumento

def multiplicacion1(num1):
    print(5 * num1)

multiplicacion1(2)

#Con argumentos

def multiplicacion2(num2, num3):
    print(num2 * num3)

multiplicacion2(3, 2)

#Con argumento predeterminado

def division(num4 = 5):
    print(10 / num4)

division(2)
division()

#Con argumentos y retorno

def suma2(num5, num6):
    return num5 + num6

print(suma2(2, 2))

#Con un argumento pero variable

def resta2(*num7): #El * indica que resibira varios argumentos
    for i in num7:
        print(10 - i)

resta2(2, 5, 7, 8, 1)


'''
 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''

def cadTexto(text1, text2) -> str:
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{text1}{text2}")
        elif i % 3 == 0:
            print(f"{text1}")
        elif i % 5 == 0:
            print(f"{text2}")
        else:
            print(i)
            i += 1
    return i

cadTexto("Fizz", "Buzz")