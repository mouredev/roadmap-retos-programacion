import re

def quita_numeros(text: str):

    quitar = re.search("[0-9]", text)
    
    while (quitar):
        text = text.replace(text[quitar.start()],"")
        quitar = re.search("[0-9]", text)
        
    print(text)

quita_numeros("1 persona con 3 perros")

#!Extra

mail = "lucasmartinez33gmail.comar"

def validar_mail(mail: str):
    
    reEmail = r""
    validar = re.search(reEmail, mail)
    if(validar.end() == len(mail)):
        print(f"tu email: {mail}, es valido")
    else:
        print(f"tu email: {mail}, no es valido")
        
validar_mail(mail)