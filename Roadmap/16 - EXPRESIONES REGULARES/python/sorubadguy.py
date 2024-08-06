import re

def obtener_numeros(text: str):
    
    numeros = re.findall("\d", text)
    return numeros   

print(obtener_numeros("Hoy es 05/08/2024 y esta nublado desde las 3PM"))

#!Extra

mail = "lucas_martinez33.hotmail.com.ar"

def validar_mail(mail: str):
    
    reEmail = r"^[\w]+@[\w]+\.{1}[\w]+\.?[\w]*"
    return bool(re.fullmatch(reEmail, mail))
    
print(validar_mail(mail))

def validar_telefono(telefono: int):
    
    reTel = r""