"""/*
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
 */"""

import re


texto = "Texto del ejercicio 16 del roadmap, hoy es 02/11/2026"

def find_numbers(text:str) -> list:
    return print(re.findall(r"[0-9]+", text))

find_numbers(texto)

def validate_email(email:str) -> bool:
    return print(bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email)))

validate_email("gparra@gmail.com")

def validate_phonenumber(phonenumber:str) -> bool:
    return print(bool(re.match(r"^\+?[\d\s\-\(\)]{7,15}$",phonenumber)))

validate_phonenumber("+34999999999")

def validate_url(url:str) -> bool:
    return print(bool(re.match(r"^https?://(?:www\.)?[\w\-]+(?:\.[\w\-]+)+[/#?]?.*$",url)))

validate_url("https://www.sadfasdfcom")
