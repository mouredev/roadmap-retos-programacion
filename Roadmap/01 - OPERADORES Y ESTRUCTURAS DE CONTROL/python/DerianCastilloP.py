######################## Operadores Aritmeticos ########################

print("# Operadores Aritmeticos #\n")

x = 3
y = 4

suma = x + y            #7
print(f"El resultado de {x} + {y} es = {suma}")

resta = x - y           #-1
print(f"El resultado de {x} - {y} es = {resta}")

multip = x * y          #12
print(f"El resultado de {x} * {y} es = {multip}")

division = x / y        #0.75
print(f"El resultado de {x} / {y} es = {division}")

modulo = x % y          #3 (el modulo es el mismo numero ya que como el 4 que el 3
print(f"El resultado de {x} % {y} es = {modulo}")

exponencial = x ** y    #81
print(f"El resultado de {x} ** {y} es = {exponencial}")

floor_div = x // y      #0
print(f"El resultado de {x} // {y} es = {floor_div}")


######################## Operadores de asignacion  ########################
print("\n\n## Operadores de Asignacion ##\n")

nombre_var = 7
print(f"Operador '=' asigna a 'nombre_variable' un valor Ej: x = {nombre_var}")

nombre_var += 2
print(f"Operador '+=' asigna a 'nombre_variable' un valor + el valor anterior de la variable Ej: x += 2 resultado es {nombre_var}")

nombre_var -= 4
print(f"Operador '-=' asigna a 'nombre_variable' un valor - el valor anterior de la variable Ej: x -= 4 resultado es {nombre_var}")

print("""\nEsto se puede hacer con todos los Operadores Aritmeticos agregandole un igual '=' 
Ej: '*=', '/=', '%=', '//=', '**=' asiendo la su respectiva operacion con la variable y
agregandole el resultado a la minma variable""")


######################## Operadores de comparacion  ########################


print("\n\n### Operadores de comparacion ###\n")

c = x == y # compara si es igual
print(f"{x} es Igual a {y} ? = {c}")

c = x != y # compara si es diferente
print(f"{x} es Diferente a {y} ? = {c}")

c = x < y # compara si es menor
print(f"{x} es Menor que {y} ? = {c}")

c = x > y # compara si es mayor
print(f"{x} es Mayor que {y} ? = {c}")

c = x <= y # compara si es menor o igual
print(f"{x} es menor o igual que {y} ? = {c}")

c = x >= y # compara si es mayor o igual
print(f"{x} es Mayor o igual que {y} ? = {c}")


######################## Operadores Logicos  ########################


print("\n\n#### Operadores Logicos ####")

verdadero = True
falso = False

print("\nSiendo V = Verdadero y Siendo F = Falso")
print("\nOperador 'and'")
# "and" si ambos son verdadero entonces es True de lo contrario es False
print("V and V = ", verdadero and verdadero)
print("V and F = ", verdadero and falso)
print("F and V = ", falso and verdadero)
print("F and F = ", falso and falso)

print("\nOperador 'or'")
# "or" si almenos hay un verdadero entonces es True de lo contrario es False
print("V or V = ", verdadero or verdadero)
print("V or F = ", verdadero or falso)
print("F or V = ", falso or verdadero)
print("F or F = ", falso or falso)

print("\nOperador 'not'")
# "not" Invierte el resultado vamos a poner un ejemplo con el operador "or"
print("(not) V or V = ", not(verdadero or verdadero))
print("(not) V or F = ", not(verdadero or falso))
print("(not) F or V = ", not(falso or verdadero))
print("(not) F or F = ", not(falso or falso))


######################## Operadores de Identidad  ########################


print("\n\n##### Operadores de Identidad #####")

# Los operadores de identidad indican si dos variables hacen referencia al mismo
# objeto, por ejemplo para saber si dos variables distintas tienen el mismo id.

print("'x' referencia al mismo valor que 'y'? : ", x is y)
print("'x' referencia no al mismo valor que 'y'? : ", x is not y)


######################## Operadores de membresia  ########################

print("\n###### Operadores de Membresia ######")

#Los operadores de membresía se utilizan para probar si un elemento esta
#dentro de una secuencia, como una lista por ejemplo.

listas = ["carro", "motor", "patin", "avion"]
vehiculo = "motor"

print(listas)
print("\nEl Vehiculo 'carro' esta en la lista? : ", vehiculo in listas)
print("El Vehiculo 'carro' no esta en la lista? : ", vehiculo not in listas)

######################################################################################################
################################### TIPOS DE ESTRUCTURAS DE CONTROS ##################################
###################################      QUE EXISTEN EN PYTHON     ###################################
######################################################################################################


######################## Condicionales  ########################


print("\n\n# Condicionales #\n")

#Las estructuras condicionales permiten ejecutar código según una condición.

print('En estas tenemos "if" si se cumple una condicion')

#Ejemplos 'if', 'else', 'elif'
if x < y:
    print("Ejemplo 1: x es menor que y")

