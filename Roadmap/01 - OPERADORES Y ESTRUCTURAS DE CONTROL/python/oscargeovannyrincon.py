'''/*
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
 */'''
print('OPERADORES DE ASIGNACION \n')
x=5
print(f'Asignacion de un valor, x={x}')
x+=3
print(f'Operador += x+=3, x={x}')
x-=3
print(f'Operador -= x-=3, x={x}')
x*=3
print(f'Operador *= x*=3, x={x}')
x/=3
print(f'Operador /= x/=3, x={x}')
x%=3
print(f'Operador %= x%=3, x={x}')
x=27
x//=3
print(f'Operador //=, x=27, x//=3, x={x}')
x**=3
print(f'Operador **= x**=3, x={x}')
x=10
x&=15
print(f'Operador &=, x={x}')
x=10
x|=5
print(f'Operador |=, x={x}')
x=10
x^=5
print(f'Operador ^=, x={x}')
x>>=3
print(f'Operador >>= x>>=3, x={x}')
x<<=3
print(f'Operador <<= x<<=3, x={x}')

print('\nOPERADORES ARITMETICOS')
x=15
y=7
z=x+y
print(f"Operador +\n{x}+{y}={z}")
z=x-y
print(f"Operador -\n{x}-{y}={z}")
z=x*y
print(f"Operador *\n{x}*{y}={z}")
z=x/y
print(f"Operador /\n{x}/{y}={z}")
z=x%y
print(f"Operador %\n{x}%{y}={z}")
z=x**y
print(f"Operador **\n{x}**{y}={z}")
z=80//6
print(f"Operador //\n{x}//{y}={z}")

print('\nOPERADORES COMPARACION')
x=15
y=7
print(f'x={x}, y={y}')
print(f'Operador  IGUAL ==\nx==y=>{x==y}')
print(f'Operador NO ES IGUAL !=\nx!=y=>{x!=y}')
print(f'Operador MAYOR QUE >\nx>y=>{x>y}')
print(f'Operador de MENOR QUE <\nx<y=>{x<y}')
print(f'Operador de MAYOR O IGUAL QUE >=\nx>=y=>{x>=y}')
print(f'Operador de MENOR O IGUAL QUE <=\nx<=y=>{x<=y}')


print('\nOPERADORES LOGICOS')
print('3 > 2 and 4 > 3', 3 > 2 and 4 > 3) #true
print('3 > 2 and 4 < 3', 3 > 2 and 4 < 3) #false
print('3 < 2 and 4 < 3', 3 < 2 and 4 < 3) #false
print('True and True: ', True and True)#true
print('3 > 2 or 4 > 3', 3 > 2 or 4 > 3)  #true
print('3 > 2 or 4 < 3', 3 > 2 or 4 < 3)  #true
print('3 < 2 or 4 < 3', 3 < 2 or 4 < 3)  #false
print('True or False:', True or False)#true
print('not 3 > 2', not 3 > 2)     #false
print('not True=>', not True)      #false
print('not False=>', not False)     #true
print('not not True=>', not not True)  #true
print('not not False=>', not not False,'\n')#false

'''* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.'''
 
#       CONDICIONALES       #

num=9
if num>=10 and num<=20:
    print('Su numero esta entre 10 y 20, incluidos')
elif num<10:
    print('El numero es menor que 10')
else:
    print('El numero es mayor que 20')

#       ITERATIVAS      #

numeros=list(range(0,20))
print(f'Esta es la lista {numeros}')
indice=0
print('Estos son los numeros divisibles por 3 de la lista')
while indice<25:
    if indice<len(numeros):
        variable=numeros[indice]
        if variable%3==0:
            print(numeros[indice])
        indice+=1
    else:
        print('Se acabo el ciclo while')
        break

frutas=['Melón', 'Ciruela', 'Melocotón', 'Nectarina', 'Sandía', 'Cereza', 'Uva', 'Higos', 'Albaricoque', 'Naranja', 'Mango', 'Aguacate', 'Níspero', 'Mora']
print(f'Esta es una lista de frutas, {frutas}')
print('Estas son las frutas en indices pares')
for indice_1 in range(len(frutas)):
    if indice_1%2==0:
        print(f'Indice {indice_1}, fruta {frutas[indice_1]}')
        
#       EXCEPCIONES     #

#print("Realizaremos una division de dos numero\nIngresa el primer numero")
numero_1=input("Realizaremos una division de dos numero\nIngresa el primer numero: ")
#numero_1=float(numero_1)
#print( "Ingrese el segundo numero")
numero_2=(input("Ingrese el segundo numero: "))
#numero_2=int(numero_2)
#print(f'El resultado de la divion {numero_1}/{numero_2} es {numero_1/numero_2}')
try:
    #print(f'El resultado de la divion {numero_1}/{numero_2} es {int(numero_1/numero_2)}')
    print(f'El resultado de la divion {numero_1}/{numero_2} es {float(numero_1)/float(numero_2)}')
except ValueError:
    print('Error de valor')
except ZeroDivisionError:
    print('Error division por cero')
else:
    print('Impresion correcta')
finally:
    print('Fin del programa de control')
    

'''/*
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */'''
numbers=list(range(10,56))
#print(numbers)
for number in numbers:
    if number%2==0:
        if number!=16:
            if number%3!=0:
                print(number)