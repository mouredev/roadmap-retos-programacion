### OPERADORES Y ESTRUCTURAS DE CONTROL ###

#AUTOR: avcenal

#Aritméticos
print("\n")
print ("Operadores De Aritméticos")
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 % 2)
print(5 // 2) #floor division
print(2 ** 2) #potencia

#Aritméticos en cadenas
print("\n")
print ("Operadores De Aritméticos en cadenas")
print ("Hola " + "mundo")
print ("Hola" * 5)
print ("Hola" * int(2.5*2))
print("Hola" * (2 ** 2))

#Comparación
print("\n")
print ("Operadores De Comparación")
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 3)
print(3 != 4)

#Lógicos
print("\n")
print ("Operadores Lógicos")
print (3 > 4 and 5 < 7)
print (3 > 4 or 5 < 7)
print (not 3 > 4)

#Pertenencia: comprueba si el valor está dentro de una estructura
print("\n")
print ("Operadores De Pertenencia")
my_tuple = (38,25,3)
print (35 in my_tuple)
print (78 not in my_tuple)

#Identidad: sirven para comprobar si dos variables emplean la misma ubicación de memoria
print("\n")
print ("Operadores De Identidad")
var_1 = 4
var_2 = 4
var_3 = 7
print(var_1 is var_2)
print(var_1 is not var_3)

#Bit a bit
print("\n")
print ("Operadores Bit a Bit")
print(var_1 & var_3)
print(var_1 | var_3)
print(var_1 ^ var_3)
print(~ var_3)
print(var_1 >> var_3)
print(var_1 << var_3)

#Estructuras condicionales
print("\n")
print ("Estructuras condicionales")
if (var_1 > var_3):
    print(f"la variable var_1 con varlor {var_1} es mayor que la variable var_3 con valor {var_3}")
elif (var_1 == var_3):
    print (f"Las variables var_1 y var_3 son iguales con el valor {var_1}")
else:
    print(f"La variable var_3 con valor {var_3} es mayor que la variable var_1 con valor {var_1}")

#Estructuras iterativas
print("\n")
print ("Estructuras condicionales")
print ("WHILE - ELSE")
limit = 0
while limit < var_3:
    print(f"El valor de la variable limit en esta vuelta es: {limit}")
    limit += 1
else:
    print(f"La variable limit ya vale lo mismo que var_3: {limit} y salgo del While")

print("\n")
print ("WHILE - ELSE con BREAK")
limit = 0
while limit < var_3:
    if limit == 4:
        print("Paro la ejecución del while mediante un break cuando la variable limit vale 4")
        break
    print(f"El valor de la variable limit en esta vuelta es: {limit}")
    limit += 1
else:
    print(f"La variable limit ya vale lo mismo que var_3: {limit} y salgo del While")
    
print("\n")
print ("FOR - ELSE")
my_list = [23, 34, 52, 16, 81, 90]
for element in my_list:
    print(element)
else:
    print("Ya he recorrido la lista my_list")

print("\n")
print ("FOR - ELSE con RANGOS")
top_range = 10
for index in range (0,10):
    print (f"Estoy en el index {index}")
else:
    print (f"He recorrido hasta el número {index} del rango (0,10)")

print("\n")
print ("FOR - ELSE con BREAK")
count = 0
for element in my_list:
    count += 1
    print(f"El elemento en la posición {count} es {element}")
    if count == 3:
        print(f"Salgo del bucle for con un break cuando llege a la posición {count} de my_list")
        break
else:
    print (f"He recorrido hasta el número {index} del rango (0,10)")

#Excepciones
print("\n")
print ("Excepciones")
value_one = 3
value_two = "5"
#try - except
print ("TRY - EXCEPT")
try:
    print(f"La suma de los valores es {value_one + value_two}")
    print("No he ha producino ningún error")
except:
    print("Se ha producido un error")

#try - except - else     
print("\n")
print ("TRY - EXCEPT - ELSE")
value_two = 5
try:
    print(f"La suma de los valores es {value_one + value_two}")
    print("No se ha producino ningún error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución sigue sin errores")

#try - except - else - finally
print("\n")
print ("TRY - EXCEPT - ELSE - FINALLY")
value_two = "5"
try:
    print(f"La suma de los valores es {value_one + value_two}")
    print("No se ha producino ningún error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución sigue sin errores")
finally:
    print("La ejecución del manejo de excepciones ha finalizado")

#Captura de excepciones por tipo
print("\n")
print ("Captura de excepciones por tipo")
try:
    print(f"La suma de los valores es {value_one + value_two}")
    print("No se ha producino ningún error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")
except IndexError:
    print("Se ha producido un IndexError")

#Captura de la información de la excepción
print("\n")
print ("Captura de la información de la excepción")
try:
    print(f"La suma de los valores es {value_one + value_two}")
    print("No se ha producino ningún error")
except ValueError:
    print("Se ha producido un ValueError")
except Exception as error:
    print(error)

# DIFICULTAD ADICIONAL o BONUS TRACK =)
print("\n")
print ("DIFICULTAD ADICIONAL o BONUS TRACK =)")

def roadmap_01():
    min_range = 10
    max_range = 55
    for index in range(min_range,max_range+1):
        if index % 2 == 0:
            if index != 16 and index % 3 != 0:
                print (index)

roadmap_01()
