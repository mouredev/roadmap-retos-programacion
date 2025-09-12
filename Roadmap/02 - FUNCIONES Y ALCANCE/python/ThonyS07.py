'''
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
'''


#Funcion simple
def simple():
    print("Soy una funcion simple")

simple()

#Función con parámetro de entrada
def func_para_entrada(nombre):
    print(f"hola, {nombre}")

func_para_entrada("Thony")

#Función con parámetro de salida y entrada
def func_para_entrada_salida(nombre):
    return f"hola, {nombre}"

print(func_para_entrada_salida("Thony"))

#Función con retorno y varios argumentos de entrada
def func_multiple_entrada_salida(nombre, apellido):
    return f"hola, {nombre} {apellido}"

print(func_multiple_entrada_salida("Thony", "Silva"))

# Función con argumento predeterminado
def func_predeterminado(nombre="Thony", apellido="Silva"):
    return f"hola, {nombre} {apellido}"

print(func_predeterminado())
print(func_predeterminado("Juan","Perez"))
print(func_predeterminado(apellido="Lopez"))

#Función con argumento de longitud variable
print("Si declaramos un argumento con * (*argumentos), esto hará que el argumento que se pase sea empaquetado en una tupla de manera automática. ")
def func_variada(*argumentos):
    for argumento in argumentos:
        print(argumento)

func_variada("hola")
func_variada("hola", "mundo")
func_variada("hola", "mundo", "a", "todos")

print("Usando doble ** es posible también tener como parámetro de entrada una lista de elementos almacenados en forma de clave y valor. En este caso podemos iterar los valores haciendo uso de items().")

def func_variada2(**argumentos):
    for clave, valor in argumentos.items():
        print(f"{clave} = {valor}")

func_variada2(a = "hola")
func_variada2(a = "hola", b = "mundo")
func_variada2(a = "hola", b = "mundo", c = "a", d = "todos")

#Funciones built-in
print(len("hola mundo"))
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))
print(pow(2,3))

#variables globales y locales
a = "global"
print(a)
def hola ():
    b = "local"
    print(a) #se puede acceder a la variable global desde cualquier espacio del codigo, sin embargo no se puede acceder a la variable local fuera del contexto local donde se define
    print(b)
hola()


"""extra"""

def multiplo(multiplo_tres, multiplo_cinco) ->int:
    inicio=0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(multiplo_tres + multiplo_cinco)
           
        elif numero % 3 == 0:
            print(multiplo_tres)
          
        elif numero % 5 == 0:
            print(multiplo_cinco)
         
        else:
            print(numero)
            inicio+=1
    return inicio
print(multiplo("Flex","Box"))
