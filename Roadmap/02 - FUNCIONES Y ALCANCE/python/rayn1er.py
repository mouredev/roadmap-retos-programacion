# /*
#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */


# en python declaramos una funcion con la palabra reservada def, seguida de sus argumentos(en caso de que los reciba) y dos puntos (:)

def first_function(): #esta es una funcion sencilla que no recibe parametros
    print("I am a function!")

first_function() #para ejecutar una funcion tenemos que llamarla, esto lo hacemos simplemente escribiendo su nombre acompanado de parentesis, al ejecutar el codigo nos muestra en pantalla ("soy una funcion!")

def say_hi(name): #las funciones pueden recibir parametros, en este caso un nombre para devolver un saludo junto a dicho nombre
    print(f'Hi {name}')

say_hi("Raul") # llamamos y le entregamos el parametro que en este caso es mi nombre, muestra por pantalla el saludo

def sum_two_numbers(n1,n2): # en este caso esta funcion recibe dos parametros

    return n1+n2 #usamos la palabra reservada return para devolver la suma de los dos numeros recibidos

print(sum_two_numbers(2,2)) #como queremos mostrar por consola el resultado de la funcion, utilizamos print, puesto que la funcion en si devuelve un dato, no un print con el resultado

def future_function():
    pass #podemos tambien utilizar la palabra reservada pass para indicar que implementaremos codigo

def args_two_numbers(n1 = 2, n2= 2): #tambien podemos agregar valores por defectos a los argumentos en caso de requerirlo
    return  n1 + n2

print(args_two_numbers()) #si ejecutamos esto tendremos 4, puesto que ambos valores valen 2
print(args_two_numbers(7,7)) # en este caso nos devuelve 14, ya que le hemos asignado parametros
print(args_two_numbers(7)) #aca nos ejecuta nueve, ya que al faltarnos un parametro, la funcion ejecuta el que tiene por defecto

def infinite_args_numbers(*args): #podemos utilizar ** para indicarle a la funcion que espere multiples valores los cuales se alamacenan en una tupla, esto para realizar operaciones en las que no sabemos cuantos argumentos necesitamos, como por ejemplo sumar multiples numeros
    return sum(args)

print(infinite_args_numbers(10,10,10)) #devuelve la suma de todos los argumentos que le hemos pasado


def infinite_items(**kwargs): #para los kwargs tenemos lo mismo, con la diferencia de que estos se almacenan en un diccionario
    return kwargs

print(infinite_items(car = 'toyota', shoes = 'nike', sports = 'soccer')) #devuelve el diccionario junto con sus valores

def event_cronogram(event, *args, **kwargs): #tambien podemos combinar todos los elementos en una funcion, como por ejemplo el nombre de un evento junto con su agenda y sus jueces
    return event, args,kwargs 

print(event_cronogram('anime festa', 'dance tournament', 'sing tournament', 'draw tournament', dance_judge = 'yoel', sing_judge = 'mariana', draw_judge = 'runny'))

#funciones dentro de funciones

def main_function(): #en python podemos anidar funciones dentro de otras, en este caso esta sera nuestra funcion principal
    def sub_function(): #dentro encontramos nuestra funcion secundaria
        print("I am a sub function")

    sub_function() #llamamos a la funcion

main_function() #ejecutamos nuestra funcion nos ejecutara el codigo de la funcion anidada que hemos llamado dentro de la funcion principal

#funciones integradas de python

print("hola") #la funcion hola que venimos utilizando desde el principio es una funcion integrada de python
print(sum([10,20,20])) #sum tambien es otra funcion integrada de python y nos sirve para sumar elementos iterables
print(type("python")) #la funcion type tambien es una integrada de python, y nos devuelve el tipo del objeto que le hemos entregado

#variables locales

global_variable = "Global variable" #en python una variable global es aquella que se declara fuera de una funcion y podemos utilizarla en cualquier funcion

def print_variable():
    print(global_variable)

print_variable() #ejecutamos para imprimir la variable global

def print_local_variable():
    local_variable = 'Local variable' #dentro de las funciones nos encontramos las variables locales, las cuales solo existen dentro de la funcion y no puede utilizarle fuera
    print(local_variable)

print_local_variable() #en este caso nos imprime la variable local de la funcion, que es "local variable".

def extra_function(string1, string2):
    total_numbers = 0
    for i in range(1,101):

        if i % 3 == 0 and i % 5 == 0:
            print(string1+string2)
        elif i %  3 == 0:
            print(string1)
        elif i % 5 == 0:
            print(string2)
        
        
        else:
            print(i)
            total_numbers += 1
    
    return f"La cantidad de veces que se ha impreso un numero es de {total_numbers}"
   

print(extra_function('python','3'))