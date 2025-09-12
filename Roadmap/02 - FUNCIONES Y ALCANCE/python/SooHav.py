#02 FUNCIONES Y ALCANCE 
#Ejemplos de funciones básicas

#Funciones sin parámetros ni retorno
def saludo():
    print("Hola Comunidad")

saludo()

#Funciones con un parámetro
def saludo(avatar):
    print(f"Hola Comunidad soy {avatar}")

saludo("SooHav")

#Funciones con mas de un parámetro
def saludo_comunidad(avatar, saludo = "Hola Comunidad"):
    print(f"{saludo} soy {avatar}")

saludo_comunidad("SooHav","Hola gente")

#Funciones con parámetros y retorno
def saludo_comunidad_v2(avatar, saludo = "Hola Comunidad"):
    return (f"{saludo} soy {avatar}")

saludo_comunidad_v2("SooHav", "Hola! comunidad de los retos-semanales")

def suma_y_media(a, b, c):
    suma = a+b+c
    media = suma/3
    return suma, media

suma, media = suma_y_media(10, 10, 10)
print("Suma:", suma)
print("Media:", media) 

#Funciones dentro de funciones (con funciones primitivas de python)
def suma_y_media_v2(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return suma, media

numeros = [10, 10, 10]
suma, media = suma_y_media_v2(numeros)
print("Suma:", suma)
print("Media:", media)

#Funciones con variable local y global
global_variable = 10

def suma_y_media_v3(lista):
   
    global global_variable
    variable_local = 5
    
    suma = sum(lista) + global_variable + variable_local
    media = suma / (len(lista)+2)
    
    return suma, media

numeros = [10, 10, 10]
suma, media = suma_y_media_v3(numeros)
print("Suma:", suma)
print("Media:", media)

#Dificultad extra
def texto_a_numero(texto_1, texto_2):
  lista = []
  contador = 0
  for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
      i = texto_1+"_y_"+texto_2
      lista.append(i) 
    elif i%5 == 0:
      i = texto_2
      lista.append(i)
    elif i%3 == 0:
      i = texto_1
      lista.append(i)
    else:
      lista.append(i)
      contador += 1     
  return (lista, contador)

resultado = texto_a_numero("tres", "cinco")
print("Cantidad de números que no son multiplos de tres y de 5 :",resultado[1])
print(resultado[0])