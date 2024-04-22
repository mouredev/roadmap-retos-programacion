import re
texto1 = "Texto sin numeros"
texto2 = "Texto con numeros 123321"
texto3 = "e42423"

nums_in_texto1 = re.findall("[0-9]", texto1)
nums_in_texto2 = re.findall("[0-9]", texto2)
nums_in_texto3 = re.findall("[0-9]", texto3)

print(nums_in_texto1)
print(nums_in_texto2)
print(nums_in_texto3)

'''
EXTRA
'''
# para correos
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = 'minauzum56@gmail.com'
resultEmail2 = re.search(regex, email)

if resultEmail2:
    print('Es válido')

# para numeros de telefonos, en mi pais los numeros de celular empienzan con 9 y tienen 9 digitos
regex = '^9[0-9]{8}$'
numero_telefono = "956442361"

if re.findall(regex, numero_telefono):
    print("Es válido")

# para  url
regex = "^https?:\/\/([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.([a-zA-Z]{3})(\.[a-zA-Z]{2,3})?\/?$"
url = 'http://www.holamundo.dev'

if re.findall(regex, url):
    print("Es válido")
    
