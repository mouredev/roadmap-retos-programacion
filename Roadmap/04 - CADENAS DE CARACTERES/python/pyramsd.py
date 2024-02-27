'''
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje.
'''
string = 'Programando con python'

# acceso directo a un caracter
print(string[5])

# subcadenas
print(string[16:22])

# longitud
print(len(string))

# concatenacion
print(string + ' y c++')
print(string, 'y javascript')

# repeticion
string_2 = 'hola'
print(string_2 * 3)

# recorrido
for i in string:
    print(i)

# conversion a mayuscula
print(string.upper())

# conversion a minuscula
print(string.lower())

# remplazo
print(string.replace(string[16:22], 'C#'))

# division de string
print(string.split())

# union
string_dividido = string.split()
print(''.join(string_dividido))

# interpolacion
otro_lenguaje = 'java'
print(f'{string} y con {otro_lenguaje}')

# verificaiones
print(string.isalnum()) # alfanuméricos
print(string.isalpha()) # alfanuméricos
print(string.isascii()) # si son ascii
print(string.isdecimal()) # si son caracteres decimal
print(string.isdigit()) # si son digitos
print(string.islower()) # si son minusculas
print(string.isupper()) # si son mayusculas
print(string.isprintable()) # si es imprimible
print(string.isspace()) # si son caracteres en blanco
print(string.istitle()) # si es de forma de titulo
print(string.startswith('P')) # si empieza con...
print(string.endswith('n')) # si termina en...

# EXTRA
'''
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
'''
def palAnaIso(txt: str, txt2=''):
    def palindromo(tx: str):
        tx = tx.lower()
        return tx == tx[::-1]
    
    def anagrama(tx:str, tx2:str):
        tx = tx.lower()
        tx2 = tx2.lower()
        return sorted(tx) == sorted(tx2)
    
    def isograma(tx: str):
        tx = tx.lower()
        return len(set(tx)) == len(tx)

    if txt2:
        return f'Palindormo({txt}): {palindromo(txt)}, Anagrama{txt, txt2}: {anagrama(txt, txt2)}, Isograma({txt}): {isograma(txt)}'
    else:
        return f'Palindormo({txt}): {palindromo(txt)}, Isograma({txt}): {isograma(txt)}'

print(palAnaIso('Ana'))
print(palAnaIso('anal', 'lana'))
print(palAnaIso('amor'))