#Tenemos el "else" por si no se cumple la condicion
if x > y:
    print("Ejemplo 2: x es mayor que y")
else:
    print("Ejemplo 2:la condicion no se cumplio")

#si queremos evaluar multiples condiciones podemos usar "elif"

if x > y:
    print("Ejemplo 3: x es mayor que y")
elif x < y:
    print("Ejemplo 3: x es menor que y")
else:
    print("Ejemplo 3:la condicion no se cumplio")


############################ Bucles  #############################

print("\n\n## Bucles For ##\n")

#Los bucles permiten repetir código varias veces

print('*Bucle "for" es un blucle que itera sobre una secuencia\n')

#Ejemplo "for"
print("Ejemplo_1")
for numero in range(7):
    print(f"Numero: {numero}")

print("\n")

#Ejemplo "for" con listas

print("Ejemplo_2")
for vehiculo in listas:
    print( vehiculo.title())

## for + enumerate() ##

print('''\n*Bucle "for" tambien lo puedes usar con la funcion "enumrate" para 
saber he imprimir el indice de los elementos en la lista\n''')

print("Ejemplo_3")
for indice, vehiculo in enumerate(listas):
    print(f'{indice} : {vehiculo}')

## for + zip() ##

print('''\n*Bucle "for" tambien lo puedes usar con la funcion "zip" para 
para recorrer 2 listas a la vez\n''')

print("Ejemplo_4")
precios = [898, 387, 77, 7123]

for price, vehiculo in zip(precios,listas):
    print(f'${price} es el valor del {vehiculo}')


print("\n\n## Bucles while ##\n")

print('*Bucle "while" es un blucle que itera mientras la condicion sea verdadera\n')

#Ejemplo "while"
print("Ejemplo_1 ")
contador = 0

while contador <= 7:
    print(f"contador: {contador}")
    contador += 1 #el contador tiene que incrementar por que si no no se cumpliria la condicion y seria un Bucle infinito

print("\nEjemplo_2 ")
condicion = True
x = 0
while condicion == True:
    print('El while se esta Ejecutando')
    x += 1
    if x == 7:
        print("la condicion cambio a False")
        print("Deteniendo el while...")
        condicion = False


############################ Control de Bucles  #############################

print("\n\n### Control de Bucles ###\n")

print('*Control de Bucles Permiten modificar el comportamiento de los bucles.\n')

print("Para detener un bucle tenemos 'break'")

#Ejemplos_1 'break'
print("\nEjemplo_1")
for numero in range(7):
    if numero == 4:
        break # se detiene antes que el numero 4
    print(f"Numero: {numero}")

print("\nPara saltar una iteracion tenemos 'continue'")

#Ejemplos_2 'continue'
print("\nEjemplo_2")
for numero in range(7):
    if numero == 4:
        continue # se salta el numero 4
    print(f"Numero: {numero}")

print("\nEl 'pass' Se usa cuando quieres dejar código sin implementar y no causar errores 'no hace nada'")

#Ejemplos_3 'pass'
print("\nEjemplo_3")
for numero in range(7):
    if numero == 4:
        pass
    print(f"Numero: {numero}")

############################ Manejo de errores  #############################

print("\n\n#### Manejo de errores ####\n")

print("\nLos Manejos de errores evitan que el programa se detenga si ocurre algun error con 'try-except'\n")

#el codigo prueba si no hay ningun error y si ocurre ejecuta la excencion (existen mas errores que el de 'ZeroDivisionError')

print("Ejemplo_1")
try:
    resultado = 7 / 0  # Error de división por cero
except ZeroDivisionError:
    print("No se puede dividir por cero")


print("\ntambien podemos usa 'try-except-else-finally'\n")
# El 'else' se ejecuta si no hay error y el 'finally' siempre se ejecuta

print("Ejemplo_2:)")
try:
    numero = 7
except ValueError:
    print("Eso no es un número válido")
else:
    print(f"El número ingresado es {numero}")
finally:
    print("Este mensaje siempre se ejecuta")

############################ Estructuras Especiales  #############################

print("\n\n##### Estruturas Especiales #####\n")

print("""Encontre algunas Estructuras especiales como:	'match-case', 'with', 'yield', 'list comprehensions' 
que aun estoy conociendo pero es bueno saber que existen""")

print("\nEjemplo_1: sobre match-case (funciona como un switch-case en otros lenguajes.)\n")
opcion = 2

match opcion:
    case 1:
        print("Elegiste opción 1")
    case 2:
        print("Elegiste opción 2")
    case _:
        print("Opción no válida")


####################################################################################################
###################################          DIFICULTAD          ##################################
###################################             EXTRA             ##################################
####################################################################################################


print("\n\n##### Dificultad Extra #####")

print("""\nCrea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3""")

numeros_extras = list() #cree la lista para que sea una visulizacion mas clara

for num_extra in range(10,56):
    if num_extra % 2 == 0:
        if num_extra % 3 != 0 and num_extra != 16:
            numeros_extras.append(num_extra)

print(f"\nResultado: {numeros_extras}")
