mi_cadena = 'Hernan'

# Acceso a caracteres específicos
print(mi_cadena[0])

# Longitud
print(len(mi_cadena))

# Subcadenas
subcadena = 'code'
print(mi_cadena.find(subcadena))

# Concatenacion
saludo = 'Hola'
print(saludo + ' ' + mi_cadena)

# Repeticion
print(mi_cadena * 5)

# Recorrido
for i in mi_cadena:
    print(i)

# Conversion
print(mi_cadena.upper())
print(mi_cadena.lower())
print(mi_cadena.capitalize())
print(mi_cadena.title())
print(mi_cadena.center(10, '*'))

# Reemplazo
nueva_cadena = 'Python'
print(mi_cadena.replace('Hernan', 'Python'))

# Division
nueva_cadena2 = 'Esta es una division de cadena'
print(nueva_cadena2.split(' '))

# Union
nueva_cadena3 = ['Esta', 'es', 'una', 'union', 'de', 'cadenas']
print(' '.join(nueva_cadena3))

# Interpolacion
cadena = 'Python'
print(f'Hola, {cadena}!')

# Verificacion
verificacion = '777'
print(verificacion.isdecimal())
print(verificacion.isdigit())
print(verificacion.isalnum())
print(verificacion.isalpha())
print(verificacion.isascii())
print(verificacion.isidentifier())
print(verificacion.islower())
print(verificacion.isnumeric())

##### DIFICULTAD EXTRA
def es_palindromo(cadena):
    return cadena == cadena[::-1]

es_palindromo('radar')

def es_anagrama(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    
    p1_arreglo = list(p1)
    p2_arreglo = list(p2)

    p1_arreglo.sort()
    p2_arreglo.sort()

    p1_ordenada = ''.join(p1_arreglo)
    p2_ordenada = ''.join(p2_arreglo)
    
    return p1_ordenada == p2_ordenada

string1 = 'Nacionalista'
string2 = 'Altisonancia'
print(es_anagrama(string1, string2))

def es_isograma(cadena):
    cadena_minuscula = cadena.lower()
    unique_letters = set(cadena_minuscula)
    return len(unique_letters) == len(cadena)

string3 = 'acondicionar'
print(es_isograma(string3))
