"""
Operadores
"""

# Operadores aritmeticos
suma= 10 + 3
print("Suma 10 + 3 = ",suma) # Tipo de forma de impresion de una suma de diferente manera

print(f"Suma: 10 + 3 = {10 + 3}")  # tipo de forma de impresion suma mas rapido
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 x 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}") # Modulo es para le resto de la operacion, lo que queda despues de dividir
print(f"Exponente: 10 ** 3 = {10 ** 3}") # Exponente para por ejemplo sacar en este caso 10 a la 3
print(f"Division entera: 10 // 3 = {10 //3}") #Te da la division sin decimales

# Operadores de comparacion
print(f"Igualdad: 10 == 3 {10 == 3}") # Te da como resultado la respuesta de si si es 10 igual a 3 en este caso false
print(f"Desigualdad: 10 != 3 {10 != 3}") # Te da como resultado la respuesta de si 10 y 3 no son iguales en este caso true
print(f"Mayor que: 10 > 3 {10 > 3}") 
print(f"Menor que: 10 < 3 {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 {10 >= 3}") 
print(f"Menor o igual que: 10 <= 3 {10 <= 3}")

# Operadores logicos
Operacion_1= 10 + 3 == 13
Operacion_2= 5 - 1 == 4
print("AND &&: 10 + 3 == 13 and 5 - 1 == 4 es", Operacion_1 and Operacion_2) # Forma larga usando variables para comprobar que si podia hacerlo
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and  5 - 1 == 4}") #El and te da como respuesta si dos condiciones o son iguales, como es verdadero y verdadero da verdadero, busca que se cumplan ambas condiciones
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or  5 - 1 == 4}") # El or solo busca que alguna de verdadero para dar true, como ambas lo son da verdarero, solo busca que se cumpla una de las condiciones
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}") #not da positivo si la condicion es falsa, niega lo verdadero

# Operadores de asignacion
my_number = 11 #asignacion
print(my_number) 
my_number += 1 #suma y asignacion
print(my_number) 
my_number -= 1 #resta y asignacion
print(my_number) 
my_number *= 2 #multiplicacion y asignacion
print(my_number) 
my_number /= 2 #division y asignacion
print(my_number) 
my_number %= 2 #modulo y asignacion
print(my_number) 
my_number **= 1 #exponentey asignacion
print(my_number) 
my_number //= 1
print(my_number) #division entera y asignacion

# Operadores de indentidad
my_new_number= my_number
print(f"my_number is my_new_number {my_number is my_new_number}") #IS Es para comparar si dos o variables son iguales y si si da true
print(f"my_number is not my_new_number {my_number is not my_new_number}") # IS NOT es para comparar si dos variables son diferetens si si son diferentes da true

# Operadores de pertenencia 
print(f"'r' in Fernando {'r' in 'Fernando'}") #sirve para comrpobar si algo forma parte de otra cosa si si da true
print(f"'j' not in Fernando {'j' not in 'Fernando'}") #para combrobar que algo no pertenece a otra cosa, si no pertenece da true

# Operadores de bit
a = 10 #1010
b = 3 #0011
print(f"AND: 10 & 3 = {10 & 3}") #0010 # en el operador and & si ambos bits dan 1 es 1
print(f"OR: 10 | 3 = {10 | 3}") #1011 #si alguno de los dos da 1 es 1
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001 #si son diferentes da 1
print(f"NOT: ~ 10 = {~10}") # ~ cambia el valor bit a bit 1 por 0 y 0 por 1
print(f"Desplazamiento a la derecha 10 >> 2 = {10 >> 2}") #desplaza dos lugares el bit a la derecha
print(f"Desplazamiento a la izquierda 10 >> 2 = {10 << 2}") #desplaza dos lugares el bit a la izquierda

"""
Estructuras de control
"""

# Condicionales

my_string = "Jeovany"

if my_string == "Fernando":          #if si algo se cumple haz algo, si no se cumple pues has otra cosa
    print("my_string es 'Fernando'")
elif my_string == "Jeovany":
    print("my_string es 'Jeovany'") #elif una comprobacion mas antes de pasar al else despues de que no se cumplio if
else:
    print("my_string no es 'Fernando' ni 'Jeovany") #else si no se cumple la condicion del if imprime o manda esta

    # Iterativas 

for j in range(11):  #for para crar bluces #range es una estructura que te da todos lo numeros hasta el que le diste sin tomar en cuanta el que le diste
    print(j)

    j = 0

while j<= 10: #while hace que el bluce se repita mientras esa condicion sea verdadera
    print(j)
    j += 1  #esto hace que cada que se ejecute el bucle le sume 1, lo que en un momento terminara con el bucle infinito

#Manejo de excepciones

try: #es decirle que pruebe lo siguiente
    print(10 / 0)
except: #lo que pondra si lo que esta en prueba sale mal 
    print("Se ah producido un error")
finally: #se pone se haga la prueba funcional o se haya realizado la excepcion
    print("Ha finalizado el manejo de exepciones")


"""
Estructuras de control
"""
for number in range(10, 56): #si pones los numero de esta forma es como si le dijeras de cual debe partir y a cual llegar
    if number %2 == 0 and number !=16 and number %3 != 0: #este if sirve para que solo haga multiplos de 2  #para que no imprima el 16
        print(number)
