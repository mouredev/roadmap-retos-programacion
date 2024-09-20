"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 """
 

nombre = "ejemplo para reto 04 sobre cadenas string suncadenas y todo lo que desees"
print(nombre)

# acceso a caracter especifico
print(nombre[5])

# subcadena
print(nombre[3:8])
print(nombre[:8])
print(nombre[10:])
print(nombre[2:10:2])
print(nombre.split())

# buscar subcadenas
print(nombre.find("ca"))

print("04" in nombre )

# concatenar cadenas
moneda = "BITCOIN"
valor = "60000"
fiat = "EURO"
operacion = "="
espacio = " "
texto = moneda + espacio + operacion + espacio + valor + espacio + fiat
print(texto)
texto += " !!!"
print(texto)
monedas = ["BITCOIN", "USDT","CRONOS", "ETHERIUM"]
texto = " ".join(monedas)
print(texto)
print("{} {} {} {}".format(moneda,operacion,valor,fiat))
print(f"La moneda diital del futuro {moneda}, hoy vale aproximadamente {valor} {fiat} ")

#longitud
print(len(nombre))

#repeticion
print(("-*-" + moneda)*10)

#recorrer cadaena
for i in texto:
    if i not in ("A","E","I","O","U"):
       print(i)  
print(texto.lower())
print(texto.upper())

#reemplazo
print(texto.replace("USDT", "CUBACoin"))



"""
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 """

# palindromo
def palindromo_for(palabra: str ):
    new_p = ""
    palabra = palabra.lower().replace(" ","")
    for i in palabra:
        new_p =  i + new_p 
    print(new_p) 
    print(palabra)

    if new_p == palabra:
        print("palindromo")
    else:
        print("NO palindromo")

        

def palindromo_slicing(palabra :str):
     
    palabra = palabra.lower().replace(" ","")
     
    if palabra == palabra[::-1] :
        print("palindromo")
    else:
        print("NO palindromo")

def anagrama(cad1:str, cad2 :str):
    if len(cad1) == len(cad2):
        cad1 = cad1.lower()
        cad2 = cad2.lower()

        cad2_invert = cad2[::-1]
        
        if cad1 == cad2_invert:
            print(f"{cad1} {cad2} anagrama")
        else:
            print(f"{cad1} {cad2} NOT anagrama")
    else:
        print(f"{cad1} {cad2} NOT anagrama")


def isograma(cad : str):
    cad = cad.lower()
    letras = {}
    for i in cad:
        letras[i] = cad.count(i)
    print(letras)
    ocurrencia = list(letras.values())[0]
    print("o",ocurrencia)
    for i in letras:
        if letras[i] != ocurrencia:
            print(f"{cad} NOT isograma")
            return
    print(letras)
    print(f"{cad} Isograma")   



palindromo_for("A mama Roma le aviva el amor a mama")
palindromo_slicing("A mama Roma le aviva el amor a mama ")
anagrama("zorra","arroz")
anagrama("Roma","amor")
anagrama("RAdAr","arroz")
isograma("cabezon")
isograma("cabezoncabezoncabezoncabezoncabezon")
