'''Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)'''

# -------ARITMÉTICOS-----------
num1 = 5
num2 = 4

# SUMA (+)
suma = num1 + num2
print("SUMA")
print(num1,"+",num2,"=",suma)
print("----")

# RESTA (-)
resta = num2 - num1
print("RESTA")
print(num1,"-",num2,"=",resta)
print("----")

# MULTIPLICACIÓN (*)
multi = num1 * num2
print("MULTIPLICACIÓN")
print(num1,"*",num2,"=",multi)
print("----")

# DIVISIÓN (/)
division = num1 / num2
print("DIVISIÓN")
print(num1,"/",num2,"=",division)
print("----")


# DIVISION ENTERA (//)
division_entera = num1 // num2
print('DIVISION ENTERA')
print(num1,'//',num2,'=',division_entera)
print('----')


# MODULO (%)
modulo = num1 % num2
print('MODULO')
print(num1,'%',num2,'=',modulo)
print('----')


# POTENCIACIÓN (**)
potencia = num1 ** num2
print('POTENCIACIÓN')
print(num1,'**',num2,'=',potencia)
print('----')







# -------LÓGICOS-----------
verdadero = True
falso = False

# AND (and)
print("AND")
print("Verdadero AND falso =",verdadero and falso )


# OR (or)
print("OR")
print("Verdadero OR falso =",verdadero or falso )


# NOT (not)
print("NOT")
print("NOT Verdadero =",not verdadero )




# -------DE COMPARACIÓN-----------


# MAYOR QUE (>)
mayor_que = num1 > num2
print('MAYOR QUE')
print(num1,'>',num2,'=',mayor_que)
print('----')

# MENOR QUE (<)
menor_que = num1 < num2
print('MENOR QUE')
print(num1,'<',num2,'=',menor_que)
print('----')

# IGUAL QUE (==)
igual_que = num1 == num2
print('IGUAL QUE')
print(num1,'==',num2,'=',igual_que)
print('----')

# MAYOR O IGUAL QUE (>=)
mayor_igual_que = num1 >= num2
print('MAYOR O IGUAL QUE')
print(num1,'>=',num2,'=',mayor_igual_que)
print('----')

# MENOR O IGUAL QUE (<=)
menor_igual_que = num1 <= num2
print('MENOR O IGUAL QUE')
print(num1,'<=',num2,'=',menor_igual_que)
print('----')

# DESIGUAL A (!=)
desigual = num1 != num2
print('DESIGUAL A')
print(num1,'!=',num2,'=',desigual)
print('----')


# -------DE ASIGNACIÓN-----------

# ARITMÉTICOS

# ASIGNACION DIRECTA (=)
variable = num1 
print('ASIGNACION DIRECTA')
print('Variable =',variable)
print('----')

# INCREMENTAR (+=)
variable += num2
print('INCREMENTAR')
print('Variable += num1 =',variable)
print('----')

# DECREMENTAR (-=)
variable -= num2
print('DECREMENTAR')
print('Variable -= num2 =',variable)
print('----')

# MULTIPLICAR (*=)
variable *= num2
print('MULTIPLICAR')
print('Variable *= num2 =',variable)
print('----')

# DIVIDIR (/=)
variable /= num1
print('DIVIDIR')
print('variable /= num1 =',variable)
print('----')

# DIVIDIR ENTERO (//=)
variable //= 2
print('DIVIDIR ENTERO')
print('variable //= 2 =',variable)
print('----')

# MODULO (%=)
variable %= num2
print('MODULO')
print('variable %= num2 =',variable)
print('----')

# POTENCIACIÓN (**=)
variable **= num2
print('POTENCIACIÓN')
print('variable **= num2 =',variable)
print('----')

# LÓGICOS BIT A BIT

# AND B a B (&=)
variable = num1
variable &= num2
print('AND B a B')
print(num1,'&=',num2,'=',variable)
print('----')

# OR BaB (|=)
variable = num1
variable |= num2
print('OR BaB')
print(num1,'|=',num2,'=',variable)
print('----')

