import re

#Texto de ejemplo
text = "Tengo 2 gatos, 3 perros, 18 iguanas y 10 tortugas"
#Patron para encontrar los numeros desde el 0 al 9
pattern = re.compile(r"[0-9]")
#Reemplazamos todos los numeros de el texto por nada.
new_text = pattern.sub("", text)
#Imprimimos el resultado
print(new_text)


###############################################################################
## DIFICULTAD EXTRA
###############################################################################  

email = input("Escribe tu email: ")
tlf = input("Escrine tu mumero de telefono: ")
url = input("Escribe la url de tu web favorita: ")

def match(data: str):
    if matches:
        print(f"Datos de {data} correctos")
    else:
        print(f"Error datos de {data} incorrectos")

email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
matches = email_pattern.search(email)
match("email")                               
                               
tlf_pattern = re.compile(r"\d{9}")
matches = tlf_pattern.search(tlf)
match("Telefono")

url_pattern = re.compile(r"\b[w]{3,}+\.[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
matches = url_pattern.search(url)
match("url")
