"Aritméticos"

print("Aritméticos") #Operadores que realizan operaciones matemáticas básicas
print("Suma: ", 7 + 8) #Suma de dos números
print("Resta: ", 1 - 4) #Resta de dos números
print("Multiplicación: ", 12 * 4) #Multiplicación de dos números
print("División: ", 12 / 4) #División de dos números
print("Módulo: ", 10 % 3) #Resto de la división
print("Exponente ", 7** 3) #Potencia (un numero elevado a otro)
print("División entera: ", 70 // 20) #División sin decimales

print("--------------------------------------------------")

"Asignación"

print("Asignación") #Operadores que asignan valores a las variables y realizan operaciones con ellas

x = 4 #Asignación de un valor a cada variable
y = 10
z = 5
a = 3
b = 8
c = 2

print("Valor de x: ", x ) #Impresión del valor de la variable
print("Valor de y: ", y )
print("Valor de z: ", z )
print("Valor de a: ", a )
print("Valor de b: ", b )
print("Valor de c: ", c )

x += 3 #Incremento del valor de la variable en 3 (Equivalente a x = x + 3)
print("Valor de x después de +=3: ", x) #Impresión del nuevo valor de la variable

y -= 2 #Decremento del valor de la variable en 2 (Equivalente a y = y - 2)
print("Valor de y después de -=2: ", y) #Impresión del nuevo valor de la variable

z *= 4 #Multiplicación del valor de la variable por 4 (Equivalente a z = z * 4)
print("Valor de z después de *=4: ", z) #Impresión del nuevo valor de la variable

a /= 3 #División del valor de la variable entre 3 (Equivalente a a = a / 3)
print("Valor de a después de /=3: ", a) #Impresión del nuevo valor de la variable

b %= 4 #Resto de la división del valor de la variable entre 4 (Equivalente a b = b % 4)
print("Valor de b después de &=4: ", b) #Impresión del nuevo valor de la variable

c **= 3 #Potencia del valor de la variable elevado a 3 (Equivalente a c = c ** 3)
print("valor de c después de **=3: ", c)

print("--------------------------------------------------")

"Comparación"

print("Comparación") #Operadores que comparan dos valores y devuelven un valor booleano (True o False)

print("¿Es 5 igual a 5?: ", 5 == 5) #Comparación de igualdad entre dos valores
print("¿Es 5 diferente a 3?: ", 5 != 3) #Comparación de desigualdad entre dos valores
print("¿Es 6 mayor que 8?: ", 6 > 8) #Comparación de mayor que entre dos valores
print("¿Es 6 menor que 8?: ", 6 < 8) #Comparación de menor que entre dos valores
print("¿Es 7 mayor o igual que 7: ", 7 >= 7) #Comparación de mayor o igual que entre dos valores
print("¿Es 8 menor o igual a 10?: ", 8 <= 10) #Comparación de menor o igual que entre dos valores

print("--------------------------------------------------")

"Logicos"

print("Lógicos") #Operadores que combinan expresiones booleanas y devuelven un valor booleano (True o False)

"and, or, not" #and (y), or (o), not (no)
"""Con And:
True and True = True
True and False = False
False and False = False
False and True = False
"""

print("Es True y False?: ", True and False) #Devuelve True si ambas expresiones son True
print("Es True y True?: ", True and True) #Devuelve True si ambas expresiones son True
print("Es False y False?: ", False and False) #Devuelve True si ambas expresiones son True
print("Es False y True?: ", False and True) #Devuelve True si ambas expresiones son True

"""Con Or:
True or True = True
True or False = True
False or False = False
False or True = True
"""
print("Es True o False?: ", True or False) #Devuelve True si al menos una de las expresiones es True
print("Es True o True?: ", True or True) #Devuelve True si al menos una de las expresiones es True
print("Es False o False?: ", False or False) #Devuelve True si al menos
print("Es False o True?: ", False or True) #Devuelve True si al menos una de las expresiones es True

"""Con Not:
not True = False
not False = True
"""

print("No es True?: ", not True) #Invierte el valor de la expresión (True a False y viceversa)
print("No es False?: ", not False) #Invierte el valor de la expresión (True a False y viceversa)

print("--------------------------------------------------")

"Identidad"

print("Identidad") #Operadores que comparan la identidad de dos objetos

x = [1, 5]
y = [1, 5]
z = x

print("¿Es x igual a y?: ", x == y) #Comparación de igualdad entre dos objetos
print("¿Es x idéntico a y?: ", x is y) #Comparación de identidad entre dos objetos
print("¿Es x idéntico a z?: ", x is z) #Comparación de identidad entre dos objetos
print("¿Es x no idéntico a y?: ", x is not y) #Comparación de no identidad entre dos objetos
print("¿Es x no idéntico a z?: ", x is not z) #Comparación de no identidad entre dos objetos

print("--------------------------------------------------")

"Pertenencia"

print("Pertenencia") #Operadores que comprueban la pertenencia de un elemento a una secuencia (como listas, tuplas o cadenas de texto)

Carros = [ "BMW", "Mercedes", "Volkswagen"] #Lista de carros

print("¿Está BMW en la lista de carros?: ", "BMW" in Carros) #Comprueba si un elemento está en la lista
print("¿Está Audi en la lista de carros?: ", "Audi" in Carros) #Comprueba si un elemento está en la lista
print("No está Audi en la lista de carros: ", "Audi" not in Carros) #Comprueba si un elemento no está en la lista
print("No está BMW en la lista de carros: ", "BMW" not in Carros) #Comprueba si un elemento no está en la lista

print("--------------------------------------------------")

"Bit a bit"

print("Bit a bit") #Operadores que realizan operaciones a nivel de bits en números enteros

x =10 #Nümero entero 10 en binario es 1010
y = 4 #Número entero 4 en binario es 0100

print("AND bit a bit (x & y): ", x & y) #Operador AND bit a bit
print("AND bit a bit (y & x): ", y & x) #Operador AND bit a bit

print("OR bit a bit (x | y): ", x | y) #Operador OR bit a bit
print("OR bit a bit (y | x): ", y | x) #Operador OR bit a bit

print("XOR bit a bit (x ^ y): ", x ^ y) #Operador XOR bit a bit
print("XOR bit a bit (y ^ x): ", y ^ x) #Operador XOR bit a bit

print("NOT bit a bit (~x): ", ~x) #Operador NOT bit a bit
print("NOT bit a bit (~y): ", ~y) #Operador NOT bit a bit

print("Desplazamiento a la izquierda (x << 2): ", x << 2) #Desplazamiento de bits a la izquierda
print("Desplazamiento a la izquierda (y << 3): ", y << 3) #Desplazamiento de bits a la izquierda

print("Desplazamiento a la derecha (x >> 2): ", x >> 2) #Desplazamiento de bits a la derecha
print("Desplazamiento a la derecha (y >> 1): ", y >> 1) #Desplazamiento de bits a la derecha

print("--------------------------------------------------")

"Operadores especiales"

print("Operadores especiales") #Operadores que realizan operaciones específicas en ciertos tipos de datos

print("Concatenación de cadenas: ", "Hola" + " " + "Mundo") #Concatenación de cadenas de texto
print("Repetición de cadenas: ", "Hola" * 3) #Repetición de una cadena de texto
print("Concatenación de listas: ", [1, 2, 3] + [4, 5, 6]) #Concatenación de listas
print("Repetición de listas: ", [1, 3, 5] * 2) #Repetición de listas
print("Concatenación de tuplas: ", (1, 2, 3) + (4, 5, 6)) #Concatenación de tuplas
print("Repetición de tuplas: ", (1, 3, 5) * 2) #Repetición de tuplas
print("Concatenación de conjuntos: ", {1, 2, 3} | {3, 4, 5}) #Unión de conjuntos
print("Intersección de conjuntos: ", {1, 2, 3} & {3, 4, 5}) #Intersección de conjuntos
print("Diferencia de conjuntos: ", {1, 2, 3} - {3, 4, 5}) #Diferencia de conjuntos
print("Diferencia simétrica de conjuntos: ", {1, 2, 3} ^ {3, 4, 5}) #Diferencia simétrica de conjuntos
print("Repetición de cadenas con f-string: ", f"{'Hola' * 3}") #Repetición de cadenas de texto usando f-string
print("Repetición de listas con f-string: ", f"{[1, 3, 5] * 2}") #Repetición de listas usando f-string
print("Repetición de tuplas con f-string: ", f"{(1, 3, 5) * 2}") #Repetición de tuplas usando f-string
print("Concatenación de cadenas con f-string: ", f"{'Hola' + ' ' + 'Mundo'}") #Concatenación de cadenas de texto usando f-string
print("Concatenación de listas con f-string: ", f"{[1, 2, 3] + [4, 5, 6]}") #Concatenación de listas usando f-string
print("Concatenación de tuplas con f-string: ", f"{(1, 2, 3) + (4, 5, 6)}") #Concatenación de tuplas usando f-string
print("Concatenación de conjuntos con f-string: ", f"{ {1, 2, 3} | {3, 4, 5} }") #Unión de conjuntos usando f-string
print("Intersección de conjuntos con f-string: ", f"{ {1, 2, 3} & {3, 4, 5} }") #Intersección de conjuntos usando f-string
print("Diferencia de conjuntos con f-string: ", f"{ {1, 2, 3} - {3, 4, 5} }") #Diferencia de conjuntos usando f-string
print("Diferencia simétrica de conjuntos con f-string: ", f"{ {1, 2, 3} ^ {3, 4, 5} }") #Diferencia simétrica de conjuntos usando f-string

print("--------------------------------------------------")

"Estructuras de control"

print("Estructuras de control") #Estructuras que permiten controlar el flujo de ejecución del programa usando operadores

"Condicionales"

print("Condicionales") #Estructuras que permiten ejecutar código según una condición

"if, elif, else" #if (si), elif (sino si), else (sino)

Edad = int(input("Ingresa tu edad: ")) #Entrada de la edad del usuario

if Edad < 18: #Si la edad es menor a 18
    print("Eres menor de edad.") #Imprime que es menor de edad

elif Edad >= 18 and Edad < 65: #Si la edad es mayor o igual a 18 y menor a 65
    print("Eres adulto.") #Imprime que es adulto
    
elif Edad >=100: #Si la edad es mayor o igual a 100
    print("Eres una persona centenaria.") #Imprime que es una persona centenaria

else: #Si la edad es mayor o igual a 65
    print("Eres adulto mayor.") #Imprime que es adulto mayor


print("--------------------------------------------------")

"Interactivas"

print("Interactivas") #Estructuras que permiten repetir código mientras una condición sea verdadera

"while, for, break, continue" #while (mientras), for (para), break (romper), continue (continuar)

print("Ejemplo con while:") #Ejemplo de uso de while

contraseña = "" #Contraseña inicialmente vacía
while contraseña != "Felix": #Mientras la contraseña sea diferente a "Felix" se repite el ciclo
    contraseña = input("Ingresa la contraseña por favor: ") #Entrada de la contraseña del usuario
    if contraseña != "Felix": #Si la contraseña es diferente a "Felix"
        print("Contraseña incorrecta, intente de nuevo.") #Imprime que la contraseña es incorrecta2

else: #Si la contraseña es igual a "Felix"
    print("Has ingresado correctamente.") #Imprime que ha ingresado correctamente

print("Ejemplo con for:") #Ejemplo de uso de for

comida = ["Pizza", "Hamburguesa", "Enchiladas", "Sushi"] #Lista de comidas favoritas

for plato in comida: #Para cada plato en la lista de comidas
    if plato == "Pizza": #Si el plato es "Pizza"
        print("Mi favorita es Pizza") #Imprime un mensaje específico para la Pizza

        continue #Continúa con la siguiente iteración del ciclo

    print(f"Me gusta comer {plato}") #Imprime el plato que te guste también
    if plato == "Sushi": #Si el plato es "Sushi"

        break #Rompe el ciclo

print("--------------------------------------------------")

"Excepciones"

print("Excepciones") #Estructuras que permiten manejar errores en el código

"try, except, finally" #try (intentar), except (excepto), finally (finalmente)

try: #Intenta ejecutar el siguiente bloque de código

    x =int(input("Ingresa un número: ")) #Entrada de un número del usuario
    f = 20 // x #División del número entre 20


except ValueError:
    print("Error: Debes ingresar un número válido.") #Imprime que el número no es válido

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.") #Imprime que no se puede dividir entre cero

else:
    print("El resultado de 20 dividido entre", x, "es:", f) #Imprime el resultado de la división si no hay errores

finally: 
    print("Gracias por usar el programa.") #Imprime un mensaje de agradecimiento al final

print("--------------------------------------------------")

"Funciones"

print("Funciones") #Estructuras que permiten definir bloques de código reutilizables

"def, return" #def (definir), return (retornar)

def saludar(nombre): #Definición de una función que saluda a una persona
    return f"Hola, {nombre}" #Retorna el saludo con el nombre de la persona

nombre = input("Ingresa tu nombre: ") #Entrada del nombre del usuario
print(saludar(nombre)) #Imprime el saludo con el nombre del usuario

print("--------------------------------------------------")

"Clases"

print("Clases") #Estructuras que permiten definir objetos con atributos y métodos

class Animales: #Definición de una clase llamada Animales
    def __init__(self, nombre, especie): #Método constructor que inicializa los atributos de la clase
        self.nombre = nombre #Atributo nombre
        self.especie = especie #Atributo especie
    
    def tipo_alimentación(self, alimentación): #Método que define el tipo de alimentación del animal
        self.alimentación = alimentación #Atributo alimentación
        return f"{self.nombre} es un {self.especie} y se alimenta de {self.alimentación}" #Retorna una descripción del animal

Animal1 = Animales(nombre = input("Ingresa el nombre del León: "), especie = "León") #Creación de un objeto de la clase Animales
print(Animal1.tipo_alimentación(input(f"Ingresa el tipo de alimentación de {Animal1.nombre}: "))) #Imprime la descripción del animal con su tipo de alimentación

Animal2 = Animales(nombre = input("Ingresa el nombre del perro: "), especie = "perro") #Creación de otro objeto de la clase Animales
print(Animal2.tipo_alimentación(input(f"Ingresa el tipo de alimentación de {Animal2.nombre}: "))) #Imprime la descripción del animal con su tipo de alimentación

print("--------------------------------------------------")

"Dificultad extra"

print("Dificultad extra") #Ejemplos adicionales de estructuras de control y operadores
print("Crea un programa que imprima por consola todos\
 los números comprendidos entre 10 y 55 (incluidos)\
 pares, y que no son ni el 16 ni múltiplos de 3.")

for num in range(10, 56): #Para cada número en el rango de 10 a 55
    multi3 = num % 3 == 0 #Variable que almacena el resultado de la operación módulo para determinar si un número es múltiplo de 3
    par = num % 2 == 0 #Variable que almacena el resultado de la operación módulo para determinar si un número es par
    if par and num != 16 and not multi3: #Si el número es par, diferente a 16 y no es múltiplo de 3
        print(num) #Imprime el número que cumple con las condiciones

print("--------------------------------------------------")