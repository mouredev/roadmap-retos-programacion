# @RoniPG

# Crear una cadena de caracteres

ejemplo="hola Mundo"
ejemplo2:str # --> Crear la cadena vacia
print("Contenido de la cadena de caracteres: "+ejemplo)
print("Ejemplo despues del capitlaze: "+str(ejemplo.capitalize())) # --> Se utiliza para convertir la cadena con su primer carácter convertido a mayúscula
print("Contenido de la cadena de caracteres: "+ejemplo)
print("Ejemplo despues del casefold: "+str(ejemplo.casefold()) ) # --> Se utiliza para convertir la cadena a minúsculas durante su ejecucion
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del center: {ejemplo.center(25,"*")}") # --> Se utiliza para centrar una cadena dentro de un ancho específico durante su ejecucion
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del count: {ejemplo.count("o")}") # --> Se utiliza para contar cuántas veces aparece una subcadena específica dentro de una cadena más grande
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del endswith: {ejemplo.endswith("a")}") # --> Se utiliza para verificar si una cadena termina con una subcadena específica
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del encode: {ejemplo.encode()}") # --> Se utiliza para convertir una cadena de caracteres en su representación en bytes utilizando una codificación específica
ejemplo="hola\tMundo\t"
print("Contenido de la cadena de caracteres: hola\\tMundo\\t")
print(f"Ejemplo despues del expandtabs:{ejemplo.expandtabs(12)}") # --> Se utiliza para expandir los tabuladores '\t' 
ejemplo="hola Mundo"
print(f"Contenido de la cadena de caracteres: {ejemplo}")
print(f"Ejemplo despues del find:{ejemplo.find("o")}") # --> Se utiliza para encontrar la primera ocurrencia de una subcadena dentro de otra cadena
ejemplo="hola Mundo {} {}"
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del format: {ejemplo.format("Python",2)}") # --> Se utiliza para formatear cadenas de texto con valores específicos
ejemplo="hola Mundo {Lenguaje} {Version}"
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del format: {ejemplo.format_map({"Lenguaje":"Python","Version":2})}") # --> Se utiliza para formatear cadenas de texto con valores específicos
ejemplo="hola Mundo"
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del index: {ejemplo.index("la")}") # --> Se utiliza para encontrar el índice de la primera ocurrencia de una subcadena dentro de otra cadena
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isalnum: {ejemplo.isalnum()}") # --> Se utiliza para verificar si una cadena contiene únicamente caracteres alfanuméricos (letras y números) y no está vacía o contiene espacios
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isalpha: {ejemplo.isalpha()}") # --> Se utiliza para verificar si una cadena contiene únicamente caracteres alfabéticos (letras) y no está vacía o contiene espacios.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isascii: {ejemplo.isascii()}") # --> Se utiliza para verificar si todos los caracteres de una cadena son caracteres ASCII y no está vacía.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isdecimal: {ejemplo.isdecimal()}") # --> Se utiliza para verificar si todos los caracteres de una cadena son dígitos decimales(0-9) y no está vacía o contiene espacios.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isdigit: {ejemplo.isdigit()}") # --> Se utiliza para verificar si todos los caracteres de una cadena son dígitos y no está vacía o contiene espacios.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isidentifier: {ejemplo.isidentifier()}") # --> Se utiliza para verificar si una cadena es un identificador válido de Python
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isnumeric: {ejemplo.isnumeric()}") # --> Se utiliza para verificar si todos los caracteres de una cadena son caracteres numéricos y no está vacía o contiene espacios.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del islower: {ejemplo.islower()}") # --> Se utiliza para verificar si todos los caracteres de una cadena están en minúsculas y no está vacía.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isprintable: {ejemplo.isprintable()}") # --> Se utiliza para verificar si todos los caracteres de una cadena son caracteres imprimibles y no está vacía
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isspace: {ejemplo.isspace()}") # --> Se utiliza para verificar si todos los caracteres de una cadena son caracteres de espacio en blanco y no está vacía.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del istitle: {ejemplo.istitle()}") # --> Se utiliza para verificar si una cadena sigue el formato de título y no está vacía.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del isupper: {ejemplo.isupper()}") # --> Se utiliza para verificar si todos los caracteres de una cadena están en mayúsculas y no está vacía.
print("Contenido de la cadena de caracteres: "+ejemplo)
cadena=["hola","Mundo"]
print(f"Lista de cadenas despues del join: {" ".join(cadena)}") # --> Se utiliza para concatenar una lista de cadenas en una sola cadena, utilizando otra cadena como separador entre cada elemento de la lista.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del ljust: {ejemplo.ljust(20,"*")}") # --> Se utiliza para justificar a la izquierda (left justify) una cadena
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del lower: {ejemplo.lower()}") # --> Se utiliza para convertir todos los caracteres de una cadena a minúsculas
ejemplo="****hola Mundo****"
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del lstrip: {ejemplo.lstrip("*")}") # --> Se utiliza para eliminar los caracteres en blanco (o cualquier otro carácter especificado) del lado izquierdo (o principio) de una cadena.
ejemplo="hola Mundo"
print("Contenido de la cadena de caracteres: "+ejemplo)
tabla=str.maketrans({"a":"1","o":"4","u":"5"}) # --> Se utiliza para crear una tabla de traducción que puede ser utilizada por los métodos translate() o str.translate() para realizar traducciones de caracteres.
print(f"La tabla despues del maketrans contiene:\n{tabla}")
print(f"Ejemplo despues del translate: {ejemplo.translate(tabla)}") # -->  Se utiliza para realizar traducciones de caracteres en una cadena utilizando una tabla de traducción creada con el método maketrans().
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del partition: {ejemplo.partition(" ")}") # -->Se utiliza para dividir una cadena en tres partes, utilizando un separador especificado
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del removeprefix: {ejemplo.removeprefix("ho")}") # --> Se utiliza para eliminar un prefijo especificado de una cadena, si la cadena comienza con ese prefijo
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del removesuffix: {ejemplo.removesuffix("do")}") # --> Se utiliza para eliminar un sufijo especificado de una cadena, si la cadena termina con ese sufijo
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del replace: {ejemplo.replace("o","a")}") # --> Se utiliza para reemplazar todas las ocurrencias de una subcadena en una cadena con otra subcadena especificada
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del rpartition: {ejemplo.rpartition(" ")}") # --> A diferencia del método partition(), rpartition() comienza la búsqueda desde el final de la cadena en lugar de desde el principio.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del rfind:{ejemplo.rfind("o")}") # --> Se utiliza para encontrar la última ocurrencia de una subcadena dentro de una cadena
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del rindex: {ejemplo.rindex("la")}") # --> Se utiliza para encontrar el índice de la ultima ocurrencia de una subcadena dentro de otra cadena
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del rjust: {ejemplo.rjust(20,"*")}") # --> Se utiliza para justificar a la derecha una cadena, añadiendo espacios o caracteres especificados en el lado izquierdo de la cadena hasta alcanzar una longitud total especificada.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del rsplit: {ejemplo.rsplit("o")}") # --> Se utiliza para dividir una cadena en una lista de subcadenas, utilizando un separador especificado, comenzando desde el final de la cadena.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del rstrip: {ejemplo.rstrip("o")}") # --> Se utiliza para eliminar los caracteres de espacio en blanco y/o los caracteres especificados en la parte derecha (final) de una cadena
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del split: {ejemplo.split("o")}") # --> Se utiliza para dividir una cadena en una lista de subcadenas, utilizando un separador especificado.
print("Contenido de la cadena de caracteres: hola\\nMundo\\n")
ejemplo="hola\nMundo\n"
print(f"Ejemplo despues del splitlines: {ejemplo.splitlines()}") # --> Se utiliza para dividir una cadena en una lista de líneas.Utiliza los caracteres(\n),(\r),(\r\n)
ejemplo="hola Mundo"
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del startswith: {ejemplo.startswith("ho")}") # --> Se utiliza para verificar si una cadena comienza con un prefijo especificado
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del strip: {ejemplo.strip("o")}") # --> Se utiliza para eliminar los caracteres de espacio en blanco y/o los caracteres especificados al principio y al final de una cadena
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del swapcase: {ejemplo.swapcase()}") # --> Se utiliza para intercambiar entre mayúsculas y minúsculas en una cadena
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del title: {ejemplo.title()}") # --> Se utiliza para convertir la primera letra de cada palabra en una cadena a mayúscula y las demás letras a minúscula.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del upper: {ejemplo.upper()}") # --> Se utiliza para convertir todos los caracteres de una cadena a mayúsculas.
print("Contenido de la cadena de caracteres: "+ejemplo)
print(f"Ejemplo despues del zfill: {ejemplo.zfill(15)}") # --> Se utiliza para rellenar una cadena con ceros ('0') a la izquierda para alcanzar una longitud específica
print("\nDIFICULTAD EXTRA (opcional):")
"""
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
Palíndromos
Anagramas
Isogramas
"""
def Palindromo(a:str):
    """
    Palíndromo:
    Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leí­da de izquierda a derecha que de derecha a izquierda.
    Por ejemplo: anilina
    """
    a1=a.lower()
    aux=""
    for letra in reversed(a1):
        aux+=letra
    if(aux.__eq__(a1)):
        print(f"La palabra {a} es palindromo")
    else:
        print(f"La palabra {a} NO es palindromo")

