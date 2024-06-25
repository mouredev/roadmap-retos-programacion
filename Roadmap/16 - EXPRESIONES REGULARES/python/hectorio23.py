#! /usr/bin/python3
import re

'''
EJERCICIO:
Utilizando tu lenguaje, explora el concepto de expresiones regulares,
creando una que sea capaz de encontrar y extraer todos los números
de un texto.

* DIFICULTAD EXTRA (opcional):
* Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un número de teléfono.
* - Validar una url.
'''

###################################################
############ ZONA DE REGEX PATTERNS ###############
###################################################

email_regex = r"^(\w+)@([a-z]{3,}\.[a-z]{,3})$"
phone_number_regex = r"^(\+\d{2,3})\s(\d{3})\s(\d{3})\s(\d{2})\s(\d{2})" # +54 339 450 85 56 
url_regex = r"^https?:\/\/([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.([a-zA-Z]{3})(\.[a-zA-Z]{2,3})?\/?"

###################################################
################ ZONA EJEMPLOS ####################
###################################################

texto_legible = "E5n e6l si5g7ui8e956nte tex8to s9e 0t4ien4e que3 extr3aer to3dos lo0s nume3ro0s pa2ra q4ue s8e7a l9e0gi9b0le"

def extract_numbers(sValue = '') -> str:
    '''extract_numbers
    Extrae los numeros de una cadena de caracteres

    Params
    - sValue: Representa el valor de la cadena para extraer los numeros 
    '''
    # Se ejecuta siempre hasta que deje de encontrar coincidencias dentro de la 
    # cadena pasada a traves del parámetro sValue
    while True:
        # Comprueba si existe un numero dentro de la cadena
        value = re.search(r'\d+', sValue)
        
        # En caso de no existir un numero, solo se retorna la cadena
        if not value:
            return sValue
        
        # De lo contrario, se extrae los numeros de sValue  
        sValue = sValue[0:value.span()[0]] + sValue[value.span()[1]:]

    # Cuando ya no existan coincidencias, se retorna la cadena de caracteres limpia
    return sValue


def verify(pattern, tipo, sValue = '') -> str:
    ''' verify
    Lo unico que hace es comparar cadenas de caracteres con un patron regex.
    retorna una secuancia de caracteres distinta en base a la coondicion.

    Params
    - pattern -> patron regex
    - tipo -> a lo que hace referencia sValue
    - sValue -> la cadena de caracteres con la que se opera
    '''

    # Compara la cadena de caracteres con el patron, en caso de no coincidir, 
    # de imprime un mensaje que hace alusion a eso.
    if not re.match(pattern, sValue):
        return f"[-] El valor [ { sValue } ] no corresponde a un { tipo }"

    # En caso de coincidir
    return f"[+] El valor [ { sValue } ] corresponde a un { tipo }"

print("----- EJERCICIO -----\n")
print(f"Cadena cruda: { texto_legible }")
print(f"Cadena sin numeros: { extract_numbers(texto_legible) }\n\n")



print("----- EJERCICIO EXTRA -----")
###################################################
################# EMAIL CHECK #####################
###################################################
print("*********************** EMAIL CHECK *********************************")
print(verify(email_regex, 'e-mail', 'hectorino2789@gmail.com'))
print(verify(email_regex, 'e-mail', 'quesobadas@outlook.es'))
print(verify(email_regex, 'e-mail', 'nocorresponde a unema%il@gmaildjfj.completo'))


###################################################
############ PHONE NUMBER CHECK ###################
###################################################
print("\n*********************** NUMBER CHECK *********************************")
print('Para que un numero sea valido, tiene que estar escrito de la siguiente forma: +52 449 369 52 34')
print(verify(phone_number_regex, 'numero de telefono', '+52 449-369-52-34'))
print(verify(phone_number_regex, 'numero de telefono', '+52 449 369 52 34'))
print(verify(phone_number_regex, 'numero de telefono', '449 369 52 34'))


###################################################
################### URL CHECK #####################
###################################################
print("\n*********************** URL CHECK *********************************")
print(verify(url_regex, "url", "https://github.com/hectorio23"))
print(verify(url_regex, "url", "outlook:///github.com\hectorio23"))
print(verify(url_regex, "url", "127.0.0.1:89/path/otherpath"))
print(verify(url_regex, "url", "https://apple.com"))


#################################################################
######################### OUTPUT ################################
#################################################################
# ----- EJERCICIO -----

# Cadena cruda: E5n e6l si5g7ui8e956nte tex8to s9e 0t4ien4e que3 extr3aer to3dos lo0s nume3ro0s pa2ra q4ue s8e7a l9e0gi9b0le
# Cadena sin numeros: En el siguiente texto se tiene que extraer todos los numeros para que sea legible


# ----- EJERCICIO EXTRA -----
# *********************** EMAIL CHECK *********************************
# [+] El valor [ hectorino2789@gmail.com ] corresponde a un e-mail
# [+] El valor [ quesobadas@outlook.es ] corresponde a un e-mail
# [-] El valor [ nocorresponde a unema%il@gmaildjfj.completo ] no corresponde a un e-mail

# *********************** NUMBER CHECK *********************************
# Para que un numero sea valido, tiene que estar escrito de la siguiente forma: +52 449 369 52 34
# [-] El valor [ +52 449-369-52-34 ] no corresponde a un numero de telefono
# [+] El valor [ +52 449 369 52 34 ] corresponde a un numero de telefono
# [-] El valor [ 449 369 52 34 ] no corresponde a un numero de telefono

# *********************** URL CHECK *********************************
# [+] El valor [ https://github.com/hectorio23 ] corresponde a un url
# [-] El valor [ outlook:///github.com\hectorio23 ] no corresponde a un url
# [-] El valor [ 127.0.0.1:89/path/otherpath ] no corresponde a un url
# [+] El valor [ https://apple.com ] corresponde a un url