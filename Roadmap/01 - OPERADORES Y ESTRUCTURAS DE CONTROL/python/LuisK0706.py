# Operadores aritmeticos (+, -, *, /)

# Operador + se utiliza para realizar sumas
mi_suma = 4 + 7 
# Operador - se utiliza para realizar restas
mi_resta = 10 - 6 
# Operador * se utiliza para realizar multiplicaciones 
mi_multiplicacion = 5 * 9 
# Operador / se utiliza para realizar divisiones
mi_division = 9 / 3 
# Operador // se utiliza para realizar una division entera
mi_division_entera = 10 // 3
# Operador % se utiliza para obtener el residuo de una division
mi_residuo = 3 % 2
# Operador ** se utiliza para realizar potencias
mi_potencia = 2**2

#Impresion de los resultados
print("Operadores aritmeticos \n"
      "---------------------------\n"
      f"Suma: {mi_suma}\n"
      f"Resta: {mi_resta}\n"
      f"Multiplicacion: {mi_multiplicacion}\n"
      f"Division: {mi_division}\n"
      f"Division entera: {mi_division_entera}\n"
      f"Residuo: {mi_residuo}\n"
      f"Potencia: {mi_potencia}\n")


# Operadores logicos (and, or, not)

# El operador and devolvera True si ambas condiciones se cumplen
usando_and = 5 < 3 and 10 > 5
# El operador or devolvera True si una de las dos condiciones se cumple
usando_or = 5 < 3 or 10 > 5
# El operador not devolvera False si su operando es True y True si es False
usando_not = True

#Impresion de los resultados
print("Operadores logicos \n"
      "---------------------------\n"
      f"Operador and: {usando_and}\n"
      f"Operador or: {usando_or}\n"
      f"Operador not: {not(usando_not)}\n")


# Operadores de comparacion (<, >, ==, !=)

# Operador < se utiliza para varificar si un elemento es menor a otro
usando_menorque = 3 < 5
# Operador > se utiliza para verificar si un elemento es mayor a otro
usando_mayorque = 3 > 5
# Operador == devuelve True si son iguales
usando_igual = 8 == 5
# Operador != devueve True si son diferentes
usando_no_es_igual = 8 != 5
# Operador <= devuelve True si el elemento es menor o igual al otro
usando_menor_o_igual = 8 <= 8
# Operador >= devuelve True si el elemento es mayor o igual al otro
usando_mayor_o_igual = 8 >= 9


#Impresion de los resultados
print("Operadores de comparación \n"
      "----------------------------\n"
      f"Operador <: {usando_menorque}\n"
      f"Operador >: {usando_mayorque}\n"
      f"Operador ==: {usando_igual}\n"
      f"Operador !=: {usando_no_es_igual}\n"
      f"Operador <=: {usando_menor_o_igual}\n"
      f"Operador >=: {usando_mayor_o_igual}\n")



# Operadores de asignacion (=, +=, -=, *=, /=, //=, %=, **=)
mi_variable = 10
print("Operadores de asignacion\n"
      "---------------------------\n")
# Asignacion simple se realiza solo con el signo = dandole algun valor a una vaiable
asignacion_simple = 'Mi asignacion simple'
# Asignacion con una suma += lo que hace es a la misma variable le suma el numero asignado
mi_variable += 5 
print(f"Suma: {mi_variable}")
# Funciona igual con los demas operadores aritmeticos
mi_variable -= 5
print(f"Resta: {mi_variable}")
mi_variable *= 5
print(f"Multiplicacion: {mi_variable}")
mi_variable //= 3
print(f"Division entera: {mi_variable}")
mi_variable %= 5
print(f"Residuo: {mi_variable}")
mi_variable **= 5
print(f"Potencia: {mi_variable}")
mi_variable /= 5
print(f"Division: {mi_variable}\n")



# Operadores de identidad (is, is not)

# Operador is devuelve True si es correcto
usando_is = usando_mayorque is True
# Operador not is devuelve True si es correcto
usando_is_not = not usando_mayorque is True

# Impresion de resultados
print("Operadores de identidad\n"
      "---------------------------------\n"
      f"Operador is: {usando_is}\n"
      f"Operador is not: {usando_is_not}\n")


# Operadores de pertenencia (in, not in)

mi_lista = [5, 4, 3, 2, 1]

# Operador in devuelve True si encuentra el dato buscado
usando_in = 5 in mi_lista
# Operador not in devuelve True si no encuentra el dato buscado
usando_not_in = 5 not in mi_lista

print("Operadores de pertenencia\n"
      "-----------------------------\n"
      f"Operador in: {usando_in}\n"
      f"Operador not in: {usando_not_in}\n")



# Operadores de bits (&, |, <<, >>)

x = 0b101
y = 0b1000
# Desplazamiento a la izquierda << desplaza el numero de bits a la izquierda de la variable asignada
izquierda = x << 2
# Desplzamiento a la derecha >> desplaza el numero de bits a la derecha de la variable asignada
derecha = y >>2
# Operador & operacion and entre dos numeros binarios
usando_and_bits = x & y
# Operador | operacion or entre dos numeros binarios
usando_or_bits = x | y

# Impresion de resultados
print("Operadores de bits\n"
      "-------------------------\n"
      f"Desplazamiento de bits a la izquierda: {izquierda}\n"
      f"Desplazamiento de bits a la derecha: {derecha}\n"
      f"Operador and en bits: {usando_and_bits}\n"
      f"Operador or en bits: {usando_or_bits}\n")


# Estructuras de control 

# Condicionales

# Estructura (if, elif, else)

# El if se utiliza para hacer algo si se cumple una condicion
print("Usando if\n"
      "-------------------------\n")
if mi_suma > mi_resta: 
    print(f"{mi_suma} es mayor que {mi_resta}\n")
# El elif se utiliza en caso de no cumplirse la primera condicion se agrega una condicion extra
elif mi_suma < mi_resta:
    print(f"{mi_resta} es mayor que {mi_suma}\n")
# El else es una ultima accion en caso de no cumplirse ninguna de las condiciones
else:
    print("son iguales\n")


# Iterativas (for, while)

# El ciclo for imprime datos segun el rango asignado o las condiciones aplicadas

print("Ciclo for\n"
      "-------------------------")
for i in range(1, 5):
    print(i)

# El ciclo while imprime datos mientras se sigue cumpliendo la condicion
contador = 0

print("Ciclo while\n"
      "-------------------------")
while(contador < 10):
    print(contador)
    contador += 1


# Excepciones

try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

# Retorna algunos mensajes de error para casos no validos
except ZeroDivisionError:
    print("No se puede dividir entre 0")

# Ejercicio extra
""" Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for i in range(10, 56):
    if i == 16 or i % 3 == 0:
        pass
    elif i % 2 == 0 or i == 55:
        print(i)
    else:
        pass
