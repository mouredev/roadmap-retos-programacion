# variable por valor 
"""
x = 10
def funcion(entrada):
    entrada = 0
    print(entrada)

funcion(x)

print (f"se imprime 10 ya que python trata los int como variable por valor y no lo modifica a pesar de la funcion {x}") 

# variable por referencia

y = [10 , 20, 30]
def funcion_2(entrada):
      entrada.append(40)
           
funcion_2(y)

print (f"esta lista si se modifica ya que la lista python la toma como una variable por referencia{y}")
"""

# Ejercicio Extra


valor_1 = 0
valor_2 = 1


def funcionvalor(parametro_1, parametro_2):

  holder = parametro_2
  parametro_2 = parametro_1
  parametro_1 = holder
  print(parametro_1, parametro_2)

  return parametro_1, parametro_2


varnew_1,varnew_2 = funcionvalor(valor_1,valor_2)

print(f"{varnew_1, varnew_2} es el return de la funcion, las variables originales son: {valor_1, valor_2}")




refer_1 = [1,2,3,4]
refer_2 = [5,6,7,8]

def funcionreferen(parametro1,parametro2):
 
  holder = parametro2
  parametro2 = parametro1
  parametro1 = holder

  
  return parametro1, parametro2


varnew_3, varnew_4 = funcionreferen(refer_1,refer_2) 

funcionreferen(refer_1, refer_2)

print(f"{varnew_3, varnew_4} es el return de la funcion, las variables originales son: {refer_1, refer_2}")

