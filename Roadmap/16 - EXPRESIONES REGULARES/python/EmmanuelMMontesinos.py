"""
/*
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
 */
"""
# Ejercicio Base y Extra

import re

class Expresion:
    def __init__(self) -> None:
        self.expres_tlf = r'\d{9}'
        self.expres_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.expres_url = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[-\w./?%&=]*'

    def numeros(self,entrada):
        resultado = re.findall(r'\d+',entrada)
        if resultado:
            for numero in resultado:
                print(f"Estos son los números dentro de la entrada:\n{numero}\n")
        else:
            print(f"No se han encontrado números:\n{entrada}\n")
        
    def telefono(self,entrada):
        resultado = re.findall(self.expres_tlf,entrada)
        if resultado:
            for tlf in resultado:
                print(f"Número de telefono encontrado:\n{tlf}\n")
        else:
            print(f"No se han encontrado número de teléfono:\n{entrada}\n")
    
    def email(self,entrada):
        resultado = re.findall(self.expres_email,entrada)
        if resultado:
            for email in resultado:
                print(f"Email encontrado:\n{email}\n")
        else:
            print(f"No se han encontrado Email:\n{entrada}\n")
        
    def url(self,entrada):
        resultado = re.findall(self.expres_url,entrada)
        if resultado:
            for url in resultado:
                print(f"Url encontrada:\n{url}\n")
        else:
            print(f"No se han encontrado Url:\n{entrada}\n")

texto_consultar = """
Bienvenido a Matrix Infinity, la empresa líder en desarrollo de software. Si deseas contactarnos, nuestro número de teléfono principal es 913456789 y nuestro correo electrónico es contacto@matrixinfinity.com. Nuestra oficina principal se encuentra en la calle Tecnología 123, y nuestro código postal es 45678.

Puedes visitar nuestro sitio web en https://www.matrixinfinity.com para más información sobre nuestros servicios. También puedes seguir nuestro blog en https://blog.matrixinfinity.com para las últimas actualizaciones y noticias. Si necesitas soporte, envía un mensaje a soporte@matrixinfinity.com.

Para consultas comerciales, llama al 687654321 o envía un correo a ventas@matrixinfinity.com. No olvides revisar nuestra sección de preguntas frecuentes en https://faq.matrixinfinity.com.

Para más información sobre nuestros productos y servicios, visita https://productos.matrixinfinity.com o llámanos al 902112648.

Recuerda que nuestras oficinas están abiertas de lunes a viernes de 9 AM a 6 PM, y puedes contactarnos en horario de oficina al 672333444.

Gracias por tu interés en Matrix Infinity. ¡Esperamos trabajar contigo pronto!

"""


consulta = Expresion()
consulta.numeros(texto_consultar)
consulta.telefono(texto_consultar)
consulta.email(texto_consultar)
consulta.url(texto_consultar)

