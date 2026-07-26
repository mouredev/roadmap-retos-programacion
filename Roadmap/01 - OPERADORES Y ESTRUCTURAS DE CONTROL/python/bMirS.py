"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
#OPERADORES ARITMÉTICOS
#Suma
print(f"5+3= {5+3}")
#Resta
print(f"9-10={9-10}")
#División
print(f"10/5={10/5}")
print(f"5/10={5/10}")
#Multiplicación
print("5*3=", 5*3)
#Division Entera
print("5//10=", 5//10)
#Modulo
print("10%2=", 10%2)
#Concatenar
nombre1="Adelina"
nombre2="Gato Montes"
print(f"Los nombres contatenados son {nombre1+" "+nombre2}")
resultado1="Hola"
resultado2=input("Ingresa tu nombre: ")
concatenar=resultado1+", "+resultado2
print(concatenar)
#Repetir 
signo="+"
print(signo*1)
print(signo*2)
print(signo*3)
print(signo*4)
print(signo*5)
print(f"Operadores de Comparación {signo*10}")
numero1=int(input("Ingresa un numero entero: "))
numero2=int(input("Ingresa otro numero entero: "))
if numero1>numero2:
    print(f"{numero1} es mayor {numero2}")
elif numero1==numero2:
    print("Los numeros son iguales")
else:
    print(f"{numero2} es mayor a {numero1}")
#Igualdad
print("5==3", 5==3)
contrasena=False #La contraseña es falsa
if contrasena!= False:
   print("Contraseña es verdadera")
else:
    print("Contraseña falsa")
numero=5
#operadores de asignación
numero+=2 #suma y asignacion
print(numero)
numero*=2
print(numero)
numero/=2
print(numero)

#operadores de identidad
texto="Acatlan"
if "a" in texto:
    print("Escuela Acatlan")
else:
    print("No eres de acatlan")

my_list=["Manzana", "taza", "tetera"]
if "Manzana" in my_list:
    print("Esta en la lista")
else:
    print("No esta en la lista")
#operadores de pertenencia 

#estan en la misma dirección de memoria
a=3
b=5
print(f"Estan en la misma direccion de memoria {a is b}")

#Condicionales
edad=int(input("Dame tu edad: "))
credencial= input("Tiene credencial si o no: ")
credencial=credencial.lower()
credencial=credencial.replace(" ","")
if edad>=18 and credencial=="si":
    print("Puede entrar")
elif credencial=="no":
    print("No puede entrar")
else:
    print("No puede entrar")
#bucles 
for fila in range(0,4):
    for columna in range(0,fila+1):
        print("*", end="")
    print()
print("\n")
for fila in range (4,0, -1):
    for columna in range(0, fila):
        print("*", end="")
    print()
for fila in range(0, 4, 1):
    for columna in range(0,7,1):
        print("*", end="")
    print()
z=4
l=1
for i in range(0,4):
  for j in range(0,z-i): 
      print(" ", end="")  
   
  for h in range(0, l): 
      print("*", end="")  
  l=l+2
  print()   

for num in range(10, 56):
    if num%3!=0 and num!=16 and num%2==0:
      print(num)
#Manejo de excepciones
try:
    print(10/0)
except:
    print("Se cacho el error")
print("Hola")