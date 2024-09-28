import re


"""
Exercise
"""


def extract_numbers(text):
    regex = r'\d+'
    pattern = re.compile(regex)
    numbers = pattern.findall(text)
    return numbers


"""
Extra
"""


def validate_data(input_data):
    regex_email = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
    regex_phone = r'^(\+?\d{1,3})?[\s-]?(\(\d{2,3}\)|\d{2,3})[\s-]?(\d{3}[\s-]?\d{4})$'
    regex_url = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(/[\w\-.~:/?#\[\]@!$&\'()*+,;=]*)?$'

    if re.match(regex_email, input_data):
        return "Email is valid"
    elif re.match(regex_phone, input_data):
        return "Phone number is valid"
    elif re.match(regex_url, input_data):
        return "URL is valid"
    else:
        return "Invalid input"


if __name__ == '__main__':
    text = "En 1992, tenía 10 años. En el 2020, tenía 38. Han pasado 200 años desde 1822."
    print(extract_numbers(text))
    print(validate_data("usuario@example.com"))
    print(validate_data("usuarioexample.com"))
    print(validate_data("usuarioexample"))
    print(validate_data("+34 912345678"))
    print(validate_data("https://www.example.com"))
