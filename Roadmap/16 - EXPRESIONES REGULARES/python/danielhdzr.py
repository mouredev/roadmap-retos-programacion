# #16 EXPRESIONES REGULARES
#### Dificultad: Media | Publicación: 15/04/24 | Corrección: 22/04/24

## Ejercicio


'''EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.'''

import re
def main():

    def validar_email(email) -> bool:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool (re.match(regex, email))

    # Ejemplo de uso
    print(validar_email("ejemplo@dominio.com"))  # True
    print(validar_email("email_incorrecto@.com"))  # False

    def validar_telefono(telefono) -> bool:
        regex = r'^(\+?\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
        return bool (re.match(regex, telefono))

    # Ejemplo de uso
    print(validar_telefono("+1-800-555-1234"))  # True
    print(validar_telefono("555-1234"))  # True
    print(validar_telefono("12345"))  # False

    def validar_url(url) -> bool:
        regex = r'^(https?:\/\/)?([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})([\/\w .-]*)*\/?$'
        return bool (re.match(regex, url))

    # Ejemplo de uso
    print(validar_url("https://www.ejemplo.com"))  # True
    print(validar_url("http://ejemplo.com/path/to/resource"))  # True
    print(validar_url("www.ejemplo"))  # False
if __name__=="__main__":
    main()

