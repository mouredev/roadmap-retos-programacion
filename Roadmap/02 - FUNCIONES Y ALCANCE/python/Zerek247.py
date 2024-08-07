# --------------------- FUNCIONES Y ALCANCE -----------------------------

#Funcion sin parametros ni retorno
'''Esta función no toma ningún parámetro y no devuelve ningún valor.
Simplemente ejecuta una acción (en este caso, imprime un mensaje).'''
def saludo():
    print("Hola, mundo!")
#Llama a la función
saludo()

#Función con parametro
'''Esta función toma un parámetro y no devuelve ningún valor. 
Ejecuta una acción utilizando el parámetro proporcionado.'''

def nombre(arg):
    print(f"\nHola, {arg}")
#Llamar a la función con un argumento
nombre("Zerek")

#Función con varios parametros
'''Esta función toma varios parámetros y no devuelve ningún valor. 
Ejecuta una acción utilizando los parámetros proporcionados.'''
def sumar(a, b):
    print(f'\nLa suma de {a} y {b} es: {a + b}')
#Llamar a la función con dos argumentos
sumar(4,6)

#Función con retorno
'''Esta función toma un parámetro y devuelve un valor. 
Realiza una operación y utiliza el return para devolver el resultado.'''
def suma():
    return 5 + 2

resultado = suma()
print(f"\n{resultado}")

#Función con varios parametros y retorno
'''Esta función toma varios parámetros y devuelve un valor. 
Realiza una operación utilizando los parámetros y devuelve el resultad.'''
def operaciones(a, b):
    resultados = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": a / b
    }
    
    for operacion, resultado in resultados.items():
        print(f"La {operacion} de {a} y {b} es: {resultado}")
    
    return resultados

resultados = operaciones(10, 2)


#Función con parametros por defecto
'''Esta función toma parámetros opcionales con valores por defecto. 
Si no se proporcionan argumentos, se utilizan los valores por defecto.'''

def saludar(nombre="Mundo"):
    return f"\nHola {nombre}"

print(saludar()) #Llamar a la funcion sin argumento
print(saludar("Zerek")) #Llamar a la funcion con argumento

#Función con un numero variable de parametro
'''Esta función puede aceptar un número variable de argumentos utilizando *args.'''
def sumar_todo(*numeros):
    total = sum(numeros)
    return total

print(f'sumar_todo(1,2,3)\n')


#Función con un número variable de parametros con nombre
'''Esta función puede aceptar un número variable de argumentos con nombre utilizando **kwargs.'''
def mostrar_info(**info):
    for clave, valor in info.items():
        	print(f"{clave}: {valor}")

# Llamar a la función con diferentes argumentos con nombre
mostrar_info(nombre="Zerek", edad=27, ciudad="México")


# ------------------ FORMAS DE CREAR UNA FUNCIÓN DENTRO DE OTRA FUNCÓN ------------------

#Llamar a una función desde otra función
def funcion_a():
    print("Esta es la función A")
    
def funcion_b():
    print("\nEsta es la función B")
    funcion_a()
    
funcion_b()

#Retornar una función desde otra función (Funciones anidadas)
def exterior():
    def interior():
        print("\nEsta es la función interior")
    return interior

func = exterior()
func()

#Pasar una función como argumento a otra función
def funcion_a():
    print("Esta es la función A")

def funcion_b(func):
    print("\nEsta es la función B")
    func()
    
funcion_b(funcion_a)


#Usando decoradores
def decorador(func):
    def envoltura():
        print("Antes de la función")
        func()
        print("Después de la función")
    return envoltura

@decorador
def funcion_a():
    print("Esta es la función A")

funcion_a()


#--------------------- FUNCIONES CREADAS POR EL LENGUAJE -----------------------
print("\n")
#Funciones de conversión de tipos

