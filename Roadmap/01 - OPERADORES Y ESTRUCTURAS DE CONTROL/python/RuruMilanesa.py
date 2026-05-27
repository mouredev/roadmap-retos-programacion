'''Operadores.'''

#Operadores aritméticos.
print(f"suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"multiplicación: 10 * 3 = {10 * 3}")
print(f"división: 10 / 3 = {10 / 3}")

#Módulo es el sobrante de una división
print(f"módulo: 10 % 3 = {10 % 3}") 

'''El modulo determina el sobrante de cuantas veces entra el divisor en el dividendo, es decir: 
Si tenemos 51 (dividendo) y lo dividimos entre 5 (el divisor) aunque la división da 10.2
el módulo usa cuántas veces entra el divisor sin pasarse (10), y calcula el resto a partir de eso
En 51 el 5 entra 10 veces, porque 5*10=50 si fuera 5*11=55, lo que es mayor a 51
entonces ya que 5 entra 10 veces en 51, eso da un total de 50 (5*10) y 51-50=1, entonces el modulo es 1'''

#Este codigo es provisional para entender el modulo, pero no funciona para numeros negativos
dividendo = int(input("ingrese un número")) #int(input) indica que se tiene que ingresar un numero entero
divisor = int(input("ingrese divisor"))

'''mientras que dividendo sea mayor o igual a divisor, seguirá restando divisor
51-5=46 (46>5), 46-5=41 (41>5),... 6-5=1 (1<5), dividendo = 1)'''
while dividendo >= divisor :
    dividendo = dividendo - divisor 
    
#una vez que dividendo no pueda ser restado por divisor, ese es el modulo, el "resto"
print(dividendo)
'''también se puede usar:
dividendo = int(input("ingrese un número"))
divisor = int(input("ingrese divisor"))
cociente = dividendo // divisor 
modulo = dividendo - cociente * divisor
print(modulo)'''

print(f"exponente: 10 ** 3 = {10 ** 3}")
print(f"division entera: 10 // 3 = {10 // 3}")

#Operadores de comparacion

print(f"igualdad: 10 == 3 es {10 == 3}")
print(f"desigualdad: 10 != 3 es {10 != 3}")
print(f"mayor que: 10 > 3 es {10 > 3}")
print(f"menor que: 10 < 3 es {10 < 3}")
print(f"mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"menor o igual que: 10 <= 3 es {10 <= 3}")

#Operadores Logicos
#And pregunta si ambas solicitudes son verdaderas
print(f"and &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
#or pregunta si una u otra es verdadera
print(f"or ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
#not pregunta si la operaicon es falsa, si es falsa, dira verdadero.
print(f"not !: not 10 + 3 == 14 {not 10 + 3 == 14}")

#Operadores de asignacion
mi_numero = 11 #Asignación
mi_numero += 1 #suma y asignación
mi_numero -= 1 
mi_numero /= 1 
mi_numero *= 1
mi_numero %= 1
mi_numero **= 1
mi_numero //= 1 

#operadores de identidad
mi_nuevo_numero = mi_numero 
print(f"mi_numero is mi_nuevo_numero = {mi_numero is mi_nuevo_numero}")
print(f"mi_numero is not mi_nuevo_numero = {mi_numero is not mi_nuevo_numero}")
#este operador estoy seguro que me dará dolores de cabeza en el futuro

#Operadores de pertenencia 
print(f"'a' in 'brain' {'a' in 'brain'}")
#este operador indica que si algo está dentro de otro algo
print(f"'c' not in 'brain' {'a' not in 'brain'}")
#lo mismo pero si no está dentro de algo

#Operadores de bit
a = 5 #101
b = 6 #110
#Compara los bits de cada parámetro
print(f"AND 5 & 6 = {a & b}") 
print(f"OR 5 | 6 = {a | b}") 
print(f"XOR 5 ^ 6 = {a ^ b}") 
print(f"NOT ~5 = {~a}") 
"""
~n = -(n + 1) Toma n, le suma 1 y lo vuelve negativo

Ejemplos:
~10   = -(10 + 1)  = -11
~5    = -(5 + 1)   = -6
~0    = -(0 + 1)   = -1
~-1   = -(-1 + 1)  = 0
~-5   = -(-5 + 1)  = 4

Una explicación interesante sobre por qué es ~n = -(n + 1):
supongamos que tenemos n = 1, sería como ~1 = -(1 + 1) = -2
y es comprensible ya que 1 decimal es 1 en binario, aunque esto tiene un matiz importante
en realidad no es 1, sino que es una fila de infinitos 0 y luego el 1, quedaría algo como ...0001
también depende de cuántos bits de información estemos usando, si tenemos 1 en binario en 8 bits, el número sería 0000 0001
cuando el módulo "da vuelta" los números binarios, esos 0 también se cambian, entonces el número binario invertido de 1 es
...1110.
entonces se interpreta de esta manera tal que n es un número cualquiera (un dato en forma de bits)
invierte todos sus números y toma el primer número, para 0000 0001 | 1111 1110
dado que el primer número es 1, el número es negativo

pero hay varios problemas, para empezar, si se lee el número nuevo "1111 1110" esto es 254 en decimal
este proceso no identifica el número completo, solo identifica el primer número y designa si es o no positivo al número
antes de invertirlo
n = 1 
1 es el número
se invierte
empieza con 1, es negativo
-1

esto funcionaría de maravilla, se lo conoce como complemento a uno, pero entonces "por qué el +1?"

la cuenta inicial dice "~n = -(n + 1)" pero en la explicación no sumé el 1, vamos a entender por qué.

el problema nace si n = 0
para cada número positivo funcionaría correctamente, pero si n = 0 entonces pasa algo curioso
para 8 bits 0 es 0000 0000, invertir todo sería 1111 1111, esto hace que el módulo indique que ~n es igual a -0
esto trae implicaciones porque le da un espacio a 0 y -0 y esto obviamente no puede existir
de aquí nace el "twos complement" que es la cuenta anterior nombrada, el "+1" que veíamos.
si n = 0, entonces:
~0 = -(0 + 1) = -1
hay que tener en cuenta que el hardware solo invierte los números.
el que se le sume +1 es lo que hace el twos complement, por eso el funcionamiento es:
para n = 0, la máquina toma 0000 0000 luego lo invierte 1111 1111
luego two complement suma 1 y queda 1 0000 0000
luego toma el primer número, es 1? entonces es negativo.
como 1111 1111 (o cualquier base bit siempre será 1) y sumas 1, pasa todo a ser 0 (y aque el 1 se descarta)
entonces diras "pero el 0 es postivio" y es correcto, es +0
Esto suma 1 bit, y quizás estés pensando que si el número principal era con 0 infinitos, al darlos vuelta serán
1 infinitos, y a 1 infinito no se le puede sumar 1, si n = 0 entonces es ...000, al darlos vuelta es ...111
y a ...111 no se le puede sumar 1, y es lógico, pero hay que separar la lógica del hardware
el hardware toma los datos ingresados en bits seleccionados, la explicación infinita anterior era para que se entienda que
5 = 101 solo en 3 bits, 5 también puede ser 0101 en 4 bits, o 00000101 en 8 bits, y eso es lo que toma el hardware,
la explicación de infinito es para que se entienda que no importa cuántos bits se tomen, para cada dato siempre habrán 0
que tiendan a infinito a su izquierda.
por eso cuando se utiliza n = 1 el resultado no es -1, es -2
~1 = -(1 + 1) = -(2), soluciona el problema del -0.

o bueno, al menos eso entendí yo
"""

print(f"desplazamiento a la derecha: 10 >> 2 {10 >> 2}") #Desplaza los numeros binarios a la derecha, 1010 pasa a ser 0010
print(f"desplazamiento a la izquierda: 10 << 2 {10 << 2}") #Desplaza los numeros binarios a la izquierda, 1010 pasa a ser 1000
'''
Estructuras de contról
'''

#Condicionales

tkm = "te quiero mucho"
if tkm == "te kiero muxo":
    print("tkm es 'te kiero muxo'")
elif tkm == "te quiero mucho":
    print("tkm es te quiero mucho")
else: 
    print("tkm no es 'te kiero muxo' ni 'te quiero mucho'")

# Iterativas

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

#Manejo de excepciones
try:
    print(10 / 1)
except:
    print("Se rompió algo oe")
finally: 
    print("terminó la cuestión")

# Extra

for p in range (10, 56):
    if p % 2 == 0 and p != 16 and p % 3 != 0:
        print(p)

#como saber si un numero es par
'''Si p fuera 20, "p % 2 == 0" buscaria el modulo, ya que no hay sobrante, porque 2 entra 10 veces en 20
el modulo da 0, entonces pregunta (p % 2) es == 0? efectivamente, entonces es par.'''
#para que no entre 16 en el rango
'''and "p != 16" está diciendo claramente "p es desigual de 16" esto quiere decir:
supongamos que va en 14, esto es par, entonces se imprime, luego sigamos con el 15, esto es impar, no se imprime
luego sigamos con 16, esto es par, se imprimiria a de no ser que la funcion completa es 
"tiene que ser par y desigual de 16" ya que 16 no es desigual de 16, entonces no cumple los requisitos. '''
#como saber si es multiplo de 3
'''and "p % 3 != 0" está indicando el modulo 3 en p es desigual de 0
la primer expresion es:
si tenemos 30, este numero es par, ya que al dividir 30 en 2 da 15 no sobra nada entonces 30 % 2 == 0
la segunda expresion es:
30 a su vez es desigual de 16
la tercer expresion es:
si 30 se divide en 3 deja un sobrante de 0, 3 entra perfectamente 10 veces en 30, entonces el modulo es 0
la pregunta es "ese modulo es desigual de 0?" ya que el modulo de 30 % 3 es 0 y es igual a 0
no se cumple el parametro, para que se cumpla el modulo 3 de p tiene que ser diferente de 0
'''
