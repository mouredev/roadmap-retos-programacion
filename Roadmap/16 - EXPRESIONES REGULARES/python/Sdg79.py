
import re

texto = "Hola, soy Sergio, tengo 46 años, me recibí a los 23 años" \
" y tuve mi primer hija a los 30 años. Mi email es sergio@estudiogiovagnoli.com.ar, " \
" mi telefono es 1111112222 y mi pagina web https://www.sdg79.com.ar"

patron = r"[0-9]{2}" #entre corchetes la cantidad de digitos
busqueda = re.findall(patron, texto)

print (busqueda)

# DIFICULTAD EXTRA:

email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+"
telefono = r"[0-9]{10}"
url = r"http[s]?://+[a-zA-Z0-9._%+-.]+$"

print(re.search(email, texto, re.I))
print(re.search(telefono, texto, re.I))
print(re.search(url, texto, re.I))


def validacion_email(mail):
    patron = r"^[\w_.+-]+@[\w-]+\.[a-zA-Z-.]+$"
    if re.match(patron, mail):
        print("email correcto")
    else:
        print("email incorrecto")

validacion_email("sergio@estudio.com.ar")



