#16 { Retos para Programadores } EXPRESIONES REGULARES

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 
"""

import re
import time

# Short for print()
log = print

# Simulate the loading of a web page
log('Retosparaprogramadores #16')
time.sleep(2)  # Simulate a delay before showing the alert
log('Retosparaprogramadores #16. Please open the Browser Developer Tools.')

# Define a pattern and flags
pattern0 = 'abc'
flags = re.IGNORECASE | re.MULTILINE  # Global and case-insensitive

# Create a regular expression using the re.compile() function
regex = re.compile(pattern0, flags)

log(regex)  # Output the regex object

text = "time: 08:07:06"
pattern1 = r'(time(:)?)? ?([01][0-9]|2[0-3])([:/-])([0-5][0-9])\4([0-5][0-9])'

# Explanation of the regular expression:
# - (time(:)?) : Optionally matches the word "time" followed by an optional colon (:).
# - ? : Matches an optional space.
# - ([01][0-9]|2[0-3]) : Matches the hour, allowing values from 00 to 23.
# - ([:/-]) : Matches one of the characters :, /, or - and captures it for later use.
# - ([0-5][0-9]) : Matches the minutes (00 to 59).
# - \4 : References the fourth captured group, which is the separator (it must be the same as used between the hour and the minutes).
# - ([0-5][0-9]) : Matches the seconds (00 to 59).

matches1 = re.search(pattern1, text)

if matches1:
    log(matches1.start())  # 0
    log(matches1.string)    # time: 08:07:06
    log(matches1.group(0))  # time: 08:07:06
    log(matches1.group(1))  # time:
    log(matches1.group(2))  # :

pattern = r'[0-9]'
matches = re.search(pattern, text)
if matches:
    log(matches.group())  # '0'

matches3 = re.findall(pattern, text)
if matches3:
    log(matches3)  # ['0', '8', '0', '7', '0', '6']

if matches3:
    log(matches3[0])  # 0
    log(matches3[1])  # 8
    log(matches3[2])  # 0

pattern2 = r'\d'
matches2 = re.search(pattern2, text)
if matches2:
    log(matches2.group())  # '0'

matches4 = re.findall(pattern2, text)
if matches4:
    log(matches4)  # ['0', '8', '0', '7', '0', '6']

# exec: Returns the first match and can be used in a loop to find all matches.
# findall: Returns a list with all matches in a more direct and straightforward way.

# Extra Difficulty Exercise:

def validate_tlf(num):
    if not re.match(r'^\d{11}$', str(num)):
        log("Invalid telephone number. Must be a numeric value and have 11 digits.")
        return False
    return True

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        log("Invalid email address")
        return False
    return True

def validate_url(url):
    url_regex = r'^(https?:\/\/)?([a-zA-Z0-9.-]+)(:[0-9]{1,5})?(\/[^\s]*)?$'
    if not re.match(url_regex, url) or (not url.startswith('http://') and not url.startswith('https://')):
        log("Invalid URL")
        return False
    return True

num1 = 1562737848
num2 = 34587452387
email1 = 'kamsutraniko@proton.me'
email2 = 'kat@hotgirl.net'
url1 = 'http://palnetaneurodiverso.org'
url2 = 'https://moebius.org'
url3 = 'something.com'
url4 = 'gato'

log(validate_tlf(num1))  # Invalid telephone number. Must be a numeric value and have 11 digits. False
log(f'Is a valid tlf: {validate_tlf(num2)}')  # Is a valid tlf: True
log(f'Is a valid email: {validate_email(email1)}')  # Is a valid email: True
log(f'Is a valid email: {validate_email(email2)}')  # Is a valid email: True
log(f'Is a valid URL: {validate_url(url1)}')        # Is a valid URL: True
log(f'Is a valid URL: {validate_url(url2)}')        # Is a valid URL: True
log(f'Is a valid URL: {validate_url(url3)}')        # Invalid URL & Is a valid URL: False
log(f'Is a valid URL: {validate_url(url4)}')        # Invalid URL & Is a valid URL: False

