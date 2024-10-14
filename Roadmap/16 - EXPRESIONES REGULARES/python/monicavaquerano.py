# 16 EXPRESIONES REGULARES
# Monica Vaquerano
# https://monicavaquerano.dev

"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */"""

# Regular Expresions
import re

text = "hola, mundo!"
x = re.search(r"hola", text)

if x:
    print("It's a match")
else:
    print("Not a match")

# Function	Description
# findall -	Returns a list containing all matches
# search -	Returns a Match object if there is a match anywhere in the string
# split -	Returns a list where the string has been split at each match
# sub - Replaces one or many matches with a string


def findDigits(txt):
    pattern = "\d+"
    digits = re.findall(pattern, txt)
    return digits


print(findDigits("The r4in in 5p4in"))

# Extra


# E-Mail
def emailCheck(email):
    pattern = r"^[\w.+-]+@[\w.+-]+\.[a-zA-Z]+$"
    check = bool(re.match(pattern, email))
    return check


print("example@example.com es un email válido? =>", emailCheck("example@example.com"))
print("Ex.4-mpl3@exampl3.co es un email válido? =>", emailCheck("Ex.4-mpl3@exampl3.co"))
print("exampleexample.com es un email válido? =>", emailCheck("exampleexample.com"))
print("example!@example.c0m es un email válido? =>", emailCheck("example@example.c0m"))


# Número de teléfono
def telephoneCheck(number):
    pattern = r"^(1\s?)?(\(\d{3}\)|\d{3})([\-\s])?(\d{3})([\-\s])?(\d{4})$"
    check = bool(re.match(pattern, number))
    return check


print("555-555-5555 es un número válido? =>", telephoneCheck("555-555-5555"))
print("1 555-555-5555 es un número válido? =>", telephoneCheck("1 555-555-5555"))
print("555-5555 es un número válido? =>", telephoneCheck("555-5555"))
print("(555)5(55?)-5555 es un número válido? =>", telephoneCheck("(555)5(55?)-5555"))


# URL
def urlCheck(url):
    pattern = r"^(http[s]?://)?(www.)?[\w]+\.[\w]{2,}[/]?$"
    check = bool(re.match(pattern, url))
    return check


print("https://google.com/ es un url válido? =>", urlCheck("https://google.com/"))
print("http://google.com es un url válido? =>", urlCheck("http://google.com"))
print("https://www.google.com es un url válido? =>", urlCheck("https://www.google.com"))
print("www.google.com es un url válido? =>", urlCheck("www.google.com"))
print("google.com es un url válido? =>", urlCheck("google.com"))
print("google.c es un url válido? =>", urlCheck("google.c"))
print("goo/gle.c es un url válido? =>", urlCheck("goo/gle.c"))
