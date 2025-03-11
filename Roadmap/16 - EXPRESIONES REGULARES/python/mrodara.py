############################################  EXPRESIONES REGULARES  ############################################################

import re # Módulo para tratamiento de expresiones regulares

my_string = "El señor Daniel tiene 3 hijos y 5 esposas, además ha sido agraciado con 1000 €"
my_other_string = "A 4 vecinos de la comunidad en el bloque nro. 2 le han tocado 100.000 $ de la lotería"

def extract_numbers_from_text(text: str) -> list:

    pattern = r"\d+" # Busca cualquier número entero

    return re.findall(pattern=pattern, string=text)

str_list = [my_string, my_other_string]

for phrase in str_list:
    matches = extract_numbers_from_text(text=phrase)
    
    if matches:
        print(f"En la frase '{phrase}' se encontraron los siguientes números: {matches}")


##############################################  EXTRA  ###################################################################################

def validate_email(email: str) -> bool:
    
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$"
    
    if re.match(pattern=pattern, string=email):
        return True
    else:
        return False
    
my_fake_email = "root.srisemipresencial.com"
my_trusted_email = "root@srisemipresencial.com"

print(validate_email(my_fake_email))
print(validate_email(my_trusted_email))

def validate_phone_number(phone: str) -> bool:
    
    pattern = r"^\+?[1-9]\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{3,4}[-.\s]?\d{3,4}$"
    
    if re.match(pattern=pattern, string=phone):
        return True
    else:
        return False

my_fake_phone = "+1234567890"
my_trusted_phone = "+1 234 567 890"
my_trusted_phone_2 = "+123456789"


print(validate_phone_number(my_fake_phone))
print(validate_phone_number(my_trusted_phone))
print(validate_phone_number(my_trusted_phone_2))

def validate_url(url: str) -> bool:
    
    pattern = r"^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(\/[^\s]*)?$"
    
    if re.match(pattern=pattern, string=url):
        return True
    else:
        return False

my_fake_url = "http://www.google"
my_trusted_url = "https://www.google.com"
my_trusted_url_2 = "www.google.com"
my_trusted_url_3 = "http://www.google.com"

print(validate_url(my_fake_url))
print(validate_url(my_trusted_url))
##############################################  FIN EXTRA  ###################################################################################




############################################  FIN EXPRESIONES REGULARES  ############################################################