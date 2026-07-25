# Operadores de cadenas

"""
Concatenar
"""

nombre = "John "
apellido = "Gutierrez"

print (f"Mi nombre completo es: {nombre + apellido}")

"""
Repetición
"""

perros = "perro"
gatos = "gato"
pajaros = "pajaro"

print(f"{perros*3} {gatos*2} {pajaros*4}")


"""
Añadir
"""

mensaje = "Hola"
mensaje += " "
mensaje += "\nBuenos días"

print(mensaje)


# Métodos para cadenas

mensaje = "Este texto contiene un mensaje oculto"
print(mensaje[1] + mensaje[3] + mensaje[13] + mensaje[15] + mensaje[20] + mensaje[21])

otorrino = str(len("otorrinolaringólogo"))
print(f"El animal más dificil de pronunciar tiene {otorrino} letras")    # Longitud

mensaje = "Ayúdame a encontrar a Javier"
print(f"Javier se encuentra en la posición {mensaje.find('Javier')}")    # Encontrar

mensaje = "EsTe eS uN mEnSaJe eN mInÚsCuLa"                              # Minúscula
print(mensaje.lower())

mensaje = "EsTe eS uN mEnSaJe eN mAyÚsCuLa"                              # Mayúscula
print(mensaje.upper())

mensaje = "El animal más fuerte es el león"
print (mensaje.replace('león','tigre'))                                  # Reemplazar

mensaje = "Esto contiene un perromensaje escondido"                      # Cortar
print(mensaje[17:22])

mensaje = "hola"                                                         # Primera letra de la cadena en mayúscula
print(mensaje.capitalize())

mensaje = "EsTe eS uN nUeVo mEnSaJe"                                     # Invierta mayúsculas y minúsculas
print(mensaje.swapcase())

mensaje = "El hombre de camisa cafe le ofreció un cafe a la mujer de ojos color cafe"
print(f"La frase tiene {mensaje.count('cafe')} veces la palabra cafe")   # Contar las veces que existe una cadena dentro de otra

mensaje = "Mas información al correo prueba@mailinator.com"
print (f"Esta cadena contiene solo caracteres alfanuméricos? {mensaje.isalnum()}")

mensaje = "ABCDEfghijk"
print (f"Esta cadena contiene solo caracteres alfabéticos? {mensaje.isalpha()}")

mensaje = "aEliminar los caracteres indeseadosv "
print(mensaje.strip("av "))                                               # Elimina los caracteres introducidos al comienzo y final

mensaje = "27340374"
print(mensaje.zfill(10))                                                 # Completa con ceros a la izquierda hasta la cantidad indicada


"""
Extra
"""

def sonAnagramas(palabra1, palabra2):
    print (sorted(palabra1))
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return True
    else:
        return False
    
def esIsograma(palabra):
    contador = palabra.count(palabra[0])
    for i in range(0, int(len(palabra))):
        letra = palabra[i]
        if palabra.count(letra) != contador:
            return False
    return True

def revisarPalabras(palabra1, palabra2):

    print(f"La palabra {palabra1} es palíndroma? {palabra1 == palabra1[::-1]}")
    print(f"La palabra {palabra2} es palíndroma? {palabra2 == palabra2[::-1]}")

    print(f"Las palabras {palabra1} y {palabra2} son anagramas? {sonAnagramas(palabra1, palabra2)}")

    isograma = esIsograma(palabra1)
    print(f"La palabra {palabra1} es un isograma? {isograma}")
    isograma = esIsograma(palabra2)
    print(f"La palabra {palabra2} es un isograma? {isograma}")

revisarPalabras("amorr", "romaroma")

