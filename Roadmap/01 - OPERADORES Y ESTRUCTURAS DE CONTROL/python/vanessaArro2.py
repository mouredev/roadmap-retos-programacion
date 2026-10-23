'''
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
#----------------------------------------------------------------------------------------------------------
#Operadores Aritméticos
"""se realiza interpolacion ("f" al principio y entre {} el codigo)
para poder realizar codigo ejecutable dentro de un string"""

print(f"suma: 24 + 5 = {24 + 5}") 
print(f"resta: 8 - 5 = {8 - 5}")
print(f"multiplicacion: 5 * 5 = {5 * 5}")
print(f"division: 5 / 2 = {5 / 2}") #el resultado es un numero decimal
print(f"division entera: 5 // 2 = {5 // 2}") #el resultado es un numero entero, sin decimales
print(f"potencia: 2 ** 3 = {2 ** 3}") #el resultado es 2 elevado a la potencia de 3
print(f"modulo: 6 % 5 = {6 % 5}") #el resultado es el resto de la division

#------------------------------------------------------------------------------------------------------------------------

#Operadores Logicos
print(f"and &&: 10 + 5 == 15 and 20 - 5 == 15: {10 + 5 == 15 and 20 - 5 == 15}") #devuelve True si ambas condiciones son verdaderas
print(f"or ||: 4 - 2 == 2 or 2 - 1 == 1: {4 - 2 == 2 or 2 - 1 == 1}" ) #devuelve True si al menos una de las condiciones es verdadera
print(f"not !: not 5 == 10: {not 5 == 5}") #niega la condicion, si es verdadera la convierte en falsa y viceversa

#------------------------------------------------------------------------------------------------------------------------

#Operadores de Comparación
print(f"igualdad: 5 == 5 = {5 == 5}")
print(f"desigualdad: 5 != 5 = {5 != 5}")
print(f"mayor que: 5 > 4 = {5 > 4}")
print(f"menor que: 4 < 10 = {4 < 10}")
print(f"mayor o igual que: 10 >= 10 ={10 >= 10}")
print(f"menor o igual que : 6 <= 5 = {6 <= 5}")

#------------------------------------------------------------------------------------------------------------------------

#Operadores de Asignación
"""
Son los operadores que permiten asignar valores a las variables y realizar operaciones al mismo tiempo.

Cada operador abreviado (+=, -=, *= ...) nunca vuelve a empezar desde el 6 original, 
sino que agarra el resultado exacto que la variable tenía justo en el paso anterior y 
le aplica la nueva operación. Los valores van cambiando en cadena
"""
ope_asig = 6  #Asignacion simple 
print(ope_asig)
ope_asig += 3  # Asignación con suma
print(ope_asig) 
ope_asig -= 3 # Asignación con resta
print(ope_asig)
ope_asig *= 2   # Asignación con multiplicación
print(ope_asig)
ope_asig /= 2 # Asignación con división
print(ope_asig) 
ope_asig //= 2 #Asignación con división entera
print(ope_asig)
ope_asig **= 2 #Asignación con potencia
print(ope_asig)
ope_asig %= 2 # Asignación con módulo
print(ope_asig)

#------------------------------------------------------------------------------------------------------------------------

#Operadores de Identidad
"""
Los operadores de identidad (is e is not) no miran el contenido de una variable, 
sino su dirección de memoria 
"""
oper_iden = 1.0
print(f"oper_iden is ope_asig es: {oper_iden is ope_asig}") #devuelve True si ambas variables apuntan al mismo objeto
print(f"oper_iden is not ope_asig es: {oper_iden is not ope_asig}") #devuelve True si ambas variables no apuntan al mismo objeto

#------------------------------------------------------------------------------------------------------------------------

#Operadores de Pertenencia
"""
El operador in te dice "Sí, está en la lista" (True) y el operador not in dice 
"No, no está en la lista" (False).
"""

trabajadores = ["Vanessa", "Juan", "Pedro", "Maria"]

print(f"'s' in 'Vanessa': {'s' in 'Vanessa'}") #devuelve True si el elemento está en la lista
print(f"'Juan' not in trabajadores: {'Juan' not in trabajadores}") #devuelve True si el elemento no está en la lista

if "Pedro" in trabajadores: # Nos sirve para comprobar si un elemento está en una lista, tupla, diccionario o conjunto
    print("Pedro es un trabajador")
else:
    print("Pedro no es un trabajador")

email = "arroyavefer@gmail.com"

if "@" in email: # Validacion rapida de si el correo es correcto 
    print("El email es valido")
else:
    print("El email no es valido")

#------------------------------------------------------------------------------------------------------------------------

#Operadores de Bits

#Sistema de permisos de un juego.

#Cada permiso es representado por un bit en un número entero.
leer_mapa = 1 #binario 001
atacar = 2 #binario 010
volar = 4   #binario 100

#Activar permisos para un jugador con | OR

#El jugador inicia sin ningun perimiso (000)
permisos_jugador = 0

#se da permiso de leer mapa y atacar (001 | 010 = 011)

permisos_jugador = permisos_jugador |leer_mapa |atacar
print(permisos_jugador) #imprime 3 (binario 011)
"""
porque 001 (1) OR 010 (2) = 011 (3) El resultado es 1 solo si los bits
son diferentes (uno es 1 y el otro es 0). Si son iguales, da 0.
ejemplo:
5  en binario ->  1  0  1
3  en binario ->  0  1  1
--------------------------
Resultado     ->  1  1  0  
"""

#Comprobacion de permisos con & AND

#se evalua si el jugador tiene permiso de atacar (011 & 010 = 010 (2))
if permisos_jugador & atacar:
    print("El jugador tiene permiso de atacar")
else: 
    print("El jugador no tiene permiso de atacar")
    
#se evaliua si el jugador tiene permiso de volar (011 & 100 = 000 (0))
if permisos_jugador & volar:
    print("El jugador tiene permiso de volar")
else: 
    print("El jugador no tiene permiso de volar")
    
#Quitar permisos con ~ NOT y & AND

#si se quiere quitar el permiso de atacar, se hace un NOT al permiso de atacar y luego un AND con los permisos del jugador
permisos_jugador = permisos_jugador & ~atacar
print(permisos_jugador) #imprime 1 (binario 001)
# Explicación: ~ATACAR convierte 010 en ...101. 
# Al hacer AND con los permisos del jugador (011), el bit del centro se apaga, quedando 001 (1).

#Alternar permiso usando ^ XOR
# El jugador encuentra una poción de vuelo (Activa VOLAR)
permisos_jugador = permisos_jugador ^ volar
print(permisos_jugador & volar)  # Imprime 4 (Permiso activado)

# Se termina el efecto de la poción (Desactiva VOLAR usando el mismo código)
permisos_jugador = permisos_jugador ^ volar
print(permisos_jugador & volar)  # Imprime 0 (Permiso desactivado)

#------------------------------------------------------------------------------------------------------------------------

#Estructuras de Control

#Estructura secuencial (es el flujo normal del programa, de arriba hacia abajo)

arriendo = 500000
servicios = 100000
total_a_pagar = arriendo + servicios
print(f"El total a pagar es: {total_a_pagar}")

#------------------------------------------------------------------------------------------------------------------------

#Estructura condicional 

""" 
if, elif, else (toma de decisiones)
Sistema de cobro para un cine, esto sirve para determinar la tarifa que debe pagar un cliente dependiendo de su edad
"""
edad_cliente = 12

if edad_cliente < 12:
    print("El cliente paga tarifa infantil $5.000")
elif edad_cliente >= 12 and edad_cliente <= 59:
    print("El cliente paga tarifa normal $10.000")
else:
    print("El cliente paga tarifa de adulto mayor $7.000")
    
    
"""
Estructura match-case (coincidencia de patrones)

sistema de envíos de un negocio. Dependiendo del código
de estado que tenga asignado el paquete, el sistema debe 
mostrar un mensaje diferente en la pantalla del cliente:
"""   
estado_del_pedido =  "P"

match estado_del_pedido:
    case "P":
        print("El pago esta pendiente, por favor realiza el pago para continuar con el proceso de envío.")
    case "E":
        print("(Enviado), El paquete esta en camino")
    case "ENT":
        print("(Entregado), El paquete ha sido entregado al destinatario")
    case "C":
        print("(Cancelado), El pedido ha sido cancelado")

#------------------------------------------------------------------------------------------------------------------------

#Estructura iterativa (bucle o ciclos)
"""
Bucle for, ideal para correr un bloque de código un número determinado 
de veces, o para recorrer elementos de una colección (lista, tupla, diccionario, etc.)

Se necesita calcular el precio total de una lista de compras que hizo un cliente.
"""

precios = [1000, 2000, 3000, 4000, 5000]
total = 0 # Variable acumuladora para guardar la suma total (comienza en 0)

for precio in precios:
    total += precio # Suma cada precio al total acumulado

print(f"El total a pagar es: {total}")

"""
Bucle while,repite el codigo de manera indefinida mientras una condicion sea verdadera, si la condicion es falsa, el bucle termina.
"""

energia_bateria = 30

while energia_bateria > 0:
    print(f"El nivel de bateria es: {energia_bateria}%")
    energia_bateria -= 10 # Disminuye la energía de la batería en 10% en cada iteración 
    
print("La batería se ha agotado. Por favor, recarga el dispositivo.")

"""
Al iniciar la vuelta, Python pregunta: ¿Es energia_bateria > 0? 
Si la respuesta es sí, ejecuta el bloque interno, resta 10 a la batería y vuelve a preguntar. Cuando llega a 0, la condición se vuelve falsa y el bucle termina, pasando a la última línea.
"""

"""
Control de bucles con break y continue
Palabras clave para alterar o finalizar el comportamiento de los bucles sobre la marcha.
"""
for numero in range(1, 11):  # Itera del 1 al 10
    if numero == 5:
        continue  # Salta la iteración cuando encuentra el número 
    if numero == 8:
        break  # Termina el bucle cuando encuentra el número 8  
        print(f"El número es: {numero}") 
else:
    print("Bucle completado sin interrupciones.")  # Se ejecuta si el bucle termina normalmente
    
#------------------------------------------------------------------------------------------------------------------------   

#Estructuras de excepción try, except, finally (manejo de errores)
"""
Controlan los fallos en tiempo de ejecución para evitar que el programa colapse 
"""
def dividir_fondos(dinero_total, personas):
    try:
        # Código que podría fallar
        cuota = dinero_total / personas
    except ZeroDivisionError:
        # Qué hacer si intentan dividir entre 0
        print("Error: No puedes dividir dinero entre cero personas.")
    except TypeError:
        # Qué hacer si mandan letras en vez de números
        print("Error: Los datos ingresados deben ser numéricos.")
    else:
        # Se ejecuta SOLO si el 'try' funcionó a la perfección
        print(f"Cada persona recibe: ${cuota}")
    finally:
        # Se ejecuta SIEMPRE, pase lo que pase
        print("Operación financiera finalizada.")


dividir_fondos(100, 0)

#------------------------------------------------------------------------------------------------------------------------

""" 
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for numero in range(10, 56):  # Itera del 10 al 55
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0: # Verifica si el número es par, no es 16 y no es múltiplo de 3
        print(numero)
