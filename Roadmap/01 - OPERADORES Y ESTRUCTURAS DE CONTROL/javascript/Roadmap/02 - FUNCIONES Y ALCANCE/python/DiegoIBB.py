""" 
  EJERCICIO:
  - Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
  - Comprueba si puedes crear funciones dentro de funciones.
  - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
  - Pon a prueba el concepto de variable LOCAL y GLOBAL.
  - Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 
  DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 
 """

#FUNCION BASICA
print("---- Función básica ----")

def contador():
    frase = input("Ponga una frase: ")
    contador_a = 0
    for letra in frase:
        if (letra == "a"):
            contador_a += 1
    print(f"Las as en la frase son: {contador_a}")

contador()


lista_1 = [3, 5, 6, 2, 7, 8, 3, 4, 3, 7, 7]

#FUNCION DENTRO DE UNA FUNCION
print("---- Función dentro de una función ----")

def ordenador(lista):
   contador_3 = 0
   contador_7 = 0
   for i in lista:
      if i == 3:
          contador_3 += 1
      elif i == 7:
          contador_7 += 1

   def contadores(val_1, val_2):
      if val_1 > val_2:
        print(f"Los valores son muy bajos; {val_1} mayor que {val_2}")
      elif (val_1 < val_2):
        print(f"Los valores son altos; {val_1} menor que {val_2}")
      elif (val_1 == val_2):
         print("Hay igual cantidad de valores")
      diferencia = val_1 - val_2
      return diferencia
   resultado = contadores(contador_3, contador_7)
   print(f"La diferencia es {resultado}")

ordenador(lista_1)

#FUNCION YA CREADA EN EL PROGRAMA

print("---- Función ya creada en el programa ----")

lista_2 = [3, 5, 6, 3, 7, 8, 4, 7, 2, 12, 34, 6, 23]

largo_lista = len(lista_2)
print(f"Función para ver el largo de una lista: {largo_lista}")


#VARIABLE LOCAL Y GLOBAL
print("---- Variables Locales y Globales ----")

reservas = int(input("Número de reservas: ")) # Variable Global, podemos usarla en las 2 funciones que se muestra a continuación

def cantidad_asistentos(ocupacion):
    total_asientos = 500 # Variable Local, su acción queda relegada a esta función
    asientos_libres = total_asientos - ocupacion
    return asientos_libres

def estado(libres):
    if(cantidad_asistentos(libres) > 450):
      print("Alta Concurrencia")
    elif(cantidad_asistentos(libres) < 400):
      print("Concurrencia Media")
    elif(cantidad_asistentos(libres) < 300):
       print("Baja Concurrencia")

    print(f"Nivel de ocupación: {reservas}")
    print(f"Asientos libres: {cantidad_asistentos(reservas)}")
    
venta_entradas = cantidad_asistentos(reservas)
estado(venta_entradas)

#DIFICULTAD EXTRA
""" 
  DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 """
 
print("---- Dificultad Extra ----")

def desafio_extra(cadena_1, cadena_2):
    lista_1_100 = range(0,101) #Evaluar cada elemento que entra a la lista según las condiciones dadas
    for i in range(1, len(lista_1_100), 1):
        #print(i)
        if (i % 3 == 0 and i % 5 == 0):
            print(f"{cadena_1}  {cadena_2}, Valor número: {i}")
        elif(i % 5 == 0):
            print(f"{cadena_1}, valor del númro: {i}")
            continue
        elif(i % 3 == 0):
            print(f"{cadena_2}, valor del número: {i}")
            continue
        else:
            print(i)

desafio_extra("Num_5", "Num_3")
