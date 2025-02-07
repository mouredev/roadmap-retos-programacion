"""
******************************************* Tipos de operados  ************************************************************** 
"""

# Los operadores se utilizan para realizar operaciones en variables y valores como son el caso de: (+, -, *, /, %, **, //)
# Estos en el caso de Python 

# ------------------------------------- Operadores aritmeticos --------------------------------------------
print("Operadores Aritmeticos :")
#Operador de Suma " + "
print(f"Suma: 10 + 3 = {10 + 3}") #Ejemplo con interploacion 
#Operador de Resta " * "
print(f"Resta: 10 - 3 = {10 - 3}")
#Operador de Multiplicacion " * "
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
#Operador de Division " / "
print(f"Multiplicacion: 10 / 3 = {10 / 3}")
#Operador de Modulo " % "
print(f"Modulo: 10 % 3 = {10 % 3}")
#Operador de Exponente " ** "
print(f"Exponente: 10 ** 3 = {10 ** 3}")
#Operador de Division entera" // "
print(f"Division entera 10 // 3 = {10 // 3} \n") #Salto de linea \n


#Operador de Suma " + "
suma = 10 + 3 
print(f"Ejemplo de suma con variable \nSuma = 10 + 3 =  {suma}") #Ejemplo con variable 

x = 5
y = 4
print(f"Ejemplo de suma con variables \nx = 5 \ny = 4 \nx + y =  {x + y}\n") #Ejemplo con variable  #Ejemplo con variable 

# ------------------------------------- Operadores de comparacion --------------------------------------------
print("Operadores de Comparacion:")

#Operador de Igualdad " == "
print(f"Igualdad: 10 == 3 = {10 == 3}") #Ejemplo con interploacion
#Operador de No es igual o desigual 
print(f"Desigual: 10 != 3 = {10 != 3}")
#Operador de Mayor que
print(f"Mayor que: 10 > 3 = {10 > 3}")
#Operador de Menor que 
print(f"Menor que: 10 < 3 = {10 < 3}")
#Operador de Mayor o igual a  
print(f"Mayor o igual que: 10 >= 3 = {10 >= 3}")
#Operador de Menor o igual a  
print(f"Menor o igual que: 10 <= 3 = {10 <= 3} \n")


# ------------------------------------- Operadores de logicos  --------------------------------------------
print("Operadores de Logicos:")
#Operador AND "y"
print(f"AND: 10 + 3 == 13 and 5 - 1 == 4 es:{10 + 3 == 13 and 5 - 1 == 4}") 
#Operador OR "o"
print(f"OR: 10 + 3 == 13 or 5 - 2 == 4 es:{10 + 3 == 13 or 5 - 2 == 4}")
#Operador NOT "negado"
print(f"NOT: not (10 + 3 == 13 or 5 - 2 == 4) es:{not (10 + 3 == 13 or 5 - 2 == 4)} \n")

"""
Los operadores logicos se encarcan de comparar uno o mas resultados para determinar si estos son verdaderos o falsos 
AND: en el caso del AND hambas condiciones establecidas en el operador tieen que ser correctas para que este operador pueda 
designar el resultado como True "verdadero" de no ser asi y fallar aunque sea en una de las tantas establesidas el resultado sera False "Falso"
OR: en el caso del OR con que una operacion o condiccion sea asertada el resultado arrojado sera True "Verdadero" la unica manera de optenr un False "Falso"
es que ninguna de las operaciones sea asertada 
NOT: en el caso de los NOT el resultado proporcionado al finalizar la comparacion logica sera negado de ser un True optenido ya sea por una operacion logica de 
un AND o un OR el resultado se invertira o negara dando como resultado un False, cumpliendo como la misma funcion para el resltado de una False 
"""

# ------------------------------------- Operadores de Identidad  --------------------------------------------
print("Operadores de Identidad:")
#operador is "ES "
print("x = ['apple', 'banana'] ")
print("y = ['apple', 'banana'] ")
print("z = x ")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x 

