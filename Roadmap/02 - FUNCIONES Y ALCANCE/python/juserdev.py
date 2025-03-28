'''
 * EJERCICIO:
 * -> Crea ejemplos de funciones básicas que representen las diferentes
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
'''

def funcion_sin_paremetros ():
  print("Hola Python --> esta es la la funcion funcion_sin_parametro")

funcion_sin_paremetros()

def funcion_con_un_parametro(num):
  print(f"El parametro es el numner {num} y sin retono --> esta es la funcion def funcion_con_un_parametro")

funcion_con_un_parametro(10)

def funcion_con_dos_parametro(num1, num2):
  print(f"Esta es la suma de dos parametros: {num1 + num2} sin retorno --> esta es la funcion funcion_con_dos_parametro")

funcion_con_dos_parametro(10,5)

def funcion_parametros_retorno(lenguaje):
  return f"El lenguaje que estas estudiando es: {lenguaje} --> Funcion con parametro y retorno"

print(funcion_parametros_retorno("Python"))

# Funcion infinita

def funcion_infinita(*param):
  return param

print(funcion_infinita("hola", "juan")) # esto es una tupla
print(type(funcion_infinita("hola", "juan")))

saludar, juan = funcion_infinita("hola", "juan") # aqui le agregue variabels a cada parametro

print(f"{saludar} {juan}")

def funcion_infinita_2(*params):
  for param in params:
    print(f"{param}")

funcion_infinita_2("hola", "python", "soy Juan")

def funcion_key_value(**names):
  for key, value in names.items():
    print(f"{value}, {key}")

funcion_key_value(leugaje="python", edad=35, nombre="Juan", alias="juserdev")

# Funciones globales y locales

var_global = "variable global"

def funcion_var_local():
  var_local = "variable local" # No se puede acceder a esta variable fuera de esta funcion
  print(f"{var_global}, {var_local}")

print(var_global)
funcion_var_local(

)

# FUNCIONES ENTRE FUNCIONES

def area(lado1, lado2):
  area = lado1 * lado2
  return area

def volumen(lado1, lado2, altura):
  base = area(lado1, lado2)
  return f"Este es el voluemn de {lado1} * {lado2} + {altura} = {base * altura} --> Funcion anidada"

print(volumen(10, 20, 10))

# Funciones creadas en el lenguage


texto = "este es un str de pruba para este ejemplo"
number = "1"

print(f"Esta es el resultado de la funcion len() --> {len(texto)}") # cuenta la cantidad de caracteres
print(f"Esta es el resultado de la funcion ucapitalize() --> {texto.capitalize()}") # pone la primera letra en Mayuscula
print(f"Esta es el resultado de la funcion upper() --> {texto.upper()}") # pone todo el texto en mayuscula
print(f"Esta es el resultado de la funcion count() --> {texto.count("e")} ") # Cuenta la cantidad de letras que tiene dentro del parentesis
print(f"Esta es el resultado de la funcion isnumeric() --> {texto.isnumeric()} ") # verifica si es int o str
print(f"Esta es el resultado de la funcion isnumeric() --> {texto.isnumeric()} ") # verifica si es int o str
print(f"Esta es el resultado de la funcion isnumeric() --> {number.isnumeric()} ") # verifica si es int o str


# DIFICULADAD EXTRA

def dificultad_extra(name, surname):
  i = 0
  while i < 100:
    if i % 3 == 0 and i % 5 == 0:
      print(name)
    elif i % 3 == 0 :
      print(surname)
    elif i % 5 == 0:
      print(f"{name} {surname}")
    else:
      print(i)
    i += 1

# dificultad_extra("juan", "rodriguez")

