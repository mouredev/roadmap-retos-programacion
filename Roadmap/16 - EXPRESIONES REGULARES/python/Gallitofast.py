# * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.

import re
text=" Y esa fue la noche mas linda del mundo aunque nos durara tan solo 1 segundo"
x_num=re.findall("[0,9]",text)
print(text)
print(f"Los numeros encontrados en el texto son: {x_num}")
print("-"*60)

# * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
recorreo=r"^[a-zA-Z0-9]*@[a-zA-Z0-9]*\.[a-z]{3}$"
retelefono= r"^\+\d{2} \d{4} \d{6}$"
reurl=r"^(https?://)?([a-z0-9]*\.)?[a-z0-9]*\.[a-z]{3}$"

def validacion(correo,telefono,url):
    if re.search(recorreo,correo):
        print(f"Correo validado: {correo}")
    else:
        print(f"correo invalidado: {correo}")
    if re.search(retelefono,telefono):
        print(f"Numero de telefono validado: {telefono}")
    else:
        print(f"Numero de telefono invalidado: {telefono}")
    if re.search(reurl,url):
        print(f"Url validada: {url}")
    else:
        print(f"Url invalidada: {url}")

validacion("Messigallito@gmail.com","+54 6324 695874","www.freecodecamp.com")
    
