"""
 EJERCICIO:
 Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 creando una que sea capaz de encontrar y extraer todos los números
 de un texto.

 DIFICULTAD EXTRA (opcional):
 Crea 3 expresiones regulares (a tu criterio) capaces de:
 - Validar un email.
 - Validar un número de teléfono.
 - Validar una url.
"""
import re


print(f"== Explicación {'=' * 30}\n")

print("""Una expresión regular es una cadena que indica como identificar un patrón dentro de otras cadena.
Así como indicamos formato prefijando la cadena a imprimir con "f", a la cadena de expresión regular
se la prefija con "r".

Algunas reglas básicas de RE son:
    [] indica secuencia =>  [a-z] letras minúsculas, [0-9] dígitos, [0-9A-F] hexadecimal
    () indica literalidad => (Hola) debe decir "Hola"
    * indica 0 más ocurrencias => (Hola)* puede o no decir "Hola"
    + indica 1 o más ocurrencias => [0-9]+ debe haber uno o más dígitos
    ^ puede indicar "negación" o "inicio":
        (^Hola) NO debe decir "Hola"
        ^(Hola) debe decir "Hola" al inicio de la cadena
    $ indica el final de una cadena (o de una línea)

def numero_a_palabra(cadena: str) -> str:
    reg_exp = r"[0-9]+"
    numeros = {0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
    for n in re.findall(reg_exp, cadena):
        numero = ""
        for d in n:
            numero += numeros[int(d)] + " "
        cadena = cadena.replace(n, numero, 1)
    return cadena


print(f"{numero_a_palabra('Hola, vivo en el 1357 de la calle 23 de la ciudad de 9 de Julio. Llamame al 9864211 -URGENCIAS-.')}")

Lo que devuelve:
""")


def numero_a_palabra(cadena: str) -> str:
    reg_exp = r"[0-9]+"
    numeros = {0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
    for n in re.findall(reg_exp, cadena):
        numero = ""
        for d in n:
            numero += numeros[int(d)] + " "
        cadena = cadena.replace(n, numero, 1)
    return cadena


print(f"{numero_a_palabra('Hola, vivo en el 1357 de la calle 23 de la ciudad de 9 de Julio. Llamame al 9864211 -URGENCIAS-.')}", end="\n\n")

print(f"== Dificultad extra {'=' * 30}\n")


def validar_mail(email: str) -> bool:
    reg_exp = r"^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9]+\.[a-zA-Z.]+$"
    return bool(re.match(reg_exp, email))


def validar_telefono(telefono: str) -> bool:
    reg_exp = r"^\+?[0-9]+[ \t]?[0-9]+[ \t\-]?[0-9]*[ \t\-]?[0-9]*$"
    return bool(re.match(reg_exp, telefono))


def validar_url(url: str) -> bool:
    reg_exp = r"^(http://|https://)?[a-zA-Z0-9_\-.]+\.[a-zA-Z]+$"
    return bool(re.match(reg_exp, url))


def validar_nombre(nombre: str) -> bool:
    reg_exp = r"^[a-zA-Z]{2,}[( \t)+[a-zA-Z]{2,}]*$"
    return bool(re.match(reg_exp, nombre))


print(f"Validar nestor.larralde@gmail.com <=> {validar_mail('nestor.larralde@gmail.com')}")
print(f"Validar nlarralde@miningrapba.com.ar <=> {validar_mail('nlarralde@miningrapba.com.ar')}")
print(f"Validar neslarra@gmail <=> {validar_mail('neslarra@gmail')}")

print(f"Validar +54 11 1234-5678 <=> {validar_telefono('+54 11 1234-5678')}")
print(f"Validar +54 11 12345678 <=> {validar_telefono('+54 11 12345678')}")
print(f"Validar +54 11 1234 5678 <=> {validar_telefono('+54 11 12345678')}")
print(f"Validar 1234 5678 <=> {validar_telefono('1234 5678')}")
print(f"Validar +AR 11 1234 5678 <=> {validar_telefono('+AR 11 1234 5678')}")

print(f"Validar http://github.com.ar <=> {validar_url('http://github.com.ar')}")
print(f"Validar https://github.com.ar <=> {validar_url('https://github.com.ar')}")
print(f"Validar github.com.ar <=> {validar_url('github.com.ar')}")
print(f"Validar htp://github.com.ar <=> {validar_url('htp://github.com.ar')}")
print(f"Validar github.999 <=> {validar_url('github.999')}")

print(f"Validar Nestor <=> {validar_nombre('Nestor')}")
print(f"Validar Nestor Larralde <=> {validar_nombre('Nestor Larralde')}")
print(f"Validar Nestor O Larralde <=> {validar_nombre('Nestor O Larralde')}")
print(f"Validar 5estor Larralde <=> {validar_nombre('5estor Larralde')}")
print(f"Validar N Larralde <=> {validar_nombre('N Larralde')}")
