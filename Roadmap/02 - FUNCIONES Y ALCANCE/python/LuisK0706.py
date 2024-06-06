# Funcion sin parametros 

def sin_parametros():
    print(f"Imprimiendo una funcion sin parametros")

sin_parametros() 



# Funcion con parametros
    
def con_parametros(num1, num2):
    print(f"La suma es: {num1 + num2}")

con_parametros(5, 9)



# Funcion con parametros y retorno de datos
    
def con_retorno(num1, num2):
    return num1 + num2

print(con_retorno(8, 7))

# Esta al retornar un dato se le puede asignar a una variable y poder llamarla despues
resultado = con_retorno(8, 7)
print(f"El resultado es: {resultado}")



# Funcion dentro de otra funcion
def primera_funcion():
    print("Dentro de la primera funcion")
    
    def segunda_funcion():
        print("Dentro de la segunda funcion")
    segunda_funcion() # Solo se podra ver si se imprime la funcion principal

primera_funcion()


# Funcion con una variable global
def restando(num1):
    mi_resta = num1 - variable_global
    return mi_resta


# Variable globales una variable que podemos usar en cualquier parte del codigo
variable_global = 5 



# Funcion con una variable local (es aquella que solo se puede usar en un segmento especifico de codigo)
def con_variable_l(num1, num2):
    # La variable mi_suma (variable local) solo se podra usar en esta funcion
    mi_suma = num1 + num2
    return mi_suma



# Ejemplo de una funcion ya creada del lenguaje (funcion len())
mi_cadena = "Esta es una cadena de ejemplo"
print(f"La longitud de la cadena es: {len(mi_cadena)}")



'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''


def numeros(cadena1, cadena2):
    i = 1
    contando_impresiones = 0
    while i < 101:
        if i % 3 == 0 and i % 5 == 0: 
            print(cadena2)
            i += 1
        if i % 3 == 0:
            print(cadena1)
            i += 1
        elif i % 5 == 0:
            print(cadena1 + cadena2)
            i += 1
        else:
            pass
            i += 1
            contando_impresiones += 1
    return f"Se imprimieron {contando_impresiones} numeros"

# Resultado ejercicio extra
print(numeros("Cadena1", "Cadena2"))
