import re

def quita_numeros(text: str):

    quitar = re.search("[0-9]", text)
    
    while (quitar):
        text = text.replace(text[quitar.start()],"")
        quitar = re.search("[0-9]", text)
        
    print(text)

quita_numeros("lucasmartinez33@gmail.com")

#!Extra
