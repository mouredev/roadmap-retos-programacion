import re

regexHasNumbers = "[0-9]"

text1 = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas desde el año 1500'
text2 = 'Solo letras, sin nada de numeros'
text3 = '1234567890-abc'

resultText1 = re.findall(regexHasNumbers, text1)
resultText2 = re.findall(regexHasNumbers, text2)
resultText3 = re.findall(regexHasNumbers, text3)

print('Numero en text1', resultText1)
print('Numero en text2', resultText2)
print('Numero en text3', resultText3)


# DIFICULTAD EXTRA

# Regex para correos

regexEmail = '^[\w\-\.]+@([\w]+\.)+[\w]{2,4}$'

email1 = 'andres.chapeton0206@gmail.com'
email2 = 'andres@gmail'

resultEmail1 = re.search(regexEmail, email1)
resultEmail2 = re.search(regexEmail, email2)

print('Es email1 valido?', resultEmail1)
print('Es email2 valido?', resultEmail2)


# Regex para telefonos (Con formato 0000-0000)

regexPhone = "([0-9]{4})-([0-9]{4})"

phone1 = '7777-9999'
phone2 = '77-5555'

resultPhone1 = re.search(regexPhone, phone1)
resultPhone2 = re.search(regexPhone, phone2)

print('Es phone1 valido?', resultPhone1)
print('Es phone1 valido?', resultPhone2)


# Regex para URL (Con formato https o http)

regexURL = "^https?:\/\/([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.([a-zA-Z]{3})(\.[a-zA-Z]{2,3})?\/?$"

url1 = 'https://www.moure.dev'
url2 = 'http://www.holamundo.dev'
url3 = 'www.google.com'
url4 = 'https://www.google'
url5 = 'w.google'

resultUrl1 = re.search(regexURL, url1)
resultUrl2 = re.search(regexURL, url2)
resultUrl3 = re.search(regexURL, url3)
resultUrl4 = re.search(regexURL, url4)
resultUrl5 = re.search(regexURL, url5)

print('Es url1 valida?', resultUrl1)
print('Es url2 valida?', resultUrl2)
print('Es url3 valida?', resultUrl3)
print('Es url4 valida?', resultUrl4)
print('Es url5 valida?', resultUrl5)

