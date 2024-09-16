import re # modulo para expresiones regulares

patron = r"estoy" # expresion regular
cadena = "Hola buenas, estoy bien" # string

coincidencia = re.search(patron, cadena)
print(coincidencia.group()) # "estoy" en cadena, no patron

"""
metacaracteres

. -> coincide con calcualquier caracter menos con nueva linea
^ -> coincide al inicio del string
$ -> coincide al final del string
* -> coincide con 0 o mas repeticiones del caracter anterior
+ -> coincide con 1 o mas repeticiones del caracter anterior
? -> coincide con 0 o 1 repeticion del caracter anterior
{n} -> coincide con n repeticiones del caracter anterior
{n,} -> coincide con n o mas repeticiones del caracter anterior
{n,m} -> coincide entre n y m repeticiones del caracter anterior
[] -> coincide con cualquier caracter dentro de []
| -> coincide con el patron a la izquierda o a la derecha
() -> agrupa partes de la expresion y captura el texto
"""

patron = r".ola"
string = "Hola cara de bola"
coincidencia = re.search(patron, string) # solo captura la primera coincidencia
print(coincidencia.group())


patron1 = f"^hola"
patron2 = f"^Hola"
string = "Hola soy Hyromy"
coincidencia1 = re.search(patron1, string)
coincidencia2 = re.search(patron2, string)
#print(coincidencia1.group()) error porque no lo encuentra
print(coincidencia2.group())

patron = r"ga*to"
string = "me gustaria un gaaaaaato"
coincidencia = re.search(patron, string)
print(coincidencia.group())

patron = r"o{2}"
string = "comida se escribe food pero se pronuncia fud"
coincidencia = re.search(patron, string)
print(coincidencia.group())

patron = r"[aeiou]"
string = "no se cuantas vocales tenga esto"
coincidencia = re.findall(patron, string) # busca todas las [a, e, i, o, u]
print(coincidencia)

patron = r"gato|perro"
string1 = "yo tenia un perro"
string2 = "yo tenia un gato"
coincidencia1 = re.search(patron, string1)
coincidencia2 = re.search(patron, string2)
print(coincidencia1.group())
print(coincidencia2.group())

"""
metodos del modulo re

re.match(pattern, string) => comprueba si hay coincidencias
re.search(pattern, string) => busca la primera coincidencia en cualquier parte
re.findall(pattern, string) => busca todas las conicidencias y devuelve una lista
re.finditer(pattern, string) => busca todas las coincidencias y devuelve un iterable
re.sub(pattern, repl, string) => encuentra todas las coincidencias, las reemplaza y devuelve un str
"""

patron = r"\d+"
string = "Este es un texto con 1 numero, bueno 2, quiza tenga 1000 o mas"
coincidencias = re.finditer(patron, string)
for i in coincidencias:
    print(i.group())

print("\n")

# ---- DIFICULTAD EXTRA ----
email = r".+@.+\.com$"
telefono = r"(\+\d{2} )?\d{10}$"
url = r"(http)s?://.+/?$"

prueba_email = "formulajoel9@gmail.com"
prueba_telefono = "5550341128"
prueba_url = "http://www.youtube.com/"

buscar_email = re.match(email, prueba_email)
if buscar_email:
    print(buscar_email)
else:
    print(None)

buscar_telefono = re.match(telefono, prueba_telefono)
if buscar_email:
    print(buscar_telefono)
else:
    print(None)

buscar_url = re.match(url, prueba_url)
if buscar_url:
    print(buscar_url)
else:
    print(None)