# XOR BaB (^=)
variable = num1
variable ^= num2
print('XOR BaB')
print(num1,'^=',num2,'=',variable)
print('----')

# DESPLAZAMIENTO A LA DERECHA BaB (>>=)
variable = num1
variable >>= num2
print('DESPLAZAMIENTO A LA DERECHA BaB')
print(num1,'>>=',num2,'=',variable)
print('----')

# DESPLAZAMIENTO A LA IZQUIERDA BaB (<<=)
variable = num1
variable <<= num2
print('DESPLAZAMIENTO A LA IZQUIERDA BaB')
print(num1,'<<=',num2,'=',variable)
print('----')


# -------DE IDENTIDAD-----------

# ES (is)
variable = num1 is num2
print('ES')
print(num1,'is',num2,'=',variable)
print('----')

# NO ES (is not)
variable = num1 is not num2
print('NO ES')
print(num1,'is not',num2,'=',variable)
print('----')


# -------DE PERTENENCIA-----------
lista = [i for i in range(10)]

# EN (in)
variable = num1 in lista
print('EN')
print(num1,'in',lista,'=',variable)
print('----')

# NO EN (not in)
variable = num1 not in lista
print('NO EN')
print(num1,'not in',lista,'=',variable)
print('----')


# -------DE BITS-----------
    # ----LÓGICOS----

# AND (&)
print("AND")
print("Verdadero AND falso =",verdadero & falso )
print('----')


# OR (|)
print("OR")
print("Verdadero OR falso =",verdadero | falso )
print('----')


# XOR (^)
print("XOR")
print("Verdadero XOR falso =",verdadero ^ verdadero )
print('----')


# NOT (~)
print("NOT")
print("NOT Verdadero =", ~verdadero )
print('----')

    # ----DE DESPLAZAMIENTO----
num1_bin = 0b100100

# A LA IZQUIERDA(<<)
print('A LA IZQUIERDA')
print('Num1_b(',bin(num1_bin),') << 3 =',bin(num1_bin << 3))
print('----')

# A LA DERECHA(>>)
print('A LA DERECHA')
print('Num1_b(',bin(num1_bin),') >> 2 =',bin(num1_bin >> 2))
print('----')




# -------ASIGNACIÓN EN EJECUCIÓN-----------

# WALRUS (:=)
if (variable := num2)==num2:
    print('WALRUS')
    print(num2,variable)


'''- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan  en tu lenguaje:
  Condicionales, iterativas, excepciones...'''

# -------CONDICIONALES-----------

# IF
print('IF')
if num1 < num2:
    print(num1,'es menor que',num2)
elif num1 > num2:
    print(num1,'es mayor que',num2)
else:
    print(num1,'es igual a',num2)
print('----')

# MATCH
print('MATCH')
match num1:
    case 1: print('num1 vale 1')
    case 2: print('num1 vale 2')
    case 3: print('num1 vale 3')
    case 4: print('num1 vale 4')
    case 5: print('num1 vale 5')
    case 6: print('num1 vale 6')
    case 7: print('num1 vale 7')
    case 8: print('num1 vale 8')
    case 9: print('num1 vale 9')
    case 10: print('num1 vale 10')
    case _: print('num1 no es un entero entre 1 y 10')
print('----')

# -------ITERATIVAS-----------
    
# FOR
print('FOR')
for i in range(num1):
    print(i+1)
print('----')

# WHILE
print('WHILE')
x=1
while x<=num2:
    print(x)
    x+=1
print('----')


# -------EXCEPCIONES----------- 
# TRY, EXCEPT, ELSE, FINALLY
print('TRY, EXCEPT, ELSE, FINALLY')

try:
    print(num1/0)
except ZeroDivisionError:
    print('No es posible realizar',num1,'/ 0','ya que la división por 0 no esta definida')
else:
    print('Esto se imprimiria si no se hubiese lanzado un error')
finally:
    print('Este texto se imprime haya o no ocurrido un error, y como se puede ver, a pesar de que ocurrio el mismo, la ejecución no se detuvo')



'''DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''

for i in range(10,56):
    if(i%2 == 0 and i%3 != 0 and i != 16):
        print(i)