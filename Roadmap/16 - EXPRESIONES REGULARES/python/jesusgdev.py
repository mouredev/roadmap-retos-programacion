'''
* EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
   creando una que sea capaz de encontrar y extraer todos los números
   de un texto.
  
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
   - Validar un email.
   - Validar un número de teléfono.
   - Validar una url.
'''

import re

def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)

numbers = find_numbers("Estoy haciendo el ejercicio 16, hoy es 22/07/2025")

print(f"Numeros encotrados: {numbers}")

'''
Extra
'''

import re

print("🔍 VALIDACIÓN DE FORMATO CON EXPRESIONES REGULARES\n")

# 📧 Validar email
def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"

    if re.match(pattern, email):
        print(f"📧 Email [{email}] → ✅ Válido")
        return True
    else:
        print(f"📧 Email [{email}] → ❌ Inválido")
        return False

validate_email("jesusgdev@gmail.com")

# 📞 Validar número de teléfono
def validate_phone(phone: str) -> bool:
    pattern = r"^\+?\d{1,3}?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"

    if re.match(pattern, phone):
        print(f"📞 Teléfono [{phone}] → ✅ Válido")
        return True
    else:
        print(f"📞 Teléfono [{phone}] → ❌ Inválido")
        return False

validate_phone("+1 426-567-3217")

# 🌐 Validar URL
def validate_url(url: str) -> bool:
    pattern = r"^(https?:\/\/)?(www\.)?[\w\-]+\.\w{2,}([\/\w\-\.]*)*\/?$"

    if re.match(pattern, url):
        print(f"🌐 URL [{url}] → ✅ Válida")
        return True
    else:
        print(f"🌐 URL [{url}] → ❌ Inválida")
        return False

validate_url("https://retosdeprogramacion.com/roadmap")
