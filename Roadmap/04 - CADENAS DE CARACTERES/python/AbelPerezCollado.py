# Concatenar
cadena = 'Hola' + ' ' + 'mundo'

# Multiplicar
ceros = '0' * 10

# Añadir
cadena = 'Hola'
cadena += ' '
cadena += 'mundo'

# Acceso a caracteres
cadena = 'Me encanta programar'
ultimo_caracter = cadena [-1]

# Subcadenas
subcadena = cadena[0:10]
longitud = len(cadena)


#Dividir cadena
division = cadena.split()

# Unión
union = ' '.join(division)

# Mayusculas minusculas
mayusculas = cadena.upper()
minusculas = cadena.lower()

#Reemplazo
reemplazo = cadena.replace('e','3').replace('a','4')

# Interpolar o formatear
lenguaje = 'Python'
cadena = f'Mi lenguaje preferido de programación es {lenguaje}'

# Verificacion
cadena = '123456'
print(cadena.isdigit())
print('a' in cadena)

# DIFICULTAD EXTRA

def es_palindromo(palabra : str):
    p = palabra.lower()
    if p == p[::-1]:
        return True
    else:
        return False

def es_anagrama(p1: str, p2:str):
    p1 = p1.lower()
    p2 = p2.lower()
    if not len(p1) == len(p2):
        return False
    else:
        anagrama = True
        for c in p1:
            if c not in p2:
                anagrama = False
    return anagrama

def es_isograma(palabra: str,):
    palabras_vistas = []
    for p in palabra.lower():
        if p not in palabras_vistas:
            palabras_vistas.append(p)
        else:
            return False
    return True

p1 = input('Introduce la primera palabra: ')

print(f'{p1} es un palindromo? -> {es_palindromo(p1)}')
print(f'{p1} es un isograma -> {es_isograma(p1)}')
p2 = input("Introduce la segunda palabra: ")
print(f'{p1} y {p2} son anagramas? -> {es_anagrama(p1,p2)}')
    