'''
Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
'''
# Funciones definidas por el usuario:
# Con retorno y con variables -------------------------------------
resta = 0

def restar(variable1, variable2):
    resta = variable1- variable2
    return resta

resta = restar(1, 2) # Asignar el resultado de la función a la variable suma
print(resta) # Imprimir el valor actualizado de la variable suma

# Con retorno y sin variables -------------------------------------
def sumar ():
    return (1+2)

print (sumar())

# Podría declararla definiendo lo que me tiene que devolver:
def sumar () -> str:  # digo que devuelve una string
    return (1+2)

print (sumar())

# Sin retorno y con variable -------------------------------------
def saludar(nombre):
    print("¡Hola, " + nombre + "!")

saludar("Troy")

# Sin retorno y sin variables -------------------------------------
def saludar():
    print("¡Hola mundo!")

saludar()

# Con parámetro por defecto, por si quiero llamarla si darle un valor al argumento -------------------------------------
def saludar(nombre="persona sin nombre"): # Si no le damos ninguno, que salude al desconocido
    print("¡Hola, " + nombre + "!")

saludar()

# Con argumentos sin orden -------------------------------------
def saludar(saludo, nombre):
    print("¡",saludo, ",", nombre, "!") # Así me pondría un espacio al lado de cada ¡ Hola , Troy !
    print (f"¡{saludo}, {nombre}!") # Así sale ¡Hola Troy! 

saludar(nombre="Troy", saludo="Hola") # en orden aunque yo al llamar a la función lo ponga desordenado pero le digo cual es cual

# Con retorno de más de un valor (una tupla) -------------------------------------
def multiple_retorno ():
    return "Hola", "Python"  #retorna 2 cadenas de texto
print (multiple_retorno()) #Muestra ('Hola', 'Python') los dos valores acoplados con paréntesis y coma entre ellos

def multiple_retorno2 ():
    return "Hi", "Python 🐍" 
saludo2, lenguaje2 =multiple_retorno2() # descompongo los valores y los introduzco en variables
print (saludo2)
print (lenguaje2)
print(f"¡{saludo2}, {lenguaje2}!")

# Una función lambda -------------------------------------
# función anónima y pequeña que puede tener cualquier número de argumentos, pero solo puede tener una expresión. 
sumar = lambda x, y: x + y
result_lambda = sumar(3, 5)
print(result_lambda)  


'''
Comprueba si puedes crear funciones dentro de funciones. -------------------------------------
'''

def imprimir ():
    def obtener_resultado (var1, var2, var3):
        resultado = (var1+var2)*var3
        return resultado

    resultado_calculado = obtener_resultado(1, 2, 3)  # Llamada a la función anidada/interna obtener_resultado y almacenamiento del resultado
    
    print(resultado_calculado)  # Imprimir el resultado almacenado

imprimir() # Llamada a la función principal

'''
Utiliza algún ejemplo de funciones ya creadas en el lenguaje
'''
# la función upper vuelve la cadena/texto/string a mayúsculas -------------------------------------
def imprimir_mayusculas(texto):
    def convertir_a_mayusculas(cadena):
        mayusculas = cadena.upper()   # upper() es una función interna del lenguaje asociada al tipo de dato
        return mayusculas

    texto_en_mayusculas = convertir_a_mayusculas(texto) # Llamada a la función anidada
    
    print(f"Texto en mayúsculas: {texto_en_mayusculas}")  # Imprimir resultados, más elegante poner el formato del texto con la f
                                                          # print("Texto en mayúsculas:", texto_en_mayusculas)  -> Otra opción
    
imprimir_mayusculas ("Troy Nebula") # Troy Nebula es el valor de la variable texto


# función con i cantidad de parametros que devuelve cantidad de números y suma de ellos -------------------------------------
def suma(*i):  
    print(f"Parametros introducidos: {len(i)}")  #len
    print(f"Resultado de la suma {sum(i)}")   #sum
    
suma(1, 3, 5, 7, 9)
suma(2, 4, 6, 8, 10)

# otro ejemplo de un número variable de elementos -------------------------------------
def saludos (*names):
    for name in names:
        print (f'Hola, {name}!')

saludos ("Troy", "Nebula", "Brais")

# otro ejemplo de un número variable de argumentos (+ exclusivo de Python) -------------------------------------
def saludos2 (**names):  #le podemos incluir una clave dentro de cada argumento con los **
    for param_key, value in names.items():   #items() acaba desomponiendo cada uno de los parámetros en clave=valor
        print (f'Hola, {value}, {param_key}!')

saludos2 (
    nombre="Troy", 
    nick="Nebula", 
    edad= 45)

# funcion que retorna mas de un número, el mínimo y el máximo de los que se introducen -------------------------------------
def minimo_y_maximo(*numeros):  
    return min(numeros), max(numeros)   # min   y   max

minimo, maximo = minimo_y_maximo (613, 6, 17, 101, 19, 111, 8001)
print(f"Mínimo: {minimo}, Máximo: {maximo}")

# otras funciones del lenguaje -------------------------------------
var_input = input("Escribe algo, texto o número aquí, para guardarlo en una variable y pulsa Enter: ")
print("Lo que has introducido es:", var_input)
# la función input() siempre lee la entrada cadena/string, incluso si ingreso un número
# así que lo tengo que convetir a número int (o float) asi:
try:
    var_algo = int(var_input)
    tipo = type(var_algo)
    print("Lo introducido es de clase:", tipo, "es decir, un número entero.")
except ValueError:
    print("Lo introducido no es un número, así que será un texto.")

print(len([0, 1, 2, 3, 4, 5])) # devuelve la cantidad de elementos que posee
print(str(1)) # convierte a texto
print(int("1")) # convierte a entero
print(float("20.55")) # convierte a decimal
print(sorted([1,3,55,8,2,11,0,31,7,6])) # ordena los elementos de una lista



'''
Pon a prueba el concepto de variable LOCAL y GLOBAL -------------------------------------
'''

variable_global = "Global" # Variable global -> Fuera de la función

def funcion_con_variable_local(): # Variable local -> dentro de la función
    
    variable_local = "Local"
    print(f"Dentro de la función: {variable_local}")
    print(f"Dentro de la función (solo sirve la global): {variable_global}")

funcion_con_variable_local() # Llamada a la función

# Intento acceder a la variable local desde fuera de la función (resultará en un error)
# print(f"Fuera de la función: {variable_local}")  # Comento esta línea porque da error, fuera de la función no está definida y no la puedo llamar

print(f"Fuera de la función: {variable_global}")  # Acceso a la variable global desde fuera de la función

'''
DIFICULTAD EXTRA (opcional): -------------------------------------
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 '''

def retornar_num (str1, str2):  # variables de tipo texto/string
    for n in range (1,101):
        if n % 3 ==0 and n % 5 !=0:
            print (str1)
        elif n % 5==0 and n % 3 !=0:
            print (str2)
        elif n % 3 ==0 and n % 5 ==0:
            print (str1, "y", str2)
        else:
            print (n)
            n +=1  #  n ==n+1   -> otra manera de escribirlo, que aumente de uno en uno el número que va iterando
    return n

retornar_num("Múltiplo Tres", "Múltiplo Cinco")
    