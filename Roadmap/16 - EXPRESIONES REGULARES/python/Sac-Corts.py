import re

pattern = r'\d+'
text = "Tengo 2 perros y 3 gatos. También tengo 6 tortugas, 1 serpiente, 2 arañas, 4 ratones y ya."
result = re.findall(pattern, text)
print(result)

### Ejercicio Extra ###

regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "ejemplo@dominio.com"
if re.match(regex_email, email):
    print("Correo válido")
else:
    print("Correo no válido")


regex_telefono = r'^\+?[\d\s-]{7,15}$'
telefono = "+123-456-7890"
if re.match(regex_telefono, telefono):
    print("Teléfono válido")
else:
    print("Teléfono no válido")


regex_url = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}(:[0-9]{1,5})?(\/.*)?$'
url = "https://www.ejemplo.com:8080/path/to/page"
if re.match(regex_url, url):
    print("URL válida")
else:
    print("URL no válida")
