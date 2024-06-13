x = 8
x = str(x) #conversión a string

x = 'Pedro es desarrollador'
print(x[6]) #acceso al 7º valor, se empieza a numerar en 0
print(x[-2]) #acceso al 2º carácter empezando por el final
name = x[0:5] #creación de subcadena de 5 carácteres
longitud = len(x) #longitud de la cadena


x = 'La luna '
y = 'sale durante las noches'
frase = x + y   #concatenación
print(frase)
print('luna' in frase) #pertenencia de un elemento

repeticion = frase * 3 #repeticion
print(repeticion)

# Recorrido
contador = 0
for caracter in frase:
    if caracter in {'a','e','i','o','u'}:
        contador += 1
print(contador)

frase_may = frase.upper() #Mayúsculas
print (frase_may)
frase_min = frase.lower() #Minúsculas
print(frase_min)
frase_cambio = frase.swapcase() #Cambio de mayúsculas a minúsculas y viceversa
print(frase_cambio)
frase_frase = frase.capitalize() #Convierte la primera letra en mayúscula
print(frase_frase)
frase_titulo = frase.title() #Convierte la primera letra de cada palabra en mayúscula
print(frase_titulo)


#Dividir una cadena
palabras = frase.split(' ') #entre parénthesis se pone el separador
print(palabras) #devolverá una lista con las palabras separadas

texto = '3 + 4'
separacion = texto.partition('+') #devolverá una tupla con la cadena separada en 3 partes
print(separacion)

#Limpiar cadenas
serial_number = '\n\t    \n 48374983274832 \n \n\t \n\t'
#La función strip() elimina los espacios en blanco al principio y al final de la cadena
cadena_limpia = serial_number.strip()
print(cadena_limpia)
#También se puede especificar el carácter a eliminar
cadena_limpia = serial_number.strip('\n')
print(cadena_limpia)

#Reemplazar
cadena = 'Hola, soy Juan'
cadena = cadena.replace('Juan','Pedro')
print(cadena)

#Unión
separador = ','
lista = ['a','b','c']
cadena = separador.join(lista)
print(cadena)

#Separación
separada = list(cadena)
print(separada)

#Conversión a número
num_str  = '123'
num = int(num_str)
print(num)
num_float = '123.45'
num = float(num_float)
print(num)

#Interpolación
nombre = 'Juan'
edad = 25
cadena = f'Hola, me llamo {nombre} y tengo {edad} años'



#Verificación
cadena = '12345'
print(cadena.isnumeric()) #devuelve True si todos los caracteres son numéricos
print(cadena.isalpha()) #devuelve True si todos los caracteres son alfabéticos
print(cadena.isalnum()) #devuelve True si todos los caracteres son alfanuméricos

#Realizar búsquedas
cadena = 'Hola, soy Juan'
print(cadena.find('Juan')) #devuelve la posición de la primera ocurrencia
print(cadena.rfind('Juan')) #devuelve la posición de la última ocurrencia
print(cadena.index('Juan')) #devuelve la posición de la primera ocurrencia
print(cadena.rindex('Juan')) #devuelve la posición de la última ocurrencia

#Contar las veces que aparece una subcadena
print(cadena.count('o'))

#Si la subcadena buscada no existe find devuelva -1, mientras que index lanza una excepción
try:
    print(cadena.index('Fran'))
except:
    print('No se ha encontrado la subcadena')

#Empieza o termina por
print(cadena.startswith('Ho'))
print(cadena.endswith('no'))


#Centrado
cadena = 'Hola'
cadena = cadena.center(20,'-') #centra la cadena en un espacio de 20 caracteres
print(cadena)

#caracteres unicode
rocket_code = 0x1F680
rocket = chr(rocket_code)
print(rocket)

# Ejercio extra

print('-----Ejercicio extra-----')
print(('***Palíndromo***')) #palabras que se escriben al revés que al derecho
def palindromo (w1:str) -> bool:
    w1 = w1.lower() #convertimos todo a minúscula
    w1 = w1.replace(' ','') #eliminamos los espacios
    #se eliminan las tildes y la diéresis
    w1 = w1.replace('á','a')
    w1 = w1.replace('é','e')
    w1 = w1.replace('í','i')
    w1 = w1.replace('ó','o')
    w1 = w1.replace('ú','u')
    w1 = w1.replace('ü','u')    
    long = len(w1)
    for i in range(long):
        if w1[i]==w1[-i-1]:
            pass
        else:
            return False
    return True

print(f'¿Anilina es un palíndromo? {palindromo("anilina")}')
print(f'¿Casa es un palíndromo? {palindromo("casa")}')
print(f'¿Dábale arroz a la zorra el abad? {palindromo("Dábale arroz a la zorra el abad")}')

def isograma(w1):
    w1 = w1.lower() #convertimos todo a minúscula
    w1 = w1.replace(' ','') #eliminamos los espacios
    #se eliminan las tildes y la diéresis
    w1 = w1.replace('á','a')
    w1 = w1.replace('é','e')
    w1 = w1.replace('í','i')
    w1 = w1.replace('ó','o')
    w1 = w1.replace('ú','u')
    w1 = w1.replace('ü','u')
    for i in w1:
        if w1.count(i) > 1:
            return False
    return True

print(f'Murciélago es un palíndromo? {isograma("Murciélago")}')
print(f'¿Casa es un isograma? {isograma("casa")}')

def anagrama(w1,w2):
    w1 = w1.lower() #convertimos todo a minúscula
    w1 = w1.replace(' ','') #eliminamos los espacios
    #se eliminan las tildes y la diéresis
    w1 = w1.replace('á','a')
    w1 = w1.replace('é','e')
    w1 = w1.replace('í','i')
    w1 = w1.replace('ó','o')
    w1 = w1.replace('ú','u')
    w1 = w1.replace('ü','u')
    w1 = w1.lower() #convertimos todo a minúscula
    w1 = w1.replace(' ','') #eliminamos los espacios
    #se eliminan las tildes y la diéresis
    w2 = w2.lower()
    w2 = w2.replace(' ','')
    w2 = w2.replace('á','a')
    w2 = w2.replace('é','e')
    w2 = w2.replace('í','i')
    w2 = w2.replace('ó','o')
    w2 = w2.replace('ú','u')
    w2 = w2.replace('ü','u')
    set_w1 = set(w1)
    for i in w2:
        if i not in set_w1:
            return False
    return True

print(anagrama('roma','amor'))
print(anagrama('Paco', 'Pepe'))
print(anagrama('Roma','amor'))
