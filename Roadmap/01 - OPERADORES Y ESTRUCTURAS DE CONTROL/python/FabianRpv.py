# Tipos de Operadores

num1 = 5
num2 = 2

#Operadores Aritmeticos:

suma = num1 + num2
print(f"suma: {suma}")
resta = num1 - num2
print(f"resta: {resta}")
multiplicacion = num1 * num2
print(f"multiplicacion: {multiplicacion}")
division = num1 / num2
print(f"division: {division}")
division_entera = num1 // num2
print(f"division entera: {division_entera}")
modulo = num1 % num2
print(f"modulo: {modulo}")
potencia = num1 ** num2
print(f"potencia: {potencia}")


#Operadores Logicos:

op_and = True and False
print(op_and)
op_or = True or False
print(op_or)
op_not = not True
print(op_not)

#Operadores de Comparación:

igualdad = 5 == 5
print(igualdad)
diferencia = 5 != 5
print(diferencia)
mayor_que = 2 > 5
print(mayor_que)
menor_que = 2 < 5
print(menor_que)
mayor_o_igual_que = 2 >= 2
print(mayor_o_igual_que)
menor_o_igual_que = 3 <= 2
print(menor_o_igual_que)


#Operadores de Asignación:

valor = 5   #Asignacion Basica
valor += 2  #sumar y asignar
valor -= 2  #restar y asignar
valor *= 2  #multiplicar y asignar
valor /= 2  #dividir y asignar
valor //= 2  #dividir entero y asignar
valor %= 2  #mmodulo y asignar
valor **= 2  #potencia y asignar


#Operadores de Identidad:

nuevo_valor = valor
print(nuevo_valor is valor)
print(nuevo_valor is not valor)


#Operadores de Pertenencia:

print('h' in 'hola')
print("h" not in "hola")


#Operadores Binarios:

and_binario = num1 & num2 
or_binario = num1 | num2 
xor_binario = num1 ^ num2 
not_binario = ~num1 
derecha_binario = num1 >> 1 
izquierda_binario = num1 << 1 




#Estructuras de Control

edad = 21

#Condicionales:

if(edad < 0 or edad > 100):
    print("Edad Invalida")
elif(edad < 18):
    print("Eres menor de Edad")
else:
    print("Eres mayor de Edad")


opcion = 3

match opcion:
    case 1:
        print("Opcion 1")
    case 2:
        print("Opcion 2")
    case 3:
        print("Opcion 3")


#Bucles:

for i in range(11):
    print(i)


frutas = ["Manzana", "Pera", "Fresa"]

for fruta in frutas:
    print(fruta)


contador = 0

while(contador < 3):
    print(contador)
    contador += 1


#Excepciones: 

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero!")
finally:
    print("Bloque final siempre se ejecuta")



for numero in range(10, 56):
    if(numero % 2 == 0 and numero != 16 and numero % 3 != 0):
        print(numero)