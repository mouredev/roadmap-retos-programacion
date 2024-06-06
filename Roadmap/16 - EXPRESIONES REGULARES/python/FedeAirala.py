#  16 EXPRESIONES REGULARES
"""

EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.

 """

import re

print ("-"*100)
text = "Las 1000 y una noches según 30 lectores"
x_num = re.findall("[0-9]",text)
print (text)
print (f"Números encontrados en el texto: {x_num}")
print ("-"*100)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
```
"""

# Ejercicio realizado considerando los siguientes formatos
# email: string@string.sss
# phone: +01 0123 012345
# url: www.string.com o https://www.string.com o http://www.string.com

#Patrones

regexemail = r"^[a-zA-Z0-9]*@[a-zA-Z0-9]*\.[a-z]{3}$"
rephone = r"^\+\d{2} \d{4} \d{6}$"
reurl = r"^(https?://)?([a-z0-9]*\.)?[a-z0-9]*\.[a-z]{3}$"

# Funcón para validar los datos

def validate_data(email,phone,url):

    if re.search(regexemail,email):
        print (f"{email}: email válido")
    else:
        print (f"{email}: email inválido")

    if re.search(rephone,phone):
        print (f"{phone}: número válido")
    else:
        print (f"{phone}: número inválido")

    if re.search(reurl,url):

        print (f"{url}: url válida")
    else:
        print (f"{url}: url inválida")


# Función para ingresar datos a validar

def main():

    validate_data("pedroalonzo84@gmail.com","+54 6324 695874","www.pedro.com")
    validate_data("pedroalonzo84@gmail.com","+3 6324 695874","www.pedro")
    validate_data("pedroalonzo84gmail.com","+32 6324 695874","www.pedro.com")
    validate_data("pedroalonzo84@gmail.com","+2 63254 695874","https://www.pedro.com")
    validate_data("pedroalonzo84@gmail.com3","+25 6354 695874","http://www.pedro.com")
 
if __name__ == "__main__":
    main()