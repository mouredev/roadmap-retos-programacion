#CADENAS DE CARACTERES

mi_cadena = "El amor no duele "

#Acceso a caracteres específicos
print(mi_cadena[3])

#Subcadenas
print(mi_cadena[3:7])

#Longitud
print(len(mi_cadena))

#Concatenación
otra_cadena = " vive y deja vivir"
print(mi_cadena +"," + otra_cadena)

#Repetición
print(mi_cadena * 3)

#Recorrido
for letra in mi_cadena:
    print(letra)

#Conversión a mayúsculas y minúsculas
print(mi_cadena.upper())
print(otra_cadena.lower())

#Reemplazo
print(otra_cadena.replace("vivir","gozar"))

#División
print(mi_cadena.split())

# Unión
print(".".join(otra_cadena))

#Interpolación
nombre = "Homero"
edad = 102
print(f" Hola mi nombre es {nombre}, tengo {edad} años, soy un lolo")

#Verificación
print("amor" in mi_cadena)
print("love" in mi_cadena)

#Eliminación de espacios
print(otra_cadena.strip())

#Capitalización
print(otra_cadena.title())

#EXTRA
"""Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas"""

def main():
    palabra = input("Escribe tu palabra para ver si es palíndromo: ").lower()
    palabra1 = input("Escribe tu primera palabra: ").lower()
    palabra2 = input("Escribe tu segunda palabra: ").lower()

    def es_palindromo(palabra):
        if palabra == palabra[::-1]:
            print(f"{palabra} es palíndromo!")
        else:
            print(f"{palabra} no es palíndromo")
    
    def es_anagrama(palabra1, palabra2):
        if sorted(palabra1) == sorted(palabra2):
            print(f"{palabra1} y {palabra2} son anagramas!")
        else:
            print(f"{palabra1} y {palabra2} no son anagramas")
    
    def es_isograma(palabra):
        if len(palabra) == len(set(palabra)):
            print(f"{palabra} es isograma!")
        else:
            print(f"{palabra} no es isograma")
    
    es_palindromo(palabra)
    es_anagrama(palabra1, palabra2)
    es_isograma(palabra1)
    es_isograma(palabra2)
    
main()
