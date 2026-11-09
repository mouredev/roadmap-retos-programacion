# Ejercicio
# 1. Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
# Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
def saludar():
    print("¡Hola desde una función!")

saludar()

def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Misael")
saludar_persona("Abraham")

# Funciones con varios parámetros
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)
    
sumar(5, 3)
sumar(10, 20)

def multiplicar(numero_uno, numero_dos):
    resultado = numero_uno * numero_dos
    return resultado

multiplicacion = multiplicar(4, 5)
print(multiplicacion)

# Función dentro de otras funciones
def operacion_completa(numero_1, numero_2):
    def sumar_interna():
        return numero_1 + numero_2
    resultado = sumar_interna()
    print(f"El resultado de la suma interna es {resultado}")
    
operacion_completa(4, 7)

# Funciones con variables locales y globales
lenguaje = "Python"

def mostrar_alcance():
    mensaje = "Soy una variable local"
    print(lenguaje)
    print(mensaje)
    
mostrar_alcance()
print(lenguaje)

# Funciones del lenguaje
texto = "Python"
numeros = [8, 3, 10, 5]

print(len(texto))
print(max(numeros))
print(min(numeros))
print(sorted(numeros))

# DIFICULTAD EXTRA (opcional):
#Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#La función retorna el número de veces que se ha impreso el número en lugar de los textos.
def imprimir_numeros(texto_1, texto_2):
    contador = 0
    
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto_1 + texto_2)
        elif numero % 3 == 0:
            print(texto_1)
        elif numero % 5 == 0:
            print(texto_2)
        else:
            print(numero)
            contador += 1
        
    return contador
resultado = imprimir_numeros("Fizz", "Buzz")
print(f"Se imprimieron {resultado} números")
