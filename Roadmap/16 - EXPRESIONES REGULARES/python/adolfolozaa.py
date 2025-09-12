'''
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 '''
import re



texto = 'Quito, la capital de Ecuador, se ubica en la altura de las laderas de los Andes a 2,850 m. Fue construida sobre los cimientos de una antigua ciudad inca y es famosa por su centro colonial bien conservado, con varias iglesias de los siglos XVI y XVII, y otras 2 estructuras que mezclan estilos europeos, moriscos e indígenas. Estos incluyen la catedral, en la Plaza Grande, y la iglesia jesuita altamente decorada de la Compañía de Jesús'

#x = re.findall(r"[0-9]+", texto)   # con + toma numeros consecutivos como un solo numero
x = re.findall(r'\d+', texto)  #\d busca los numeros
print(x)
#print(texto)


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 '''

#validar correo electronico

def valid_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    if re.match(regex, email):
        return True
    else:
        return False
    
emails = ['adolfolozaa@gmail.com', 'alozavera@gmail.com', 'vera.gaby@gmail.com', 'ddjjdjdjjd.djdjd']

for email in emails:
    if valid_email(email):
        print(f'{email} es valido')
    else:
        print(f'{email} es NO valido')

for email in emails:
    match = re.search(r'^[a-z0-9]+[\._]?\w+@\w+[.]\w+$', email)
    if match:
        print(match.group()) 

# validar numero telefonico
def valid_phone(phone):
    phone_number_regex = re.compile(r"^(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s\.-]?\d{4}$")

    if re.match(phone_number_regex, phone):
        return True
    else:
        return False

phones = ['+1 555 123 4567','+1-555-123-4567', '+1.555.123.4567','+15551234567','+1 (555) 1234567', '0963564397','+593999447336' ]

for phone in phones:
    if valid_phone(phone):
        print(f'{phone} es valido')
    else:
        print(f'{phone} es NO valido')

# validar una url
def valid_url(url):
    url_regex = re.compile("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
)

    if re.match(url_regex, url):
        return True
    else:
        return False

urls = ['https://uibakery.io/regex-library/url-regex-python','https://keep.google.com/#NOTE/1QHupYobDyDMiNA0zZSYuAqkGM0HSaOunci0o78fxH-qQ2Ynl4U5afF4bxJp_yA', 'https://www.guru99.com/es/python-check-if-file-exists.html','https://mail.google.com/mail/u/0/?hl=es#inbox','https://blog.artegrafico.net/composicion-de-numeros-de-telefono-y-expresion-regular-con-python', 'https://github.com/adolfolozaa/roadmap-retos-programacion','https://developers.google.com/edu/python/regular-expressions?hl=es-419' ]

for url in urls:
    if valid_url(url):
        print(f'{url} es valido')
    else:
        print(f'{url} es NO valido')



