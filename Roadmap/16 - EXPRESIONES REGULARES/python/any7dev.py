""" /*
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
 */ """

#EJERCICIO
import re

texto = ("La sociedad francesa estaba dividida en estamentos dependiendo de sus clases sociales",
        "el poder mas alto lo tenía el rey, detrás estaban la nobleza y el clero y el nivel mas bajo de poder", 
        "lo tenia el tercer estado que estaba constituido por la burguesía, los artesanos y los campesinos.", 
        "Los Estados Generales eran una asamblea, compuesta por tres ordenes separados: el clero, la nobleza y el grupo formado", 
        "por burguesía y campesinado. Este último orden se conoce como el tercer estadeo, término que usaremos para referirnos", 
        "a él en lo sucesivo. Dicha asamblea se había citado por ultima vez en 1614 y el dramatismo de la situación obligó al", 
        "gobierno a convocarla nuevamente.",
        "Luis XVI cedió a las presiones de la reina María Antonieta y del conde de Artois y dio instrucciones para que varios", 
        "regimientos extranjeros leales se concentraran en París y Versailles. Al mismo tiempo, Necker fue nuevamente destituido.", 
        "El pueblo de París respondió con la insurrección ante estos actos de provocación; los disturbios comenzaron el 12 de julio", 
        "y las multitudes asaltaron y tomaron La Bastilla -una prisión real que simbolizaba el despotismo de los Borbones- el 14", 
        "de julio.",
        "El 5 de octubre de 1789, las mujeres parisinas partieron desde los barrios obreros hacia la residencia real de Versailles,", 
        "este suceso dió comienzo a la revolución.", 
        "A fines de 1792 comenzó el proceso de Convención contra Luis XVI, quien fue juzgado y condenado a la guillotina por mayoría",
        "de votos. El 21 de enero de 1793, Luis subió al cadalso, inconmovible hasta el último momento en el sentimiento", 
        "de su inocencia. La noticia de la muerte del rey produjo indignación en Inglaterra, la que despidió al embajador o",  
        "representante francés. Francia contestó declarando la guerra a Inglaterra y a Holanda, su aliada.")

patron1 = re.findall(r"\b(\d{1,})\b", str(texto))
print(patron1)
for match in re.finditer(r"\b(\d{1,})\b", str(texto)):
    print(match.group())

patron2 = re.findall("[0-9]", str(texto))
print(patron2)

#DIFICULTAD EXTRA
email1 = "ana@ana.es"
email2 = "-1.3@_dev.com"
email3 = "12345"

patron_email = r"\b[a-z0-9\"#$% &`*+-_.\/|\^\{\} ~]+[a-z0-9]@[a-z0-9-]+.[a-z]{2,}\b"  

if re.match(patron_email, email1):
    print(f"{email1} válido")
else:
    print(f"{email1} no válido")

if re.match(patron_email, email2):
    print(f"{email2} válido")
else:
    print(f"{email2} no válido")

if re.match(patron_email, email3):
    print(f"{email3} válido")
else:
    print(f"{email3} no válido")        

tlf1 = "911203650"
tlf2 = "541201459"
tlf3 = "770777007"

patron_tlf = r"\b[6-9]+[0-9]{8}\b"

if re.match(patron_tlf,tlf1):
    print(f"{tlf1} válido")
else:
    print(f"{tlf1} no válido")

if re.match(patron_tlf,tlf2):
    print(f"{tlf2} válido")
else:
    print(f"{tlf2} no válido")

if re.match(patron_tlf,tlf3):
    print(f"{tlf3} válido")
else:
    print(f"{tlf3} no válido")


url1 = "http://www.hack.com"	
url2 = "123.com"
url3 = "hola_!3.es"

patron_url = "(http|https|ftp):\/\/[w]{3}\.[a-z0-9]+\.[a-z0-9]{2,}"

if re.match(patron_url,url1):
    print(f"{url1} válida")
else:
    print(f"{url1} no válida")

if re.match(patron_url,url2):
    print(f"{url2} válido")
else:
    print(f"{url2} no válida")

if re.match(patron_url,url3):
    print(f"{url3} válida")
else:
    print(f"{url3} no válida")