# abs() -> Devuelve un numero absoluto (Siempre positivo)
print(abs(-5))
# all() -> Devuelve True si todos los elementos de un iterable son verdaaderos o esta vacío, si uno es False devuelve False
print(all([True, True, False]))
# any() -> Devuelve True si al menos uno de los elementos de un iterable es verdadero, si todos son False o está vacío devuelve False
print(any([False, False, True]))
# ascii() -> Especial para caracteres especiales 
print(ascii('ä'))
# bin() -> Convierte un numero entero en su representación binaria
print(bin(10))
# bool() -> Convierte a True o False (Cualquier valor no vacío o que no sea None, False, 0, 0.0 devuelve True)
print(bool([1,2]))
# bytearray() -> crea una secuencia mutable de bytes, es decir, se puede modificar
barr = bytearray("Hola", "utf-8")
barr[0] = 87
print(barr)
# bytes() -> Crea un objeto de tipo bytes, que es una secuencia inmutable, no se puede modificar
barr = bytearray([72, 111, 108, 97])
b = bytes(barr)
print(b)
# chr -> Toma un núnero entero y devuelve como cadena de un solo caracter ascii
print(chr(97))
# complex() -> Crear numero complejo (Un argumento = 1 numero complejo) (2 argumentos parte real o imaginaria de un complejo)
c = complex(2, 3)
print(c)
# dict() -> Crear un nuevo diccionario o convertir otros objetos en diccionarios
d = dict(a=1,b=2)
print(d)
# dir() -> Listar los nombres de los atributos y metodos de un objeto
print(dir([]))
# divmod() -> Toma dos numeros y devuelve una tupla que contiene el resto de la division entera de esos dos numeros
print(divmod(47,24))
# enumerate() -> Agregar un contador a un iterable y devolverlo como un objeto enumerado
for i, value in enumerate(['a', 'b','c']):
    print(i, value)
# filter() -> Filtrar elementos de una secuencia iterable que determina si cada elemento debe mantenerse o no en el resultado
print(list(filter(lambda x: x > 0, [3, 0, 1, 2]))) 
# float() -> Converrtir un número o una cadena que representa un número en un número decimal
cadena = "3.14"
num_float = float(cadena)
print(num_float + 5)
# format() -> Formatea valores en una cadena de de manera más flexible y legible
nombre = "Alice"
edad = 30
saludo = "Hola, {}. Tienes {} años.".format(nombre, edad)
print(saludo)
# frozenset() -> Creo conjunto cuyo elemento no puede ser modificado despues de su creacion
lista = [1, 2, 3, 4]
fset = frozenset(lista)
print(fset)
# getattr() -> Obtener el valor de un atributo de un objeto
class MyClass:
    a = 1
obj = MyClass()
print(getattr(obj, 'a'))
# globals() -> devuelve un diccionario que representa la tabla de simbolos global actual
print(globals())
# hasattr() -> Comprobar si un objeto tiene un atributo con un nombre especifico
class MyClass:
    a = 1
obj = MyClass()
print(hasattr(obj, 'a'))
# hash() - > Obtener el valor hash de un objeto, que es un numero entero que reprensenta de manera única el contenido del opbjeto
print(hash("hello"))
# hex() -> Muestra el valor de un número en hexadecimal
print(hex(10))
# id() -> Devuelve un identificador unico para un objeto especifico durante su ciclo de vida 
# Muestra la dirección en memoria del objeto 1
print(id(1))  
# input() -> Toma la entrada de un usuario desde la consola
# name = input("Enter your name: ")
# print(name)
# int() -> Convierte un valor a entero
print(int("10") + 10)
# isinstance() -> Determinar si un objeto es de un tipo específico antes de realizar ciertas operaciones
print(isinstance(1, int)) 
# issubclase() -> Comprueba si una clase es una sublcase de otra clase
class A:
    pass
class B(A):
    pass
print(issubclass(B, A))
# iter() -> Obtener un iterador de un objeto iterable
it = iter([1,2,3])
print(next(it))
print(next(it))
# len() -> Obtener la longitud de un objeto
print(len([1, 2, 3]))  # 3
# list() -> Crea una lista
l = list([1,2,3])
print(l)
# locals() -> Devuelve un diccionario que representa la tabla de simbolos local actual
def func():
    a = 1
    print(locals())
func()
# map() -> Aplicar una funcion a cada elemento de un iterable y devolver un map object(iterador) con los resultados
def doblar(n):
    return n * 2
numeros = [1, 2, 3, 4, 5]
resultado = map(doblar, numeros)
print(list(resultado))
# max() -> Encontrar el valor maximo en un iterable o entre dos o argumentos
print(max(1,2,3))
# memoryview() -> Devuelve un objeto de vista de memoria que permite acceder a los datos subyacentes 
datos = b"Hola, mundo"
vista = memoryview(datos)
print(vista)  # Salida: <memory at 0x7f83b40c7f40>
# min() -> Encontrar el valor minimo de un iterable o entre dos o mas argumentos
print(min(1,2,3))
# next() -> Obtener el siguiente elemento de un iterador
lista = [1, 2, 3, 4]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))  
print(next(iterador)) 
print(next(iterador))  
# object() -> Crear una nueva instancia base de un objeto
obj = object()
print(obj)
# oct -> Convertir un número entero en su representacion octal como una cadena
print(oct(8))
# open() -> Abrir un archivo y devolver un objeto de archivo
# archivo = open('archivo.txt', 'r')
# contenido = archivo.read()
# print(contenido)
# archivo.close()

