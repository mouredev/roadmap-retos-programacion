# Ejercicio 01
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# Los retos se encuentran en https://retosdeprogramacion.com

# Tipo de operadores de Lenguaje *Aritmenticos*

# Variables para uso Aritmetico


my_suma = 0
my_resta = 0
my_multiplicacion = 0
my_division = 0
my_modulo = 0
my_exponencial = 0
my_division_entera = 0

my_variable_1 = 10
my_variable_2 = 5
my_variable_3 = 2

my_suma = my_variable_1 + my_variable_2  # Suma de dos variables
my_resta = my_variable_1 - my_variable_2  # Resta de dos variables
my_multiplicacion = my_variable_1 * my_variable_2  # Multiplicacion de dos variables
my_division = my_variable_1 / my_variable_2  # Division de dos variables
my_modulo = my_variable_1 % my_variable_2  # Modulo de dos variables
my_exponencial = my_variable_1**my_variable_2  # Exponencial de dos variables
my_division_entera = my_variable_1 // my_variable_2  # Division entera de dos variables

print(f"el valor de la suma es {my_suma}")
print(f"el valor de la resta es {my_resta}")
print(f"el valor de la multiplicacion es {my_multiplicacion}")
print(f"el valor de la division es {my_division}")
print(f"el valor del modulo es {my_modulo}")
print(f"el valor de la exponencial es {my_exponencial}")
print(f"el valor de la division entera es {my_division_entera} \n")

# Tipo de operadores de Lenguaje de *Asignacion*

# Variables para uso de Asignacion


my_asig_suma = 0
my_asig_resta = 0
my_asig_multiplicacion = 0
my_asig_division = 0
my_asig_modulo = 0
my_asig_exponencial = 0
my_asig_division_entera = 0

my_asig_variable_1 = 10
my_asig_variable_2 = 5
my_asig_variable_3 = 2

my_asig_suma = 10
my_asig_suma += 5  # Asignacion de suma

my_asig_resta = 5
my_asig_resta -= 2  # Asignacion de resta

my_asig_multiplicacion = 2
my_asig_multiplicacion *= 5  # Asignacion de multiplicacion

my_asig_division = 10
my_asig_division /= 5  # Asignacion de division

my_asig_modulo = 10
my_asig_modulo %= 5  # Asignacion de modulo

my_asig_exponencial = 10
my_asig_exponencial **= 5  # Asignacion de exponencial

my_asig_division_entera = 10
my_asig_division_entera //= 5  # Asignacion de division entera

print(f"my asing suma es {my_asig_suma}")
print(f"my asing resta es {my_asig_resta}")
print(f"my asing multiplicacion es {my_asig_multiplicacion}")
print(f"my asing division es {my_asig_division}")
print(f"my asing modulo es {my_asig_modulo}")
print(f"my asing exponencial es {my_asig_exponencial}")
print(f"my asing division entera es {my_asig_division_entera} \n")

# Tipo de operadores de Lenguaje de *Comparacion*

# Variables para uso de Comparacion

my_comp_variable_1 = 10
my_comp_variable_2 = 5
my_comp_variable_3 = 2
my_comp_variable_4 = 10

if my_comp_variable_1 == my_comp_variable_4:
    # Comparacion de igualdad
    print(f"{my_comp_variable_1} es igual a {my_comp_variable_4}")

if my_comp_variable_2 != my_comp_variable_3:
    # Comparacion de desigualdad
    print(f"{my_comp_variable_2} es diferente a {my_comp_variable_3}")

if my_comp_variable_4 > my_comp_variable_3:
    # Comparacion mayor que
    print(f"{my_comp_variable_4} es mayor que {my_comp_variable_3}")

if my_comp_variable_4 < my_comp_variable_3:
    print("Esto no se cumpliria")
else:
    # Comparacion menor que
    print(f"{my_comp_variable_4} es mayor que {my_comp_variable_3}")

if my_comp_variable_4 < my_comp_variable_3:
    print("Esto no se cumpliria")
elif my_comp_variable_4 <= my_comp_variable_3:
    print("Esto no se cumpliria")
elif my_comp_variable_4 >= my_comp_variable_3:
    # Comparacion menor o igual que
    print(f"{my_comp_variable_4} es mayor que {my_comp_variable_3} \n")
else:
    print("Esto no se cumpliria")

# Tipo de operadores de Lenguaje de *Logicos*

my_log_varaible_1 = True

if my_comp_variable_1 == my_comp_variable_4 or my_comp_variable_2 == my_comp_variable_3:
    # Comparacion de igualdad
    print(f"{my_comp_variable_1} es igual a {my_comp_variable_4}")
    print(f"o {my_comp_variable_2} es igual a {my_comp_variable_3}")

if not my_log_varaible_1:
    print("Vacio")
else:
    print("No es vacio")  # Comparacion de negacion


# Utilizacion de estructuras de control.

# Estructura de control IF-ELIF-ELSE

my_if_variable_1 = 10
my_if_variable_2 = 5

if my_if_variable_1 != my_if_variable_2:  # Comparacion de desigualdad
    print(f"{my_if_variable_1} es diferente a {my_if_variable_2}")
elif my_if_variable_1 > my_if_variable_2:
    print(f"{my_if_variable_1} es mayor que {my_if_variable_2}")
else:
    print(f"{my_if_variable_1} es igual a {my_if_variable_2}")


# Estructura de control WHILE

my_while_variable_1 = 10
my_while_variable_2 = 5
my_while_variable_3 = 0

while my_while_variable_1 > my_while_variable_2:
    print(f"{my_while_variable_1} es mayor que {my_while_variable_2}")
    my_while_variable_2 += 1  # Incremento de la variable 2

for i in range(1, 6):
    print(i)  # Estructura de control FOR


for i in range(1, 6):
    if i == 3:
        break  # Rompe el ciclo cuando i es igual a 3
    print(i)  # Estructura de control FOR con break
    if i == 2:
        continue


# Extra

for i in range(10, 56):
    if (i % 2 == 0 and i != 16 and i % 3 != 0) or i == 55:
        print(i)
