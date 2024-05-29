import re

text = "Ej6emplo 3 de buscar 2 números entre 1 text0 5073.22"
pattern = r"[0-9]"
print(re.findall(pattern, text))


"""
Extra
"""

#EMAIL
text = "ejemplo@terra.es"
text= "0nuevo@dia-e.com" 
text= "a3@media.n-e-t"
pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.findall(pattern_email, text))

#MOBILE PHONE
text = "766666466"
pattern_mobile = r"^[6|7][0-9]{8}"
print(re.findall(pattern_mobile, text))

#URL
text = "www.google.es"
pattern_url = r"^[w]{3}\.[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.findall(pattern_url, text))
