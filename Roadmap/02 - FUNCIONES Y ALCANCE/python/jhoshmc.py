#funcion sin parametros ni rotorno

def saludar():
  print("hola a todos los usuarios de puthon")

# funciones con parametros y retorno
def suma(numero_1,numero_2):
  return numero_1+numero_2

# fuciones anidadas

def anidada():
  def hijo():
    print("hola, soy el hijo")
  hijo()

#funciones de python 
def listas_nativas():
  my_lista=["hola",3,True,"banaja"]
  print(my_lista)
  tamaño= len(my_lista) # len(): funcion para ver el rango, cuanta, ya sea una lista, string(lista de caracteres),etc
  print(tamaño)
  for element in my_lista:
    print(type(element)) # type(): permite ver el tipo que es el elemento
  #forma de crear una lista usando la funcion lis()
  lista_frutas= list(("manzana","pera","naranja"))
  print(lista_frutas)
  #print es una funcion que manda a imprimit en consola

#variables globales y locales
variable_global= "soy global" # esta disponible en cualquier parte del código,
                              # no tiene scope
def variables():
  variable_local= "soy local" # solo está disponible en su scope,
                              #en este caso solo en la funcion varables, fuera no existe
  print(variable_global)
  print(variable_local)

# print(variable_local) aca daria error, ya que esta variable no existe fuera de la funcion donde fue creada
print(variable_global) # todo lo contrario con la variable global
# funcion para retornar mas de un valor
def multiple_return():
  return "hola","mundo"

uno,dos = multiple_return()
print(uno)
print(dos)

#funcion con numero variable de argumentos

def  suma_2(*numeros):
  resultado=0
  for n in numeros:
    resultado += n
  return resultado

# funcion con numero varible de argumentos y palabras clave
# si , esta parte vi el video en youtuve :v
def variable_key_arg_greet(**names):
  for key,value in names.items():
    print(f"hola {value} ({key})!")

#ejercicio extra
def extra(fizz,buzz)-> int: # -> int : indica que voy a retornar un valor numerico entero
  contador=0
  for i in range(1,101):
    if(i % 15== 0):
      print(f"{i} {fizz}{buzz}")
    elif(i%5 == 0):
      print(f"{i} {buzz}")
    elif(i% 3 == 0):
      print(f"{i} {fizz}")
    else:
      contador+=1
  return contador
# funciones 
saludar()
print(suma(5,3))

anidada()
listas_nativas()
variables()
print(suma_2(1,2,3,4,5))
contador= extra(fizz="fizz",buzz="buzz") # se pone biz="biz", para que no importe el orden que ponga el argumento
print(contador)
variable_key_arg_greet(
  lenguaje="python",
  name="brais",
  alias="MoureDev",
  age=36
)

print("hola".upper())
print("hola".lower())