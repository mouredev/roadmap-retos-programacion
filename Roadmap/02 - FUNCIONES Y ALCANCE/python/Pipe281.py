#Función sin parametros ni retorno

def saludar():
    print("Que tal vieja?")

saludar()

#Función con uno o varios parametros y retorno

def suma(a , b):
    return a + b

resultado = suma( 1, 2 )

print(resultado)

def persona(nombre, apellido):
    return nombre + apellido

canditado = persona("Elsa", "Pato")

print("El candidato se llama", canditado)

#Función dentro de función
#Función para multiplicar por si mismo el valor ingresado
def multiplicador(n):
    def interior(x):
        return x * n
    return interior

duplicar = multiplicador(2)
triplicar = multiplicador(3)

print(duplicar(5))  # Resultado: 10
print(triplicar(5))  # Resultado: 15

#Funciones propias de Python
numero = int("10") #Convierte texto en número
print(type(numero))

texto = str(42) #Convierte número en texto
print(type(texto))

longitud = len("Hola") #Imprime el número de caracteres de la palabra
print(longitud)

#Variable Local y Global
def mi_funcion():
    variable_local = "Esto es local"
    print(variable_local)

mi_funcion()

variable_global = "Esto es global"

def otra_funcion():
    print(variable_global)

otra_funcion()
print(variable_global)

'* DIFICULTAD EXTRA (opcional):'
'* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.'
'* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:'
'*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.'
'*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.'
'*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.'
'*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'

def imprimir_numeros(texto1, texto2):
    contador = 100

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
            contador -= 1
        elif numero % 3 == 0:
            print(texto1)
            contador -= 1
        elif numero % 5 == 0:
            print(texto2)
            contador -= 1
        else:
            print(numero)

    return contador

repeticiones = imprimir_numeros("Pipe", "Churrasco")
print("Número de repeticiones:", repeticiones)