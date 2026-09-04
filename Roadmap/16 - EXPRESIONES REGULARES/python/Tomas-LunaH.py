# #Funciones principales con regex

import re

# #Burcar un digito \d

texto = "tengo 40 pesos"
num = re.findall(r"\d", texto)
print(num)

# #Buscar un numero mas de una vez y agruparlos \d+

texto = "tengo 10 monedas y 5 billetes"
money = re.findall(r"\d+" , texto)
print(money)

# #Buscar cualquier caracter \w

texto = "Angel_123"
space= re.findall(r"\w" , texto)
print(space)

# #Buscar espacios \s

texto = "Hola Mundo"
space = re.findall(r"\s",texto)
print(space)

# #Buscar vocales [aeiou]

texto = "Almendrita"
vocal = re.findall(r"[aeiou]" , texto)
print(vocal)

# #Buscar numero [0-9]

texto = "RTX600"
numer = re.findall(r"[0-9]", texto)
print(numer)

#Buscar tres numeros seguidos exactamente \d{3}

texto = "RTX5550"
num_segidos = re.findall(r"\d{3}", texto)
print(num_segidos)

# #Buscar tres letras mayusculas concecutivas [A-Z]{3}

texto = "RTXG878"
letras=re.findall(r"[A-Z]{3}", texto)
print(letras)


# "caracter" debe de estar al inicio ^

texto = "Hola a todos"
inicio  = re.findall(r"^Hola", texto)
print(inicio)

#"caracter" debe de etar al inicio $

texto = "Hola Angel"
final = re.findall(r"Angel$", texto)
print(final)


# #   EJERCICIO:
# * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# * creando una que sea capaz de encontrar y extraer todos los números
# * de un texto.

# texto = "Tengo 10 pesos y quiero comprarme 5 chicles de 2 pesos cada 1, me van a sobrar 0 pesos"
# numeros = re.findall(r"\d+", texto)
# print(f"Estos son los numeros: {numeros} del texto: {texto}")


# * DIFICULTAD EXTRA (opcional):
# * Crea 3 expresiones regulares (a tu criterio) capaces de:
# * - Validar un email.
# * - Validar un número de teléfono.
# * - Validar una url.

#Corro
gmail = "angel@gmail.com"

validation = r"^\w+@\w+\.\w+$"

if re.fullmatch(validation, gmail):
    print("Correo válido")
else:
    print("Correo inválido")

#Telefono
phone = 8991193849
validation = f"^\\d{{{10}}}$"
if re.search(validation,str(phone)):
    print("Tiene 10 digitos")
else:
    print("No tiene 10 digitos")

#web
url = "https://python.com"
validation = r"^https://\w+\.\w{2,}$"
if re.search(validation,str(url)):
    print("URL valida")
else:
    print("No es una URL")

