
#! operaciones con cadenas 


def operaciones_con_cadenas():
  print("--- concatenar cadenas de caractes ------")
  texto1= "hola"
  texto2=" como esta?"
  print(f"concatenados: {texto1+texto2}")
  print("---- reemplazar cadenas con otra --------------")
  """
  * el metodo es replace(), su sintaxis es: replace(old, new, coutn )
  * old: es la cadena sub cadena que se va a reemplazar
  * new: es la subcadena con la que se va a reemplazar
  * coutn: (opcional), el el número de ocurrencias de la subcadena old  se desee reemplazar
  """
  mensaje= "hola mundo, me gusta programar en javascript, porque javascript es un buen lenguaje"
  mensaje_python= mensaje.replace("javascript","python",1)
  #* solo reemplazara el primer javascript
  print(mensaje_python)
  #* reemplazara todas las ocurrencias
  mensaje_python= mensaje.replace("javascript","python")
  print(mensaje_python)
  #? ordenar cadednas de caracteres
  print("--------- ordenar las cadenas -------------")
  raw = "hola"
  ordenada = "".join(sorted(raw)) # sorted, es como sort en c++, javascript
  print(ordenada)

  print("----- minucula lower()--------------")
  texto3= "MAMA MIA"
  print(f"original: {texto3} , en minuscula: {texto3.lower()}")

  print("------- texto en mayuscula upper()-------------")
  texto4="awesome!"
  print(f"original: {texto4} , en mayuscula: {texto4.upper()}")

  print("----------- eliminar espacios en blanco usando .join y split()")
  texto5= "h o l a"
  print(f"texto original: {texto5}, sin espacios: {"".join(texto5.split())}")

  print("---- voltear un string ------------------")
  #* notacion de rebanado (string) con un paso negativo
  cadena = "Hola"
  cadena_volteada = cadena[::-1]
  print(cadena_volteada)
  #* utilizando la funcion reversed(), devuelve un iterador inverso de la cadena, 
  #* luego uniendolo con join()
  cadena_volteada = "".join(reversed(cadena))
  print(cadena_volteada)


operaciones_con_cadenas()

#! ejercicio extra

def palindromo(palabra)->bool:
  reverso= palabra[::-1]
  return reverso == palabra

def isograma(palabra)->bool:
  
  for i in range(len(palabra)-1):
    for j in range(i+1,len(palabra)):
      if palabra[i] == palabra[j]:
        return False
  return True        

def anagrama(palabra1,palabra2)->bool:
  if len(palabra1) != len(palabra2):
    return False
  palabra1="".join(sorted(palabra1))
  palabra2="".join(sorted(palabra2))
  if palabra1 == palabra2:
    return True
  
  
def ejercicio_exta():
  palabra1= input("ingrese el la primera palabra: ")
  palabra2= input("ingrese la segunda palabra: ")
  compacto1= "".join(palabra1.split())
  compacto2="".join(palabra2.split())
  respuesta1=palindromo(compacto1)
  respuesta2=palindromo(compacto2)

  if respuesta1:
    print(f"la palabra {palabra1} es un palindromo")
  else:
    respuesta1= isograma(compacto1)
    if respuesta1:
      print(f"la palabra {palabra1} es un isograma")

  if respuesta2:
    print(f"la palabra {palabra2} es un palindromo")
  else:
    respuesta2= isograma(compacto2)
    if respuesta2:
      print(f"la palabra: {palabra2} es un isograma")
  respuesta3=anagrama(compacto1,compacto2)
  if respuesta3:
    print(f"la palabra: {palabra1} y la plabra: {palabra2}, conforman un anagrama")    
    

ejercicio_exta()

