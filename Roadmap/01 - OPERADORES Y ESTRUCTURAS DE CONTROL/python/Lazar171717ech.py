## 1. OPERADORES DE LENGUAJE ##

# Aritmeticos #
print(f"Suma: 5 + 2 = {5 + 2}") #Es 7
print(f"Resta: 5 - 2 = {5 - 2}") #Es 3
print(f"Multiplicación: 5 * 2 = {5 * 2}") #Es 10
print(f"División: 5 / 2 = {5 / 2}") #Es 2.5
print(f"División Entera: 5 // 2 = {5 // 2}") #Es 2 (Se quitan los decimales y deja un resultado entero)
print(f"Módulo: 5 % 2 = {5 % 2}") #Es 1 (Se refiere al resto de la división)
print(f"Potencia: 5 ** 2 = {5 ** 2}") #Es 25

# Lógicos #
print(f"True and True = {True and True} / True and False = {True and False}") #Solo será True si ambos son True (True, False)
print(f"True or False = {True or False} / False or False = {False or False}") #Solo será True si uno o ambos son True (True, False)
print(f"not True = {not True} / not False = {not False}") #Cambia de True a False y de False a True (False, True)

# Comparación #
print(f"Mayor: 5 > 2 = {5 > 2} / 2 > 5 = {2 > 5}") #Será True si el primer valor es mayor al segundo (True, False)
print(f"Menor: 5 < 2 = {5 < 2} / 2 < 5 = {2 < 5}") #Será True si el primer valor es menor al segundo (False, True)
print(f"Igual: 5 == 2 = {5 == 2} / 5 == 5 = {5 == 5}") #Será True si los dos valores son iguales (False, True)
print(f"Diferente: 5 != 2 = {5 != 2} / 5 != 5 = {5 != 5}") #Será True si los dos valores son diferentes (True, False)
print(f"Mayor o igual: 5 >= 2 {5 >= 2} / 5 >= 5 = {5 >= 5}") #Será True si el primer valor es mayor al segundo o si ambos son iguales (True, True)
print(f"Menor o igual: 5 <= 2 {5 <= 2} / 5 <= 5 = {5 <= 5}") #Será True si el primer valor es menor al segundo o si ambos son iguales (True, True)

# Asignación #
var: int = 5
var += 2 #Esto sería equivalente a "var = var + 2" por lo que se sumaría al valor de var (var = 7)
var -= 2 #Esto sería equivalente a "var = var - 2" por lo que se restaría al valor de var (var = 5)
var *= 2 #Esto sería equivalente a "var = var * 2" por lo que se multiplicaría al valor de var (var = 10)
var /= 2 #Esto sería equivalente a "var = var / 2" por lo que se dividiría al valor de var (var = 5)

# Identidad #
var1: int = 5
var2: int = 2
print(f"var1 is var2 = {var1 is var2} / var1 is var1 = {var1 is var1}") #Comprobamos si estamos haciendo referencia a la misma instancia (False, True)
print(f"var1 is not var2 = {var1 is not var2} / var1 is not var1 = {var1 is not var1}") #Comprobamos si estamos haciendo referencia a diferente instancia (True, False)
#Podríamos decir que lo que compara no son las variables en sí sino sus id's (id(var1) == id(var2))

# Pertenencia #
lista = [1, 3, 5, 7, 9]
print(f"5 in lista = {5 in lista} / 2 in lista = {2 in lista}") #Comprobamos que la primera parte está en la lista (True, False)
print(f"5 not in lista = {5 not in lista} / 2 not in lista = {2 not in lista}") #Comprobamos que la primera parte NO está en la lista (False, True)

# Bits #
print(f"y: bin(5 & 2) = {bin(5 & 2)} / bin(5 & 4) = {bin(5 & 4)}") #Aquí se comparan los bits de los números por parejas siendo 1 si ambos son 1 (0b0, 0b100)
print(f"o: bin(5 | 2) = {bin(5 | 2)} / bin(5 | 4) = {bin(5 | 4)}") #Aquí se comparan los bits de los números por parejas siendo 1 si al menos alguno de los dos es 1 (0b111, 0b101)
print(f"xor: bin(5 ^ 2) = {bin(5 ^ 2)} / bin(5 ^ 4) = {bin(5 ^ 4)}") #Aquí se comparan los bits de los números por parejas siendo 1 si solo uno de los dos es 1 (0b111, 0b1)
print(f"not: ~bin(5) = {bin(~5)} / ~bin(2) = {bin(~2)}") #Aquí se cambian cada uno de los bits de 1 a 0 y de 0 a 1. Aquí lo que hace es el contrario.
print(f"deslizar a la derecha: bin(5>>2) = {bin(5>>2)} / bin(2>>2) = {bin(2>>2)}") #Aquí traslada los bits ciertas unidades a la derecha (0b1, 0b0)
print(f"deslizar a la izquierda: bin(5<<2) = {bin(5<<2)} / bin(2<<2) = {bin(2<<2)}") #Aquí traslada los bits ciertas unidades a la izquierdas (0b10100, 0b1000)

## 2. ESTRUCTURAS DE CONTROL ##

# Condicional #

if "Hola" == "Adiós": #Aquí se realiza una condición y solo si esta es True se ejecuta el codigo.
    print("Es el fin del mudo") #Este es el codigo que se ejecuta si la condición es True.
elif "Hola" == "Hasta mañana": #Esta condición solo se ejecutará si la anterior no lo hizo. elif viene de un "else: if:"
    print("Es el fin del mundo") #Este es el codigo que se ejecuta si la segunda condición es True.
else: #Esta condición solo se ejecutará si todas las anteriores no lo hicieron.
    print("Todo bien") #Este es el codigo que se ejecuta si la última condición es True.

# Bucle while #

var: int = 0
while var <= 10: #Se establece una condición que se comprueba en cada ciclo
    var += 1
    print(var) #El código dentro del bucle se ejecutará continuamente hasta que la condición deje de cumplirse
print("¡Bucle terminado!")

# Bucle for #

for index in range(0, 10): #Se establece una variable que recorrerá un contenedor dandole cada valor del contenedor en cada ciclo
    if index == 3: #Cuando hacemos referencia al index dentro del bucle hacemos referencia a su valor en el ciclo
        continue #El continue hace saltar al bucle al siguiente ciclo
    print(index)
print("¡Bucle terminado!")

# Excepción #

try:
    var: int = int("Hola") #Intenta realizar la operación
except ValueError: #Si en la operación del try surge un error, en este caso un ValueError, Ejecutará el codigo
    print("Error!")

## 3. EJERCICIO EXTRA ##

for index in range(10, 56, 2):
    if index != 16 and index % 3 != 0:
        print(index)
