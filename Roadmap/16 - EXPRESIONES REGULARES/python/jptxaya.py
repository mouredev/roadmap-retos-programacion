# #16 EXPRESIONES REGULARES
# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
#  */

import re

#Ejercicio
texto = "0-Texto a evaluar con 1,2,3 y como maximo 10, es decir un rango de [0-10] numeros para regex"
print(re.findall(r"[0-9]+",texto))

#Dificultad Extra

def validar_email(email:str)->bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]{2,4}$",email))

print("Validacion email")
print(validar_email("jos@gg.io"))
print(validar_email("jos.sdad@gg.io"))
print(validar_email("jos.sdad@gg.i"))
print(validar_email("jos.sdadgg.io"))

def validar_tlfno(tlfno:str)->bool:
    return bool(re.match(r"^\+{0,1}[\d\s]{3,15}$",tlfno))

print("Validacion Tlfno")
print(validar_tlfno("+3411106"))
print(validar_tlfno("666882788"))
print(validar_tlfno("666 88 27 88"))
print(validar_tlfno("66688a788"))


print("Validacion url")
def validar_url(url:str)->bool:
    return bool(re.match(r"^https?://(www\.)?[0-9a-zA-Z]*\.[a-zA-Z]{2,}[\w/]*$",url))

print(validar_url("http://hola.com"))
print(validar_url("http://hola.com/1"))
print(validar_url("http://www.hola.com/1"))
print(validar_url("https://www.hola.com/1"))
print(validar_url("hatp://www.hola.com/1"))
