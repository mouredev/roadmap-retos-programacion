"""
 EJERCICIO:
  Utilizando tu lenguaje, explora el concepto de expresiones regulares,
  creando una que sea capaz de encontrar y extraer todos los números
  de un texto.
 
  DIFICULTAD EXTRA (opcional):
  Crea 3 expresiones regulares (a tu criterio) capaces de:
  - Validar un email.
  - Validar un número de teléfono.
  - Validar una url.
 """
 
import re

cadena = "abc1def2gh1"
numeros = re.findall(r"\d+",cadena)
print(numeros)        

#EXTRA
def val_email (email:str) -> bool:
   re.match (r"[\w.+-]+@[\w]+\.[a-z]+",email)
   
print(val_email("lalala@jo2.com"))