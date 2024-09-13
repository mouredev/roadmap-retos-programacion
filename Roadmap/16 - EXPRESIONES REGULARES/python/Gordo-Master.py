# 16 Expresiones Regulares.

import re

text = """This regular expression example was made on September 8, 2024 
and never revised. 
Aunque yo empece este proyecto de retos de programación hace mas de 
5 meses"""

pattern = r"[\d]+"

print(re.findall(pattern,text))

"""
Ejercicio Extra
"""

def valid_mail(mail: str) -> bool:
    pattern = r"^[a-zA-Z][\w\.+-]{6,30}@[a-zA-Z]+\.[a-zA-Z]+(\.[a-zA-Z]{2})?$"
    return bool(re.match(pattern,mail))

print(f"El correo es valido: {valid_mail("GordoMaster@yahoo.net")}")

def valid_num(num: str) -> bool:
    pattern = r"^\+\d{1,3}\s?9\d{2}\s?\d{3}\s?\d{3,4}$"
    return bool(re.match(pattern,num))

print(f"El numero es valido: {valid_num("+595 912 345 678")}")

def valid_url(url: str) -> bool:
    pattern = r"^http[s]?://(www\.|blog\.|store\.)?[a-zA-Z]\w*\.[a-zA-Z]+(\.[a-zA-Z]{2})?(/\w+)*(\?\w+=\w+)?(#\w+)?$"
    return bool(re.match(pattern,url))

print(f"La URL es valido: {valid_url("https://www.example.com.es/ruta/ruta2?parametro=true#prueba")}")