def Anagrama(a:str, b:str):
    """
    Anagrama:
    Cambio en el orden de las letras de una palabra o frase que da lugar a otra palabra o frase distinta.
    Por ejemplo: Amor --> Roma
    """
    a1=a.lower()
    b1=b.lower()

    a1=sorted(a1)
    b1=sorted(b1)

    if(a1.__eq__(b1)):
        print(f"La palabra {a} es anagrama de la palabra {b}")
    else:
        print(f"La palabra {a} NO es anagrama de la palabra {b}")    
def Isograma(a:str):
    """
    Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
    Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así­ sucesivamente.
    Por ejemplo:
    Heterogramas: yuxtaponer, centrifugado, luteranismo.
    Isogramas con una repetición o de segundo orden: acondicionar, escritura, intestinos.
    """
    flag=False
    count=0
    a1=set()
    for letra_a in a:
        a1.add(letra_a)
    for letra_a1 in a1:
        for letra_a in a:
            if (letra_a1.__eq__(letra_a)):
                count +=1
        print(f"La letra: \"{letra_a1}\" esta repetida: {count} veces")
        if count>1:
            flag=True
        count=0
    if flag:
        print("Es un isograma")
    else:
        print("Es un heterograma")
    
Anagrama("Roma","Amor")
Palindromo("Anilina")
Isograma("acondicionar")
