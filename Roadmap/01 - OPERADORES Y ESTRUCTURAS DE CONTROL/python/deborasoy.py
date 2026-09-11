'''
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: 
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
'''

#Operadores Ariméticos 
suma = 2001+24
print(f"suma: 2001 + 24 = {suma}") #f{} interpolacion en cadena de texto, logra incorporar codigo en medio de cadenas de texto
resta= 2025-2001
multiplicacion = suma * resta
division = multiplicacion / resta 
exponenciacion = 10**2
modulo = multiplicacion % resta 
division_entera = multiplicacion // resta 
#A diferencia de la division / da un numero con coma si es que el resultado lo tiene, la division entera // redondea el numero 

#operadores de Asignación 
numero_tres = 3
numero_tres += 4
numero_tres -= 5
numero_tres *= 6
numero_tres /= 7
numero_tres %= 8
numero_tres **= 9

#Operadores Lógicos
conjuncion = 3 < 5 and  2 < 10
disyuncion = 2 < 5 or 10 < 4
negacion = not(conjuncion)

#Operadores de Comparación 
igual = 3 == 3
no_igual = 3 != "3"
mayor_que = 5 > 4 
menor_que = 4 < 5
mayor_igual = 10 >= 6
menor_igual = 2 <= 2

#Operadores de Pertenencia 
#Verifican si un elemento o secuencia existe dentro de una colección (cadena, lista, tupla, diccionario, conjunto)

email = "debora@ejemplo.com"
print("@" in email)         # True  -> Revisa si el carácter '@' está presente.
print("admin" not in email) # True  -> Confirma que 'admin' no forma parte de la cadena.

frutas = ["manzana", "banana"]
print("manzana" in frutas)  # True  -> Revisa pertenencia en una lista.

#Operadores de Identidad
#Comparan si dos variables apuntan a la mismas posición exacta en la memoria RAM

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)     # True  -> Tienen el mismo contenido (igualdad de valor)
print(x is y)     # False -> Son dos objetos DISTINTOS guardados en memorias diferentes.
print(x is z)     # True  -> z apunta exactamente a la misma posición que x.

#operadores bit a bit 

#Operan convirtiendo los números decimales a su representación binaria (0s y 1s) y aplicando puertas lógicas bit a bit

a = 10  # 1010 (valor del 10 en bit) 
b = 3 #0010 ( valor del 3 en bit)

f" AND : 10 & 3 = { 10 & 3 } " #output 0010
f" OR : 10 | 3 = { 10 |  3 } " # output 1011
f" XOR : 10 ^ 3 = { 10 ^3}" #output 1001
f" NOT : ~10 = { ~10 }" #output 


'''
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que exista en tu lenguaje:
Condicionales, iterativas, excepciones...
Debes hacer print por consola del resultado de todos los ejemplos.
'''
#estructuras condicionales 
'''
if "condicion":
    print()

if "condicion":
    print()
elif "condicion":
    print()

if "condition":
    print()
else:
    print()

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#estructuras iterativas
i= 1
while i < 6: 
   print(i)
   if i == 3: 
      break 


for i, variable in lista : 
  print(i)
  print(variable)

for variable in lista : 
  print()

range(0,5)

for variable in range()

   '''

'''
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
indice = 9


while indice < 55: 
    indice += 1
    resto_division_pares = indice % 2 
    resto_division_multiplos_tres = indice % 3

    if resto_division_pares == 0 and resto_division_multiplos_tres != 0 and indice != 16 :
        print(indice)

for number in range(10,56):
    if number % 2 == 0  and number != 16 and number % 3 != 0:
        print(number)