"""
**OPERADORES**
"""

# OPERADORES ARIMETICOS

print(f"Suma: 470 + 90 = { 470 + 90 }") #Interpolando codigo en una cadena texto
valor_mayor = 987
valor_menor = 222
def resta(valor1,valor2):
    return valor1 - valor2
print(f"Resta con funcion " + str(resta(valor_mayor,valor_menor)))
print('Multiplicacion usando formato {} por {} es {}.'.format(valor_mayor,valor_menor, valor_mayor*valor_menor))
print(f"Division: 10 / 3 = {10 / 3}") 
print(f"Division entera: 10 // 3 = {10 // 3}") 
print(f"Modulo: 10 % 3 = {10 % 3}") 
#modulo igual a resto o sobrante de la division
print(f"Exponente: 10 ** 3 {10 ** 3}")
#potencia

# OPERADORES DE COMPARACION

print(f"Igualdad: 10 == 3 { 10 == 3 }") #retorna un boolean
print(f"Desigualdad: 10 != 3 { 10 != 3 }") 
print(f"Mayor que: 10 > 3 { 10 > 3 }") 
print(f"Menor o igual que: 10 <= 3 { 10 <= 3 }")

# OPERADORES LOGICOS

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4: {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4: {10 + 3 == 13 or 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4: {10 + 3 == 13 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14: {not 10 + 3 == 14}")

# OPERADORES DE ASIGNACION

my_number = 11 # '=' asignacion  
print(my_number)
my_number += 5 # '+=' suma y asignacion  
print(my_number)
my_number -= 5  
print(my_number)
my_number *= 5   
print(my_number)
my_number /= 5   
print(my_number)
my_number %= 5   
print(my_number)  
print(my_number)
my_number **= 5  
print(my_number)
my_number //= 5  
print(my_number)

# OPERADORES DE IDENTIDAD

my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
# Igualdad compara la posicion en memoria, no importa que las dos variables contengan el mismo valor
print(f"my_number is not my_new_number es {my_number is not my_new_number}")
# Desigualdad

# OPERADORES DE PERTENENCIA

print(f"'u' in 'juan' {'u' in 'juan'}")
print(f"'u' not in 'juan' {'u' not in 'juan'}")

"""
**ESTRUCTURAS DE CONTROL**
"""

# CONDICIONALES

my_string = 15

if type(my_string) == str:
    print("Si es una String yay")
elif type(my_string) == int:
    print("cabezon esto es un numero")
else:
    print("Sabra Dios que hay en esa variable")
# Puede haber un if dentro de otro pero no creo que sea buena idea, 
# Debe ser mejor usar funciones, nota en python no existe el switch

# ITERATIVAS

for i in range(5):
    print(i)
# no es necesario definir i, hara el conteo desde 0 hasta 4 sin incluir 5

f = 17

while f <= 21:
    print(f"tu numero es: {f}")
    f += 1
          
# MANEJO DEE EXCEPCIONES

try:
    print(10 / 0)
except:
    print("uyyy algo fallo")
finally:
    print("Ha finalizado el manejo de excepciones")


"""
----------------------------------------------------
********DIFICULTAD EXTRA**********
___________________________________________________
"""
z = 1
for z in range(10,56):
    if z % 2 == 0 and z != 16 and z % 3 != 0:
        print(z)
