# funcion con retorno
def return_greet ():
    return "Hola python"

valor_return = return_greet()

print (return_greet())
print (valor_return)

# funcion con argumento de entrada

def di_hola (carro):
    print ("Saluda a mi", carro)

di_hola("Skoda")

# funcion con argumentos por posicion 

def suma (a,b):
    return (a+b)

print (suma(5 ,4))

# funcion con argumentos por nombre 

def resta (a = 2, b =3):
    return (a-b)

print (resta())

# funcion con argumentos por defecto

def multiplicacion (a,b,c=2):
    return (a*b*c)

print (multiplicacion(3,2,))

# funcion con argumentos de longitud variable (con tuplas)

def suma_tupla (*numeros):
    print (type(numeros))
    total = 0
    for i in numeros:
        total += i
    return total 
    
print(suma_tupla(1,3,4,5,6))

# funcion con argumentos de longitud variable (con key y value)

def suma_value(**numeros):
    print (type(numeros))
    total = 0
    for key, value in numeros.items():
        print (key,value)
        total += value
    return total

print (suma_value(a=5, b=20, c=23))  

dic = {"a" : 10, "b" : 20, "c" :23}

def suma_entry(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print (key, value)
        total += value
    return total

print (suma_entry(**dic))     

# funcion con return dobles

def suma_con_returns (a,b,c):
          suma = a+b+c
          resta = a-b-c
          return suma, resta

print(suma_con_returns(1, 2, 3))

# funcion con anotacion 

def suma_anotacion (numero : int):
     return numero*3

print (suma_anotacion("carro"))

    
# funcion lambda

suma_lambda = lambda a,b : a + b

print (suma_lambda (2,4))

print((lambda a, b: a - b)(2, 4))


# funcion factorial recursiva

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

print (factorial_recursivo(5)) # 120

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    
print (fibonacci(7))    


#funcion decorador (una funcion dentro de otra funcion)

def funciondecorador (funcion):
    def reloj(a,b):
         
         print (f" askjdajdklsa {a-b}")

         funcion(a,b)

    return reloj         

@funciondecorador
def suma(a,b):
    
    print (f" carro {a+b}")

suma(5,3)


# funcion generador (yield)

def yield_example(a):

    for i in range (a):
     print (i)

yield_example(5)     

# funcion map 

lista = [1,2,3,4,5]

def por_2(x):
    return x*2
listapor_2 = map(por_2, lista)

print(list(listapor_2))

#funcion filter 

lista = [1,2,3,4,5,7,8,9,10]

def pares(x):
   
     return  x % 2 == 0

filtropares = filter(pares, lista)

print(list(filtropares))

#funciones globales y locales

variable_global = "Esta variable puede ser accedida por cualquier funcion"

def funcion_local ():
    variable_local = 2*2+2
    print (variable_local)

funcion_local()

def funcion_x():

   """variable_local  no sirve pues esta definida dentro de una funcion"""


# ejercicio dificultad extra 

def ejercicio (a, b):

    contador = 0  

    for i in range (1,101):

       

        if i % 3 == 0 and i % 5 == 0:
            
            formato = (f"{a} y {b}")
            print(formato)

        elif i % 3 == 0:
             
             print(a)

        elif i % 5 == 0 :
            
             print (b)

        else:
             print (i) 
             contador += 1

    return contador 
                    

resultado = ejercicio("Multiplo de 3","Multiplo de 5")
print(f"se imprio un numero en vez de un texto un total de: {resultado} veces")

        

    
        
          