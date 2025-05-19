# """
# Operadores
# """
# #operadores aritmeticos

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta = {10 - 3}" )
print (f"Modulo = {10 % 3}")
print(f"Multiplicacion = {10 * 3}")
print(f"division = {10 / 3}")

#Operadores comparacion
print(f"Igualdad: 10==3 es {10==3}")
print(f"Desigualdad:!= {10 !=3}" )
print(f"mayor que = {10>3}")
print(f"mejor que {10<3}")
print(f"mayor o igual que = {10 >= 3}")
print(f"menor o igual que = {10<=3 }")

#Operadores logicos
print(f"AND es {10 + 3 == 13 and 5 - 1 ==4 }")
print(f"OR es {10 + 3 == 13 and 5 - 1 ==4 } ")
print(f"NOT es {not 10 + 3 == 14}") 

#Operaciones de aignacion
my_number = 11
print (my_number)
my_number += 4
print (my_number)
my_number -= 2
print(my_number)
my_number *=3
print(my_number)
my_number /=1
print(my_number)
my_number %= 2
print(my_number)

#Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_numberc es {my_number is my_new_number}")
print(f"my_number is not my_new_numberc es {my_number is not my_new_number}")

#Operadores de pertenencia
print(f"'u' in 'moure' = {'u' in 'moure'}")
print(f"'A' in 'Anzin' = {'A' in 'Anzin'}")
print(f"'b' not in 'lucho'= {'b' not in 'lucho'}")

#Operadores de bit
a = 10  #numero bits 1010
b = 3   # 0011
print(f"AND: = {10 & 3}")
print(f"OR = {a | b}")
print(f"XOR = {a ^ b}")
print(f"NOT = {~10}")
print(f"Desplazamiento D = {a >> b}")
print(f"Desplazamiento I = {a << b}")

# """
# Estructura de control
# """

# #condicionales
# my_string = "viejo"

# if my_string == "anzin":
#     print("Mi usuario es anzin")
# elif my_string == "viejo":
#     print("Este si es mi usuario")    
# else:
#     print("Ese no es mi usuario")
    
# #Iterativas
# for i in range(11):
#     print(i)   

# for i in range(5):
#     print(i)

# i = 0

# while i <= 10:
#     print(i)  
#     i += 1


# #Manejo de excepciones
# try:
#     print(10 / 0)
# except:
#     print("Se a producido un error") 
# finally:
#     print("Ha finalizado el manejo de excepcion")    

# ##EJERCICIO EXTRA
     
# for num in range(10, 56):
#     if num % 2 ==0 and num !=16 and num % 3 ==0:
#         print(num)



# saludo = "Hola"
# print(saludo)  
# nombre = input("¿Como te llamas?: ")   
# print("Bienvenido", nombre)
# edad = int(input("Ingresa tu edad: "))
# print("Tu edad es: ", edad)

# if edad>=18:

#     print("Usted puede continuar")
# else:
#     print("Disculpe no puede continuar")    

# text = input("Quien te envio? ")

# text =="anzin"

# if text == "anzin":
#     print("Bienvenido señor")
# else:
#     print("Usted no puede ingresar")   
    


####################################################################

#Operadores 
#Aritmeticos
x = 15
y = 5

suma = x + y 
print(f"La suma de 15 + 5: {suma}")
resta = x - y
print(f"resta de 15 - 5: {resta}")

#Comparacion
print(f"15 es mayor que 5? :{15 > 5}")
print(f"5 es mejor que 15?: {15>5}")

#asignacion
num1 = 5
print(f"Estos numeros son {num1}")
num2 = 10
print(f"Este numero es {num2}")

#logicos
print(f"estos numeros son: {num1 < 10 and num2 > 5}")
print(f"num1 es mayor que 10 y num2 es menor que 5: {num1 > 10 or num2<5}")
print(f"num1 no es mayor que num2: {not(num1 > num2)}")

j = 10
if not (j > 5):
    print("j no es mayor que 5")
else:
    print("j es mayor que 5")

#Condiciones
a = 20
if a > 5:
    print("a es mayor que 5")
elif a == 5:
    print("a es igual a 5")
else:
    print("a es menor que 5")


#Bucles 
    #for

personas = ["Jose", "Luis", "Mateo"]
for persona in personas:
    print(persona)

#recorrer numeros
for i in range(3):
    print(i)


    #while
#repetir mientras es verdadera
contador = 0
while contador < 5:
    print(contador)
    contador += 1 #incrementea para evitar bucles infitos



usuarioc = "Andy"
clavec = "python123"

usuario = ""

while usuario != usuarioc:
    usuario = input("Ingresa tu usuario: ")
    if usuario != usuarioc:
        print("Usuario incorrecto")
print(f"Bienvenido señor {usuario}")

clave = ""
while clave != clavec:
    clave = input("Ingrese la clave: ")
    if clave != clavec:
        print("Contraseña incorrecta. Ingrese otra vez")
else:
    print("Ingreso accedido, disfruta las comodidades")



