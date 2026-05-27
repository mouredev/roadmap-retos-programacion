import re

#Exercise

regex = r"[0-9]+" #same "/d+"

text = "Yesterday I walked 7 kilometers and drank 2 liters of water before 8:30 PM."

def find_numbers(text: str) -> list:
    return re.findall(regex, text)

print(find_numbers(text))

#Extra exercise

#r"[a-zA-Z0-9_.]+" == r"[\w]+"

def validate_email(email: str) -> bool:
    pattern = r"^[\w.+-]{3,40}@[A-Za-z0-9-]{2,7}\.[A-Za-z]{2,6}$"
    return bool(re.match(pattern, email))

print(validate_email("Jordi-265@gmail.com"))

def val_phone_num(num: str) -> bool:
    pattern2 = r"^\+?\d{1,3}?[- ]?\d{7,14}$"
    return bool(re.match(pattern2, num))

print(val_phone_num("+34123456789"))
print(val_phone_num("+1-234567890")) 
print(val_phone_num("0123456789"))

def validate_url(url: str) -> bool:
    pattern3 = r"^(https?|ftp)://[A-Za-z0-9.-]{2,56}\.[A-Za-z]{2,8}$"
    return bool(re.match(pattern3, url))

print(validate_url("http://domain")) 
print(validate_url("http://google.es"))
print(validate_url("ftp://my-site123.org"))