# ord() -> Obtener el valor unicode de un caracter
print(ord('a'))
# pow () -> Calcular la potencia de un numero
print(pow(2,5))
# print() -> Enviar datos a la salida estandar
print("Hello, World!")
# property() -> Crear y gestionar atributos de una clase de manera controlada
class MyClass:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

obj = MyClass()
obj.x = 5
print(obj.x)  # 5
# range() -> Generar una secuencia de numeros
for rango in range(1, 5):
    print(rango)
# repr() -> Obtener una representacion de cadena oficial de un objeto
print(repr("Helo, World!"))
# reversed() -> Devolver un iterador que accede a los elementos de una secuencia en orden inverso
lista = [1, 2, 3, 4, 5]
lista_invertida = list(reversed(lista))
print(lista_invertida)
# round() - > Redondear un número al número de digitos especificado
print(round(4.2353453445,3))
# set() -> Crear un conjunto, que es la coleccion desordenada de elementos unicos
s = set([1,2,2,4])
print(s)
# slice() -> Crear un objeto de segmento que se puede utilizar para extraer una parte especifica de una secuencia
lista = [3, 3, 6, 4, 6, 9, 3, 6, 6, 11]
segmento = slice(3, 8, 2)
print(lista[segmento])
# sorted() ->  Devolver una nueva lista con los elementos de un iterable ordenados
lista = [3,1,2,4,7]
print(sorted(lista))
# staticmethod() -> Definir un metodo estatico dentro de una clase
class MyClass:
    @staticmethod
    def static_method():
        print("Static method called")

MyClass.static_method()
# str() -> Convertir un objeto en una cadena de texto
print(str(123))
# sum() -> Sumar los elementos y devolver un resultado
suma = [1,2,3,4]
print(sum(suma))
# super() -> llamar a metodos de una superclase desde una subclase
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print("B")
b = B()  # A B
# tuple() -> Crear una tupla
t = tuple([1,2,3])
print(t)
# type() -> Determinar el tipo de dato de un objeto o para crear un nuevo tipo de objeto
print(type("Hola"))
# zip() -> Combinar varios iterables en un solo iterable
print(list(zip([1, 2], ['a', 'b'])))  # [(1, 'a'), (2, 'b')]



# ------------------------ VARIABLES LOCALES Y GLOBALES ----------------------------

# Definir una variable global
x = 10

def funcion_global():
    # Acceder a la variable global
    global x
    print("Dentro de la función global, antes de cambiar: x =", x)
    
    # Modificar la variable global
    x = 20
    print("Dentro de la función global, después de cambiar: x =", x)

def funcion_local():
    # Definir una variable local con el mismo nombre
    x = 30
    print("Dentro de la función local: x =", x)

# Mostrar el valor de la variable global antes de llamar a las funciones
print("\n\nAntes de llamar a las funciones: x =", x)

# Llamar a la función que modifica la variable global
funcion_global()

# Mostrar el valor de la variable global después de modificarla
print("Después de llamar a la función global: x =", x)

# Llamar a la función que define una variable local
funcion_local()

# Mostrar el valor de la variable global después de la función local
print("Después de llamar a la función local: x =", x)



# ------------------ EJERCICIO EXTRA ---------------------------------

'''Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
La función retorna el número de veces que se ha impreso el número en lugar de los textos. '''



def extra(cad1, cad2):
    contador = 0
    for i in range(1,101):
        if i % 3 == 0:
            print(cad1)
        
        elif i % 5 == 0: 
            print(cad2)
        
        elif i % 3 and i % 5 == 0:
            print(cad1 + cad2)
        else:
            print(i)
            contador += 1
    
    return contador

# Ejemplo de uso
cadena1 = "Hola"
cadena2 = "Zerek"
resultado = extra(cadena1, cadena2)
print(f"El número se imprimió {resultado} veces en lugar de los textos.")



            









    
    