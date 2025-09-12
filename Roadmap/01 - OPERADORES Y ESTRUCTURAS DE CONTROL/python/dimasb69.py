print("\n\n\tTratare de ser muy especifico mas que concentrarme en resolver!!\n\n")


print(f"""\nOperadores Aritméticos\n
      uso del operador + (suma)
      1 + 3 = {1+3}
      
      uso del operador - (resta)
      10 - 3 = {10-3}
      
      uso del operador * (multiplicacion)
      3 * 5 = {3*5}
      
      uso del operador / (division)
      5 / 2 = {5/2}
      
      uso del operador % (modulo devuelve el resto de la división)
      5 % 2 = {5 % 2}
      
      uso del operador ** (Realiza la potencia de los operandos)
      2 ** 3 = {2**3}
      
      uso del operador // (convierte el resultado de la division a enetero)
      5 // 2 = {5//2}  (devuelve 2 en vez de 2.5)
      """ )

print(f"""Operadores Relacionales

      mayor que > para determinar si un numero es mayor que otro
      2 es mayor que 1: {2>1} (True = si // Flase = no)
      
      menor que < para determinar si un numero es menor que otro
      2 es menor que 1: {2<1} (True = si // Flase = no)
      
      igual que == para determinar dos valores son iguales
      100 es igual que 200: {100 == 200} (True = si // Flase = no)
    
      mayor ó igual que >= valida si el 1er numero es igual o mayor que el 2do
      100 es mayor ó igual que 200: {100 >= 200} (True = si // Flase = no)
      
      menor ó igual que <= valida si el 1er numero es igual o menor que el 2do
      100 es menor ó igual que 200: {100 <= 200} (True = si // Flase = no)
      
      diferente que != para determinar dos valores son diferentes
      100 es diferente que 200: {100 != 200} (True = si // Flase = no)
      
      """ )

print("Operadores Asignación\n")
## = asigna el valor descrito a la variable
a = 500
print(f"\ta = 500, valor de a: {a}")
print("\tse asigna el valor de 500 a la variable a\n")

## += suma el valor dado al valor actual de la variable
a += 1
print(f"\ta += 1, valor de a: {a}")
print("\tsuma el valor 1 al valor actual de a\n")

## -= resta el valor dado al valor actual de la variable
a -= 499
print(f"\ta -= 499, valor de a: {a}")
print("\tresta el valor 499 al valor actual de a\n")

## *= multiplica el valor de la variable por valor dado
a *= 10
print(f"\ta *= 10, valor de a: {a}")
print("\tmultiplica el 10 dado al valor actual de a\n")

## /= divide el valor de la variable por valor dado y devuelve un Float
a /= 2
print(f"\ta /= 2, valor de a: {a}")
print("\tdivide el valor dado al valor actual de a y devuelve un float\n")

## %= devuelve el resto de la divicion de la variable entre valor dado
a %= 6
print(f"\ta %= 6, valor de a: {a}")
print("\tdevuelve el resto de la division de a entre 6 mantiene el tipo float\n")

## **= exponencia la variable al valor dado
a **= 3
print(f"\ta **= 3, valor de a: {a}")
print("\texponencia a la 3 el valor de a (a*a*a) mantiene el tipo float\n")

## //= divide la variable y el resultado si lo tiene le elimina los decimales
a //= 5
print(f"\ta //= 5, valor de a: {a} ")
print("\tdivide a entre 5 y le quita el decimal el resultado debio ser 12.8 mantiene el tipo float\n")


