@ -1,99 +0,0 @@


### Ejercicio

cadena = "mi cadena de texto 1"
cadena2= "cadena de texto 2"


# Concatenación 
print(cadena,cadena2)
print(cadena+" "+cadena2)

# Repetición
cadena = "mi cdena de texto 1 con salto\n" # con salto de linea
print(cadena*3)
cadena = "mi cadena de texto 1 con tabulación\t" # con tabulación
print(cadena*3)
cadena = "mi cadena de texto 1 con barra\\" # para representar barra invertida
print(cadena*3)

# Cuenta en la cadena caracteres que cumplen con el requisito
print(cadena.count("mi"))


# Indexación
print(cadena[3] + cadena2[7] )

# Por proporciones
print(cadena[1:5])

# Longitud 
print(len(cadena2))
print(len(cadena))

#Minusculas, Mayusculas, Titulo
print(cadena.lower())
print(cadena.upper())
print(cadena.title())
cadena = "    mi cAdena de texto 1 con barra     "
# Sin Espacios principio y final
print(cadena.strip())

#Busqueda

print("a" in cadena)
print("Dentro de la cadena se encuentra de en: ",cadena.find("de"))

#Reemplazar

print(cadena.replace("a","x"))

## Divide por donde esta el caracter asignado omitiendolo
print(cadena.split("a")) 

#Unión
cadena3="/".join(cadena2)

print(cadena3)

#Formateo
cadena4=" HUECOS "
print(f"yo puedo poner en los huecos {cadena4} lo que yo quiera {cadena4}")
print("yo puedo poner en los huecos {} lo que yo quiera {}".format(cadena4,cadena4))


#Transformación de cadena a lista y viceversa
cadena_list=list(cadena)
print(cadena_list)

print("".join(cadena_list))

# Comprobaciones
cadena="11asdf"
print(cadena.isalnum())
cadena="asdf"
print(cadena.isalpha())
cadena="2"
print(cadena.isdigit())
cadena="1"
print(cadena.isnumeric())

def comprueba(palabra: str, palabra2: str):
    print(palabra[::-1])
    print(f"la palabra {palabra} es Palíndromos: ", palabra[::-1]==palabra)
    print(f"la palabra {palabra2} es Palíndromos: ", palabra2[::-1]==palabra2)


    print(f"la palabra {palabra2} es Anagramas de {palabra}: ", sorted(palabra)==sorted(palabra2))
    palabra.lower()
comprueba("roma","amor")



def son_isogramas(word1: str):
    set1 = set(word1)

    print(f"¿{word1} son isogramas?: {len(set1)==len(word1)}")

son_isogramas("python")