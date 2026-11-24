import re

# EJERCICIO:
# Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# creando una que sea capaz de encontrar y extraer todos los números
# de un texto.

texto = """#15 ASINCRONÍA
Dificultad: Díficil | Publicación: 08/04/24 | Corrección: 15/04/24
EJERCICIO
Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
asíncrona una función que tardará en finalizar un número concreto de
segundos parametrizables. También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará
su ejecución y cuando finaliza.

DIFICULTAD EXTRA (opcional):
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
- Una función C que dura 3 segundos.
- Una función B que dura 2 segundos.
- Una función A que dura 1 segundo.
- Una función D que dura 1 segundo.
- Las funciones C, B y A se ejecutan en paralelo.
- La función D comienza su ejecución cuando las 3 anteriores han
  finalizado."""

print(re.findall(r"\d+", texto))

# DIFICULTAD EXTRA (opcional):
# Crea 3 expresiones regulares (a tu criterio) capaces de:
# - Validar un email.
# - Validar un número de teléfono.
# - Validar una url.

VALID_EMAIL = re.compile(r"(?!.*\.{2}.*)" # Sin dos puntos consecutivos
                         r"(?=\A.{1,64}@)" # Username con máximo 64 caracteres en total
                         r"(?!\A\.)(?!.*\.@)" # Sin punto al inicio o final del username
                         r"[a-z0-9!#$%&'*+-/=?^_`{|}~.]+@"
                         r"(?=.{1,253}\Z)" # Dominio con máximo 253 caracteres en total
                         r"(?!-)(?!.*-\.)" # Sin guión al inicio o final de un label de dominio
                         r"([a-z0-9\-]{1,63}\.*)+",
                         flags=re.I)

emails_validos = [
    "gabriel@gmail.com",
    "!#$%&'*+-/=?^_`.{|}~@gmail.com",
    "john.doe@gmail.com",
    "user+tag@gmail.com",
    "admin_2025@gmail.com",
    "first-last@gmail.com",
    "user@example.com",
    "user@mail.company.co.uk",
    "user@server-01.internal.org",
    "email_con_username_de_sesenta_y_cuatro_caracteres_es_valido_123@gmail.com",
    f"email_con_campo_de_dominio_de_63_caracteres@{"a" * 63}.com.pe",
    f"email_con_dominio_de_253_caracteres_en_total@{"a" * 249}.com"
]

emails_no_validos = [
    "!#$%&'*+-/=?^_`{|}~.@gmail.com",
    ".!#$%&'*+-/=?^_`{|}~gmail.com",
    "!#$%&'..*+-/=?^_`{|}~@gmail.com",
    "email_con_username_mas_de_sesenta_y_cuatro_caracteres_es_invalido@gmail.com",
    "user@-example.com",
    "user@example-.com",
    "user@example..com",
    "user@campode_dominio_con_mas_de_sesenta_y_tres_caracteres_es_invalido.com",
    f"email_con_dominio_de_mas_de_253_caracteres_en_total@{"a" * 254}.com"
]

for email in emails_validos + emails_no_validos:
    print(f"\nIs {email} a valid email?")
    print("Yes" if VALID_EMAIL.fullmatch(email) else "NO")

NUM_CEL_PER = re.compile(r"\+519\d{8}")
NUM_CEL_ESP = re.compile(r"\+34(6\d{8}|7[1-4]\d{7})")
NUM_CEL_MEX = re.compile(r"\+52[2-9]\d{9}")

numeros_celulares = [
    "+34767584938",
    "+51987654321",
    "+34684730289",
    "+34735748390",
    "+522758690460",
    "+520774389017",
    "+51975849302",
    "+529655748392",
    "+525758694738",
    "+51912312323",
    "+34717764759",
    "+51823156748"
]

for num_cel in numeros_celulares:
    print()
    if NUM_CEL_ESP.fullmatch(num_cel):
        print(f"España: {num_cel}")
        continue
    if NUM_CEL_PER.fullmatch(num_cel):
        print(f"Perú: {num_cel}")
        continue
    if NUM_CEL_MEX.fullmatch(num_cel):
        print(f"México: {num_cel}")
        continue
    print(f"Desconocido: {num_cel}")

VALID_URL = re.compile(r"(?:[a-z])" # Scheme debe empezar con una letra
                       r"[a-z0-9+.-]*://"
                       r"([a-z0-9-_]+\.{0,1})+(/[a-z0-9-_./]*)*"
                       r"(\?(\w+=.+(&)?)*)?", flags=re.I) # Parámetros opcionales

valid_urls = [
    "https://www.example.com?",
    "http://www.example.com/questions?q=search",
    "ftp://www.example.com/questions/3456/?q=search&p",
    "mailto://www.example.com//3456/?q=search&",
    "file://www.example.com/questions/3456/my-document?q=search&p=2",
    "data://www.example.com/questions/3456/my-document.html?q=3=3",
    "irc://www.example.com/questions/3456",
    "https://www.youtube.com/"
]

invalid_urls = [
    "0x10://www.example.com",
    "-ftp://www.example.com",
    ".://www.example.com",
    "-://www.example.com",
    "www.example.com",
    "http:www.example.com/main.html",
    "https://example.com page.html",
    "https://www.example.com\\folder\\file.html",
    "/main.html"
]

for url in valid_urls + invalid_urls:
    print(f"\nIs {url} a valid URL?")
    print("Yes" if VALID_URL.fullmatch(url) else "NO")