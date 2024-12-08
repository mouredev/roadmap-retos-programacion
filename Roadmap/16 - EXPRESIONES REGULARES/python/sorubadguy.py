import re

def obtener_numeros(text: str):
    
    numeros = re.findall("\d", text)
    return numeros   

print(obtener_numeros("Hoy es 05/08/2024 y esta nublado desde las 3PM"))

#!Extra

mail = "lucas_martinez33@hotmail.com.ar"
telefono = "+54 9 2234 537643"
url = "https://github.com/sorubadguy"

def validar_mail(mail: str):
    
    reEmail = r"^[\w]+@[\w]+\.{1}[\w]+\.?[\w]*"
    return bool(re.fullmatch(reEmail, mail))
    
print(validar_mail(mail))

def validar_telefono(telefono: str):
    
    reTel = r"^\+\d+\s{1}\d+\s{1}\d+\s{1}\d+"
    return bool(re.fullmatch(reTel, telefono))

print(validar_telefono(telefono))

def validar_url(url: str):
    
    reUrl = r"^http[s]?://\w+\.{1}\w+\.?\w*\.?\w*[/\w]*[\.\w]*"
    return bool(re.fullmatch(reUrl, url))

print(validar_url(url))