print(f"""Operadores Logicos

      and (y) obliga a cumplir dos o mas condiciones si una de ellas
      no se cumple retorna false, si todas se cumple retorna True
      
      2 > 1:True and 5 < 3:False = {(2>1)and(5<3)} (retorna False por la segunda
      condicion no se cumple)
      2 > 5 < 10: {(2>1)and(5<10)} (retorna True por ambas condiciones
      se cumplen)
      
      or (ó) evalua dos o mas condiciones y si una se cumple retorna True
      si ninguna se cumple retorna False
      
      2 > 1:True or 5 < 3:False = {(2>1)or(5<3)} (retorna True por que la primera
      condicion es valida)
      2 > 3:False or 5 < 4:False = {(2>3)or(5<4)} (retorna False por ninguna
      condicion se cumplen)
      
            
      -*Logicos de Pertenencia
      
      in (en) Retornara True si lo buscado estan en lo comparado
             
      carro in (perro, 20, True, carro) = {'carro' in ({'perro', 20, True, 'carro'})} 
      (retorna True carro esta en la lista)
      12 in (perro, 20, True, carro) = {12 in ({'perro', 20, True, 'carro'})} 
      (retorna False 12 no esta en la lista)
      
      Funciona igual para string
      ola in Hola = {('ola') in ('Hola') }
      (ola si esta es parte de la palabra Hola)
      hola in Hola = {('hola') in ('Hola') }
      (hola no esta la comparacion la h es direfente a H)
      
      
      not in (no esta en) Retorna True si el valor comparado no existe
      
      Hola not in (perro, 20, True, carro) = {'Hola' not in ({'perro', 20, True, 'carro'})} 
      (retorna True Hola no esta en la lista)
      20 not in (perro, 20, True, carro) = {20 not in ({'perro', 20, True, 'carro'})} 
      (retorna False 20 si esta en la lista)
      
      Funciona igual para string
      Mundo not in 'Hola como estas!!' = {('Mundo') not in ('Hola como estas!!')}
      (Mundo no esta en 'Hola como estas!!')
      Hola not in 'Hola como estas!!' = {('Hola') not in ('Hola como estas!!') }
      (Hola si esta en 'Hola como estas!!')
      
      -*Logicos de Identidad
      
      is (es) Retorna True si la comparacion es Valida
      es decir valida que el resultado sea lo esperado
      
      2 is 3 = {2 is 3} (retorna Falso 2 no es 3)
      3 is 3 = {3 is 3} (retorna True 3 si es 3)
      
      Funciona igual para string y otros valores
      Hola is ola = {('Hola') is  ('ola')}
      False is False = {(False) is (False)}
      
      is not (no es) Evalua que el resultado no sea Verdadero
      si es verdadero retorna False
      
      2 is not 3 = {2 is not 3} (retorna True 2 no es 3)
      3 is 3 = {3 is not 3} (retorna Falso 3 si es 3)
      
      Funciona igual para string y otros valores
      Hola is not ola = {('Hola') is not  ('ola')}
      True is not True = {(True) is not (True)}
      
      """ )
print("Estructuras de control\n")
print("\tSecuenciales\n")
def secuenciales(): #se define la funcion
      #se ejecuta cada instruccion una por una en secuencia!
      a = "Hola "
      print("\tSe crea una varibale a ='Hola '")
      b = "Mundo"
      print("\tSe crea una varibale b ='Mundo'")
      c = a+b
      print("\tSe crea una varibale c y se le suma a+b")
      print('\tSe imprime el resultado de c')
      print(f"\tc = {c}\n")
      
secuenciales() #se ejecuta la funcion

