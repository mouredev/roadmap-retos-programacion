import re

text = "THis is a text with 3 numbers: 4,3,5"

#Find all numbers in text
print(re.findall('[0-9]', text))

#Extra 

#Create a regular expresion to validate an email
def validate_email(email):
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$",email))

print(validate_email("raul.garcia@text.com"))
print(validate_email("raul.garcia@textcom"))

#Validate phone number
def validate_phone(phone):
    return bool(re.match(r'[6|7]\d{8}',phone))

print(validate_phone("925259972"))

#Validate url
def validate_url(url):
    return bool(re.match(r'^http[s]?://www.\S*\.[a-zA-Z]{2,}$',url))

print(validate_url("https://www.marca.es"))
