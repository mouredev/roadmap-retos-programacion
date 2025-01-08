# --- Cadena de Caracteres ---
# Javier Molina

# Concatenacion 
var1 = 'Javi'
var2 = 'Molina'

print(var1 + var2)
print(var1 +' '+var2)

# Indexacion
print(var1[0:2])
print(var1[::-1])

# Longitud
print(len(var1))

# Verificar in string
print('a' in var1 and 'o' in var2)

# Reemplazo
print(var1.replace('J', 'j'))

# Division
print(var1.split('v'))

# Mayusculas - Minusculas
print(var1.upper())
print(var1.lower())
print(var2.upper())
print(var2.lower())

# Eliminación de espacios al principio y al final
print(" Javier Molina ".strip())

# Metodo title() pone la primera letra de cada palabra en Mayusculas
print('javier molina'.title())

# Invertir el metodo title() con swapcase() 
print('javier molina'.title().swapcase())

# Metodo capitalize() pone la primera letra en mayusculas solo de la primera palabra
print('javier molina'.capitalize())

# endswith() Veridica el final del string con el argumento pasado
print(var1.endswith('i'))

# Buscar
print(var1.find('i'))

# Corrobora si contiene numeros
print(var2.isalnum())
print('Javi2'.isalnum())

# Corrobora si solo tiene letras del alfabeto
print(var2.isalpha())
print('abc1'.isalpha())

# Corrobora si solo contiene numeros
print('abc1'.isnumeric())
print('321'.isnumeric())

# Corrobora si todos los caracteres son imprimibles
print('Javier Molina'.isprintable())
print('Javier\nMolina'.isprintable())
print('Javier \tMolina'.isprintable())

# Retorna el indice del parametro a buscar, caso contrario retorna -1
print(var1.rfind('f'))

# Rellena con ceros el principio de la cadena
print("54".zfill(4))


""" --- Ejercicio Extra --- """

palindromo = lambda palab_1, palab_2: palab_1.replace(' ','') == palab_2.replace(' ','')[::-1]


def ejercicio(palab_1: str, palab_2: str):
    palab_1 = palab_1.lower()
    palab_2 = palab_2.lower()
        
    ispalindromo = palindromo(palab_1, palab_2)
    
    if ispalindromo:
        print(f'{palab_1} - {palab_2} Son palindromos')
    
    anagrama = [letra in palab_2 for letra in palab_1]
    if anagrama.count(True) == len(palab_1):
        print(f'"{palab_1}" es un anagrama de: {palab_2}')
    
    anagrama2 = [letra in palab_1 for letra in palab_2]
    if anagrama2.count(True) == len(palab_2):
        print(f'"{palab_2}" es un anagrama de: {palab_1}')
        
    isograma = [letra for letra in palab_1 if palab_1.count(letra) == 1]
    if len(isograma) == len(palab_1):
        print(f'Es un isograma: {palab_1}')

    isograma2 = [letra for letra in palab_2 if palab_2.count(letra) == 1]
    if len(isograma2) == len(palab_2):
        print(f'Es un isograma: {palab_2}')

    print("-"*30)

ejercicio('Oracion', 'Caroino')
ejercicio(' Amor', 'Roma')
ejercicio('Mial', 'Lima')
ejercicio('perro', 'romper')
ejercicio('a mama roma', 'amor a mama')
