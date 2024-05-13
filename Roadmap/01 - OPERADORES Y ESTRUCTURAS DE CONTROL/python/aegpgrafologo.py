"""
Operadores
"""
"""Operadores matemáticos
Operador de adición con interpolación 
sustituyendo el nombre de una variable por sus valores 
cuando se construye un «String»"""
#Operador de adición
print(f"Operación 250 + 895 = {250+895}")
#Operador de sustracción
print(f"Operación 895 - 250 = {895-250}")
#Operador de multiplicación
print(f"Operación 250 * 895 = {250*895}")
#Operador de división
print(f"Operación 895 / 250 = {895/250}")
#Operador de módulo
print(f"Operación 4 % 3 = {4%3}")
#Operador exponencial
print(f"Operación 3 ** 3 = {3**3}")
#Operador disión exacta
print(f"Operación 895 // 250 = {895//250}")

#Operadores de comparación (Sirven para comparar valores)
#Operador igualdad - no solo con números, tambien variables, string e.t.c
print(f"Igualdad: 895 == 895 es: {895==895}")
#Operador desigualdad
print(f"Desigualdad: 895 != 250 es: {895!=250}")
#Operadores mayor que, menor que, mayor o igual que o menor o igual que
print(f"Mayor que: 895 > 250 es: {895>250}")
print(f"Menor que: 895 < 250 es: {895<250}")
print(f"Mayor o igual que: 895 >= 250 es: {895>=250}")
print(f"Menor o igual que: 895 <= 250 es: {895<=250}")

# Operadores logicos
#Operador AND
print(f"AND &&: 895 + 250 == 687 and 6-8 == 2 es: {895 + 250 == 687 and 6 - 8 == 2}")
#Operador OR - Que por lo menos una de las concidiones sea verdadera
print(f"OR ||: 895 + 250 == 687 or 6-4 == 2 es: {895 + 250 == 687 or 6 - 4 == 2}")
#Operador NOT
print(f"NOT !: not 895 + 250 == 687 es: {not 895 + 250 == 687}")

# Operadores de asignación
variable_prueba = 12 # En este caso se hace asignación con el operador igual
print(variable_prueba)
variable_prueba += 2 # Suma y asignación
print(variable_prueba)
variable_prueba -= 2 # resta y asignación
print(variable_prueba)
variable_prueba *= 2 # multipliación y asignación
print(variable_prueba)
variable_prueba /= 2 # división y asignación
print(variable_prueba)
variable_prueba %= 2 # módulo y asignación
print(variable_prueba)
variable_prueba **= 2 # exponente y asignación
print(variable_prueba)
variable_prueba //= 2 # división exacta y asignación
print(variable_prueba)

#Operadores de identidad - Comparar el valor de la posición en memoria
nueva_variable_prueba = variable_prueba
print(f"variable_prueba is nueva_variable_prueba es: {variable_prueba is nueva_variable_prueba}")
print(f"variable_prueba is not nueva_variable_prueba es: {variable_prueba is not nueva_variable_prueba}")

# Operadores de pertenencia - Verifica si algo esta dentro de un conjunto.
print(f"'A' in 'Anyelo' = {'A' in 'Anyelo'}")
print(f"'a' not in 'Anyelo' = {'a' not in 'Anyelo'}")

# Operadores de bit - Operaciones con bits
Primera = 10
Segunda = 3
# Operador AND - Transforma a binario y opera
print (f"AND: 10 & 3 = {10 & 3}")
# Operador OR - Transforma a binario y opera, SI AL MENOS UNO DE LOS DOS BIT ES UNO EL RESULTADO ES UNO
print (f"OR: 10 | 3 = {10 | 3}")
# Operador XOR - Transforma a binario y opera, SI los bit son diferentes el resultado es UNO Y SI SON IGUALES ES CERO
print (f"XOR: 10 ^ 3 = {10 ^ 3}")
# Operador NOT - INTERCAMBIA EL VALOR BIT A BIT DE CUALQUIERA DE LOS ELEMENTOS
print (f"NOT: ~10 = {~10}")
# Operador Desplazamiento a la derecha
print (f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
# Operador Desplazamiento a la izquierda
print (f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

"""
Estructuras de control - indica al código que camino debe seguir
"""
#Condicionales
mi_nombre = "Esneider"
if mi_nombre == "Anyelo":
    print("mi_nombre es 'Anyelo'")
elif mi_nombre == "Esneider":
    print("mi_nombre es 'Esneider'")
else:
    print("mi_nombre no es 'Anyelo' ni 'Esneider'")

#Iterativas
#For - crea bucles - recorrer estructura con más de un elemento o para ejecutar una acción varias veces
for x in range (5):
    print(x) 
#While - el bucle se ejecuta mientras la condición sea verdadera
x = 0
while x <= 10:
    print(x)
    x += 1 

#Manejo de excepciones
try:
    print (10 / 0)
except:
    print ("Se ha detectado un error")
finally:
    print ("Ha terminado el manejo de excepciones")

"""
Programa impresos por consola de numeros entre el 10 y 55,
pares y que no son ni el 16 ni multiplos de 3.
"""
for numeros in range(10, 56):
    if numeros % 2 == 0 and numeros != 16 and numeros % 3 !=0:
        print(numeros)


