# 02 - Python - FUNCIONES Y ALCANCE
# Las funciones permiten definir un bloque de código reutilizable que se puede ejecutar muchas veces dentro de un programa.
# El alcance (o scope) se refiere a la región de un programa donde una variable es visible y accesible. 
# EJERCICIO:
'''*- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: 
Sin parámetros ni retorno, con uno o varios parámetros, con retorno'''

def funcion_sin_parametros():
    print("Función sin parámetros ni retorno")
def funcion_sin_retorno_con_parametros(param1, param2):
    suma = param1 + param2
    print(f"Suma de {param1} y {param2} es: {suma}")
def funcion_con_un_parametro(nombre):
    print(f"Hola, {nombre}!")
def funcion_con_varios_parametros(a, b):
    return a + b
def funcion_con_retorno():
    return "Esta es una función con retorno."
# Llamadas a las funciones
funcion_sin_parametros()
funcion_sin_retorno_con_parametros(5, 10)
funcion_con_un_parametro("Pablo")
resultado = funcion_con_varios_parametros(3, 7)
print(f"Resultado de la función con varios parámetros: {resultado}")
mensaje = funcion_con_retorno()
print(mensaje)

'''*- Comprueba si puedes crear funciones dentro de funciones.'''
# Si es posible usar funciones anidadas, pero por lo que entiendo, su uso es poco frecuente.
def funcion_externa():
    def funcion_interna():
        return "Hola desde la función interna!"
    return funcion_interna()

print(funcion_externa())

'''*- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.'''
# Ejemplo usando la función len() que devuelve la longitud de un objeto.
mi_lista = [1, 2, 3, 4, 5]
longitud = len(mi_lista)
print(f"La longitud de la lista es: {longitud}")
# Ejemplo usando la función sum() que devuelve la suma de los elementos de un iterable.
suma_lista = sum(mi_lista)
print(f"La suma de la lista es: {suma_lista}")
for i in range(5):
    print(f"Elemento {i} de la lista")
# Ejemplo usando la función max() que devuelve el valor máximo de un iterable.
maximo = max(mi_lista)
print(f"El valor máximo de la lista es: {maximo}")

'''*- Pon a prueba el concepto de variable LOCAL y GLOBAL. Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)'''
# Variable global
mensaje_global = "Soy global"
def funcion_con_local(): # Esta es una nueva variable local que "oculta" a la global.
  mensaje_local = "Soy local"
  print(f"Dentro de la función: {mensaje_local}")
  print(f"Accediendo a la global desde dentro: {mensaje_global}")
# Llamada a la función
funcion_con_local()
print(f"Fuera de la función: {mensaje_global}")
# Dentro de la función: Soy local
# Accediendo a la global desde dentro: Soy global
# Fuera de la función: Soy global
# Si intentamos acceder a la variable local fuera de la función, obtendremos un error.

'''* DIFICULTAD EXTRA (opcional):
 *- Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
   La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''

#Respuesta al ejercicio extra: con ayuda de copilot
def magic_math(param1, param2):
        contador = 0
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print(param1 + param2)
            elif i % 3 == 0:
                print(param1)
            elif i % 5 == 0:
                print(param2)
            else:
                print(i)
                contador += 1
        return contador

#Respuesta al ejercicio extra: indagando un poco más, recordando un ejercicio similar en turbo pascal, y una revision con DeepSeek
def dificil_extra():
    print("Hola, por favor ingresa las palabras.")
    param1 = input("Palabra 1:")
    param2 = input("Palabra 2:")
    def magic_math(param1, param2):
        contador = 0
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print(param1 + param2)
            elif i % 3 == 0:
                print(param1)
            elif i % 5 == 0:
                print(param2)
            else:
                print(i)
                contador += 1
        return contador
    return magic_math(param1, param2)
veces = dificil_extra()
print(f"El número se imprimió {veces} veces.")

# Respuesta al ejercicio extra: indagando un poco más y mucha más ayuda de DeepSeek
def get_inputs(): #Función para obtener las palabras del usuario
    print("Bienvenido, por favor ingresa las palabras.")
    param1 = input("Palabra 1: ")
    param2 = input("Palabra 2: ")
    if not param1.strip() or not param2.strip():
        print("Error: Las palabras no pueden estar vacías")
        return get_inputs()
    return param1, param2

def magic_math(param1, param2): #Función para realizar la lógica principal
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(param1 + param2)
        elif i % 3 == 0:
            print(param1)
        elif i % 5 == 0:
            print(param2)
        else:
            print(i)
            contador += 1
    return contador

def main(): #Función principal para ejecutar el programa
    param1, param2 = get_inputs()
    veces = magic_math(param1, param2)
    print(f"El número se imprimió {veces} veces.")

if __name__ == "__main__": #Punto de entrada del programa
    main()