'''
* Utilizando tu lenguaje, explora el concepto de expresiones regulares,
* creando una que sea capaz de encontrar y extraer todos los numeros
* de un texto.
'''
import re

print("\n\n=======================================EJERCICIO=======================================\n\n")

string = "Mariano 1234"
regex = r"\d+" 
numbers = re.findall(regex, string)
print(numbers)

numbers2 = re.search(regex, string)
print(numbers2)


print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

'''
* Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un numero de telefono.
* - Validar una url.
'''
    

def check_email():
    email = input("\n[+] Introduce un email: ")
    verify_email = r"^[a-zA-Z0-9_+-.]+@[a-zA-Z0-9_+-]+\.[a-zA-Z]{2,}$"
    
    if re.findall(verify_email, email):
        print("\n[+] El email introducido es correcto")
    else:
        print("\n[!] El email introducido no es correcto")
    
def check_number():
    number_phone = input("\n[+] Introduce un un numero de telefono: ")
    verify_phone = r"^[+[0-9]{1,3}]?[0-9]{4,9}$"
    
    if re.findall(verify_phone, number_phone):
        print("\n[+] El numero introducido es correcto")
    else:
        print("\n[!] El numero introducido es incorrecto")
    
    
def check_url():
    url = input("\n[+] Introduce una direccion url: ")
    verify_url = r"((https?://(www\.)?)|www\.)\w{3,}\.[a-z]{2,}"

    if re.search(verify_url, url):
        print ("\n[+] La direccion url introdudida es correcta")
    else:
        print("\n[!] La direccion url introducida no es corrrecta")

check_email()
check_number()
check_url()
