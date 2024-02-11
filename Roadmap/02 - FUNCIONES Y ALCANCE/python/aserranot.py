#Python dispone de 69 funciones básicas o integradas, algunas de las más utilizadas son:
#print(), con la función print podremos imprimir un texto o valor por pantalla/consola.
print("Hello world")
#len(), la función len nos devuelve la longitud de un objeto, como una cadena o una lista.
cadena = ("coche")
print(len(cadena))
my_list_len = [1, 2, 3, 4, 5]
print(len(my_list_len))
#max(), devuleve el elemento más grande de un iterable
my_list_max = [1, 2, 3, 4, 5]
print(max(my_list_max))
#max(), devuleve el elemento más pequeño de un iterable
my_list_min = [1, 2, 3, 4, 5]
print(min(my_list_min))
#sum(), devuleve la suma de todos los elementos de un iterable
my_list_sum = [1, 2, 3, 4, 5]
print(sum(my_list_sum))
#Las funciones dentro de funciones en python se llaman funciones anidadas
def funcion_padre():
    def funcion_hija():
        return "¡Soy la función hija!"
    return funcion_hija()

print(funcion_padre())
#El python una variable local es una variable que solamente se puede utilizar dentro del código de la función que se declara. En cambio una variable global se puede utilizar dentro de todo el probrama y por todas las funionces.
def calculaIVA(val1, valIva):
    iParcial = val1 * valIva / 100
    print("Valor del IVA", iParcial)

iTotal = 2000  # Variable global
iParcial = 0  # Variable global
print("Precio sin IVA es", iTotal)
calculaIVA(iTotal, 16)
print("Precio con IVA es", iTotal + iParcial)
#Ejercicio opcional
def mi_funcion (valor1, valor2):
  for cadena in range (100):
    if ((cadena % 3 == 0) and (cadena % 5 == 0)):
      print (f"{valor1}{valor2}")
    elif (cadena % 3 == 0):
      print(f"{valor1}")
    elif (cadena % 5 == 0):
      print(f"{valor2}")
    else:
       print(f"{cadena}")

mi_funcion("Hola","mundo")
