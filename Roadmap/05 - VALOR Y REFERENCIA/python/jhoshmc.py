def ejercicio():
  val="hola"
  print(f"texto original: {val} \n")
  f_valor(val)
  print(f"texto original: {val}")
  print(f"\n pasando variables por referencia ")
  f_referencia()

def f_valor(text):
  """
  * cuando se pasa variable inmutables como enteros, tuplas, cadenas, cualquier cambio que se aga dentro
  * de esa funcion, no afectará a la variable original fuera de es scope
  """
  print(f"texto en la funcion: {text}")
  text = "chiao"
  print(f"texto modificado: {text}")

def f_referencia():
  """
  *cuando se pasa variables mutables, como listas, diccionarios, objetos o conjuntos, se pasa la 
  * referencia a ese objeto, por lo que cualquier modificacion se llevara acabo tambien a la variable
  * original que esta fuera de este scope 
  """
  lista=[1,2,3,4]
  eliminar_elemento_lista(lista)
  print(f"lista original: {lista}")

def eliminar_elemento_lista(lista):
  print(f"elementos de la lista: {lista}")
  lista.pop()

ejercicio()

def extra():
  print("\n ejercico extra: \n")
  p_1= 1
  p_2=2
  [c_1,c_2]= e_valor(p_1,p_2)
  print(f"el valor de p_1 es: {p_1}")
  print(f"el valor de p_2 es: {p_2}")
  print("\n pasndo por valor: ")
  print(f"el valor de c_1 es: {c_1}")
  print(f"el valor de c_2 es: {c_2}")
  print("\n pasando por referencia: ")
  r_1=[1]
  r_2=[2]
  print(f"el valor de r_1 es: {r_1[0]}")
  print(f"el valor de r_2 es: {r_2[0]}")
  [cr_1,cr_2]=e_referencia(r_1,r_2)
  print(f"el valor de cr_1 es: {cr_1[0]}")
  print(f"el valor de cr_2 es: {cr_2[0]}")
  print("\nnuevos valores\n")
  print(f"valor de r_1 es: {r_1[0]}")
  print(f"valor de r_2 es: {r_2[0]}")

def e_valor(p_1,p_2)->int:
  aux= p_1
  p_1=p_2
  p_2= aux
  return [p_1,p_2]

def e_referencia(r_1,r_2):
  aux=r_1[0]
  r_1[0]=r_2[0]
  r_2[0]=aux

  return [r_1,r_2]

extra()