import os, re
os.system('cls')


"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
"""
text = "Un año tiene 365 días excepto si es bisiesto que tiene 366 divididos en 12 meses que pueden tener hasta 31 días cada uno."
pattern = re.compile("\d") #La er para cualquier número se puede declarar como "\d" o "[0-9]"
nums = pattern.findall(text)

for num in nums:
    print(num, end=" ")
print()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url."""

def email_validation(email:str):
    pattern = ("(?i)[a-z0-9\\._-]+(@)[a-z0-9]+\\.[a-z]{2,4}")

    if re.match (pattern, email):
        return True
    else:
        return False
'''Función que valida una dirección de email con usuario que puede tener letras, números, puntos
    o guiones, a continuación una @ , despues el proveedor que sólo puede incluir letras y números
    y separado por un punto el dominio que puede tener de 2 a 4 letras'''



def spain_phone_validation(phone_num:str):
    pattern = ("[9|7|6][0-9]{8}||(\\+34)[9|7|6][0-9]{8}")
    if re.match(pattern, phone_num):
        return True
    else:
        return False
'''Función que valida un nº de tlf español particular cuyo primer número debe ser 6,7 (móvil) o 9 (fijo) ,
   tener en total 9 números y que puede incluir o no el prefijo español +34, el número no puede contener espacios.  '''



def url_validation(url:str):
    pattern = ("(?i)[a-z0-9._-]{1,63}\\.[a-z]{2,8}||(www)\\.[a-z0-9._-]{1,63}\\.[a-z]{2,8}")
    if re.match(pattern, url):
        return True
    else:
        return False
'''Función que valida una url básica con dominio de hasta 63 caracteres que pueden incluir puntos y guiones
    y , separado por un punto el TLD que puede ser de entre 2 y 8 letras (por ej .business)'''



def dni_validation(dni:str):
    pattern = ("(?i)[0-9]{8}[^IOU]{1}")
    if re.match(pattern,dni):
        return True
    else:
        return False
'''Función que valida un dni español con 8 cifras y una letra al final que no puede ser i,o,u ni ñ
    tal y como establece la normativa al respecto.  '''


def date_validation(date:str):
    pattern = ("^([0-2][0-9]||[3][0-1])(\/|-)(0[1-9]||1[0-2])(\/|-)((19)[5-9][0-9]||(20)[0-4][0-9]||(2050))$")
    if re.match(pattern, date):
        return True
    else:
        return False
'''Función que valida una fecha en formato dd/mm/aaaa o dd-mm-yyyy con límites de días a 31,meses a 12 y años entre 1950 y 2050'''
    
print(email_validation("je.suSw-ay69@hotmail.com"))
print(spain_phone_validation("+34716984941"))
print(url_validation("moure.dev"))
print(dni_validation("60965022t"))
print(date_validation("22/04/2050"))