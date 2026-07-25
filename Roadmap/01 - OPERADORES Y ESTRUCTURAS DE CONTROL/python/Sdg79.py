#Aritmeticos
numero1 = 4
numero2 = 10
suma = numero1 + numero2
print(suma)
resta = numero2 - numero1
print(resta)
multiplicacion = numero1 * numero2
print(multiplicacion)
division = numero2 / numero1
print(division)
modulo = numero2 % numero1
print(modulo)
exponente = numero2 ** numero1
print(exponente)
division_entera = numero2 // numero1
print(division_entera)

#Comparación
print(f"Numero 1 Igual al Numero 2: {numero1 == numero2}")
print(f"Numero 1 distinto al Numero 2: {numero1 != numero2}")
print(f"Numero 1 menor al Numero 2: {numero1 < numero2}")
print(f"Numero 1 mayor al Numero 2: {numero1 > numero2}")
print(f"Numero 1 menor o igual al Numero 2: {numero1 <= numero2}")
print(f"Numero 1 mayor o igual al Numero 2: {numero1 >= numero2}")

#Lógicos
print(f"and Numero 1 = 4 y Numero 2 = 10: {numero1 == 4 and numero2 == 10}")
print(f"or Numero 1 = 4 o Numero 2 = 10: {numero1 == 4 or numero2 == 10}")
print(f"not Numero 1 = 4 y Numero 2 = 10: {not numero1 == 4 and numero2 == 10}")

#Asignación
numero1 = 4
print(numero1)
numero1 += 1
print(numero1)
numero1 -= 1
print(numero1)
numero1 *= 2
print(numero1)
numero1 /= 2
print(numero1)
numero1 %= 2
print(numero1)
numero2 //= 2
print(numero2)
numero2 **= 2
print(numero2)
numero1 = int(numero1)
numero1 &= 2
print(numero1)
numero2 |= 2
print(numero2)
numero2 ^= 2
print(numero2)
numero2 >>= 2
print(numero2)
numero2 <<= 2
print(numero2)

#Identidad
print(numero1 is numero2)
print(numero1 is not numero2)

#Pertenencia
print(f"S en Sergio: {"S" in "Sergio"}")
print(f"S no en Sergio: {"S" not in "Sergio"}")

#Estructuras de control
edad = 45
if edad < 18:
    print("Es menor de Edad")
elif edad < 30:
    print("Es una persona adulta joven, menor de 30 años")
else:
    print("Es un adulto mayor de 30 años")


for i in range(5):
    print("numero: " + str(i))
    

contador = 0
while contador <= 6:
    print("Numeros hasta el 6: " + str(contador))
    contador += 1

#Excepciones

try:
    print(4/0)
except:
    print("Error, no se puede dividir por 0")
finally:
    print("continúa la aplicación")

"""
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
 """

for i in range(56):
    if i % 2 == 0 and i >= 10:
        if i % 3 != 0 and i != 16:
            print(i)
    