print(f"x is z: {x is z} ")
#Compara x  con z y devuvle el valor de "TRUE" o verdadero ya que es lo mismo 
print(f"x is y: {x is y } \n")



"""

"""

# ------------------------------------- Operadores de Asignacion   --------------------------------------------
print("Operaradores de asignacion: ")
#Operador de = Asignacion de valor
numero = 5
print(f"El valor de numero = {numero} " )
#Operador de + Suma
numero += 3
print(f"El valor de numero ahora es :{numero}")
#Operador de Resta
numero -= 2
print(f"El valor de numero ahora es: {numero}")
#Operador de multiplicacion
numero *= 2
print(f"El valor de numero se multiplicara por 2 Numero ={numero}")
#Operador de Divicion /
numero /= 2
print(f"El valor de numero se divide por 2 Numero ={numero}")
#Operador de Modulo o Residuo %
numero %= 2
print(f"El valor de numero se divide por 2  y el modulo o residuo de Numero ={numero}")
#Operador de //
numero = 6 #Nueva asignacion de valor a numero para poder seguir con los distitnos ejemplos de asignacion
numero //= 2
print(f"El valor de numero se divide por 2  y el valor entero es = {numero}")
#Operador de Potencia **
numero **= 2
print(f"El valor de numero se multiplica por la potencia asignada en este caso potencia 2 = {numero}\n")  

print("Operadores de Peertenencia \n") #Los operadores de peretenencia se utilizan para probar si se presenta una secuencia en un objeto 
#Operadr In
fruta = ["aple", "banana"]
print(f"El resultado es {"banana" in  fruta} " )
#Operador Not in
print(f"El resultado es {"pepino" not in  fruta}\n " )

print("Operadores de bit a bit \n") #Los operadores bit a bit, se utilizan para comparar numeros binarios 
#AND o &
num_1 = 28 #11100 en binario
num_2 = 20 #10100 en binario

resultado = num_1 & num_2
#Compara cada bit y los establece en 1 si hambos son 1 de lo contrario lo estabelece en 0
print(f"El el  valor binario es: {bin(resultado)} " )

resultado = num_1 | num_2
#OR  0 |
print(f"El valor de binario es: {bin(resultado)} ") #compara cada balor binario si uno o ambos son 1 lo establce en el valor 1 de lo contrario lo establece en el valor 0
#Xor o ^
resultado = num_1 ^ num_2
print(f"El el  valor binario es: {bin(resultado)} " ) #El operador compara cada bit y lo establece en 1 si solo uno es 1; de lo contrario si ambos son 1 o son 0 se establecen en 0
#Not o ~
print(f"El valor binario de ~{num_1} es: {bin(~num_1)}") #El operador compara niega el resultado trasnformado los 1 en 0 y los 0 en 1, invierte el valor de cada bit
# << rellena dos ceros con desplazamiento a la izquierda 
print(f"El el  valor binario es: {bin(  num_2 << num_1)}")#Genra un desplazamiento entre 2 ceros hacia a izquierda 
# >> o desplazamiento a la derecha firmado 
print(f"El valor binario es: {bin(num_1 >> num_1)}")# Desplaza todos los bits una pocicion a la derecha

#Estrucutras de contol 

#Condicionales 
a = 33
b = 200
if b > a:
    print("b es mayor que a") 
elif b < a:
    print("b es menor que a")
else:
    print("los valores son iguales")

#bucle while

i = 0
while i < 5:
    print(f"repeticion numero{i} del bucle")
    i+=1


#bucle for

i = 0
for i in range(6):
    print(f"esta es la iteracion numero {i}")

#el bucle for se intra hasta llegar al limite del rango establecido 

#Estra 
for i in range(10, 56):
    if (i % 2 == 0) and (i != 16) and (i % 3 != 0):  # Condición válida
        print(f"{i}")  # Se imprime el valor que cumple la condición