print("\tCondicionales y Ciclos\n")
def condicionales(): #se define la funcion
      
      print("\tCONDICION: if\n\tejecuta solo la instruccion que cumpla la condicion")
      #se ejecutara solo la funcion que cumpla la condicion
      a = "Hola "
      print("\tSe crea una varibale a ='Hola '")
      b = "Mundo"
      print("\tSe crea una varibale b ='Mundo'")
      c = a+b
      print("\tSe crea una varibale c y se le suma a+b")
      print("\tse crea una funcion con una serie de condicionales If\n")
      def condIf():#es importante mantener la identacion para que la estructura se mantenga
            print("\tSe compara a y c si son iguales mostraria el primer print\n\tpero como no cumple se ejecuta el print del else\n")
            if(a == c):
                  #esta instruccion no se va a ejecutar
                  print (f"\t nda que hacer")
            else:
                  #como la condicion anterion no se cumple esta es la instruccion que se ejecutara
                  print(f"\ta='{a}' es diferente a c='{c}'por eso esto se imprime")
            
            print("\tLa funcion de este if fue: if(a==c)\n")
            
            print("\tEsta vez se comparan varias condiciones en secuencia con elif\n\tse imprime solo las condiciones que se cumpla\n\tel esle del final se ejecutaria solo si ninguna de las anterios se cumple\n")
            if(c == 'Hola Mundo'):
                  #esta instruccin es correcta se ejecutara
                  print(f"\tc='{c}' es igual a 'Hola Mundo' por eso esto se imprime")
            elif(c != a):
                  #esta tambien es correcta pero no se mostrara por que ya se cumplio la primera
                  print(f"\tc='{c}' es diferente a a='{a}', esta condicion tambien se cumple pero no se imprime")
            elif(a+b != 'Hola Mundo'):
                  #esta ultima condicion no se cumple este elif se omite igualmente por la primer ya se cumplio
                  print("\tEste print no se muestra pero por que ya se cumplio una\n\tno por que la funcion no es valida")
            else:
                  #esta instruccion se ejecutaria solo si alguna de las anteriores no cumple la condicion
                  print("\testa linea no se imprimira")
            print("""\tEn este if se compararon 3 condiciones y una alternativa
                  if(c == 'Hola Mundo') 
                  //esta es correcta y se ejecuto lo que contiene
                  elif(c != a) 
                  //esta es correcta pero la primera ya se cumplio se omite
                  elif(a+b != 'Hola Mundo') 
                  //esta no se cumple pero la primera se cumplio se omite 
                  else 
                  // el else se ejecuta si ninguna de las anteriores se cumplio
                  \n""")
      def cicloFor():
            print("\tCICLO: for\n\tEl ciclo for ejecuta las instrucciones por el lapso que se indique")
            print("\tSe crea una lista x={0,1,2,3,4,5,6,7,8,9,10}con los numeros del 0 al 10")
            print("\tSe creara una funcion con un ciclo for que imprima lo que esta en x\n")
            x={0,1,2,3,4,5,6,7,8,9,10}
            for n in x:
                  print(f"\tNumero: {n}")
            print("\tEsto se imprime cuando termina el ciclo for\n")
            
            print("\ttambien funciona con strings ejemplo y='Hola Mundo!'\n")
            y='Hola Mundo!'
            for n in y:
                  print(f"\tcaracter: {n}")
            print("\tEn etse ciclo se descompuso la oracion, el espacio y ! tambien cuenta\n")
            
      def cicloWhile():
            print("\tCICLO: while\n\tEl ciclo while ejecuta las instrucciones mientras una condicion se cumpla\n\tsi no se tiene cudado se puede crear un ciclo infinito\n")
            print("\tSe crea variable en 1 v=1")
            print("\tSe creara una funcion con un ciclo un while para que imprima los numeros sean pares\n\tentre el 1 y el 10 incrementando en cada vuelta el valor de v")
            v=1
            while v < 11:
                  if(v%2 == 0):     
                        print(f"\tNumero: {v}")
                  v = v+1      
            print("\tEsto se imprime cuando terminan el ciclo\n")
            
            
      
      condIf()
      cicloFor()
      cicloWhile()
      
condicionales() #se ejecuta la funcion

print("Excepciones")
print ("\tEl manejo de excepciones es la forma de evitar que debido a un erro conocido\n\tla aplicacion finalice inesperadamente\n")

print("\tuna forma de manejar ecepciones es con la funcion try except\n\testo permite capturar la excepcion y realizar un proceso sin finalizar la app")
print("\tCreemos una funcion que tomes dos variables y las divida entre si\n\tEn la primera opcion colocare b=0 para probar como muestra\n\tel mensajde del error ZeroDivisionError\n\tLuego colocare uno de los valores como texto y veremos el mensaje de TypeError\n")
def tryExcept(a, b):
      try:
            result= a/b
            print(f"\tResultado= {result}\n")
      except ZeroDivisionError:
            print("\tERROR: La división entre 0 no se puede realizar")
      except TypeError:
            print('\tERROR: revisa los valores uno de ellos no es correcto')
      except Exception:
            print('\tERROR: Algo Salio Mal')
            
            
tryExcept(10, 0)
print("\tSe observa el mensaje dentro de execpt ZeroDivisionError\n")

tryExcept(20, 'Hola')
print("\tSe observa el mensaje  dentro de execpt TypeError\n")

print("\tExisten muchos tipos de errores que se pueden manejar para eviar el colapso\n\tAlgunos son: AttributeError | IndexError | NotImplementedError | ValueError ")


print("\n\t*****EXTRA*****\n")

def numCiclo(n):
      print("\tFuncion que imprime los numeros entre 10 y el 55 incluidos")
      print("\t__________________________")
      while n <= 55:
            print(f"\tNumero: {n}")
            n = n+1     
                 
def numPar(n):
      print("\n\tFuncion que imprime los numeros pares entre 10 y el 55 incluidos")
      print("\t__________________________")
      while n <= 55:
            if(n%2 == 0):     
                  print(f"\tNumero: {n}")
            n = n+1 
            
def numMult(n):
      print("\n\tFuncion que imprime los numeros multiplos de 3 sin incluir el 16\n\tentre los numeros 10 y 55 incluidos")
      print("\t__________________________")
      while n <= 55:
            if(n%3== 0 and n is not 16):     
                  print(f"\tNumero: {n}")
            n = n+1           
                  
numCiclo(10)
numPar(10)
numMult(10)

print("\n\n\tSALUODS A TODOS -  me estoy uniendo tarde pero siempre es bueno practicar!!")


