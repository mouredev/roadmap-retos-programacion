print("01 - Python")
#Operadores aritméticos
my_first_value = 8
my_second_value = 3
print("-----------------------")
print("OPERADORES ARITMÉTICOS")
print("-----------------------")
# Suma
my_suma = my_first_value + my_second_value
print("Suma: %d + %d =  %d" % (my_first_value, my_second_value ,my_suma))

# Resta
my_resta = my_first_value - my_second_value
print("Resta: %d - %d =  %d" % (my_first_value, my_second_value ,my_resta))

# Multiplicación
my_multiplicacion = my_first_value * my_second_value
print("Multiplicación: %d * %d =  %d" % (my_first_value, my_second_value ,my_multiplicacion))

# División
my_division = my_first_value / my_second_value
print("División: %d / %d =  %d" % (my_first_value, my_second_value ,my_division))

# División entera
my_division_entera = my_first_value // my_second_value
print("División Entera: %d // %d =  %d" % (my_first_value, my_second_value ,my_division_entera))

# Módulo
my_modulo = my_first_value % my_second_value
print("Módulo: %d %% %d =  %d" % (my_first_value, my_second_value ,my_modulo))

# Potencia
my_potencia = my_first_value ** my_second_value
print("Potencia: %d ** %d =  %d" % (my_first_value, my_second_value ,my_potencia))

#Operadores de comparación Se puede realizar con números y cadenas de texto
print("-----------------------")
print("OPERADORES DE COMPARACIÓN")
print("-----------------------")
# Igualdad ==
my_igualdad = my_first_value == my_second_value
my_igualdad_string = "Hola" == "HolaPython"
print("Igualdad: %d == %d =  %s" % (my_first_value, my_second_value ,my_igualdad))

# Desigualdad != 
my_desigualdad = my_first_value != my_second_value
my_desigualdad_string = "Hola" != "HolaPython"
print("Desigualdad: %d != %d =  %s" % (my_first_value, my_second_value ,my_desigualdad))

# Mayor que >
my_mayor_que = my_first_value > my_second_value
print("Mayor que: %d > %d =  %s" % (my_first_value, my_second_value ,my_mayor_que))

# Menor que <
my_menor_que = my_first_value < my_second_value
print("Menor que: %d < %d =  %s" % (my_first_value, my_second_value ,my_menor_que))

# Mayor o igual que >=
my_mayor_igual_que = my_first_value >= my_second_value
print("Mayor o igual que: %d >= %d =  %s" % (my_first_value, my_second_value ,my_mayor_igual_que))

# Menor o igual que <=
my_menor_igual_que = my_first_value <= my_second_value
print("Menor o igual que: %d <= %d =  %s" % (my_first_value, my_second_value ,my_menor_igual_que))

#Operadores lógicos (AND, OR, NOT)
print("-----------------------")
print("OPERADORES LÓGICOS")
print("-----------------------")
my_and = True and False
print("AND: %s" % my_and)

my_or = True or False
print("OR: %s" % my_or)

my_not = not True
print("NOT: %s" % my_not)

#Operadores de asignación
print("-----------------------")
print("OPERADORES DE ASIGNACIÓN")
print("-----------------------")
my_asignacion = 2
print("Asignación: %d" % my_asignacion)

my_asignacion += 2
print("Asignación +=: %d" % my_asignacion)

my_asignacion -= 2
print("Asignación -=: %d" % my_asignacion)

my_asignacion *= 2
print("Asignación *=: %d" % my_asignacion)

my_asignacion /= 2
print("Asignación /=: %d" % my_asignacion)

my_asignacion **= 2
print("Asignación **=: %d" % my_asignacion)

my_asignacion %= 2
print("Asignación %%=: %d" % my_asignacion)

my_asignacion //= 2
print("Asignación //=: %d" % my_asignacion)

#Operadores de identidad
print("-----------------------")
print("OPERADORES DE IDENTIDAD")
print("-----------------------")
my_number = 2

my_is = my_number is 2
print("Is: %s" % my_is)

my_is_not = my_number is not 2
print("Is not: %s" % my_is_not)

#Operadores de Pertenencia
print("-----------------------")
print("OPERADORES DE PERTENENCIA")
print("-----------------------")
my_list = [1,2,3,4,5]
print(my_list)
my_in = 1 in my_list
print("1 IN my_list: %s" % (my_in))
my_not_in = 3 not in my_list
print("3 NOT IN my_list: %s" % (my_not_in))


#Condicionales
print("-----------------------")
print("CONDICIONALES")
print("-----------------------")

my_var = 34 
my_var2 = 45

print("my_var: %d" % my_var)
print("my_var2: %d" % my_var2)

if(my_var>my_var2):
    print("La variable my_var es mayor que my_var2")
elif(my_var==my_var2):
    print("La variable my_var es igual que my_var2")
else:
    print("La variable my_var es menor que my_var2")

#Bucles
print("-----------------------")
print("BUCLES")
print("-----------------------")

#Bucle for

for i in range(1,10):
    print("Esto es un bucle for: %d" % i)

#Bucle while
my_new_var = 0
while(my_new_var<10):
    print("Esto es un bucle while: %d" % my_new_var)
    my_new_var += 1

# Estructura de control de excepciones
print("-----------------------")
print("EXCEPCIONES")
print("-----------------------")

my_first_value = 10
my_second_value = 0

# Intentamos realizar una división que causará una excepción de división por cero
try:
    resultado = my_first_value / my_second_value
except ZeroDivisionError as e:
    print("Error: %s. No se puede dividir por cero." % e)
else:
    print("Resultado: %d" % resultado)
finally:
    print("Fin del programa")


#PARTE OPCIONAL
print("-----------------------")
print("PARTE OPCIONAL")
print("-----------------------")

print("Imprimimos por consola los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3")
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)

print("-----------------------")
print("FIN DEL EJERCICIO 01 - PYTHON")








