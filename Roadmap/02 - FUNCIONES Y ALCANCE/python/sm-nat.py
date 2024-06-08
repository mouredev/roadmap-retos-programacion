
#FUNCIONES BÁSICAS

#función básica
def imprimir_saludo():
    print("Hola")

imprimir_saludo()

#función con parametros
def funcion_parametros(param1, param2):
    print(param1, param2)
funcion_parametros("Hola", "que tal")

#Función con Valor de Retorno
def funcion_con_retorno(a,b):
    return a + b
suma = funcion_con_retorno(4,3)
print(suma)

# Función con Parámetros por Defecto
def saludar(nombre="mundo"):
    print(f"Hola, {nombre}!")

saludar() 
saludar("Natalia")  

#Funciones Anidadas
def exterior():
    print("Esta es la función exterior.")
    
    def interior():
        print("Esta es la función interior.")
    
    interior()

exterior()

# Función Lambda
sumar = lambda x, y: x + y

resultado = sumar(10, 5)
print(f"El resultado de la suma lambda es: {resultado}")  

#FUNCIONES BUILT IN

print(type(3.14))
print(len("supercalifragilistico"))
numeros = [1, 2, 3, 4]
print(sum(numeros))  
print(min(numeros))  
print(max(numeros))  
for num in range(3):
    print(num)

#VARIABLE LOCAL Y GLOBAL

mensaje_global = "Soy una variable global"

def mi_funcion():
    mensaje_local = "Soy una variable local"
    print(mensaje_local)
    
    print(mensaje_global)
    
mi_funcion()

#EXTRA
"""Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""

def ejercicio_extra(txt_1,txt_2):
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(txt_1 + txt_2)
        elif number % 3 == 0:
            print(txt_1)
        elif number % 5 == 0:
            print(txt_2)
        else:
            print(number)
            count += 1
    return count
    
print(ejercicio_extra("hola","mundo"))



