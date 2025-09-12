# #04CADENAS DE CARACTERES
#### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

# Ejercicio

"""
* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas 
 """
 
def main():
    # Creamos una cadena de texto (string) (str)
    cadena_de_texto = "hola"
    cadena_de_texto2 = "python"
    espacio = " "
    # Concatenamos stings
    cadena_completa = cadena_de_texto + espacio + cadena_de_texto2
    print(f"{cadena_completa}")
    # Primer caracter se vuelve mayuscula
    print(f"{cadena_completa.capitalize()}")
    # cadena_de_texto.casefold()
    # Contar el numero de veces que aparece un caracter dado: count(arg1, arg2, arg3) arg2 y 3 son opcionales
    print(cadena_completa.count("o", 0, 9))
    # cadena_de_texto.encode()
    # Regresa True o False si el string termina con el argumento dado
    print(cadena_completa.endswith("hon"))
    # Remplaza el caracter tab (\t) con espacios tabulados(8 espacios por defecto)
    cadena_con_barras = 'Hola\tpython'
    print(cadena_con_barras.expandtabs())
    # Regresa el index de la primera aparicion del substring dado: find(arg1, args2, arg3) arg2 y tres son opcionales
    print(cadena_completa.find("ol"))
    # Regresa el index de la ultima apareicion del substring dado
    print(cadena_completa.rfind("o"))
    # Da formato al string 
    name = "Daniel"
    last_name = "Hernandez"
    language = "pyhton"
    print("Me llamo {} {}. Y aprendo {}".format(name, last_name, language))
    # Se utiliza para formatear cadenas utilizando un diccionario
    data = {'name': 'Daniel', 'age': 33}
    text = "My name is {name} and I am {age} years old.".format_map(data)
    print(text)
    # Regresa el index mas bajo del substring dado, arg2 y arg3 indican start y end, default es 0
    print(last_name.index("e"))
    # Regresa el index mas alto del substring dado
    print(last_name.rindex("e"))
    # Regresa True o False si el string es alfanumerico (los espacios no lo son)
    print(last_name.isalnum())
    # Regresa True o False si elementos en string pertenecen al alfabeto (a-z A-Z)
    print(last_name.isalpha())
    # Revisa si los caracteres en string son decimales (0-9)
    print(last_name.isdecimal())
    # Revisa si los caracteres en string son numeros (0-9 y algun otro caracter unicode para numeros)
    print(last_name.isdigit())
    # Revisa si los caracteres son numeros o se relacionan a numeros (acepta simbolos como ½)
    print(last_name.isnumeric())
    # Revisa si el string tiene una nombre valido de variable (False si empieza con numero)
    print(last_name.isidentifier())
    # Revisa si los caracteres alfabeticos estan en minusculas
    print(last_name.islower())
    # Revisa si los caracteres alfabeticos estan en mayusculas
    print(last_name.isupper())
    # Regresa un string concatenado
    web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
    print("# ".join(web_tech))
    # Remueve todos los espacios en blanco al principio y al final del string
    str_with_spaces = " Hola me llamo Daniel "
    print(str_with_spaces.strip())
    # Remueve los espacios al final del string
    print(str_with_spaces.rstrip()) 
    # Remueve los espacios al inicio del string
    print(str_with_spaces.lstrip()) 
    # Reemplaza un cararcter por el otro 
    print(str_with_spaces.replace("D", "d"))
    # Remueve el prefijo indicado
    print(str_with_spaces.removeprefix(" H")) 
    # Remueve el sufijo indicado
    print(str_with_spaces.removesuffix("l "))
   
    str_withno_spaces = "Hola me llamo Daniel"
    # Parte el string en una lista comenzando desde el inicio usando un caracter dado como separador, esa el espacio como separador por defecto
    print(str_withno_spaces.split(" ",2))
    # Parte el string en una lista comenzando desde el final usando un caracter dado como separador, esa el espacio como separador por defecto
    print(str_withno_spaces.rsplit(" ",2))
    # Convierte cada primer caracter en mayuscula
    print(str_with_spaces.title())
    # Cambia mayusculas por minusculas y viceversa
    full_name = "Daniel Hernandez"
    print(full_name.swapcase())
    # Revisa si el string comienza con el string dado. Regresa True o False
    print(full_name.startswith("Dan"))
    # Convierte todo a mayusculas
    print(full_name.upper())
    # Convierte todo a minusculas
    print(full_name.lower())

 
if __name__=="__main__":
    main()


