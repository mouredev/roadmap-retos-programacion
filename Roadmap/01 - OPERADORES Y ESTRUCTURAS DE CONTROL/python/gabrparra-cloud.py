## ME EQUIVOQUE DE CARPETA, DESARROLLARE EL EJERCICIO EN LA CARPETA CORRECTA, PERO DEJO ESTE ARCHIVO COMO REFERENCIA

# Un comentario
# URL del sitio web oficial del lenguaje de programación que has seleccionado
# URL: https://www.python.org/
# Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...)
"""
Comentario de varias líneas
"""
'''
Comentario de varias líneas
'''

Var_bool= True              #boolean
Var_int= 10                 #integer
Var_float= 10.5             #float
Var_string= "Hola Mundo"    #string

VAR_CONSTANT= 3.1416        #constante por convención se escribe en mayúsculas

print("¡Hola, Python!")     #Primer print



#Tipos de operadores


#Operadores de asignación

print("Operaciones de asignación ")
var_a= 10
var_b= 5
print("var_a inicial :", var_a)  #valor inicial de la variable var_a
print("var_b inicial :", var_b) #valor inicial de la variable var_b

var_a+= 5
var_b-= 5
print("var_a+ :", var_a)    #suma de 5 a la variable var_a
print("var_b- :", var_b)    #resta de 5 a la variable var_b

var_a= 10
var_b= 5
var_a*= 5
var_b/= 5
print("var_a* :", var_a) #multiplicación de 5 a la variable var_a
print("var_b/ :", var_b) #división de 5 a la variable var_b

var_a= 10
var_b= 5
var_a%= 5
var_b//= 5
print("var_a% :", var_a) #modulo de 5 a la variable var_a
print("var_b// :", var_b) #división entera de 5 a la variable var_b


var_a= 10
var_b= 5
var_a**= 5
var_b&= 1
print("var_a** :", var_a)   #exponente de 5 a la variable var_a
print("var_b& :", var_b) #operador AND de 5 a la variable var_b

var_a= 10
var_b= 5
var_a|= 7
var_b^= 5
print("var_a| :", var_a)   #operador OR de 5 a la variable var_a
print("var_b^ :", var_b) #operador XOR de 5 a la variable var_b

var_a= 10
var_b= 5
var_a>>= 5
var_b<<= 5
print("var_a>> :", var_a)   #operador desplazamiento a la derecha de 5 a la variable var_a
print("var_b<< :", var_b) #operador desplazamiento a la izquierda de 5 a la variable var_b

print("------------------------------------------------------------------------\n")

# Operadores aritméticos
print("Operaciones aritméticas ")
var_a= 10
var_b= 5

suma= var_a + var_b
resta= var_a - var_b
multiplicacion= var_a * var_b
division= var_a / var_b
modulo= var_a % var_b
division_entera= var_a // var_b
exponente= var_a ** var_b

print("Suma :", suma)
print("Resta :", resta) 
print("Multiplicación :", multiplicacion)
print("División :", division)
print("Módulo :", modulo)
print("División entera :", division_entera)
print("Exponente: ", exponente)

print("------------------------------------------------------------------------\n")

#Operadores de comparación

print("Operaciones de comparación ")
var_a= 10
var_b= 5

print("var_a :", var_a)
print("var_b :", var_b)
print("var_a == var_b :", var_a == var_b) #igualdad
print("var_a != var_b :", var_a != var_b) #diferente
print("var_a > var_b :", var_a > var_b)   #mayor que
print("var_a < var_b :", var_a < var_b)   #menor que
print("var_a >= var_b :", var_a >= var_b) #mayor o igual que
print("var_a <= var_b :", var_a <= var_b) #menor o igual que    

var_string= "Hola"
var_string2= "Holaa"

print("var_string :", var_string)
print("var_string2 : ", var_string2)
print("var_string == var_string2: ", var_string == var_string2) #igualdad
print("var_string != var_string2: ", var_string != var_string2) #diferente
print("var_string > var_string2: ", var_string > var_string2)   #mayor que
print("var_string < var_string2: ", var_string < var_string2)   #menor que
print("var_string >= var_string2: ", var_string >= var_string2) #mayor o igual que
print("var_string <= var_string2: ", var_string <= var_string2) #menor o igual que

print("------------------------------------------------------------------------\n")

#Operadores de identidad

print("Operaciones de identidad ")


print("1 is 1 :", 1 is 1)                   
print("1 is not 2 :", 1 is not 2)     
print("9 is 3 ** 3 :", 9 is 3 ** 2)  
print("9 is 2 ** 3 :", 9 is 2 ** 3)

print("------------------------------------------------------------------------\n")

#Operadores de pertenencia

print("Operaciones de pertenencia ")


print("A in Avion :", "A" in "Avion") 
print("B not in Avion :", "B" not in "Avion") 
print("hola in Hola mundo :", "hola" in "Hola mundo") 
print("hola in hola mundo :", "hola" in "hola mundo") 
print("a in casa :", "a" in "casa")      


print("------------------------------------------------------------------------\n")

# Operadores lógicos

print("Operaciones lógicas ")

print("3 > 2 and 4 > 3 :",3 > 2 and 4 > 3) 
print("3 > 2 and 4 < 3 :",3 > 2 and 4 < 3) 
print("3 < 2 and 4 < 3 :",3 < 2 and 4 < 3) 
print("3 > 2 or 4 > 3 :",3 > 2 or 4 > 3)  
print("3 > 2 or 4 < 3 :",3 > 2 or 4 < 3)  
print("3 < 2 or 4 < 3 :",3 < 2 or 4 < 3)  
print("not 3 > 2 :",not 3 > 2)     
print("not True :",not True)      
print("not False :",not False)     
print("not not True :",not not True)  
print("not not False :",not not False) 

print("------------------------------------------------------------------------\n")

##Estructuras de control

# Estructuras de control condicionales

print("Estructuras de control condicionales ")

var_a= 10
var_b= 5
if var_a > var_b:
    print("var_a es mayor que var_b")
elif var_a == var_b:
        print("var_a es igual a var_b")
else:
    print("var_a es menor que var_b")


# Estructuras de control iterativas 

# For

numbers = [12, 7, 20, 15, 3]

for number in numbers:
    if number % 2 == 0:
        print(f"El número {number} es PAR.")
    else:
        print(f"El número {number} es IMPAR.")

# while

ahorro = 0
meta = 50

while ahorro < meta:
    ahorro += 15 
    print(f"Llevas ahorrado: ${ahorro}")
    
    if ahorro >= meta:
        print("¡Meta alcanzada!")
        break  

print("Proceso finalizado.")

# Manejo de excepciones

#var_a = "10"
var_a = 10
#var_b = 0
var_b = 2

try:
    # Operador aritmético de división
    division = var_a / var_b
    print(f"Resultado: {division}")
except Exception as e:
    # Se ejecuta solo si ocurre una división por cero
    print(f"Error: {e}")
else:
    # Se ejecuta solo si NO hubo ningún error
    print("La división se realizó con éxito.")
finally:
    # Se ejecuta SIEMPRE, haya o no error
    print("Fin del bloque de control de errores.\n")


"""
     * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)