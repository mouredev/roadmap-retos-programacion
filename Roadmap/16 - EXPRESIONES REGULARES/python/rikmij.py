import re

texto_ejemplo = "2 y dos son 4, cuatro y dos son 6, seis y dos son 8 y ocho 16"

'''find_nums = re.findall(r'\d+', texto_ejemplo)

print(find_nums)'''
find_nums = r'\d+'
for elem in re.finditer(find_nums, texto_ejemplo):
    first = elem.start()
    last = elem.end()
    print(f"{texto_ejemplo[first:last]} -> posiciones ({first}-{last})")

print('\n', '~'*7, "EJERCICIO EXTRA", '~'*7)
#Validar email
email = r'\w+\S*@\w+.\w+'
texto_email = "Buenas tardes, el correo electrónico es correo.deprueba_hola@corporacion.es. Muchas gracias"
print(re.search(email, texto_email))

#Validar número teléfono
telf = r'[+]\d+\s\d+'
texto_telf = "Puede llamar al número +34 6874521035200 para más información"
print(re.search(telf,texto_telf))

#Validar URL
web = r'https?://\w+.\w+.\w+[.\w+]*'
texto_web = "Puede visitar nuestra web: https://www.unaweb_deprueba101.com.wordpress.es para más información"
print(re.search(web, texto_web))
