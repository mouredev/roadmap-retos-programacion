cadena = 'Hola Python!.'

print(f"Acceso a un caracter: {cadena[0]}")
print(f"Subcadena: {cadena[0:5]}, resto de la cadena: {cadena[5:]}")
print(f"Longitud de la cadena: {len(cadena)}")
print(f"Concatenación a la cadena: {cadena + ' ' + 'Me gustas.'}")
print(f"Repetición de la cadena {cadena*2}")
print("Recorrido de la cadena:")
for char in cadena:
    print(char)
print(f"Toda la cadena en mayúsculas: {cadena.upper()}")
print(f"Toda la cadena en minúsculas: {cadena.lower()}")
print(f"Reemplazando en la cadena: {cadena.replace('Python', 'Guillermo')}")
cadena_dividida = cadena.split(' ')
print(f"División de la cadena: {cadena_dividida[0]}, resto de la cadena: {cadena_dividida[1]}")
cadena_dos = 'I love Python.'
tupla = (cadena, cadena_dos)
print(f"Unión de cadenas: {' '.join(tupla)}")
print(f"Interpolación de cadenas. (lo he estado haciendo desde el inicio sin darme cuenta) {cadena} {cadena_dos}")
print("Verificación.")
palabra = 'Queso'
if palabra in cadena:
    print(f'La palabra: {palabra}, está en la cadena.')
else:
    print(f"La palabra: {palabra}, no está en la cadena.")
print("Búsqueda de subcadenas.")
palabra_dos = 'Python'
if cadena.find(palabra_dos) > 0:
    print(f"La palabra: {palabra_dos}, está en el índice {cadena.find(palabra_dos)}")
else:
    print(f"La palabra: {palabra_dos}, no está en la cadena.")
cadena_tres = '          Soy una cadena mala.    '
print(f"Eliminación de espacios (inicio y final): {cadena_tres.strip()}")
print(f"Mayúsculas a minúsculas y visceversa: {cadena.swapcase()}")
print(f"Invertir cadena: {cadena[::-1]}")

# Ejercicio EXTRA
print("Ejercico EXTRA")
def test_words(palabra1: str, palabra2: str):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Palíndromos
    def es_palindromo(palabra: str) -> bool:
        if palabra == palabra[::-1]:
            return True
        else:
            return False
    print(f"¿{palabra1.capitalize()} es palíndromo?: {es_palindromo(palabra1)}")
    print(f"¿{palabra2.capitalize()} es palíndromo?: {es_palindromo(palabra2)}")

    # Anagramas
    def son_anagramas(palabra1: str, palabra2: str) -> bool:
        if sorted(palabra1) == sorted(palabra2):
            return True
        return False   
    print(f"¿Son {palabra1.capitalize()} y {palabra2.capitalize()} anagramas?: {son_anagramas(palabra1, palabra2)}")

    # Isogramas
    def es_isograma(palabra: str) -> bool:
        veces = palabra.count(palabra[0])
        for char in palabra:
            if palabra.count(char) != veces:
                return False
        return True
    print(f"¿{palabra1.capitalize()} es isograma?: {es_isograma(palabra1)}")
    print(f"¿{palabra2.capitalize()} es isograma?: {es_isograma(palabra2)}")
    
test_words('Nacionalista', 'Altisonancia')
print()
test_words('murcielago', 'reconocer')
print()
test_words("radar", "pythonpythonpythonpython")
print()