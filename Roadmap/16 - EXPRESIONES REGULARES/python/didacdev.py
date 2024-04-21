import re

text = '''
En un día soleado de abril, caminé 3 kilómetros por un sendero montañoso. 
Luego, compré 2 manzanas y 1 naranja en la tienda del pueblo. 
Después, tomé el autobús número 45 de regreso a casa.
'''


def main():
    get_numbers(text)
    check_email("diego@gmail.com")
    check_tlf_number("645324565")
    check_URL("https://web.didacdev.es/fotos/foto")


def get_numbers(text: str):
    regex = r"\d+"
    findall = re.findall(regex, text)
    print(findall)


def check_email(email: str):
    regex = r"\w+@\w+\.(es|com)"
    search = re.search(regex, email)
    print(search)


def check_tlf_number(number: str):
    regex = r"^6\d{8}$"
    search = re.search(regex, number)
    print(search)


def check_URL(URL: str):
    regex = r"^(http://|https://)?[a-z0-9]+(\.[a-z0-9]+)*\.[a-z]{2,5}(/.*)$"
    search = re.search(regex, URL)
    print(search)


if __name__ == "__main__":
    main()
