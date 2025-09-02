"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

#funciones básicas
print("\n\tfunciones básicas")
print('================================')
print("\n\tSon funciones definias por el usuario para realizar tareas \n\tsimple que se necesiten y se pueden repetir n cantidad de veces en el codigo")
print("\n\tEstas pueden tener un retorno o no, y recibir uno o varios parametros con el \n\tual trabajar")

#Simple sin Parametro y sin retorno
def func_simple():
    print ("Hola!!, MUNDO\n")
    

print("""\nEn el ejemplo se define una funcion simple sin parametros y sin retorno\ny solo muestra por consola un 
print: \n\ndef func_simple():\n    print('Hola!!, MUNDO')\n\nEsto al llamar la funcion nuevamente con: \n\nfunc_simple() ##esto devuelve por consola:\n""")
func_simple()


print("\n\tSon funciones definias por el usuario para realizar tareas \n\tsimple que se necesiten y se pueden repetir n cantidad de veces en el codigo")
print("\n\tEstas pueden tener un retorno o no, y recibir uno o varios parametros con el \n\tual trabajar")
#Simple sin Parametro y con retorno
def func_simple_return():
   return "Hola!!, MUNDO\n"
    

print("""\nEn este ejemplo se define una funcion simple sin parametros y con retorno\nesta que con solo invocarla no mostrara nada por consola\nSolo si se asocia con una variable o se inserta directamente en el print \nse puede ver el resultado:\n\ndef func_simple_return():\n    return 'Hola!!, MUNDO'\n\nEsto al llamar la funcion nuevamente con: \n\nfunc_simple_return() No mostrara nada en consola\n""")
func_simple_return() #no devolvio nada por consola
print("\nSi se iguala a una variable se puede usar la variable apra imprimirla por ejemplo:\n\nretorno_simple = func_simple_return()\n\nEsto al imprimirlo por consola con \nprint(retorno_simple) ##Esto si mostrara por consola:\n")
retorno_simple = func_simple_return()
print(retorno_simple)
print("\nTambien se puede llamar directamente en el print:\n\nprint(func_simple_return()) ##esto mostrara por consola:\n")
print(func_simple_return())

print("\n\n\tSon funciones definias por el usuario para realizar tareas \n\tsimple que se necesiten y se pueden repetir n cantidad de veces en el codigo")
print("\n\tEstas pueden tener un retorno o no, y recibir uno o varios parametros con el \n\tual trabajar")
#Simple con Parametro y con retorno y sin retorno
def func_simple_return_args(nombre):
   print(f"Hola {nombre}") 
   return "Bienvenido\n"
    

print("""\nEn este ejemplo se define una funcion simple con parametros y con y sin retorno\n Se puede asociar con una variable e inserta directamente en el print \npara ver  el resultado deseado:\n\ndef func_simple_return_args():\n    print(f'Hola {nombre}')\n    return 'Bienvenido'\n\nal llamar la funcion con el prin se recibe Beinvenido y al asociarla se obtiene el mensaje con el parametro dado\n\n""")

print("\nSi se iguala a una variable se puede usar la variable apra imprimirla por ejemplo:\n\nretorno_simple = func_simple_return()\n\nEsto al imprimirlo por consola con \nprint(retorno_simple) ##Esto si mostrara por consola:\n")

print("\nDefiniendo la variable Saludo = func_simple_return_args('Dimas B')  Y luego print(saludo) \nesto mostrara primeo el print de la funcion \ny luego con el segundo print de la variabel el saludo:\n")

saludo = func_simple_return_args('Dimas B') #aqui ya se muestra el print de la funcion

print(saludo) #Esto devulve el mensaje con el Saludo

print("\nNOTA: Sepueden recibir multiples variables y tener multiples retornos\nCon este ejemplo se muestra:\n\n")
print("""def multiples_arg_ret(nombre, edad, saludo):
    name = f"Tu Nombre es: {nombre}"
    age = f"Tienes {edad} años"
    greeting = f"{saludo}, bienvenido a este ejercicio"
    return name, age, greeting\n
valor1, valor2, valor3 = multiples_arg_ret('Dimas B', '43', 'Buenos Dias')\n
print(valor3)
print(valor1)
print(valor2)  

para retornar:    
      """)

def multiples_arg_ret(nombre, edad, saludo):
    name = f"Tu Nombre es: {nombre}"
    age = f"Tienes {edad} años"
    greeting = f"{saludo}, bienvenido a este ejercicio"
    return name, age, greeting

valor1, valor2, valor3 = multiples_arg_ret('Dimas B', '43', 'Buenos Dias')


print(valor3)
print(valor1)
print(valor2)
print("\nComo se observa en el Ejercicio anterio se ingresaron a la funcion varios agrumento los cuales \nse pasaron a nuevas variales para ser retonadas tas para luego ser usada\n")


